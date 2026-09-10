# Folder B - Designs

**Project Developer:** TG Assegaai  
**Build:** SentinelT

## Purpose

This folder contains the physical and electronic blueprints for SentinelT: mechanical CAD, fabrication intent, electronic design, annotated circuit/safety schematics and digital simulation evidence.

## 1. Mechanical Design

Location: `Mechanical_Design/`

The canonical Blender model is `Mechanical_Design/CAD/SentinelT_Rob.blend`. A fresh audit of the current submitted model checked **204 engineering mesh objects** over **Frames 0-180** and recorded an approximate digital envelope of **316.10 mm x 466.11 mm x 405.99 mm** with **0 failed footprint frames** against the 500 mm x 500 mm limit.

`Mechanical_Design/CAD/README.md` explains how a reviewer can open the Blender file, return SentinelT to its Frame 0 neutral position, select `SentinelT_Controls`, play the prepared mechanism demonstration and inspect wheel/drive motion, cutter ON/OFF behavior, hammer movement and upper-body rotation.

### Fabrication Approach

The physical build will follow the same design intent represented in CAD:

- metal/raw stock is included in the procurement plan for structural brackets, shafts, weapon components and load-bearing parts;
- armor/chassis panels are fabricated to match the packaged geometry while preserving the verified 500 mm x 500 mm footprint limit;
- bolted and serviceable joints are used where practical so panels, drive units and electronics can be inspected or replaced;
- drive components remain protected inside the chassis envelope;
- sloped guards reduce direct loading on vulnerable flat surfaces;
- the internal service area provides locations for the battery, motor drivers, receiver, control board, fuse/protection, power distribution, main isolator, E-Stop isolation hardware and active-mechanism controllers.

The final physical robot is not represented as already weighed or bench-tested. During hardware implementation, purchased components will be fitted and the build will be adjusted as required so the completed robot remains within the applicable Robo Wars dimensional, weight and safety limits.

### Mechanical Render Evidence

`Mechanical_Design/Renders/` contains:

- `01_SentinelT_FRONT.png`
- `02_SentinelT_SIDE.png`
- `03_SentinelT_TOP.png`
- `04_SentinelT_ISOMETRIC.png`
- `3D_PHYSICAL_SENTINELTPM.png` - physical-implementation concept illustration showing the intended external/internal arrangement.
- `SentinelT_Remote.png`
- `SentinelT_Remote.svg`

The physical-implementation illustration is a concept visualization of how fabricated SentinelT is intended to resemble the submitted CAD and system layout; it is not presented as a photograph of already-built hardware.

## 2. Electronic Design

Location: `Electronic_Design/`

The dedicated electronic-design report is:

`Electronic_Design/Electronic_Design.pdf`

It documents the battery architecture, 2.4 GHz RC control link, motor-control architecture, protection and distribution, main ON/OFF isolation, E-Stop integration, component placement and hardware-stage verification requirements.

### Electronic Pictures

`Electronic_Design/Pictures/` contains:

- `SentinelT_Internal_Layout.png` and `.svg` - internal component/wiring layout.
- `SentinelT_Exploded_Layout.png` and `.svg` - labelled internal component layout.
- `SentinelT_EStop_Integration.png` and `.svg` - emergency-stop integration evidence.
- `SentinelT_Power_Architecture.png` - power architecture overview.

## 3. Schematics

Location: `Schematics/`

The annotated schematic source is `SentinelT_Power_Architecture.svg`, supported by `SentinelT_Power_and_EStop.md`.

The corrected architecture separates the **high-current actuator path** from the **low-current E-Stop control loop**:

```text
HIGH-CURRENT PATH
3S Battery
   -> Main Fuse / Protection
   -> Accessible MAIN ON/OFF Isolator
   -> K1/K2 High-Current Contactor / Relay Contacts
   -> Power Distribution
       -> Drive Branch
       -> Weapon / Auxiliary Branch
       -> Control Branch

LOW-CURRENT E-STOP CONTROL LOOP
Post-isolator protected control feed
   -> Normally-Closed E-STOP contact
   -> Safety / enable logic
   -> K1/K2 contactor coil
```

Pressing the E-Stop opens the low-current control loop, de-energizes the contactor/relay coil and removes high-current actuator power. The mushroom switch is not assumed to carry the full drive/weapon current itself.

## 4. Simulation

Location: `Simulation/`

Contains:

- `SentinelT_Footprint_Audit.py` - Blender/Python world-space footprint verification.
- `SentinelT_Footprint_Audit.txt` - recorded result for the current submitted model.
- `SentinelT_Mass_Budget.py` - engineering mass-planning tool.

Current recorded audit:

| Item | Result |
|---|---:|
| Maximum X | **316.10 mm** |
| Maximum Y | **466.11 mm** |
| Maximum Z | **405.99 mm** |
| Engineering mesh objects | **204** |
| Frames checked | **0-180** |
| Failed footprint frames | **0** |
| Status | **PASS** |

The footprint audit verifies digital geometry only. It does not substitute for physical weighing, current testing, structural verification, weapon-energy testing or E-Stop interruption testing.

## Physical Hardware Verification

Hardware implementation will follow the submitted CAD, circuit architecture and control logic. Before operation, the completed robot will be checked for:

- measured physical mass below 5 kg;
- final overall footprint within 500 mm x 500 mm;
- correct 2.4 GHz RC operation and failsafe behavior;
- main ON/OFF accessibility;
- E-Stop interruption of actuator power;
- final fuse, contactor/relay and wire ratings;
- battery restraint and insulation;
- drivetrain direction and thermal/current behavior;
- mechanism clearances, guards and fastener security.

If a physical measurement differs from the digital design assumptions, the hardware build will be modified before operation so it conforms to the applicable Robo Wars requirements.
