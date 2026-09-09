# SentinelT - Robo Wars RC Combat Robot

**Project owner and designer:** Thato Glen Assegaai  
**Category:** Robo Wars - RC Combat

## Project Overview

SentinelT is my independently designed and developed RC combat robot for Robo Wars. I developed the mechanical concept, Blender CAD model, dimensional-verification scripts, 2.4 GHz control framework, power and safety architecture, component plan, and technical documentation contained in this repository.

The design combines a compact armored chassis, protected drive layout, sloped external protection, serviceable body panels, an articulated upper structure, human-operated 2.4 GHz RC control, and a guarded active-mechanism provision.

## Robo Wars Design Requirements

| Requirement | SentinelT Status |
|---|---|
| Maximum footprint | **PASS - 318.16 mm x 495.00 mm** |
| Current CAD height | **405.99 mm** |
| Footprint verification | **180/180 frames PASS** |
| Failed footprint frames | **0** |
| Mass limit | Strictly below **5.000 kg** |
| Engineering mass budget | **4.650 kg** |
| Design margin | **0.350 kg** |
| Control | Human-operated **2.4 GHz RC** |
| Main ON/OFF | Included in the power-isolation architecture |
| Emergency Stop | Included and explicitly documented |
| Projectiles / flames / liquids | Not used |

> **Mass note:** 4.650 kg is an engineering design allocation, not a measured physical mass. The completed physical robot must be weighed on a calibrated scale before operational use.

## Repository Map

```text
SentinelT/
|- README.md
|- Source_Code/
|  |- Firmware/
|  |- RC_Control/
|  `- Flowcharts/
|- Designs/
|  |- Mechanical_Design/
|  |  |- CAD/
|  |  `- Renders/
|  |- Electronic_Design/
|  |- Schematics/
|  `- Simulation/
|- Documentation/
|  |- Pitch_Deck/
|  |- BOM/
|  |- Holistic_Build_Document/
|  |- FQA_Attendance_Log.md
|  `- FQA_Proof/
`- PROJECT_COMPLETENESS_CHECKLIST.md
```

## Mechanical Design Evidence

The Blender CAD model is stored in `Designs/Mechanical_Design/CAD/`. Mechanical renders and technical packaging views are stored in `Designs/Mechanical_Design/Renders/`.

I used Blender/Python dimensional auditing throughout development. The current verified CAD envelope is **318.16 mm x 495.00 mm x 405.99 mm**, with **0 failed frames out of 180 checked**.

The current digital package also includes:

- an internal electronics and drivetrain packaging layout;
- an exploded component-layout view with labelled hardware;
- a SentinelT + 2.4 GHz transmitter presentation view;
- a repeatable footprint-audit report.

## Control and Safety

SentinelT uses human-operated 2.4 GHz RC control. The safety architecture includes:

- accessible main ON/OFF isolation;
- Emergency Stop (E-Stop) power-disable architecture;
- safe-state actuator disable on invalid or lost RC signal;
- disabled outputs during controller startup/reset;
- separate drive and auxiliary control paths.

The annotated power and E-Stop architecture is documented in `Designs/Schematics/SentinelT_Power_and_EStop.md`.

## Documentation

The `Documentation/` folder contains:

- the 7-page A4 portrait pitch deck PDF;
- the Bill of Materials spreadsheet;
- the A4 portrait holistic build report;
- the Facilitator Q&A attendance-log structure and proof folder.

## Project Status

The CAD geometry, internal packaging concept, technical component views, dimensional simulation, control framework, safety architecture, current component plan and technical documentation are complete as a digital engineering package.

Physical fabrication and testing remain separate implementation stages. Measured physical mass, actual current draw, thermal behaviour, drivetrain performance and E-Stop interruption performance will be verified only on the completed hardware.

## Ownership Statement

SentinelT is independently designed and developed by **Thato Glen Assegaai**. Third-party commercial components are identified by manufacturer and supplier in the Bill of Materials; the SentinelT system design, CAD work, integration architecture, control framework and documentation are presented as my project work.
