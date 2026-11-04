/**
 * SIMULADOR DE TRANSMISIÓN S-TRONIC DL501 (0B5) — AUDI Q5 2.0 TFSI (2012)
 * Cátedra de Trenes de Potencia — Creado para Grupo 04
 * Control de estados electrohidráulicos, comunicación CAN-Bus y diagrama interactivo SVG.
 */

// Estado global de la aplicación
const AppState = {
  currentGear: 'D',
  speed: 45,       // km/h
  throttle: 35,    // % TPS
  atfTemp: 84.5,   // °C
  telemetryDebounceTimer: null
};

// Base positions para pistones en SVG (centrados en Neutro)
const PISTON_BASE_X = {
  '1-3': 55,
  '2-R': 195,
  '5-7': 338,
  '4-6': 483
};

/**
 * Inicialización al cargar el DOM
 */
document.addEventListener('DOMContentLoaded', () => {
  console.log('[S-tronic DL501] Inicializando simulador mecatrónico...');
  // Cargar estado inicial (D)
  selectGear('D');
  
  // Iniciar telemetría con valores predeterminados
  fetchTelemetry();

  // Pequeña oscilación simulada de temperatura ATF (84.0 - 85.5 °C)
  setInterval(() => {
    AppState.atfTemp = (84.0 + Math.random() * 1.5).toFixed(1);
    const tempEl = document.getElementById('hdr-temp');
    if (tempEl) tempEl.textContent = AppState.atfTemp;
  }, 4000);
});

/**
 * Selección de marcha desde botones de la interfaz
 * @param {string} gear - 'P', 'R', 'N', 'D', 'M1'...'M8'
 */
async function selectGear(gear) {
  AppState.currentGear = gear;

  // 1. Actualizar apariencia de los botones del selector
  updateGearButtonsUI(gear);

  // 2. Actualizar badge de marcha actual
  const badge = document.getElementById('current-gear-badge');
  if (badge) {
    badge.textContent = `MARCHA: ${gear}`;
  }

  // 3. Consultar datos técnicos detallados al backend Flask
  try {
    const response = await fetch(`/api/gear/${encodeURIComponent(gear)}`);
    if (!response.ok) throw new Error(`HTTP Error: ${response.status}`);
    const data = await response.json();

    // 4. Renderizar todos los subsistemas con la respuesta
    renderGearState(data);
    
    // 5. Actualizar telemetría dinámica para la nueva relación de transmisión
    fetchTelemetry();

    // 6. Log en la consola de diagnóstico
    logToConsole(`CAN-Tx: Comando de marcha [${gear}] ejecutado por J743.`);
  } catch (err) {
    console.error('Error al obtener datos de marcha:', err);
    logToConsole(`ERR: Falla al comunicar con ECU/TCU: ${err.message}`, 'error');
  }
}

/**
 * Actualiza clases CSS de los botones de marchas
 */
function updateGearButtonsUI(activeGear) {
  const allGearButtons = document.querySelectorAll('.btn-gear');
  allGearButtons.forEach(btn => {
    // Resetear a estilo inactivo
    btn.className = 'btn-gear py-2 lg:py-2.5 rounded-lg font-mono font-bold text-xs lg:text-sm border transition-all duration-150 flex flex-col items-center justify-center bg-slate-900 border-slate-800 hover:border-slate-600 text-slate-300';
  });

  const activeBtn = document.getElementById(`btn-gear-${activeGear}`);
  if (activeBtn) {
    if (activeGear === 'P') {
      activeBtn.className = 'btn-gear py-2 lg:py-2.5 rounded-lg font-mono font-bold text-xs lg:text-sm border transition-all duration-150 flex flex-col items-center justify-center bg-amber-600 border-amber-500 text-white shadow-lg shadow-amber-600/30';
    } else if (activeGear === 'R') {
      activeBtn.className = 'btn-gear py-2 lg:py-2.5 rounded-lg font-mono font-bold text-xs lg:text-sm border transition-all duration-150 flex flex-col items-center justify-center bg-purple-600 border-purple-500 text-white shadow-lg shadow-purple-600/30';
    } else if (activeGear === 'N') {
      activeBtn.className = 'btn-gear py-2 lg:py-2.5 rounded-lg font-mono font-bold text-xs lg:text-sm border transition-all duration-150 flex flex-col items-center justify-center bg-slate-700 border-slate-500 text-white shadow-lg';
    } else {
      activeBtn.className = 'btn-gear py-2 lg:py-2.5 rounded-lg font-mono font-bold text-xs lg:text-sm border transition-all duration-150 flex flex-col items-center justify-center bg-audi-red border-red-500 text-white shadow-lg shadow-red-600/30';
    }
  }
}

