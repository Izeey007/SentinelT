# SentinelT Project Completeness Checklist

**Project Developer:** TG Assegaai  
**Category:** Robo Wars - RC Combat

This checklist separates completed digital submission evidence from checks that require the fabricated robot. Hardware-stage items will be measured and verified during implementation and are not represented as already physically tested.

## Repository Structure & README - 10 Points

- [x] Root `README.md` contains a high-level SentinelT summary.
- [x] Root `README.md` maps Folder A: Source Code, Folder B: Designs and Folder C: Documentation.
- [x] Required folders are ordered and named `A_Source_Code/`, `B_Designs/`, `C_Documentation/`.
- [x] Root `README.md` explains the contents of all three accessible folders.
- [x] Detailed folder READMEs are included for Source Code, Designs and Documentation.
- [x] CAD folder includes a dedicated simulation/control README for the Blender model.

## Folder A - Source Code - 20 Points

- [x] C/C++ / Arduino-style programming method documented.
- [x] 2.4 GHz RC architecture documented.
- [x] `SAFE_DISABLED` / `RC_READY` / `OPERATING` state logic documented.
- [x] Differential-drive mixing documented.
- [x] 250 ms RC timeout documented.
- [x] Startup/reset safe state documented.
- [x] Auxiliary default-OFF logic documented.
- [x] High-resolution control flowchart included in SVG and PNG form.
- [x] Firmware/control framework included.
- [ ] Exact receiver protocol/channel mapping - **completed during hardware implementation**.
- [ ] Final controller pin mapping - **completed during hardware implementation**.
- [ ] Motor-driver calibration/end-points - **completed during hardware implementation**.

## Folder B - Designs - 40 Points

### Mechanical Design

- [x] Canonical Blender CAD model included as `B_Designs/Mechanical_Design/CAD/SentinelT_Rob.blend`.
- [x] Front, side, top and isometric CAD renders included.
- [x] Physical-implementation concept illustration included.
- [x] 2.4 GHz remote presentation evidence included.
- [x] Internal component-layout evidence included.
- [x] Exploded component-layout evidence included.
- [x] Fabrication material/fastening intent documented.
- [x] Raw HDPE and mild-steel stock included in the funding BOM.
- [x] Fresh current-model footprint audit completed.
- [x] Current digital envelope approximately **316.10 mm x 466.11 mm x 405.99 mm**.
- [x] 204 engineering meshes checked across Frames 0-180 with **0 failed footprint frames**.
- [x] Blender model includes reviewer controls for wheel drive, cutter, hammer motion and upper-body rotation.

### Electronic Design

- [x] Dedicated `Electronic_Design.pdf` included.
- [x] Power/circuit architecture evidence included.
- [x] Internal wiring/component-layout evidence included.
- [x] Main ON/OFF isolation explicitly documented and budgeted.
- [x] Mandatory E-Stop integration explicitly documented and budgeted.
- [x] E-Stop uses a **low-current normally-closed control loop** that de-energizes a **separate high-current contactor/relay**.
- [x] High-current actuator path is separated from the E-Stop pushbutton control circuit.
- [x] Four-wheel drive hardware and independent left/right Cytron MDD20A control are included in the funding BOM.
- [x] Cutter motor/controller candidate and hammer/torso actuators are included in the funding BOM.
- [ ] Final fuse, relay/contactor, connector and wire-current ratings - **verified during hardware implementation**.

### Simulation / Technical Excellence

- [x] Blender/Python footprint simulation included.
- [x] Current audit records 204 engineering meshes and 0 failed frames.
- [x] Engineering mass-planning tool included.
- [x] Mechanism animation and control guide included.
- [ ] Calibrated physical mass measurement - **verified during hardware implementation; completed robot must remain strictly below 5 kg**.

## Folder C - Documentation - 30 Points

- [x] Maximum-seven-page `SentinelT_Pitch_Deck.pdf` included.
- [x] `SentinelT_Bill_of_Materials.xlsx` included and rebuilt as a valid workbook.
- [x] BOM contains component name, exact quantity, unit price, supplier, stock code/model and direct buying/source URL for every funded line.
- [x] BOM includes raw fabrication material, four-wheel drivetrain, RC equipment, cutter hardware, hammer/torso actuators, safety hardware, wiring, charging and supporting components.
- [x] Formula-driven final procurement total is **R15,985.04** and is highlighted in RED in the workbook.
- [x] GitHub-readable funding CSV and funding-total note are included as supporting procurement evidence.
- [x] A4 portrait `SentinelT_Holistic_Build_Document.pdf` included.
- [x] Holistic report includes title header, Robo Wars constraints and solution overview.
- [x] Holistic report includes mechanical, electronic and programming sections with visual evidence.
- [x] Holistic report includes BOM summary and implementation status.
- [x] Project Developer and signature are included in formal documentation.
- [ ] Final physical measurements and hardware test results - **recorded during hardware implementation**.

## FQ&A Bonus

- [ ] FQ&A attendance bonus - **not claimed; no Facilitator Q&A session was attended**.
- [ ] Attendance screenshots - **not available because no FQ&A session was attended**.

## Physical Hardware Implementation Verification

The physical SentinelT build will follow the same CAD packaging, circuit architecture, control method and safety intent documented in the digital submission. Before operation, the following will be measured or verified:

- [ ] completed robot mass is strictly below 5 kg;
- [ ] completed robot footprint remains within 500 mm x 500 mm;
- [ ] main ON/OFF switch is accessible and correctly isolates the robot;
- [ ] E-Stop de-energizes the high-current actuator isolation stage;
- [ ] 2.4 GHz RC link and signal-loss/failsafe behavior are verified;
- [ ] motor direction and response are verified;
- [ ] final fuse, contactor/relay, wire and connector ratings match measured loads;
- [ ] motor/driver current and thermal behavior are tested;
- [ ] battery runtime and voltage-under-load are checked;
- [ ] battery restraint, insulation, guards, fasteners and strain relief are inspected;
- [ ] mechanism clearances are confirmed through the required motion range.

If any physical measurement differs from a digital assumption, the hardware build will be adjusted before operation until the applicable Robo Wars constraints are satisfied. No physical-compliance result is claimed before the robot is built and measured.
