# SentinelT Robo Wars Combat Robot

**Designer:** Thato Glen Assegaai  
**Category:** Robo Wars - RC Combat  
**Competition:** Robo Rumble 2026 - Elimination Round

## Project Summary

SentinelT is a compact remotely controlled combat-robot CAD concept developed for the Robo Wars category. The design combines an armored mobile chassis, protected drive layout, sloped external protection, articulated upper structure, serviceable covers, 2.4 GHz RC control architecture, and a guarded active-mechanism provision.

The repository is organised specifically around the Robo Rumble elimination rubric: source code and flowcharts, mechanical/electronic designs and safety schematics, plus the required documentation package.

## Competition Compliance

| Requirement | SentinelT Status |
|---|---|
| Maximum footprint | **PASS** - 318.16 mm x 495.00 mm |
| CAD height | 255.41 mm |
| Footprint audit | **180/180 frames PASS** |
| Mass limit | Strictly below 5.000 kg |
| Engineering mass budget | **4.650 kg** |
| Mass design margin | **0.350 kg** |
| Control | Human-operated **2.4 GHz RC** |
| Main ON/OFF | Included in safety architecture |
| Emergency Stop | Included and explicitly documented |
| Projectiles / flames / liquids | Not used |

> **Mass note:** 4.650 kg is an engineering design allocation, not a measured physical mass. The completed robot must be weighed on a calibrated scale before competition.

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
`- Documentation/
   |- Pitch_Deck/
   |- BOM/
   |- Holistic_Build_Document/
   |- FQA_Attendance_Log.md
   `- FQA_Proof/
```

## Mechanical Evidence

The final Blender CAD model is stored in `Designs/Mechanical_Design/CAD/` and the front, side, top and isometric renders are stored in `Designs/Mechanical_Design/Renders/`.

Automated Blender/Python dimensional auditing was used during development. The final compliant model measures **318.16 mm x 495.00 mm x 255.41 mm**, with **0 failed frames out of 180 checked**.

## Control & Safety

SentinelT is designed for human-operated 2.4 GHz RC control. The safety architecture includes:

- accessible main ON/OFF isolation;
- Emergency Stop (E-Stop);
- fail-safe actuator disable on invalid/lost RC signal;
- safe startup state;
- explicit isolation of drive and auxiliary actuation.

See `Designs/Schematics/SentinelT_Power_and_EStop.md` for the annotated architecture.

## Documentation

The documentation folder contains the Bill of Materials, holistic build report source/final document, pitch-deck source/final PDF, and FQ&A attendance evidence structure.

## Development Status

**CAD and elimination-round documentation stage.** Final component ratings, fabricated mass, electrical load measurements, E-Stop hardware response, drivetrain performance and arena testing must still be physically verified before competition use.
