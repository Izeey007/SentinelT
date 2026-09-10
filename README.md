# SentinelT - Robo Wars RC Combat Robot

**Project Developer:** TG Assegaai  
**Category:** Robo Wars - RC Combat

## Project Summary

SentinelT is a human-operated **2.4 GHz RC combat robot** developed around a compact armored chassis, protected drivetrain, serviceable internal electronics bay, hardware emergency isolation and guarded active mechanisms. I developed the mechanical CAD, dimensional-verification tools, control framework, safety architecture, component plan and technical documentation contained in this repository.

A fresh digital audit of the current submitted `SentinelT_Rob.blend` model checked **204 engineering mesh objects** across **Frames 0-180**. The measured digital envelope is approximately **316.10 mm x 466.11 mm x 405.99 mm**, with **0 failed frames** against the required **500 mm x 500 mm** maximum footprint.

The physical robot will be fabricated to follow the same documented Robo Wars design intent and constraints. Hardware-dependent results - including calibrated physical mass, final electrical ratings, current draw, actuator loads, cable routing, battery runtime and E-Stop interruption performance - will be measured and verified during hardware implementation. SentinelT is designed with a **below-5 kg physical mass target**, and the completed build will be adjusted as required before operation so it remains within the applicable Robo Wars limits.

## Required Repository Structure

```text
SentinelT/
|-- README.md
|-- A_Source_Code/          # Folder A: Source Code
|-- B_Designs/              # Folder B: Designs
`-- C_Documentation/        # Folder C: Documentation
```

The folders are prefixed A, B and C so GitHub displays them in the same order as the submission requirements while remaining safe to clone on Windows.

## Folder A: `A_Source_Code/`

Contains the programming scripts, embedded-control framework, programming method and flowchart used to explain and implement SentinelT control.

- `Firmware/SentinelT_RoboWars_Control_Skeleton.ino` - C/C++ Arduino-style control and safety framework.
- `Flowcharts/SentinelT_Control_Flow.svg` - vector control-flow diagram.
- `Flowcharts/SentinelT_Control_Flow.png` - high-resolution raster copy.
- `README.md` - detailed language, framework, RC method, differential-drive logic, state architecture and failsafe behavior.

SentinelT uses human-operated **2.4 GHz RC**. The software architecture defaults to `SAFE_DISABLED` at startup/reset and returns to a disabled state on invalid/stale RC input, an active E-Stop condition or invalid command data. Hardware-specific receiver mapping, controller pins and calibration are finalized during hardware implementation.

## Folder B: `B_Designs/`

Contains the complete mechanical, electronic, safety and simulation design package.

- `Mechanical_Design/CAD/SentinelT_Rob.blend` - canonical Blender CAD/simulation model.
- `Mechanical_Design/CAD/README.md` - reviewer guide for Frame 0, `SentinelT_Controls`, wheel drive, cutter, hammers and body rotation.
- `Mechanical_Design/Renders/` - exterior CAD views, remote-control evidence and physical-implementation concept illustration.
- `Electronic_Design/Electronic_Design.pdf` - dedicated electronic-design report.
- `Electronic_Design/Pictures/` - internal component layout, exploded layout, E-Stop integration and power architecture.
- `Schematics/` - annotated circuit/power documentation showing the mandatory MAIN ON/OFF and E-STOP functions.
- `Simulation/` - footprint-audit script/result and engineering mass-budget tools.
- `README.md` - detailed design-folder summary.

### Current Digital Geometry Verification

| Verification item | Result |
|---|---:|
| Maximum X | **316.10 mm** |
| Maximum Y | **466.11 mm** |
| Maximum Z | **405.99 mm** |
| Engineering mesh objects | **204** |
| Frames audited | **0-180** |
| Failed footprint frames | **0** |
| Footprint result | **PASS** |

## Folder C: `C_Documentation/`

Contains the formal SentinelT submission documents.

- `Pitch_Deck/SentinelT_Pitch_Deck.pdf` - maximum-seven-page pitch deck.
- `BOM/SentinelT_Bill_of_Materials.xlsx` - procurement/funding BOM with component, quantity, unit cost, supplier/model, buying URL and total cost information.
- `Holistic_Build_Document/SentinelT_Holistic_Build_Document.pdf` - comprehensive A4 report tying the build together.
- `FQA_Attendance_Log.md` - records that no FQ&A attendance bonus is claimed.
- `PROJECT_COMPLETENESS_CHECKLIST.md` - maps completed digital evidence and hardware-stage verification.
- `README.md` - documentation-folder summary.

## Robo Wars Requirements and SentinelT Response

| Requirement | SentinelT response |
|---|---|
| Maximum footprint | Current Blender audit: **316.10 mm x 466.11 mm**, 0 failed frames |
| Weight | Physical design target **< 5 kg**; calibrated measurement during hardware implementation |
| Control frequency | Human-operated **2.4 GHz RC** |
| Main ON/OFF | Separate accessible battery-isolation function documented |
| Emergency Stop | Normally-closed E-Stop control loop de-energizing a separate high-current contactor/relay |
| Restricted weapon types | No projectiles, flames or liquids |
| Simulation | Blender CAD, mechanism animation and Python footprint verification |

## Control and Safety Architecture

SentinelT uses layered safety:

1. Accessible main ON/OFF battery isolation.
2. Main battery fuse/protection.
3. Independent E-Stop low-current control loop.
4. Separate high-current contactor/relay that removes actuator power when the E-Stop loop opens.
5. Software `SAFE_DISABLED` state at startup/reset.
6. RC-signal validation and timeout handling.
7. Active mechanisms disabled unless explicitly enabled by the operator.

The E-Stop pushbutton is not assumed to carry the full motor/weapon current. It commands the separate high-current isolation stage documented in `B_Designs/Schematics/`.

## Hardware Implementation Statement

The submitted CAD, schematics, control framework and procurement plan define the intended physical SentinelT build. During fabrication, actual purchased parts will be fitted to the same architecture and all hardware-dependent checks will be completed before operation. If measured mass, dimensions, current, thermal behavior or mechanism clearances differ from the digital plan, the physical implementation will be adjusted until the applicable Robo Wars constraints are satisfied.

## Project Developer

**Thato Glen Assegaai**
