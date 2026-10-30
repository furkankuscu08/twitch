(() => {
  "use strict";
  const query = new URLSearchParams(location.search);
  const demo = query.get("demo") === "1";
  const frozen = demo && query.has("step");
  const showLatency = query.get("latency") === "1";
  const byId = id => document.getElementById(id);
  const chips = new Map();
  let context;
  let voice;
  let noiseBuffer;
  let burstTimer;
  let cachedPlantUrl;
  let currentBoomId;
  if (frozen) document.documentElement.dataset.frozen = "true";

  function sound(kind) {
    if (frozen) return;
    try {
      context ||= new (window.AudioContext || window.webkitAudioContext)();
      if (context.state !== "running") {
        context.resume().catch(() => {});
        return;
      }
      const now = context.currentTime;
      // One voice at a time: rapid booms and status cues never add their peaks.
      if (voice) {
        for (const source of voice.sources) { source.stop(now); source.disconnect(); }
        for (const gain of voice.gains) gain.disconnect();
      }
      const current = {sources: [], gains: []};
      voice = current;
      function play(source, volume, duration) {
        const gain = context.createGain();
        current.sources.push(source);
        current.gains.push(gain);
        gain.gain.setValueAtTime(volume, now);
        gain.gain.exponentialRampToValueAtTime(.0001, now + duration);
        source.connect(gain).connect(context.destination);
        source.start(now);
        source.stop(now + duration);
        source.onended = () => {
          source.disconnect();
          gain.disconnect();
          current.sources = current.sources.filter(item => item !== source);
          if (!current.sources.length && voice === current) voice = undefined;
        };
      }
      const oscillator = context.createOscillator();
      const frequencies = {plant: 560, armed: 880, spark: 160, fizzle: 360, boom: 95};
      const duration = kind === "boom" ? .7 : .16;
      oscillator.type = kind === "spark" ? "triangle" : "sine";
      oscillator.frequency.setValueAtTime(frequencies[kind], now);
      oscillator.frequency.exponentialRampToValueAtTime(
        kind === "fizzle" ? 80 : kind === "boom" ? 30 : frequencies[kind] * 1.2,
        now + duration
      );
      // The three boom layers sum to at most .5 (~-6 dBFS), even at attack.
      play(oscillator, kind === "boom" ? .32 : .045, duration);
      if (kind === "boom") {
        if (!noiseBuffer) {
          noiseBuffer = context.createBuffer(1, context.sampleRate * .7, context.sampleRate);
          const samples = noiseBuffer.getChannelData(0);
          for (let i = 0; i < samples.length; i++) samples[i] = Math.random() * 2 - 1;
        }
        const noise = context.createBufferSource();
        noise.buffer = noiseBuffer;
        play(noise, .17, .45);
        const crack = context.createOscillator();
        crack.type = "triangle";
        crack.frequency.setValueAtTime(1800, now);
        crack.frequency.exponentialRampToValueAtTime(120, now + .05);
        play(crack, .01, .05);
      }
    } catch (_) { /* Audio permissions must not interrupt the overlay. */ }
  }

  // Fixed reusable fragments; no per-frame work or accumulating particles.
  for (let index = 0; index < 12; index++) {
    const fragment = document.createElement("i");
    fragment.className = "fragment";
    fragment.style.setProperty("--angle", `${index * 30 + 12}deg`);
    fragment.style.setProperty("--travel", `${260 + (index % 3) * 60}px`);
    byId("explosion").append(fragment);
  }
  function stopBurst() {
    clearTimeout(burstTimer);
    byId("explosion").hidden = true;
    byId("stage").classList.remove("shaking");
    byId("boom-banner").classList.remove("impact");
  }
  function burst() {
    if (frozen) return;
    byId("explosion").hidden = false;
    void byId("explosion").offsetWidth;
    byId("stage").classList.add("shaking");
    byId("boom-banner").classList.add("impact");
    burstTimer = setTimeout(stopBurst, 900);
  }

  function plantLink(url, running) {
    byId("plant").hidden = !running || !url;
    if (!url || url === cachedPlantUrl) return;
    cachedPlantUrl = url;
    byId("plant-url").textContent = url.replace(/^https?:\/\//, "");
    byId("qr").replaceChildren();
    try {
      const code = qrcodegen.QrCode.encodeText(url, qrcodegen.QrCode.Ecc.MEDIUM);
      const canvas = document.createElement("canvas");
      const border = 4, scale = 4;
      canvas.width = canvas.height = (code.size + border * 2) * scale;
      const painter = canvas.getContext("2d");
      painter.fillStyle = "#fff";
      painter.fillRect(0, 0, canvas.width, canvas.height);
      painter.fillStyle = "#000";
      for (let y = 0; y < code.size; y++) {
        for (let x = 0; x < code.size; x++) {
          if (code.getModule(x, y)) painter.fillRect((x + border) * scale, (y + border) * scale, scale, scale);
        }
      }
      byId("qr").append(canvas);
    } catch (_) { /* Keep the readable URL if a QR cannot be produced. */ }
  }

  function updateChip(chip) {
    chip.element.dataset.status = chip.status;
    chip.element.querySelector(".status").classList.toggle("false-alarm-stamp", chip.status === "false_alarm");
    const remaining = frozen ? chip.seconds : Math.max(0, (chip.deadline - performance.now()) / 1000);
    chip.element.querySelector(".status").textContent = chip.status === "arming"
      ? `Arming · ${Math.ceil(remaining)}s` : chip.status.replace("_", " ");
    chip.element.querySelector(".arming-ring").style.setProperty(
      "--progress", `${chip.seconds ? 100 * (1 - remaining / chip.seconds) : 100}%`
    );
  }

  function addChip(mine) {
    if (chips.has(mine.id)) { chips.get(mine.id).element.remove(); chips.delete(mine.id); }
    if (chips.size >= 4) {
      const old = [...chips.values()].find(chip => ["exploded", "false_alarm"].includes(chip.status))
        || chips.values().next().value;
      chips.delete(old.id);
      old.element.remove();
    }
    const element = document.createElement("div");
    element.className = "mine-chip";
    element.dataset.id = mine.id;
    const ring = document.createElement("span");
    ring.className = "arming-ring";
    const text = document.createElement("div");
    const owner = document.createElement("span");
    owner.className = "owner";
    owner.textContent = mine.owner;
    const status = document.createElement("span");
    status.className = "status";
    text.append(owner, status);
    element.append(ring, text);
    const seconds = Math.max(0, mine.arms_in_s);
    const chip = {id: mine.id, status: mine.status || "arming", seconds,
      deadline: performance.now() + seconds * 1000, element};
    chips.set(mine.id, chip);
    byId("mines").append(element);
    updateChip(chip);
  }

  function hideBanner() {
    byId("boom-banner").hidden = true;
    byId("false-alarm").hidden = true;
    stopBurst();
    currentBoomId = undefined;
  }

  function valid(message) {
    if (!message || typeof message !== "object") return false;
    const text = field => typeof message[field] === "string";
    switch (message.type) {
      case "snapshot": return typeof message.round?.running === "boolean"
        && (message.plant_url === null || typeof message.plant_url === "string")
        && Array.isArray(message.mines)
        && message.mines.every(mine => mine && typeof mine.id === "string"
          && typeof mine.owner === "string" && typeof mine.status === "string"
          && Number.isFinite(mine.arms_in_s));
      case "mine_planted": return text("id") && text("owner") && Number.isFinite(message.arms_in_s);
      case "mine_armed": case "spark": case "fizzle": return text("id");
      case "false_alarm": return text("id") && text("owner");
      case "boom": return ["id", "owner", "word"].every(text)
        && Number.isFinite(message.planted_ago_s) && Number.isFinite(message.latency_ms)
        && Array.isArray(message.receipt) && message.receipt.every(item => item
          && typeof item.text === "string" && typeof item.hit === "boolean");
      case "reveal": return Number.isFinite(message.stats?.booms) && Array.isArray(message.duds)
        && message.duds.every(dud => dud && typeof dud.owner === "string" && typeof dud.word === "string");
      default: return false;
    }
  }

  function receive(message) {
    if (!valid(message)) return;
    const chip = chips.get(message.id);
    switch (message.type) {
      case "snapshot":
        hideBanner();
        chips.clear();
        byId("mines").replaceChildren();
        {
          const live = message.mines.filter(mine => ["arming", "armed", "sparking"].includes(mine.status));
          const inactive = message.mines.filter(mine => !live.includes(mine));
          [...inactive, ...live].slice(-4).forEach(addChip);
        }
        plantLink(message.plant_url, message.round.running);
        if (message.round.running) byId("reveal").hidden = true;
        break;
      case "mine_planted": addChip(message); sound("plant"); break;
      case "mine_armed": case "spark": case "fizzle": case "false_alarm":
        if (chip) {
          chip.status = {mine_armed: "armed", spark: "sparking", fizzle: "armed", false_alarm: "false_alarm"}[message.type];
          updateChip(chip);
          if (message.type === "fizzle" && !frozen) {
            chip.element.classList.add("fizzling");
            chip.element.addEventListener("animationend", () => chip.element.classList.remove("fizzling"), {once: true});
          }
        }
        if (message.type === "false_alarm") {
          if (currentBoomId === message.id) byId("false-alarm").hidden = false;
        } else sound({mine_armed: "armed", spark: "spark", fizzle: "fizzle"}[message.type]);
        break;
      case "boom": {
        hideBanner();
        currentBoomId = message.id;
        if (chip) { chip.status = "exploded"; updateChip(chip); }
        byId("reveal").hidden = true;
        byId("boom-owner").textContent = `${message.owner.toUpperCase()}'S MINE:`;
        byId("boom-word").textContent = message.word.toUpperCase();
        byId("boom-age").textContent = `planted ${Math.floor(message.planted_ago_s / 60)} min ago`;
        byId("receipt").replaceChildren();
        message.receipt.forEach((item, index) => {
          if (index) byId("receipt").append(" ");
          const text = document.createElement(item.hit ? "mark" : "span");
          text.textContent = item.text;
          byId("receipt").append(text);
        });
        byId("latency").hidden = !showLatency;
        byId("latency").textContent = `${Math.round(message.latency_ms)} ms · ${message.source}`;
        byId("boom-banner").hidden = false;
        burst();
        sound("boom");
        break;
      }
      case "reveal":
        hideBanner();
        byId("plant").hidden = true;
        byId("round-stats").textContent = `${message.stats.booms} booms`;
        byId("duds").replaceChildren();
        for (const dud of message.duds) {
          const line = document.createElement("p");
          const word = document.createElement("strong");
          word.textContent = dud.word;
          line.append(`${dud.owner}'s mine `, word, " never went off");
          byId("duds").append(line);
        }
        byId("reveal").hidden = false;
        break;
    }
  }

  if (demo) {
    const steps = window.overlayDemoSteps;
    const selected = Math.max(0, Math.min(steps.length - 1, Number.parseInt(query.get("step"), 10) || 0));
    function runStep(index) {
      steps[index].forEach(receive);
      document.documentElement.dataset.demoStep = String(index);
    }
    if (frozen) for (let index = 0; index <= selected; index++) runStep(index);
    else {
      let index = 0;
      runStep(index);
      setInterval(() => { index = (index + 1) % steps.length; runStep(index); }, 1700);
    }
  } else {
    function connect() {
      const socket = new WebSocket(`${location.protocol === "https:" ? "wss" : "ws"}://${location.host}/ws/overlay`);
      socket.onmessage = event => { try { receive(JSON.parse(event.data)); } catch (_) {} };
      socket.onclose = () => setTimeout(connect, 750);
      socket.onerror = () => socket.close();
    }
    connect();
  }
  if (!frozen) setInterval(() => {
    for (const chip of chips.values()) if (chip.status === "arming") updateChip(chip);
  }, 200);
  window.overlayReady = true;
})();