/**
 * Renderiza el estado completo recibido del backend Flask
 */
function renderGearState(data) {
  // A. Embragues K1 y K2
  const k1 = data.clutches.K1;
  const k2 = data.clutches.K2;

  // K1
  const k1Bar = document.getElementById('k1-bar');
  const k1PctLabel = document.getElementById('k1-pct-label');
  const k1PressLabel = document.getElementById('k1-press-label');
  if (k1Bar) k1Bar.style.width = `${k1.engagement_pct}%`;
  if (k1PctLabel) {
    k1PctLabel.textContent = `${k1.engagement_pct} % (${k1.status})`;
    k1PctLabel.className = `font-mono font-bold ${k1.engagement_pct > 0 ? 'text-audi-red' : 'text-slate-500'}`;
  }
  if (k1PressLabel) k1PressLabel.textContent = `${k1.pressure_bar.toFixed(2)} bar`;

  // K2
  const k2Bar = document.getElementById('k2-bar');
  const k2PctLabel = document.getElementById('k2-pct-label');
  const k2PressLabel = document.getElementById('k2-press-label');
  if (k2Bar) k2Bar.style.width = `${k2.engagement_pct}%`;
  if (k2PctLabel) {
    k2PctLabel.textContent = `${k2.engagement_pct} % (${k2.status})`;
    k2PctLabel.className = `font-mono font-bold ${k2.engagement_pct > 0 ? 'text-audi-cyan' : 'text-slate-500'}`;
  }
  if (k2PressLabel) k2PressLabel.textContent = `${k2.pressure_bar.toFixed(2)} bar`;

  // B. Horquillas selectoras
  const forks = data.shift_forks;
  updateForkUI('fork-1-3', forks['1-3']);
  updateForkUI('fork-2-R', forks['2-R']);
  updateForkUI('fork-5-7', forks['5-7']);
  updateForkUI('fork-4-6', forks['4-6']);

  // C. Actualizar Diagrama SVG del Cuerpo de Válvulas
  updateSVGSchematic(data);

  // D. Actualizar Tabla de Solenoides
  updateSolenoidTable(data.solenoids);

  // E. Actualizar Pasos de Flujo Hidráulico
  updateFluidFlowSteps(data.fluid_flow_steps);

  // F. Actualizar Resumen Técnico
  const summaryEl = document.getElementById('gear-tech-summary');
  if (summaryEl) {
    summaryEl.textContent = data.technical_explanation;
  }
}

/**
 * Actualiza el indicador visual de una horquilla selectora
 */
function updateForkUI(elementId, forkData) {
  const el = document.getElementById(elementId);
  if (!el || !forkData) return;

  const mm = forkData.position_mm >= 0 ? `+${forkData.position_mm.toFixed(1)}` : `${forkData.position_mm.toFixed(1)}`;
  el.textContent = `${mm} mm (${forkData.status})`;

  if (forkData.status === 'Engaged') {
    el.className = 'font-bold text-emerald-400';
  } else if (forkData.status === 'Preselected') {
    el.className = 'font-bold text-audi-amber';
  } else {
    el.className = 'font-bold text-slate-500';
  }
}

/**
 * Actualiza el diagrama esquemático SVG interactivo
 */
