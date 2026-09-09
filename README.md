# SentinelT - Robo Wars RC Combat Robot

**Project Developer:** TG Assegaai  
**Category:** Robo Wars - RC Combat

## Project Summary

SentinelT is a human-operated **2.4 GHz RC combat robot** built around a compact armored chassis, protected drivetrain, serviceable internal electronics bay, fail-safe power architecture and guarded active-mechanism provision. I developed the mechanical CAD, dimensional-verification tools, control framework, safety architecture, component plan and technical documentation contained in this repository.

The verified digital CAD baseline is **318.16 mm x 495.00 mm x 405.99 mm**. The recorded footprint audit checks **180 frames** with **0 failed frames** and a result of **PASS - 180/180** against the required **500 mm x 500 mm** maximum footprint. The current **4.650 kg** value is an engineering mass allocation, leaving **0.350 kg** design margin below 5 kg. Measured physical mass and other hardware-dependent results will be verified after hardware implementation.

## Required Repository Structure

The three required submission folders are named and ordered as **A, B and C** so they appear in the intended evaluation sequence. Underscores are used instead of colon characters so the repository remains safe to clone and use on Windows.

```text
SentinelT/
├── README.md
├── A_Source_Code/          # Folder A: Source Code
├── B_Designs/              # Folder B: Designs
└── C_Documentation/        # Folder C: Documentation
```

## Folder A: `A_Source_Code/`

Contains the programming scripts, firmware framework, programming method and flowchart required to explain and operate SentinelT.

- `Firmware/SentinelT_RoboWars_Control_Skeleton.ino` - C/C++ Arduino-style control and safety framework.
- `Flowcharts/SentinelT_Control_Flow.svg` - vector control-flow diagram.
- `Flowcharts/SentinelT_Control_Flow.png` - high-resolution raster version for quick viewing.
- `README.md` - detailed programming language, framework, state logic, RC method, differential-drive mixing, failsafe behavior and implementation notes.

The control architecture is human-operated **2.4 GHz RC**, not autonomous. Software defaults to `SAFE_DISABLED` at startup/reset and returns to that state when RC data is invalid or stale, the E-Stop status is active, or command validation fails. Hardware-specific receiver mapping, MCU pins and ESC calibration are intentionally marked for verification after hardware implementation.

## Folder B: `B_Designs/`

Contains the complete physical and electronic design evidence.

- `Mechanical_Design/CAD/SentinelT_Rob.blend` - canonical Blender CAD/simulation model.
- `Mechanical_Design/CAD/README.md` - judge/reviewer guide for Frame 0, `SentinelT_Controls`, wheel drive, cutter, hammers and upper-body simulation.
- `Mechanical_Design/Renders/` - front, side, top, isometric and 2.4 GHz remote presentation views.
- `Electronic_Design/Electronic_Design.pdf` - dedicated electronic-design report.
- `Electronic_Design/Pictures/` - internal component/wiring layout, exploded layout, E-Stop integration and power-architecture evidence.
- `Schematics/` - annotated source schematics for main ON/OFF, E-Stop, power distribution and RC safety.
- `Simulation/` - footprint-audit script/report and engineering mass-budget script.
- `README.md` - detailed mechanical, fabrication, electronic, schematic, simulation and safety summary.

### Verified Digital Geometry

| Verification item | Result |
|---|---:|
| Maximum X | **318.16 mm** |
| Maximum Y | **495.00 mm** |
| Maximum Z | **405.99 mm** |
| Physical mesh objects in recorded audit | **204** |
| Frames audited | **180** |
| Failed footprint frames | **0** |
| Recorded footprint result | **PASS - 180/180** |

The Blender file also contains mechanism animation controls for reviewer inspection. Because the animation controls were refined after the recorded baseline audit, any further geometry or animation changes should be followed by rerunning the supplied footprint-audit script before physical fabrication.

## Folder C: `C_Documentation/`

Contains the formal submission documents and status evidence.

- `Pitch_Deck/SentinelT_Pitch_Deck.pdf` - 7-page A4 portrait pitch deck.
- `BOM/SentinelT_Bill_of_Materials.xlsx` - Bill of Materials with component name, quantity, unit cost, supplier, stock code, direct URL and cost totals.
- `Holistic_Build_Document/SentinelT_Holistic_Build_Document.pdf` - comprehensive A4 report tying together the Robo Wars constraints, solution, mechanical design, electronic design, E-Stop, programming, simulation, mass budget and BOM summary.
- `FQA_Attendance_Log.md` - records that no Facilitator Q&A session was attended; no FQ&A bonus is claimed and no evidence is fabricated.
- `FQA_Proof/` - reserved proof directory, intentionally without attendance screenshots.
- `PROJECT_COMPLETENESS_CHECKLIST.md` - separates completed digital evidence from hardware-dependent verification still to be performed.
- `README.md` - detailed documentation-folder summary.

## Robo Wars Requirements and SentinelT Response

| Requirement | SentinelT response |
|---|---|
| Maximum footprint | Recorded digital audit: **PASS - 318.16 mm x 495.00 mm** |
| Weight | Engineering allocation **4.650 kg**; physical weighing after hardware implementation |
| Control frequency | Human-operated **2.4 GHz RC** |
| Main ON/OFF | Accessible main battery-isolation stage documented |
| Emergency Stop | Mushroom E-Stop controlling a separate high-current relay/contactor isolation stage |
| Restricted weapon types | No projectiles, flames or liquids |
| Simulation | Blender CAD + Python footprint verification and mechanism animation |

## Control and Safety Architecture

SentinelT uses layered safety:

1. Accessible main ON/OFF battery isolation.
2. Independent E-Stop control loop commanding a separate high-current relay/contactor.
3. Software `SAFE_DISABLED` state at startup/reset.
4. RC-signal validation and timeout handling.
5. Auxiliary actuation disabled unless explicitly enabled by the operator.

The hardware E-Stop is not treated as a software-only feature.

## Current Development Status

The digital engineering submission contains the CAD model, mechanical renders, internal packaging evidence, electronic architecture, annotated E-Stop integration, control framework, flowchart, footprint simulation, engineering mass allocation, BOM spreadsheet, pitch deck and holistic report.

The following require the physical robot and therefore remain intentionally unverified until hardware implementation: measured mass, current draw, final cable routing and strain relief, drivetrain performance, thermal behavior, battery runtime, final receiver/ESC calibration and physical E-Stop interruption testing.

## Project Developer

**Thato Glen Assegaai**
