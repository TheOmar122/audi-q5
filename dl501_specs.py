"""
Audi Q5 2.0 TFSI (2012) - Transmisión S-tronic DL501 (0B5)
Base de datos técnica del cuerpo de válvulas, solenoides y cinemática de marchas.
"""

VEHICLE_INFO = {
    "model": "Audi Q5 2.0 TFSI Quattro S-tronic",
    "year": 2012,
    "engine": "2.0 TFSI EA888 Gen 2 (CDNC)",
    "displacement_cc": 1984,
    "nominal_power_hp": 211,
    "nominal_torque_nm": 350,
    "transmission_model": "S-tronic 0B5 (DL501)",
    "transmission_type": "Doble embrague húmedo longitudinal de 7 velocidades",
    "max_torque_capacity_nm": 550,
    "drivetrain": "Tracción integral permanente Quattro con diferencial central Torsen C (40:60)",
    "atf_fluid_spec": "G 052 529 A2 (Circuito de embragues y mecatrónica: ~7.0 L)",
    "gear_oil_spec": "G 055 532 A2 (Circuito de engranajes y Torsen: ~4.5 L)"
}

SOLENOID_DEFINITIONS = {
    "N433": {
        "audi_code": "N433",
        "generic_code": "N88",
        "role": "Válvula de selección de horquilla 1-3 (Subtransmisión 1)",
        "type": "Solenoide de conmutación ON/OFF (Pilotaje de corredera hidráulica)",
        "resistance_ohms": 4.8,
        "max_voltage_v": 12.0,
        "location": "Placa Mechatronic J743 - Módulo de válvulas inferior",
        "description": "Comanda el cilindro de doble efecto para engranar 1.ª o 3.ª marcha en el eje secundario 1."
    },
    "N437": {
        "audi_code": "N437",
        "generic_code": "N89",
        "role": "Válvula de selección de horquilla 2-R (Subtransmisión 2)",
        "type": "Solenoide de conmutación ON/OFF (Pilotaje de corredera hidráulica)",
        "resistance_ohms": 4.8,
        "max_voltage_v": 12.0,
        "location": "Placa Mechatronic J743 - Módulo de válvulas inferior",
        "description": "Comanda el cilindro selector para engranar 2.ª marcha o Reversa (R) en el eje secundario 2."
    },
    "N434": {
        "audi_code": "N434",
        "generic_code": "N90",
        "role": "Válvula de selección de horquilla 5-7 (Subtransmisión 1)",
        "type": "Solenoide de conmutación ON/OFF (Pilotaje de corredera hidráulica)",
        "resistance_ohms": 4.8,
        "max_voltage_v": 12.0,
        "location": "Placa Mechatronic J743 - Módulo de válvulas superior",
        "description": "Desplaza el sincronizador de 5.ª o 7.ª marcha en la subtransmisión impar."
    },
    "N438": {
        "audi_code": "N438",
        "generic_code": "N91",
        "role": "Válvula de selección de horquilla 4-6 (Subtransmisión 2)",
        "type": "Solenoide de conmutación ON/OFF (Pilotaje de corredera hidráulica)",
        "resistance_ohms": 4.8,
        "max_voltage_v": 12.0,
        "location": "Placa Mechatronic J743 - Módulo de válvulas superior",
        "description": "Desplaza el sincronizador de 4.ª o 6.ª marcha en la subtransmisión par."
    },
    "N435": {
        "audi_code": "N435",
        "generic_code": "N92",
        "role": "Válvula de seguridad y corte del embrague K1",
        "type": "Solenoide de seguridad ON/OFF (Corte rápido)",
        "resistance_ohms": 4.8,
        "max_voltage_v": 12.0,
        "location": "Mechatronic J743 - Circuito primario K1",
        "description": "Habilita o bloquea de emergencia el flujo de presión hacia el pistón del embrague impar K1."
    },
    "N436": {
        "audi_code": "N436",
        "generic_code": "EPC K1 / EDS1",
        "role": "Regulador de presión proporcional del embrague K1 (VFS PWM)",
        "type": "Solenoide proporcional de fuerza variable (VFS) modulado por PWM a 1000 Hz",
        "resistance_ohms": 4.8,
        "max_voltage_v": 13.5,
        "location": "Mechatronic J743 - Control modulado K1",
        "description": "Modula progresivamente la presión de acoplamiento de K1 (0 a 10 bar) para arranque y cambios suaves."
    },
    "N439": {
        "audi_code": "N439",
        "generic_code": "N93",
        "role": "Válvula de seguridad y corte del embrague K2",
        "type": "Solenoide de seguridad ON/OFF (Corte rápido)",
        "resistance_ohms": 4.8,
        "max_voltage_v": 12.0,
        "location": "Mechatronic J743 - Circuito primario K2",
        "description": "Habilita o bloquea de emergencia el paso hidráulico hacia el embrague par/reversa K2."
    },
    "N440": {
        "audi_code": "N440",
        "generic_code": "EPC K2 / EDS2",
        "role": "Regulador de presión proporcional del embrague K2 (VFS PWM)",
        "type": "Solenoide proporcional de fuerza variable (VFS) modulado por PWM a 1000 Hz",
        "resistance_ohms": 4.8,
        "max_voltage_v": 13.5,
        "location": "Mechatronic J743 - Control modulado K2",
        "description": "Modula progresivamente la presión de acoplamiento de K2 (0 a 10 bar) para cambios impares a pares."
    },
    "N471": {
        "audi_code": "N471",
        "generic_code": "Cooling Valve",
        "role": "Válvula moduladora de caudal de refrigeración del ATF",
        "type": "Solenoide proporcional PWM (0-100%)",
        "resistance_ohms": 4.8,
        "max_voltage_v": 13.5,
        "location": "Mechatronic J743 - Circuito térmico",
        "description": "Regula el caudal de aceite que baña los paquetes multidisco K1 y K2 en función de la temperatura G509."
    },
    "N472": {
        "audi_code": "N472",
        "generic_code": "EPC Main / EDS3",
        "role": "Regulador de presión principal del sistema hidráulico (Main Line Pressure)",
        "type": "Solenoide proporcional PWM (Frecuencia constante)",
        "resistance_ohms": 4.8,
        "max_voltage_v": 13.5,
        "location": "Mechatronic J743 - Salida de bomba ATF",
        "description": "Regula la presión de línea del sistema mecatrónico entre 5.0 y 16.0 bar para todo el cuerpo de válvulas."
    }
}

