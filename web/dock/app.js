"use strict";
(() => {
  const byId = id => document.getElementById(id);
  let running = false, connected = false, mines = new Map(), booms = [];
  let retry = 500;
  let socket;
  const correctionWindow = 10000;

  function render() {
    byId("round-state").textContent = running ? "Running" : "Idle";
    byId("start").disabled = !connected || running;
    byId("end").disabled = !connected || !running;
    byId("typed").disabled = byId("send").disabled = !connected || !running;
    byId("empty").hidden = mines.size > 0;
    const rows = [];
    for (const [id, mine] of mines) {
      if (mine.inactiveDeadline && mine.inactiveDeadline <= Date.now()) { mines.delete(id); continue; }
      const row = document.createElement("li");
      const owner = document.createElement("span");
      owner.className = "owner";
      owner.textContent = mine.owner;
      const status = document.createElement("span");
      status.className = "mine-status";
      const seconds = Math.max(0, Math.ceil((mine.armsDeadline - Date.now()) / 1000));
      status.textContent = mine.status === "arming" ? `arming · ${seconds}s` : mine.status;
      row.append(owner, status); rows.push(row);
    }
    byId("mines").replaceChildren(...rows);
    byId("empty").hidden = mines.size > 0;
    booms = booms.filter(boom => boom.deadline > Date.now());
    byId("false-alarm").disabled = !connected || !running || !booms.length;
  }

  function receive(event) {
    let message;
    try { message = JSON.parse(event.data); } catch { return; }
    if (!message || typeof message.type !== "string") return;
    switch (message.type) {
      case "snapshot":
        if (!message.round || !Array.isArray(message.mines)) return;
        running = message.round.running === true;
        mines = new Map(message.mines.map(mine => [mine.id, {...mine,
          armsDeadline: Date.now() + Math.max(0, mine.arms_in_s || 0) * 1000,
          inactiveDeadline: ["exploded", "false_alarm"].includes(mine.status) ? Date.now() + correctionWindow : null}]));
        booms = [];
        break;
      case "mine_planted":
        mines.set(message.id, {id:message.id, owner:message.owner, status:"arming",
          armsDeadline: Date.now() + (message.arms_in_s || 0) * 1000}); break;
      case "mine_armed": case "spark": case "fizzle": case "boom": case "false_alarm": {
        const mine = mines.get(message.id);
        if (mine) mine.status = {mine_armed:"armed", spark:"sparking", fizzle:"armed",
          boom:"exploded", false_alarm:"false_alarm"}[message.type];
        if (message.type === "boom") {
          const deadline = Math.min(Date.now() + correctionWindow, message.at * 1000 + correctionWindow);
          booms.push({id:message.id, deadline});
          if (mine) mine.inactiveDeadline = deadline;
        }
        if (message.type === "false_alarm") booms = booms.filter(boom => boom.id !== message.id);
        break;
      }
      case "reveal": running = false; mines.clear(); booms = []; break;
      case "status":
        for (const name of ["mic", "engine", "deepgram", "eventsub", "tunnel"]) {
          const state = name === "tunnel" ? (message.tunnel_url ? "connected" : "disconnected") : message[name];
          document.querySelector(`[data-health="${name}"]`).dataset.state = state === "connected" ? "connected" : "disconnected";
        }
        break;
      default: return;
    }
    render();
  }

  async function post(path, body) {
    byId("error").textContent = "";
    try {
      const response = await fetch(path, {method:"POST", headers:{"Content-Type":"application/json"},
        body:body ? JSON.stringify(body) : undefined});
      if (!response.ok) { byId("error").textContent = "Action rejected. Check the round and try again."; return false; }
      return true;
    } catch { byId("error").textContent = "Connection lost. Reconnecting automatically."; return false; }
  }
  byId("start").onclick = () => post("/dock/round/start");
  byId("end").onclick = () => post("/dock/round/end");
  byId("false-alarm").onclick = () => post("/dock/false-alarm");
  byId("typed-form").onsubmit = async event => {
    event.preventDefault();
    const text = byId("typed").value.trim();
    if (text && await post("/dock/typed", {text})) byId("typed").value = "";
  };
  function connect() {
    socket = new WebSocket(`${location.protocol === "https:" ? "wss" : "ws"}://${location.host}/ws/dock`);
    socket.onopen = () => { connected = true; retry = 500; byId("connection").textContent = "Connected"; render(); };
    socket.onmessage = receive;
    socket.onclose = () => {
      connected = false; byId("connection").textContent = "Disconnected · reconnecting…"; render();
      setTimeout(connect, retry); retry = Math.min(retry * 2, 8000);
    };
    socket.onerror = () => socket.close();
  }
  setInterval(() => {
    const expired = booms.some(boom => boom.deadline <= Date.now());
    if (expired || [...mines.values()].some(mine => mine.status === "arming" ||
      (mine.inactiveDeadline && mine.inactiveDeadline <= Date.now()))) render();
  }, 100);
  connect();
})();
