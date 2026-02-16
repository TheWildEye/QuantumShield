async function loadJSON(path) {
  const r = await fetch(path);
  return r.json();
}

function severityClass(sev) {
  return sev.toLowerCase();
}

function exportPDF() {
  fetch("/export-pdf")
    .then(() => alert("PDF export triggered. Check project directory."))
    .catch(() => alert("PDF export failed."));
}

async function render() {
  const state = await loadJSON("runtime_state.json");
  const events = await loadJSON("events.json");

  // Status
  const statusEl = document.getElementById("status");
  if (state.status === "crypto_failure") {
    statusEl.textContent = "Security Degraded";
    statusEl.className = "status fail";
  } else {
    statusEl.textContent = "Quantum-Safe";
    statusEl.className = "status ok";
  }

  // Crypto
  document.getElementById("crypto").innerHTML = `
    <li>Transport: ${state.transport}</li>
    <li>KEM: ${state.kem}</li>
    <li>Signature: ${state.signature}</li>
    <li>Hash: ${state.hash}</li>
  `;

  // Events
  const tbody = document.getElementById("events");
  tbody.innerHTML = "";
  events.slice().reverse().forEach(e => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${e.time}</td>
      <td>${e.category}</td>
      <td>${e.event}</td>
      <td class="${e.result.toLowerCase()}">${e.result}</td>
      <td class="${severityClass(e.severity)}">${e.severity}</td>
    `;
    tbody.appendChild(tr);
  });

  if (events.length) {
    document.getElementById("lastEvent").textContent =
      events[events.length - 1].event;
  }
}

render();
setInterval(render, 3000);