function updateSVGSchematic(data) {
  const solenoids = data.solenoids;

  // Actualizar cada válvula en el SVG
  for (const [code, sol] of Object.entries(solenoids)) {
    const rect = document.getElementById(`rect-${code}`);
    const pressText = document.getElementById(`svg-press-${code}`);
    const stateText = document.getElementById(`svg-state-${code}`);

    let fillUrl = 'url(#grad-off)';
    let strokeColor = '#334155';

    if (sol.state === 'ON' || sol.pressure_bar > 4.0 || sol.pwm_pct > 50) {
      fillUrl = 'url(#grad-active)';
      strokeColor = '#EF4444';
    } else if (sol.state === 'Preselected' || (sol.pressure_bar > 0 && sol.pressure_bar <= 4.0) || (sol.pwm_pct > 0 && sol.pwm_pct <= 50)) {
      fillUrl = 'url(#grad-pre)';
      strokeColor = '#F59E0B';
    }

    if (rect) {
      rect.setAttribute('fill', fillUrl);
      rect.setAttribute('stroke', strokeColor);
    }

    if (pressText) {
      pressText.textContent = `${sol.pressure_bar.toFixed(1)} bar (${sol.pwm_pct}%)`;
    }

    if (stateText) {
      stateText.textContent = `${sol.state}`;
      stateText.setAttribute('fill', sol.state === 'ON' ? '#F87171' : (sol.state === 'Preselected' ? '#FDE68A' : '#64748B'));
    }
  }

  // Actualizar embragues en SVG
  const svgK1 = document.getElementById('svg-k1-clutch');
  if (svgK1) {
    if (data.clutches.K1.engagement_pct > 0) {
      svgK1.setAttribute('fill', '#7F1D1D');
      svgK1.setAttribute('stroke', '#EF4444');
    } else {
      svgK1.setAttribute('fill', '#1E293B');
      svgK1.setAttribute('stroke', '#334155');
    }
  }

  const svgK2 = document.getElementById('svg-k2-clutch');
  if (svgK2) {
    if (data.clutches.K2.engagement_pct > 0) {
      svgK2.setAttribute('fill', '#0C4A6E');
      svgK2.setAttribute('stroke', '#38BDF8');
    } else {
      svgK2.setAttribute('fill', '#1E293B');
      svgK2.setAttribute('stroke', '#334155');
    }
  }

  // Animar / desplazar los pistones de horquilla en el SVG
  const forks = data.shift_forks;
  updatePistonPosition('1-3', forks['1-3']?.position_mm);
  updatePistonPosition('2-R', forks['2-R']?.position_mm);
  updatePistonPosition('5-7', forks['5-7']?.position_mm);
  updatePistonPosition('4-6', forks['4-6']?.position_mm);
}

/**
 * Ajusta la coordenada X del pistón hidráulico según su desplazamiento real en mm
 */
function updatePistonPosition(forkKey, positionMm) {
  const piston = document.getElementById(`svg-piston-${forkKey}`);
  if (!piston || positionMm === undefined) return;

  const baseX = PISTON_BASE_X[forkKey];
  // Factor de escala: +8.5 mm -> +15 px en SVG; -8.5 mm -> -15 px
  const offsetPx = (positionMm / 8.5) * 15;
  const newX = baseX + offsetPx;
  
  piston.setAttribute('x', newX);

  if (Math.abs(positionMm) > 2) {
    piston.setAttribute('fill', positionMm > 0 ? '#10B981' : '#F59E0B');
  } else {
    piston.setAttribute('fill', '#475569');
  }
}

/**
 * Llena la tabla interactiva con la matriz de solenoides
 */
