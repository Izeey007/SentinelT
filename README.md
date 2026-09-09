# SentinelT - Robo Wars RC Combat Robot

**Project Developer:** TG Assegaai  
**Category:** Robo Wars - RC Combat

## Project Summary

SentinelT is a human-operated 2.4 GHz RC combat robot built around a compact armored chassis, protected drivetrain, serviceable internal electronics bay, fail-safe power architecture and guarded active-mechanism provision. I developed the mechanical CAD, dimensional verification tools, control framework, safety architecture, component plan and technical documentation contained in this repository.

The current digital build has been audited across frames 1-180. The verified CAD envelope is **318.16 mm x 495.00 mm x 405.99 mm**. The X/Y footprint remains inside the required **500 mm x 500 mm** limit for all audited frames: **180/180 PASS, 0 failed frames**. The current **4.650 kg** value is an engineering mass allocation, leaving **0.350 kg** design margin below 5 kg; measured physical mass will be verified after hardware implementation.

## Repository Structure

The repository is organized in the required evaluation order below. GitHub may display folders alphabetically, but the project structure maps directly to Folder A, Folder B and Folder C.

```text
SentinelT/
├── README.md
├── Folder A: Source_Code/
├── Folder B: Designs/
├── Folder C: Documentation/
└── PROJECT_COMPLETENESS_CHECKLIST.md
```

### Folder A: `Source_Code/`

Contains the programming framework required to operate SentinelT and the visual logic used to explain it.

- `Firmware/` - C/C++ Arduino-style control framework for RC validation, safe-state handling, differential-drive mixing and auxiliary enable logic.
- `Flowcharts/` - high-resolution control-flow diagram showing startup, E-Stop checks, RC validation, command handling and SAFE_DISABLED behavior.
- `README.md` - detailed explanation of the programming language, framework, control method, state logic, failsafe strategy, implementation parameters and folder contents.

The control architecture is human-operated **2.4 GHz RC**, not autonomous. The software defaults to a disabled state on startup/reset and returns to SAFE_DISABLED when the RC signal is invalid/lost, the E-Stop is active or command data fails validation. Hardware-specific receiver protocol, pin mapping and ESC calibration will be verified and locked after hardware implementation.

### Folder B: `Designs/`

Contains the complete mechanical, electronic, safety and simulation design evidence.

- `Mechanical_Design/CAD/` - canonical Blender model: `SentinelT_Rob.blend`.
- `Mechanical_Design/Renders/` - front, side, top and isometric CAD views plus internal component layout, exploded layout and robot + 2.4 GHz remote presentation view.
- `Electronic_Design/Electronic_Design.pdf` - dedicated A4 electronic-design report covering component selection, circuit architecture, wiring, main ON/OFF isolation and mandatory E-Stop integration.
- `Electronic_Design/Pictures/` - circuit/power schematic, E-Stop integration diagram and internal wiring/component-layout evidence.
- `Schematics/` - source safety/power architecture diagrams and annotations.
- `Simulation/` - Blender/Python footprint verification scripts, mass-budget tool and the recorded footprint audit.
- `README.md` - detailed summary of the mechanical, electronic, schematic, simulation and safety evidence.

Verified digital geometry:

| Verification item | Result |
|---|---:|
| Maximum X | **318.16 mm** |
| Maximum Y | **495.00 mm** |
| Maximum Z | **405.99 mm** |
| Physical mesh objects | **204** |
| Frames audited | **180** |
| Failed footprint frames | **0** |
| Footprint result | **PASS - 180/180** |

### Folder C: `Documentation/`

Contains the formal submission documents.

- `Pitch_Deck/SentinelT_Pitch_Deck.pdf` - 7-page A4 portrait pitch deck covering the Robo Wars constraints, SentinelT solution/buildability, CAD verification, electronics/safety, mass/cost and Project Developer responsibilities.
- `BOM/SentinelT_Bill_of_Materials.xlsx` - component financing workbook with component name, quantity, cost per unit, supplier, stock code, direct URL and cost totals.
- `Holistic_Build_Document/SentinelT_Holistic_Build_Document.pdf` - comprehensive A4 report tying together the context, constraints, solution overview, mechanical design, electronic design, E-Stop integration, programming framework, simulation, mass budget and BOM summary.
- `FQA_Attendance_Log.md` - records that no Facilitator Q&A session was attended; no FQ&A bonus is claimed and no evidence is fabricated.
- `FQA_Proof/` - reserved proof directory; intentionally contains no attendance screenshots because no FQ&A session was attended.
- `README.md` - detailed summary and status of every documentation deliverable.

## Robo Wars Requirements and SentinelT Response

| Requirement | SentinelT response |
|---|---|
| Maximum footprint | **PASS - 318.16 mm x 495.00 mm** |
| Weight | Engineering allocation **4.650 kg**; physical weighing after hardware implementation |
| Control frequency | Human-operated **2.4 GHz RC** |
| Main ON/OFF | Accessible main battery-isolation stage included in the electrical architecture |
| Emergency Stop | Explicit mushroom E-Stop + separate high-current relay/contactor power-disable architecture |
| Restricted weapon types | No projectiles, flames or liquids |
| Simulation | Blender CAD + Python footprint verification, 180/180 frames PASS |

## Control and Safety Architecture

SentinelT uses a layered safety approach:

1. Accessible main ON/OFF battery isolation.
2. Independent E-Stop control loop commanding a separate high-current relay/contactor.
3. Software SAFE_DISABLED state at startup/reset.
4. RC-signal validation and timeout handling.
5. Disabled auxiliary actuation unless explicitly enabled by the operator.

The hardware E-Stop is not treated as a software-only feature. The power architecture is documented in `Designs/Schematics/` and summarized visually in `Designs/Electronic_Design/Pictures/`.

## Current Development Status

The digital engineering package is complete for the current design stage: CAD model, mechanical renders, internal packaging, electronic architecture, E-Stop integration, control framework, flowchart, footprint simulation, mass allocation, BOM structure, pitch deck and holistic report are included.

The following items require the physical robot and therefore remain intentionally unverified until hardware implementation: measured robot mass, measured current draw, final cable routing/strain relief, drivetrain performance, thermal behavior, battery runtime, receiver/ESC calibration and physical E-Stop interruption testing.

## Project Developer

**Thato Glen Assegaai**
