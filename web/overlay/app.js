(async () => {
  "use strict";
  const query = new URLSearchParams(location.search);
  const demo = query.get("demo") === "1";
  const frozen = demo && query.has("step");
  const BANNER_FULL_S = 3;
  const showLatency = query.get("latency") === "1";
  const byId = id => document.getElementById(id);
  const chips = new Map();
  const sounds = {};
  let context;
  let master;
  let voice;
  let burstTimer;
  let cachedPlantUrl;
  let currentBoomId;
  let shrinkTimer;
  let scoreTimer;
  if (frozen) document.documentElement.dataset.frozen = "true";

  async function renderSound(kind) {
    const boom = kind === "boom";
    const duration = boom ? 1.15 : .18;
    const ctx = new OfflineAudioContext(1, Math.ceil((duration + .2) * 48000), 48000);
    const compressor = ctx.createDynamicsCompressor();
    compressor.threshold.value = -14;
    compressor.knee.value = 10;
    compressor.ratio.value = 4;
    compressor.attack.value = .004;
    compressor.release.value = .18;
    compressor.connect(ctx.destination);
    const start = .015;

    function envelope(level, attack, length, points = []) {
      const gain = ctx.createGain();
      gain.gain.setValueAtTime(0, start);
      gain.gain.linearRampToValueAtTime(level, start + attack);
      for (const [time, value] of points) {
        gain.gain.exponentialRampToValueAtTime(value, start + time);
      }
      gain.gain.exponentialRampToValueAtTime(.0001, start + length - .008);
      gain.gain.linearRampToValueAtTime(0, start + length);
      gain.connect(compressor);
      return gain;
    }

    if (boom) {
      // Soft & Airy: a filtered rumble, warm 155 Hz thump and softened crack.
      const buffer = ctx.createBuffer(1, Math.ceil(duration * 48000), 48000);
      const samples = buffer.getChannelData(0);
      let seed = 739391;
      for (let i = 0; i < samples.length; i++) {
        seed = (Math.imul(seed, 1664525) + 1013904223) >>> 0;
        samples[i] = seed / 2147483648 - 1;
      }
      const body = ctx.createBufferSource();
      body.buffer = buffer;
      const highpass = ctx.createBiquadFilter();
      highpass.type = "highpass";
      highpass.frequency.value = 35;
      highpass.Q.value = .5;
      const lowpass = ctx.createBiquadFilter();
      lowpass.type = "lowpass";
      lowpass.Q.value = .65;
      lowpass.frequency.setValueAtTime(1200, start);
      lowpass.frequency.exponentialRampToValueAtTime(180, start + duration);
      body.connect(highpass).connect(lowpass).connect(
        envelope(.8, .025, duration, [[.2, .55], [.6, .14]])
      );
      body.start(start);
      body.stop(start + duration);

      const thump = ctx.createOscillator();
      thump.type = "sine";
      thump.frequency.setValueAtTime(155, start);
      thump.frequency.exponentialRampToValueAtTime(72, start + .26);
      const warmth = ctx.createWaveShaper();
      const curve = new Float32Array(2049);
      for (let i = 0; i < curve.length; i++) {
        const x = i * 2 / (curve.length - 1) - 1;
        curve[i] = Math.tanh(1.2 * x) / Math.tanh(1.2);
      }
      warmth.curve = curve;
      warmth.oversample = "4x";
      thump.connect(warmth).connect(envelope(.95, .014, .26, [[.055, .6]]));
      thump.start(start);
      thump.stop(start + .26);

      const crack = ctx.createBufferSource();
      crack.buffer = buffer;
      const bright = ctx.createBiquadFilter();
      bright.type = "highpass";
      bright.frequency.value = 1000;
      bright.Q.value = .5;
      const air = ctx.createBiquadFilter();
      air.type = "lowpass";
      air.frequency.value = 3000;
      crack.connect(bright).connect(air).connect(envelope(.06, .012, .065));
      crack.start(start);
      crack.stop(start + .065);
    } else {
      const oscillator = ctx.createOscillator();
      const frequencies = {plant: [560, 672], armed: [880, 1056], spark: [160, 220], fizzle: [360, 80]};
      const [from, to] = frequencies[kind];
      oscillator.type = kind === "spark" ? "triangle" : "sine";
      oscillator.frequency.setValueAtTime(from, start);
      oscillator.frequency.exponentialRampToValueAtTime(to, start + duration);
      oscillator.connect(envelope(.18, .005, duration));
      oscillator.start(start);
      oscillator.stop(start + duration);
    }

    const buffer = await ctx.startRendering();
    const samples = buffer.getChannelData(0);
    let peak = 0;
    for (const value of samples) peak = Math.max(peak, Math.abs(value));
    // Measure after compression; the live master sets boom peaks to -1 dBFS.
    // Cues finish at -15 dBFS, about 4x the old .045 peak. No stacked voices.
    const scale = (boom ? 1 : Math.pow(10, -14 / 20)) / peak;
    for (let i = 0; i < samples.length; i++) samples[i] *= scale;
    return buffer;
  }

  function sound(kind) {
    if (frozen) return;
    try {
      context ||= new (window.AudioContext || window.webkitAudioContext)();
      if (context.state !== "running") {
        context.resume().catch(() => {});
        return;
      }
      if (!sounds[kind]) return;
      if (!master) {
        master = context.createGain();
        master.gain.value = Math.pow(10, -1 / 20);
        master.connect(context.destination);
      }
      const now = context.currentTime;
      // Fade the old voice out before the next starts, avoiding clicks or overlap.
      if (voice) {
        voice.gain.gain.cancelScheduledValues(now);
        voice.gain.gain.setValueAtTime(voice.gain.gain.value, now);
        voice.gain.gain.linearRampToValueAtTime(0, now + .006);
        voice.source.stop(now + .008);
      }
      const source = context.createBufferSource();
      const gain = context.createGain();
      source.buffer = sounds[kind];
      source.connect(gain).connect(master);
      const current = {source, gain};
      voice = current;
      source.onended = () => {
        source.disconnect();
        gain.disconnect();
        if (voice === current) voice = undefined;
      };
      source.start(now + .01);
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

  function compactBanner() {
    if (currentBoomId === undefined) return;
    const banner = byId("boom-banner");
    // Give the natural full height a numeric start so height also shrinks smoothly.
    banner.style.height = `${banner.getBoundingClientRect().height}px`;
    void banner.offsetHeight;
    banner.classList.add("compact");
    banner.style.height = "260px";
  }

  function renderScores(scores, awardedOwner) {
    clearTimeout(scoreTimer);
    byId("score-rows").replaceChildren();
    byId("score-empty").hidden = scores.length > 0;
    for (const score of scores) {
      const row = document.createElement("div");
      row.className = "score-row";
      const owner = document.createElement("span");
      owner.className = "score-owner";
      owner.textContent = score.owner;
      const points = document.createElement("strong");
      points.textContent = `${score.points} ${score.points === 1 ? "pt" : "pts"}`;
      row.append(owner, points);
      if (score.owner === awardedOwner) {
        const gain = document.createElement("span");
        gain.className = "score-gain";
        gain.textContent = "+1";
        row.append(gain);
      }
      byId("score-rows").append(row);
    }
    if (awardedOwner && !frozen) scoreTimer = setTimeout(() => {
      byId("score-rows").querySelector(".score-gain")?.remove();
    }, 1000);
  }

  function hideBanner() {
    clearTimeout(shrinkTimer);
    byId("boom-banner").classList.remove("compact");
    byId("boom-banner").style.height = "";
    byId("boom-banner").hidden = true;
    byId("false-alarm").hidden = true;
    stopBurst();
    currentBoomId = undefined;
  }

  function valid(message) {
    if (!message || typeof message !== "object") return false;
    const text = field => typeof message[field] === "string";
    const scoresValid = () => Array.isArray(message.scores) && message.scores.every(row =>
      row && typeof row.owner === "string" && Number.isInteger(row.points) && row.points > 0);
    if (["snapshot", "boom", "false_alarm", "reveal"].includes(message.type) && !scoresValid()) return false;
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
      case "reveal": return Array.isArray(message.round_top) && message.round_top.every(row =>
          row && typeof row.owner === "string" && Number.isInteger(row.booms) && row.booms > 0)
        && Number.isFinite(message.stats?.booms) && Array.isArray(message.duds)
        && message.duds.every(dud => dud && typeof dud.owner === "string" && typeof dud.word === "string");
      default: return false;
    }
  }

  function receive(message) {
    if (!valid(message)) return;
    const chip = chips.get(message.id);
    switch (message.type) {
      case "snapshot":
        renderScores(message.scores);
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
          renderScores(message.scores);
          if (currentBoomId === message.id) byId("false-alarm").hidden = false;
        } else sound({mine_armed: "armed", spark: "spark", fizzle: "fizzle"}[message.type]);
        break;
      case "boom": {
        renderScores(message.scores, message.owner);
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
        // Commit the hidden reset before showing a replacement at full size.
        void byId("boom-banner").offsetWidth;
        byId("boom-banner").hidden = false;
        burst();
        sound("boom");
        if (!frozen) shrinkTimer = setTimeout(compactBanner, BANNER_FULL_S * 1000);
        break;
      }
      case "reveal":
        renderScores(message.scores);
        hideBanner();
        {
          const count = message.stats.booms;
          const leaders = message.round_top;
          byId("round-top").textContent = leaders.length
            ? `TOP TRAPPER${leaders.length === 1 ? "" : "S"}: ${leaders.map(row => row.owner).join(", ")} · ${leaders[0].booms} boom${leaders[0].booms === 1 ? "" : "s"}`
            : count ? `${count} boom${count === 1 ? "" : "s"}` : "No booms this round";
        }
        byId("plant").hidden = true;
        byId("round-stats").textContent = `${message.stats.booms} boom${message.stats.booms === 1 ? "" : "s"}`;
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

  // Five fixed synthesized buffers, prepared once before handling game events.
  // Frozen screenshot steps need no audio work; synthesis failure stays silent.
  if (!frozen) {
    try {
      const kinds = ["boom", "plant", "armed", "spark", "fizzle"];
      const buffers = await Promise.all(kinds.map(renderSound));
      kinds.forEach((kind, index) => { sounds[kind] = buffers[index]; });
    } catch (_) { /* Audio support must not interrupt the overlay. */ }
  }

  if (demo) {
    const steps = window.overlayDemoSteps;
    const selected = Math.max(0, Math.min(steps.length - 1, Number.parseInt(query.get("step"), 10) || 0));
    function runStep(index) {
      steps[index].forEach(receive);
      if (window.overlayDemoCompactSteps.includes(index)) compactBanner();
      document.documentElement.dataset.demoStep = String(index);
    }
    if (frozen) for (let index = 0; index <= selected; index++) runStep(index);
    else {
      let index = 0;
      runStep(index);
      function next() {
        setTimeout(() => {
          index = (index + 1) % steps.length;
          runStep(index);
          next();
        }, window.overlayDemoHolds[index] || 1700);
      }
      next();
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
