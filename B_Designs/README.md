# Folder B - Designs

**Project Developer:** TG Assegaai  
**Build:** SentinelT Robo Wars RC Combat Robot

## Purpose

This folder contains the physical and electronic blueprints for SentinelT: mechanical CAD, fabrication intent, electronic design, circuit/safety schematics and digital simulation evidence.

## 1. Mechanical Design

Location: `Mechanical_Design/`

The canonical Blender model is `Mechanical_Design/CAD/SentinelT_Rob.blend`. The recorded digital baseline is **318.16 mm x 495.00 mm x 405.99 mm**. The footprint audit checked **204 physical mesh objects** across frames **1-180**, with **0 failed frames** and a recorded result of **PASS - 180/180**.

`Mechanical_Design/CAD/README.md` explains how a reviewer can open the Blender file, return SentinelT to its Frame 0 neutral position, select `SentinelT_Controls`, play the prepared mechanism demonstration, inspect wheel/drive movement, cutter ON/OFF behavior, hammer motion limits and upper-body rotation, and rerun footprint verification after any geometry or animation edit.

### Fabrication Approach

- 6 mm HDPE is the current chassis/armor material plan.
- Metal is used where shafts, brackets, motor hardware, fasteners and electrical terminals require higher strength.
- Bolted panels support access, repair and component replacement.
- Drive components are placed inside protected chassis zones.
- Sloped outer protection reduces direct loading on flat vulnerable faces.
- Internal service space is reserved for the battery, drive controller, receiver, fuse, power distribution, main isolation, E-Stop relay/contactor and auxiliary controller.

### Mechanical Render Evidence

`Mechanical_Design/Renders/` contains:

- `01_SentinelT_FRONT.png`
- `02_SentinelT_SIDE.png`
- `03_SentinelT_TOP.png`
- `04_SentinelT_ISOMETRIC.png`
- `SentinelT_Remote.png`
- `SentinelT_Remote.svg`

The four main Blender renders provide direct mechanical CAD evidence. The remote files document the intended human-operated 2.4 GHz control relationship.

## 2. Electronic Design

Location: `Electronic_Design/`

The dedicated electronic-design report is:

`Electronic_Design/Electronic_Design.pdf`

It documents:

- 3S battery architecture;
- 2.4 GHz RC receiver/control link;
- brushed drive-control architecture;
- fuse and high-current distribution;
- accessible main ON/OFF isolation;
- mandatory E-Stop integration;
- separate high-current relay/contactor isolation stage;
- component justification;
- internal wiring/component placement;
- hardware items that still require physical current/rating verification.

### Electronic Pictures

`Electronic_Design/Pictures/` contains clear circuit and layout evidence, including:

- `SentinelT_Internal_Layout.png` and `.svg` - internal wiring/component placement.
- `SentinelT_Exploded_Layout.png` and `.svg` - labelled component layout.
- `SentinelT_EStop_Integration.png` and `.svg` - explicit mandatory E-Stop integration.
- `SentinelT_Power_Architecture.png` - power architecture overview.

The editable/source power schematic is also stored at `Schematics/SentinelT_Power_Architecture.svg`.

## 3. Schematics

Location: `Schematics/`

The documented power path is:

```text
3S Battery
   -> Main Fuse / Protection
   -> Accessible Main ON/OFF Isolator
   -> E-Stop Controlled High-Current Relay/Contactor
   -> Power Distribution
       -> Drive Branch
       -> Control Branch
       -> Auxiliary Branch
```

The mushroom E-Stop is not assumed to carry full motor current by itself. It commands a separate high-current isolation device so actuator power can be removed independently of software.

## 4. Simulation

Location: `Simulation/`

Contains:

- `SentinelT_Footprint_Audit.py` - Blender/Python world-space footprint verification.
- `SentinelT_Footprint_Audit.txt` - recorded audit result.
- `SentinelT_Mass_Budget.py` - engineering mass-allocation check.

Recorded audit result:

| Item | Result |
|---|---:|
| Maximum X | **318.16 mm** |
| Maximum Y | **495.00 mm** |
| Maximum Z | **405.99 mm** |
| Physical meshes | **204** |
| Frames checked | **180** |
| Failed frames | **0** |
| Status | **PASS - 180/180** |

The final Blender file also contains refined reviewer animation controls. The supplied audit remains valid evidence for the verified digital baseline; if geometry or animation is changed again, the audit must be rerun before treating the modified state as a new verification result.

## Physical Verification Status

Digital design and simulation evidence is complete for this stage. Measured mass, final current draw, physical cable routing, drivetrain behavior, receiver/ESC calibration and E-Stop interruption testing require fabricated hardware and will be verified after hardware implementation.