# Definición técnica de estados por marcha
GEAR_STATES = {
    "P": {
        "gear_name": "Park (Estacionamiento)",
        "gear_code": "P",
        "ratio": 0.0,
        "active_clutch": "Ninguno (K1 y K2 abiertos)",
        "clutch_k1_pct": 0,
        "clutch_k2_pct": 0,
        "mechanical_lock": "Trinquete de bloqueo mecánico de estacionamiento engranado en la corona diferencial",
        "fork_status": {
            "fork_1_3": "Neutral (0.0 mm)",
            "fork_2_R": "Neutral (0.0 mm)",
            "fork_5_7": "Neutral (0.0 mm)",
            "fork_4_6": "Neutral (0.0 mm)"
        },
        "solenoids": {
            "N433": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N437": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N434": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N438": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N435": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N436": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N439": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N440": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N471": {"state": "ACTIVE", "voltage_v": 4.5, "current_ma": 350, "pwm_pct": 30, "pressure_bar": 2.5},
            "N472": {"state": "ACTIVE", "voltage_v": 6.8, "current_ma": 580, "pwm_pct": 45, "pressure_bar": 5.5}
        },
        "fluid_flow_path": [
            "Bomba hidráulica de aceite ATF accionada por engranaje intermedio desde el volante motor.",
            "La válvula de presión principal N472 (EPC) regula la línea a 5.5 bar de lubricación estática.",
            "Válvulas de embrague N435 y N439 cerradas; conductos K1 y K2 drenados hacia el cárter inferior.",
            "Todas las cámaras de los cilindros selectores de horquilla permanecen despresurizadas.",
            "El aceite circula por el circuito de recirculación y enfriador a través de la válvula N471."
        ],
        "technical_summary": "La transmisión está completamente desacoplada de la fuerza motriz del motor. Un trinquete mecánico bloquea el eje de salida hacia el diferencial Torsen. Las válvulas de embrague están desexcitadas por seguridad para evitar cualquier transmisión de par accidental."
    },
    "R": {
        "gear_name": "Reversa (Marcha Atrás)",
        "gear_code": "R",
        "ratio": 3.375,
        "active_clutch": "K2 (Embrague interior - Eje primario hueco)",
        "clutch_k1_pct": 0,
        "clutch_k2_pct": 100,
        "mechanical_lock": "Desbloqueado",
        "fork_status": {
            "fork_1_3": "Neutral (0.0 mm)",
            "fork_2_R": "Posición Reversa (-8.5 mm hacia piñón loco R)",
            "fork_5_7": "Neutral (0.0 mm)",
            "fork_4_6": "Neutral (0.0 mm)"
        },
        "solenoids": {
            "N433": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N437": {"state": "ACTIVE", "voltage_v": 12.0, "current_ma": 850, "pwm_pct": 100, "pressure_bar": 4.8},
            "N434": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N438": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N435": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N436": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N439": {"state": "ACTIVE", "voltage_v": 12.0, "current_ma": 800, "pwm_pct": 100, "pressure_bar": 8.5},
            "N440": {"state": "ACTIVE", "voltage_v": 9.8, "current_ma": 780, "pwm_pct": 75, "pressure_bar": 8.5},
            "N471": {"state": "ACTIVE", "voltage_v": 6.2, "current_ma": 500, "pwm_pct": 45, "pressure_bar": 3.8},
            "N472": {"state": "ACTIVE", "voltage_v": 11.5, "current_ma": 920, "pwm_pct": 82, "pressure_bar": 12.0}
        },
        "fluid_flow_path": [
            "Bomba genera caudal de alta presión; N472 (EPC) eleva la presión de línea a 12.0 bar.",
            "Solenoide N437 conmuta a ON: canaliza aceite a 4.8 bar hacia la cámara de reversa del cilindro selector 2-R.",
            "La horquilla 2-R se desplaza -8.5 mm engranando el inversor de marcha en el eje secundario 2.",
            "Sensor Hall G489 valida el acoplamiento mecánico.",
            "La válvula de seguridad N439 abre el paso hidráulico hacia el embrague K2.",
            "El solenoide proporcional N440 genera una rampa de presión controlada de 8.5 bar sobre el pistón de K2, transmitiendo par invertido a las ruedas."
        ],
        "technical_summary": "La reversa utiliza la subtransmisión 2 (eje concéntrico hueco accionado por el embrague K2). Un piñón intermedio invierte el sentido de rotación hacia el árbol secundario y de allí hacia el diferencial central Torsen."
    },
    "N": {
        "gear_name": "Neutral (Punto Muerto)",
        "gear_code": "N",
        "ratio": 0.0,
        "active_clutch": "Ninguno (K1 y K2 abiertos)",
        "clutch_k1_pct": 0,
        "clutch_k2_pct": 0,
        "mechanical_lock": "Desbloqueado (Ruedas libres)",
        "fork_status": {
            "fork_1_3": "Neutral (0.0 mm)",
            "fork_2_R": "Neutral (0.0 mm)",
            "fork_5_7": "Neutral (0.0 mm)",
            "fork_4_6": "Neutral (0.0 mm)"
        },
        "solenoids": {
            "N433": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N437": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N434": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N438": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N435": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N436": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N439": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N440": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N471": {"state": "ACTIVE", "voltage_v": 4.5, "current_ma": 350, "pwm_pct": 30, "pressure_bar": 2.5},
            "N472": {"state": "ACTIVE", "voltage_v": 6.8, "current_ma": 580, "pwm_pct": 45, "pressure_bar": 5.5}
        },
        "fluid_flow_path": [
            "Bomba hidráulica mantiene línea base a 5.5 bar regulada por N472.",
            "Pistones de K1 y K2 descargados totalmente al cárter.",
            "Horquillas hidráulicas centradas en reposo.",
            "Flujo constante de enfriamiento a baja presión hacia los paquetes de fricción."
        ],
        "technical_summary": "Punto muerto sin retención mecánica. No existe arrastre viscoso residual significativo. La centralita J743 monitorea constantemente la velocidad de las ruedas y la posición de la palanca selectora."
    },
    "D": {
        "gear_name": "Drive (Modo Automático - 1.ª Marcha Activa con Preselección de 2.ª)",
        "gear_code": "D",
        "ratio": 3.692,
        "active_clutch": "K1 (Embrague exterior acoplado) + K2 en standby",
        "clutch_k1_pct": 100,
        "clutch_k2_pct": 0,
        "mechanical_lock": "Desbloqueado",
        "fork_status": {
            "fork_1_3": "Engranada 1.ª (+8.5 mm)",
            "fork_2_R": "Preseleccionada 2.ª (+8.5 mm)",
            "fork_5_7": "Neutral (0.0 mm)",
            "fork_4_6": "Neutral (0.0 mm)"
        },
        "solenoids": {
            "N433": {"state": "ACTIVE", "voltage_v": 12.0, "current_ma": 850, "pwm_pct": 100, "pressure_bar": 4.8},
            "N437": {"state": "PRESELECT", "voltage_v": 12.0, "current_ma": 850, "pwm_pct": 100, "pressure_bar": 4.8},
            "N434": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N438": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N435": {"state": "ACTIVE", "voltage_v": 12.0, "current_ma": 800, "pwm_pct": 100, "pressure_bar": 9.2},
            "N436": {"state": "ACTIVE", "voltage_v": 10.5, "current_ma": 820, "pwm_pct": 82, "pressure_bar": 9.2},
            "N439": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N440": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N471": {"state": "ACTIVE", "voltage_v": 7.5, "current_ma": 600, "pwm_pct": 55, "pressure_bar": 4.2},
            "N472": {"state": "ACTIVE", "voltage_v": 12.5, "current_ma": 980, "pwm_pct": 90, "pressure_bar": 14.5}
        },
        "fluid_flow_path": [
            "Línea principal presurizada a 14.5 bar por N472 (EPC).",
            "N433 activo presuriza el vástago de la horquilla 1-3 engranando la 1.ª marcha.",
            "N437 presuriza la horquilla 2-R engranando mecánicamente la 2.ª marcha de forma preventiva.",
            "N435 abierto y N436 regulando a 9.2 bar hacia el émbolo de empuje de K1.",
            "K2 permanece sin presión (N440 en 0 bar), girando en vacío el engranaje de 2.ª sin transferir par hasta que ocurra el cambio sin interrupción de potencia."
        ],
        "technical_summary": "En 'D', la transmisión arranca en 1.ª marcha con el embrague K1 totalmente cerrado y sincroniza simultáneamente la 2.ª marcha en el eje par. El cambio ascendente a 2.ª se realiza en menos de 0.2 segundos cruzando las presiones entre K1 y K2."
    },
    "M1": {
        "gear_name": "Manual 1.ª Marcha",
        "gear_code": "M1",
        "ratio": 3.692,
        "active_clutch": "K1 (Exterior)",
        "clutch_k1_pct": 100,
        "clutch_k2_pct": 0,
        "mechanical_lock": "Desbloqueado",
        "fork_status": {
            "fork_1_3": "Engranada 1.ª (+8.5 mm)",
            "fork_2_R": "Preseleccionada 2.ª (+8.5 mm)",
            "fork_5_7": "Neutral (0.0 mm)",
            "fork_4_6": "Neutral (0.0 mm)"
        },
        "solenoids": {
            "N433": {"state": "ACTIVE", "voltage_v": 12.0, "current_ma": 850, "pwm_pct": 100, "pressure_bar": 4.8},
            "N437": {"state": "PRESELECT", "voltage_v": 12.0, "current_ma": 850, "pwm_pct": 100, "pressure_bar": 4.8},
            "N434": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N438": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N435": {"state": "ACTIVE", "voltage_v": 12.0, "current_ma": 800, "pwm_pct": 100, "pressure_bar": 9.5},
            "N436": {"state": "ACTIVE", "voltage_v": 11.0, "current_ma": 840, "pwm_pct": 85, "pressure_bar": 9.5},
            "N439": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N440": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N471": {"state": "ACTIVE", "voltage_v": 7.0, "current_ma": 550, "pwm_pct": 50, "pressure_bar": 4.0},
            "N472": {"state": "ACTIVE", "voltage_v": 12.0, "current_ma": 950, "pwm_pct": 88, "pressure_bar": 14.0}
        },
        "fluid_flow_path": [
            "Presión de línea 14.0 bar controlada por N472.",
            "N433 alimenta la cámara izquierda de la horquilla 1-3.",
            "N437 activa la preselección de 2.ª marcha.",
            "N435 y N436 aplican 9.5 bar al embrague K1.",
            "Torque canalizado al árbol secundario hacia el diferencial Torsen central."
        ],
        "technical_summary": "1.ª Marcha en modo manual: Bloqueo de relación corta para máximo empuje (desmultiplicación total i_tot = 16.407). 2.ª marcha pre-engranada lista en el eje concéntrico par."
    },
    "M2": {
        "gear_name": "Manual 2.ª Marcha",
        "gear_code": "M2",
        "ratio": 2.150,
        "active_clutch": "K2 (Interior)",
        "clutch_k1_pct": 0,
        "clutch_k2_pct": 100,
        "mechanical_lock": "Desbloqueado",
        "fork_status": {
            "fork_1_3": "Preseleccionada 3.ª (-8.5 mm)",
            "fork_2_R": "Engranada 2.ª (+8.5 mm)",
            "fork_5_7": "Neutral (0.0 mm)",
            "fork_4_6": "Neutral (0.0 mm)"
        },
        "solenoids": {
            "N433": {"state": "PRESELECT", "voltage_v": 12.0, "current_ma": 850, "pwm_pct": 100, "pressure_bar": 4.8},
            "N437": {"state": "ACTIVE", "voltage_v": 12.0, "current_ma": 850, "pwm_pct": 100, "pressure_bar": 4.8},
            "N434": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N438": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N435": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N436": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N439": {"state": "ACTIVE", "voltage_v": 12.0, "current_ma": 800, "pwm_pct": 100, "pressure_bar": 8.8},
            "N440": {"state": "ACTIVE", "voltage_v": 10.0, "current_ma": 790, "pwm_pct": 78, "pressure_bar": 8.8},
            "N471": {"state": "ACTIVE", "voltage_v": 7.0, "current_ma": 550, "pwm_pct": 50, "pressure_bar": 4.0},
            "N472": {"state": "ACTIVE", "voltage_v": 11.5, "current_ma": 910, "pwm_pct": 84, "pressure_bar": 13.0}
        },
        "fluid_flow_path": [
            "Conmutación instantánea: N435 descarga K1 mientras N439/N440 presurizan K2 a 8.8 bar.",
            "N437 mantiene la horquilla de 2.ª marcha fijada.",
            "N433 pre-desplaza la horquilla 1-3 hacia la 3.ª marcha (-8.5 mm).",
            "Transmisión de par por el árbol primario exterior hueco hacia el eje secundario 2."
        ],
        "technical_summary": "2.ª Marcha activa con embrague K2. La subtransmisión 1 tiene pre-engranada la 3.ª marcha en standby, esperando la siguiente orden de cambio ascendente."
    },
    "M3": {
        "gear_name": "Manual 3.ª Marcha",
        "gear_code": "M3",
        "ratio": 1.406,
        "active_clutch": "K1 (Exterior)",
        "clutch_k1_pct": 100,
        "clutch_k2_pct": 0,
        "mechanical_lock": "Desbloqueado",
        "fork_status": {
            "fork_1_3": "Engranada 3.ª (-8.5 mm)",
            "fork_2_R": "Neutral (0.0 mm)",
            "fork_5_7": "Neutral (0.0 mm)",
            "fork_4_6": "Preseleccionada 4.ª (+8.5 mm)"
        },
        "solenoids": {
            "N433": {"state": "ACTIVE", "voltage_v": 12.0, "current_ma": 850, "pwm_pct": 100, "pressure_bar": 4.8},
            "N437": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N434": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N438": {"state": "PRESELECT", "voltage_v": 12.0, "current_ma": 850, "pwm_pct": 100, "pressure_bar": 4.8},
            "N435": {"state": "ACTIVE", "voltage_v": 12.0, "current_ma": 800, "pwm_pct": 100, "pressure_bar": 7.5},
            "N436": {"state": "ACTIVE", "voltage_v": 8.8, "current_ma": 710, "pwm_pct": 68, "pressure_bar": 7.5},
            "N439": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N440": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N471": {"state": "ACTIVE", "voltage_v": 6.5, "current_ma": 520, "pwm_pct": 46, "pressure_bar": 3.5},
            "N472": {"state": "ACTIVE", "voltage_v": 10.5, "current_ma": 830, "pwm_pct": 74, "pressure_bar": 11.5}
        },
        "fluid_flow_path": [
            "K1 presurizado a 7.5 bar por N436.",
            "Horquilla 1-3 engranada en 3.ª marcha (-8.5 mm).",
            "N438 presuriza la horquilla 4-6 para preseleccionar la 4.ª marcha.",
            "K2 despresurizado a 0 bar."
        ],
        "technical_summary": "3.ª marcha en árbol macizo central K1. Horquilla 4-6 engranando anticipadamente la 4.ª marcha en la subtransmisión K2."
    },
    "M4": {
        "gear_name": "Manual 4.ª Marcha",
        "gear_code": "M4",
        "ratio": 1.025,
        "active_clutch": "K2 (Interior)",
        "clutch_k1_pct": 0,
        "clutch_k2_pct": 100,
        "mechanical_lock": "Desbloqueado",
        "fork_status": {
            "fork_1_3": "Neutral (0.0 mm)",
            "fork_2_R": "Neutral (0.0 mm)",
            "fork_5_7": "Preseleccionada 5.ª (+8.5 mm)",
            "fork_4_6": "Engranada 4.ª (+8.5 mm)"
        },
        "solenoids": {
            "N433": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N437": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N434": {"state": "PRESELECT", "voltage_v": 12.0, "current_ma": 850, "pwm_pct": 100, "pressure_bar": 4.8},
            "N438": {"state": "ACTIVE", "voltage_v": 12.0, "current_ma": 850, "pwm_pct": 100, "pressure_bar": 4.8},
            "N435": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N436": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N439": {"state": "ACTIVE", "voltage_v": 12.0, "current_ma": 800, "pwm_pct": 100, "pressure_bar": 7.0},
            "N440": {"state": "ACTIVE", "voltage_v": 8.5, "current_ma": 680, "pwm_pct": 65, "pressure_bar": 7.0},
            "N471": {"state": "ACTIVE", "voltage_v": 6.0, "current_ma": 480, "pwm_pct": 42, "pressure_bar": 3.2},
            "N472": {"state": "ACTIVE", "voltage_v": 10.0, "current_ma": 800, "pwm_pct": 70, "pressure_bar": 10.8}
        },
        "fluid_flow_path": [
            "K2 presurizado a 7.0 bar.",
            "Horquilla 4-6 engranando 4.ª marcha (+8.5 mm).",
            "N434 preselecciona la 5.ª marcha en horquilla 5-7 (+8.5 mm).",
            "K1 en reposo."
        ],
        "technical_summary": "4.ª marcha prácticamente directa (1.025:1) en K2. Preselección de 5.ª marcha activada en el subconjunto impar."
    },
    "M5": {
        "gear_name": "Manual 5.ª Marcha",
        "gear_code": "M5",
        "ratio": 0.787,
        "active_clutch": "K1 (Exterior)",
        "clutch_k1_pct": 100,
        "clutch_k2_pct": 0,
        "mechanical_lock": "Desbloqueado",
        "fork_status": {
            "fork_1_3": "Neutral (0.0 mm)",
            "fork_2_R": "Neutral (0.0 mm)",
            "fork_5_7": "Engranada 5.ª (+8.5 mm)",
            "fork_4_6": "Preseleccionada 6.ª (-8.5 mm)"
        },
        "solenoids": {
            "N433": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N437": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N434": {"state": "ACTIVE", "voltage_v": 12.0, "current_ma": 850, "pwm_pct": 100, "pressure_bar": 4.8},
            "N438": {"state": "PRESELECT", "voltage_v": 12.0, "current_ma": 850, "pwm_pct": 100, "pressure_bar": 4.8},
            "N435": {"state": "ACTIVE", "voltage_v": 12.0, "current_ma": 800, "pwm_pct": 100, "pressure_bar": 6.2},
            "N436": {"state": "ACTIVE", "voltage_v": 7.8, "current_ma": 620, "pwm_pct": 58, "pressure_bar": 6.2},
            "N439": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N440": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N471": {"state": "ACTIVE", "voltage_v": 5.5, "current_ma": 440, "pwm_pct": 38, "pressure_bar": 2.8},
            "N472": {"state": "ACTIVE", "voltage_v": 9.5, "current_ma": 750, "pwm_pct": 65, "pressure_bar": 10.0}
        },
        "fluid_flow_path": [
            "K1 presurizado a 6.2 bar.",
            "Horquilla 5-7 engranando 5.ª marcha (+8.5 mm).",
            "N438 preselecciona 6.ª marcha (-8.5 mm).",
            "K2 despresurizado."
        ],
        "technical_summary": "5.ª marcha overdrive (0.787:1). Relación de crucero medio con preselección de 6.ª marcha activa."
    },
    "M6": {
        "gear_name": "Manual 6.ª Marcha",
        "gear_code": "M6",
        "ratio": 0.625,
        "active_clutch": "K2 (Interior)",
        "clutch_k1_pct": 0,
        "clutch_k2_pct": 100,
        "mechanical_lock": "Desbloqueado",
        "fork_status": {
            "fork_1_3": "Neutral (0.0 mm)",
            "fork_2_R": "Neutral (0.0 mm)",
            "fork_5_7": "Preseleccionada 7.ª (-8.5 mm)",
            "fork_4_6": "Engranada 6.ª (-8.5 mm)"
        },
        "solenoids": {
            "N433": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N437": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N434": {"state": "PRESELECT", "voltage_v": 12.0, "current_ma": 850, "pwm_pct": 100, "pressure_bar": 4.8},
            "N438": {"state": "ACTIVE", "voltage_v": 12.0, "current_ma": 850, "pwm_pct": 100, "pressure_bar": 4.8},
            "N435": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N436": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N439": {"state": "ACTIVE", "voltage_v": 12.0, "current_ma": 800, "pwm_pct": 100, "pressure_bar": 5.8},
            "N440": {"state": "ACTIVE", "voltage_v": 7.2, "current_ma": 580, "pwm_pct": 54, "pressure_bar": 5.8},
            "N471": {"state": "ACTIVE", "voltage_v": 5.2, "current_ma": 420, "pwm_pct": 36, "pressure_bar": 2.6},
            "N472": {"state": "ACTIVE", "voltage_v": 9.0, "current_ma": 720, "pwm_pct": 62, "pressure_bar": 9.5}
        },
        "fluid_flow_path": [
            "K2 presurizado a 5.8 bar.",
            "Horquilla 4-6 engranando 6.ª marcha (-8.5 mm).",
            "N434 preselecciona 7.ª marcha (-8.5 mm).",
            "K1 en reposo."
        ],
        "technical_summary": "6.ª marcha (0.625:1) en eje par hueco. En este desarrollo de 39.0 km/h / 1000 rpm el vehículo alcanza su velocidad máxima de 222 km/h."
    },
    "M7": {
        "gear_name": "Manual 7.ª Marcha (Overdrive Máximo DL501)",
        "gear_code": "M7",
        "ratio": 0.519,
        "active_clutch": "K1 (Exterior)",
        "clutch_k1_pct": 100,
        "clutch_k2_pct": 0,
        "mechanical_lock": "Desbloqueado",
        "fork_status": {
            "fork_1_3": "Neutral (0.0 mm)",
            "fork_2_R": "Neutral (0.0 mm)",
            "fork_5_7": "Engranada 7.ª (-8.5 mm)",
            "fork_4_6": "Neutral (0.0 mm)"
        },
        "solenoids": {
            "N433": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N437": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N434": {"state": "ACTIVE", "voltage_v": 12.0, "current_ma": 850, "pwm_pct": 100, "pressure_bar": 4.8},
            "N438": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N435": {"state": "ACTIVE", "voltage_v": 12.0, "current_ma": 800, "pwm_pct": 100, "pressure_bar": 5.2},
            "N436": {"state": "ACTIVE", "voltage_v": 6.8, "current_ma": 540, "pwm_pct": 50, "pressure_bar": 5.2},
            "N439": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N440": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N471": {"state": "ACTIVE", "voltage_v": 5.0, "current_ma": 400, "pwm_pct": 34, "pressure_bar": 2.5},
            "N472": {"state": "ACTIVE", "voltage_v": 8.5, "current_ma": 680, "pwm_pct": 58, "pressure_bar": 9.0}
        },
        "fluid_flow_path": [
            "K1 presurizado a 5.2 bar de crucero sostenido.",
            "Horquilla 5-7 engranando 7.ª marcha (-8.5 mm).",
            "K2 totalmente despresurizado a 0 bar.",
            "Consumo y revoluciones mínimas del motor a alta velocidad."
        ],
        "technical_summary": "7.ª marcha súper-overdrive (0.519:1) con desarrollo de 47.1 km/h / 1000 rpm. A 120 km/h el motor gira a sólo 2,550 rpm."
    },
    "M8": {
        "gear_name": "Manual M8 (Modo Virtual Eco-Cruising / Referencia 8HP)",
        "gear_code": "M8",
        "ratio": 0.435,
        "active_clutch": "K2 (Simulado / Ultra Overdrive)",
        "clutch_k1_pct": 0,
        "clutch_k2_pct": 100,
        "mechanical_lock": "Desbloqueado",
        "fork_status": {
            "fork_1_3": "Neutral (0.0 mm)",
            "fork_2_R": "Neutral (0.0 mm)",
            "fork_5_7": "Neutral (0.0 mm)",
            "fork_4_6": "Engranada 6.ª con lockup desmultiplicado (-8.5 mm)"
        },
        "solenoids": {
            "N433": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N437": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N434": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N438": {"state": "ACTIVE", "voltage_v": 12.0, "current_ma": 850, "pwm_pct": 100, "pressure_bar": 4.8},
            "N435": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N436": {"state": "OFF", "voltage_v": 0.0, "current_ma": 0, "pwm_pct": 0, "pressure_bar": 0.0},
            "N439": {"state": "ACTIVE", "voltage_v": 12.0, "current_ma": 800, "pwm_pct": 100, "pressure_bar": 4.8},
            "N440": {"state": "ACTIVE", "voltage_v": 6.2, "current_ma": 490, "pwm_pct": 46, "pressure_bar": 4.8},
            "N471": {"state": "ACTIVE", "voltage_v": 4.5, "current_ma": 360, "pwm_pct": 30, "pressure_bar": 2.2},
            "N472": {"state": "ACTIVE", "voltage_v": 8.0, "current_ma": 640, "pwm_pct": 54, "pressure_bar": 8.5}
        },
        "fluid_flow_path": [
            "Presión reducida a 4.8 bar para minimizar arrastres de bombeo.",
            "K2 acoplado con mínimo consumo parásito.",
            "Simulación de desmultiplicación extrema para autopista interestatal."
        ],
        "technical_summary": "Paso 8 simulado: Representa el escalón de máxima eficiencia aerodinámica y de combustible (relación 0.435:1 equivalente a la 8.ª marcha de las cajas automáticas Audi Tiptronic ZF 8HP55). Permite circular a 120 km/h por debajo de 2,150 rpm."
    }
}