function updateSolenoidTable(solenoids) {
  const tbody = document.getElementById('solenoid-table-body');
  if (!tbody) return;

  tbody.innerHTML = '';

  for (const [code, sol] of Object.entries(solenoids)) {
    const tr = document.createElement('tr');
    tr.className = 'hover:bg-slate-800/40 transition-colors border-b border-slate-800/60';

    // Badge de estado
    let badgeClass = 'bg-slate-800 text-slate-400 border border-slate-700';
    if (sol.state === 'ON') {
      badgeClass = 'bg-red-500/10 text-red-400 border border-red-500/30';
    } else if (sol.state === 'Preselected') {
      badgeClass = 'bg-amber-500/10 text-amber-400 border border-amber-500/30';
    }

    tr.innerHTML = `
      <td class="py-2.5 px-3 font-bold text-white">${code}</td>
      <td class="py-2.5 px-3 text-slate-400">${sol.generic_code}</td>
      <td class="py-2.5 px-3 font-sans text-slate-300 text-[11px]">${sol.function}</td>
      <td class="py-2.5 px-3 text-center">
        <span class="inline-block px-2 py-0.5 rounded text-[10px] font-bold ${badgeClass}">
          ${sol.state}
        </span>
      </td>
      <td class="py-2.5 px-3 text-center text-slate-300">${sol.voltage_v.toFixed(1)} V</td>
      <td class="py-2.5 px-3 text-center text-slate-300">${sol.current_ma.toFixed(0)} mA</td>
      <td class="py-2.5 px-3 text-center font-bold ${sol.pwm_pct > 0 ? 'text-audi-cyan' : 'text-slate-500'}">
        ${sol.pwm_pct}%
      </td>
      <td class="py-2.5 px-3 text-right font-bold ${sol.pressure_bar > 0 ? 'text-emerald-400' : 'text-slate-500'}">
        ${sol.pressure_bar.toFixed(1)} bar
      </td>
    `;
    tbody.appendChild(tr);
  }
}

/**
 * Renderiza la lista paso a paso del flujo hidráulico
 */
function updateFluidFlowSteps(steps) {
  const list = document.getElementById('fluid-steps-list');
  if (!list || !steps) return;

  list.innerHTML = '';
  steps.forEach((step, index) => {
    const li = document.createElement('li');
    li.className = 'flex items-start gap-2.5';
    li.innerHTML = `
      <span class="flex-shrink-0 w-5 h-5 rounded-full bg-slate-800 text-audi-cyan border border-slate-700 flex items-center justify-center font-mono text-[10px] font-bold mt-0.5">
        ${index + 1}
      </span>
      <span class="flex-1">${step}</span>
    `;
    list.appendChild(li);
  });
}

/**
 * Escucha cambios en el slider de velocidad
 */
function onSpeedChange(val) {
  AppState.speed = parseFloat(val);
  const label = document.getElementById('slider-speed-val');
  if (label) label.textContent = `${val} km/h`;

  const hdrSpeed = document.getElementById('hdr-speed');
  if (hdrSpeed) hdrSpeed.textContent = parseFloat(val).toFixed(1);

  debounceTelemetry();
}

/**
 * Escucha cambios en el slider de acelerador
 */
function onThrottleChange(val) {
  AppState.throttle = parseFloat(val);
  const label = document.getElementById('slider-throttle-val');
  if (label) label.textContent = `${val} %`;

  debounceTelemetry();
}

/**
 * Debounce para evitar sobrecargar llamadas a /api/telemetry durante arrastre de sliders
 */
function debounceTelemetry() {
  clearTimeout(AppState.telemetryDebounceTimer);
  AppState.telemetryDebounceTimer = setTimeout(() => {
    fetchTelemetry();
  }, 60);
}

/**
 * Consulta endpoint de telemetría dinámica
 */
