# Source Code - SentinelT Robo Wars

This folder contains the Robo Wars-specific control framework for SentinelT. The robot is **human-operated over 2.4 GHz RC**; it is not autonomous.

## Architecture

```text
2.4 GHz Transmitter
        |
        v
2.4 GHz Receiver
        |
        v
Embedded Controller
   |            |
   v            v
Drive ESC     Auxiliary Enable
   |            |
   v            v
Drive Motors  Guarded Active Mechanism
```

## Safety Logic

The control software defaults to a safe state. Drive and auxiliary outputs are disabled when:

- the E-Stop is active;
- the RC signal is lost or invalid;
- the controller starts or resets;
- command data is outside the expected range.

The E-Stop itself is treated as a **hardware safety function** and is documented separately in `Designs/Schematics/SentinelT_Power_and_EStop.md`.

## Folder Map

- `Firmware/` - embedded control skeleton and safety-state logic.
- `RC_Control/` - 2.4 GHz operator-control mapping and failsafe behaviour.
- `Flowcharts/` - software architecture and operating-state flowcharts.

## Development Status

The software is an elimination-round engineering framework. Hardware-specific pin numbers, receiver protocol details, ESC calibration and final actuator limits must be updated after the physical components are selected and bench-tested.
