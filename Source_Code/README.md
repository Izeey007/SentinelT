# Source Code - SentinelT Robo Wars

**Designer and developer:** Thato Glen Assegaai

This folder contains the Robo Wars control framework I developed for SentinelT. The robot is human-operated over **2.4 GHz RC** and is not autonomous.

## Architecture

```text
2.4 GHz Transmitter
        |
        v
2.4 GHz Receiver
        |
        v
Embedded Controller / Interface Logic
   |                         |
   v                         v
Dual Drive ESC        Auxiliary Enable
   |                         |
   v                         v
Drive Motors          Guarded Active Mechanism
```

## Safety Logic

The software defaults to a safe state. Drive and auxiliary outputs are disabled when:

- the E-Stop is active;
- the RC signal is lost or invalid;
- the controller starts or resets;
- command data is outside the expected range.

The E-Stop is a **hardware safety function** and is documented separately in `Designs/Schematics/SentinelT_Power_and_EStop.md`.

## Folder Map

- `Firmware/` - embedded control skeleton and safe-state logic.
- `RC_Control/` - 2.4 GHz operator-control mapping and failsafe behaviour.
- `Flowcharts/` - control architecture and operating-state flowcharts.

## Current Development State

The control framework is hardware-aware but still keeps final pin assignments, receiver protocol details and ESC calibration as implementation parameters. Those values will be locked after the selected hardware is physically obtained and bench-tested.