async function fetchTelemetry() {
  try {
    const url = `/api/telemetry?gear=${encodeURIComponent(AppState.currentGear)}&speed=${AppState.speed}&throttle=${AppState.throttle}`;
    const res = await fetch(url);
    if (!res.ok) throw new Error(`HTTP Error: ${res.status}`);
    const data = await res.json();

    // Actualizar Header RPM
    const hdrRpm = document.getElementById('hdr-rpm');
    if (hdrRpm) {
      hdrRpm.textContent = Math.round(data.engine_rpm);
      if (data.engine_rpm > 5500) {
        hdrRpm.className = 'text-sm font-bold text-audi-red animate-pulse';
      } else {
        hdrRpm.className = 'text-sm font-bold text-white';
      }
    }

    // Actualizar Métricas de Par y Relación
    const metricRatio = document.getElementById('metric-ratio');
    if (metricRatio) metricRatio.textContent = `${data.total_ratio.toFixed(3)}:1`;

    const metricTorque = document.getElementById('metric-torque');
    if (metricTorque) metricTorque.textContent = `${Math.round(data.wheel_torque_nm).toLocaleString()} Nm`;

    const metricFront = document.getElementById('metric-front-tq');
    if (metricFront) metricFront.textContent = `${Math.round(data.front_axle_torque_nm).toLocaleString()} Nm`;

    const metricRear = document.getElementById('metric-rear-tq');
    if (metricRear) metricRear.textContent = `${Math.round(data.rear_axle_torque_nm).toLocaleString()} Nm`;

    // Presión de línea modulada por carga
    const rectN472 = document.getElementById('rect-N472');
    const pressN472 = document.getElementById('svg-press-N472');
    if (pressN472) {
      pressN472.textContent = `${data.line_pressure_bar.toFixed(1)} bar`;
    }
  } catch (err) {
    console.error('Error al actualizar telemetría dinámica:', err);
  }
}

/**
 * Ejecuta barrido de diagnóstico VAS 6154 / VCDS sobre la mecatrónica J743
 */
async function runDiagnosticsScan() {
  logToConsole('----------------------------------------');
  logToConsole('>> INICIANDO AUTO-DIAGNÓSTICO TCU J743...');
  
  const btn = document.getElementById('btn-run-diag');
  if (btn) {
    btn.disabled = true;
    btn.innerHTML = `<span class="animate-spin">⚙</span> <span>Diagnosticando...</span>`;
  }

  try {
    const res = await fetch('/api/diagnostics');
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();

    setTimeout(() => {
      logToConsole(`Protocolo: ${data.protocol} | Módulo: ${data.module_address}`);
      logToConsole(`Part Number: ${data.part_number} | Calibración: ${data.software_version}`);
      
      data.checks.forEach(chk => {
        logToConsole(`✔ ${chk.name}: ${chk.value} (${chk.result})`);
      });

      logToConsole(`>> DTC Activos: ${data.dtc_codes.length} encontrados.`);
      logToConsole('>> Diagnóstico J743 completado exitosamente. Estado: 100% OPERATIVO.', 'success');

      if (btn) {
        btn.disabled = false;
        btn.innerHTML = `<svg class="w-3.5 h-3.5 text-audi-cyan" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg><span>Diagnóstico TCU J743</span>`;
      }
    }, 600);

  } catch (err) {
    logToConsole(`ERR: Error en enlace de diagnóstico: ${err.message}`, 'error');
    if (btn) {
      btn.disabled = false;
      btn.innerHTML = `<span>Reintentar Diagnóstico</span>`;
    }
  }
}

/**
 * Agrega un mensaje a la consola de diagnóstico en pantalla
 */
function logToConsole(message, type = 'normal') {
  const consoleEl = document.getElementById('diagnostic-console');
  if (!consoleEl) return;

  const now = new Date();
  const timeStr = `${String(now.getHours()).padStart(2, '0')}:${String(now.getMinutes()).padStart(2, '0')}:${String(now.getSeconds()).padStart(2, '0')}.${String(Math.floor(now.getMilliseconds() / 10)).padStart(2, '0')}`;

  const line = document.createElement('div');
  if (type === 'error') {
    line.className = 'text-red-400 font-bold';
    line.textContent = `[${timeStr}] ${message}`;
  } else if (type === 'success') {
    line.className = 'text-emerald-400 font-bold';
    line.textContent = `[${timeStr}] ${message}`;
  } else {
    line.className = message.startsWith('>>') ? 'text-audi-cyan' : 'text-slate-300';
    line.textContent = `[${timeStr}] ${message}`;
  }

  consoleEl.appendChild(line);
  consoleEl.scrollTop = consoleEl.scrollHeight;
}

/**
 * Limpia el terminal de diagnóstico
 */
function clearConsole() {
  const consoleEl = document.getElementById('diagnostic-console');
  if (consoleEl) {
    consoleEl.innerHTML = '<div class="text-slate-500">// Terminal reseteado. Sistema de diagnóstico VAS listo.</div>';
  }
}
