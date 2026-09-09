# Folder A - Source Code

**Project Developer:** TG Assegaai  
**Build:** SentinelT Robo Wars RC Combat Robot

## Purpose

This folder contains the programming framework required to operate SentinelT. The code is written specifically for a human-operated Robo Wars robot using a **2.4 GHz RC link**. It is not autonomous control code.

## Programming Method

- **Language:** C/C++.
- **Framework style:** Arduino-compatible embedded C/C++ conventions.
- **Control method:** Human-operated 2.4 GHz RC receiver input.
- **Drive method:** Differential-drive command mixing.
- **State architecture:** `SAFE_DISABLED`, `RC_READY`, `OPERATING`.
- **Safety model:** safe state at startup/reset, RC validation, signal timeout, hardware E-Stop status check and default-disabled auxiliary output.
- **Hardware safety separation:** the E-Stop power cut is a hardware function; software safe-state logic is an additional layer.

## Control Architecture

```text
2.4 GHz Transmitter
        |
        v
2.4 GHz Receiver
        |
        v
Embedded Controller / Interface Logic
        |
        +----------------------+----------------------+
        |                      |                      |
        v                      v                      v
RC validation            Drive mixing          Auxiliary enable
+ timeout                L = T + S             default OFF
                         R = T - S
        |                      |                      |
        +----------------------+----------------------+
                               |
                               v
                     Actuator command outputs
```

Where `T` is throttle and `S` is steering. Mixed commands are constrained to the expected command range before being sent to the selected motor-control interface.

## Operating Logic

### 1. Startup

When the controller starts or resets, all actuator commands are forced OFF and the state is `SAFE_DISABLED`.

### 2. Hardware E-Stop Check

The software checks the E-Stop status input before applying commands. The physical E-Stop itself is designed to remove actuator power independently through the high-current isolation stage documented under `Designs/Schematics/`.

### 3. RC Signal Validation

The receiver command must be valid before SentinelT can enter `RC_READY`. The control framework uses a **250 ms RC validity timeout**; invalid or stale input returns the robot to `SAFE_DISABLED`.

### 4. Differential Drive

The control logic converts throttle and steering into left/right commands:

```text
left  = throttle + steering
right = throttle - steering
```

Both outputs are constrained to the normalized command range before conversion to the final ESC/motor-interface signal.

### 5. Auxiliary Control

The auxiliary/active-mechanism command defaults OFF. It only becomes enabled when a valid operator command is present and the safety state allows operation.

## Folder Contents

```text
Source_Code/
├── README.md
├── Firmware/
│   └── SentinelT_RoboWars_Control_Skeleton.ino
└── Flowcharts/
    └── SentinelT_Control_Flow.svg
```

### `Firmware/SentinelT_RoboWars_Control_Skeleton.ino`

Contains the embedded control/safety framework, including:

- robot operating-state enumeration;
- RC-command data structure;
- 250 ms signal timeout;
- startup disabled state;
- hardware E-Stop status hook;
- receiver-reading hook;
- differential-drive mixing;
- auxiliary enable function;
- actuator-disable function;
- clear comments identifying hardware implementation parameters.

### `Flowcharts/SentinelT_Control_Flow.svg`

Shows the complete command flow from POWER ON through initialization, E-Stop validation, RC validation, operator command processing, differential drive and the SAFE_DISABLED fallback state.

## Hardware Implementation Parameters

The following values cannot be truthfully locked before the selected physical hardware is wired and bench-tested, so they are intentionally treated as implementation parameters:

- exact receiver protocol/channel mapping;
- microcontroller pin assignments;
- ESC neutral/end-point calibration;
- final actuator output scaling;
- final E-Stop status-input wiring;
- measured RC failsafe behavior;
- measured motor-current and thermal limits.

These items will be verified after hardware implementation. Their absence from the current digital package is not represented as completed physical testing.
