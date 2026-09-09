# SentinelT Project Completeness Checklist

**Project Developer:** TG Assegaai  
**Category:** Robo Wars - RC Combat

This checklist separates completed digital evidence from items that require the fabricated hardware. Unchecked hardware items will be verified after hardware implementation; they are not claimed as already tested.

## Repository Structure & README - 10 Points

- [x] Root `README.md` contains a high-level SentinelT summary.
- [x] Root `README.md` maps Folder A: Source Code, Folder B: Designs and Folder C: Documentation.
- [x] Root `README.md` explains the contents of all three accessible folders.
- [x] Exactly one detailed README is retained at the root of each required folder: `Source_Code/README.md`, `Designs/README.md`, `Documentation/README.md`.

## Folder A - Source Code - 20 Points

- [x] C/C++ / Arduino-style programming method documented.
- [x] 2.4 GHz RC architecture documented.
- [x] SAFE_DISABLED / RC_READY / OPERATING state logic documented.
- [x] Differential-drive mixing documented.
- [x] 250 ms RC timeout documented.
- [x] Startup/reset safe state documented.
- [x] Auxiliary default-OFF logic documented.
- [x] High-resolution control flowchart included.
- [x] Firmware/control framework included.
- [ ] Exact receiver protocol/channel mapping - **will be verified after hardware implementation**.
- [ ] Final microcontroller pin mapping - **will be verified after hardware implementation**.
- [ ] ESC calibration/end-points - **will be verified after hardware implementation**.

## Folder B - Designs - 40 Points

### Mechanical Design

- [x] Canonical Blender CAD model prepared as `SentinelT_Rob.blend`.
- [x] Front, side, top and isometric CAD renders included.
- [x] Internal component-layout evidence included.
- [x] Exploded component-layout evidence included.
- [x] Fabrication material/fastening method documented.
- [x] 318.16 mm x 495.00 mm footprint digitally verified.
- [x] 180/180 animation frames PASS with 0 failed frames.

### Electronic Design

- [x] Dedicated `Electronic_Design.pdf` included.
- [x] Power/circuit schematic picture included.
- [x] Internal wiring/component-layout picture included.
- [x] Main ON/OFF isolation explicitly documented.
- [x] Mandatory E-Stop integration explicitly documented and pictured.
- [x] Separate high-current relay/contactor isolation concept documented.
- [ ] Final fuse/contactor/wire-current validation - **will be verified after hardware implementation**.

### Simulation / Technical Excellence

- [x] Blender/Python footprint simulation included.
- [x] Audit report records 204 physical meshes, 180 frames, 0 failures.
- [x] Engineering mass-budget script included.
- [ ] Physical scale mass measurement - **will be verified after hardware implementation**.

## Folder C - Documentation - 30 Points

- [x] 7-page A4 portrait `SentinelT_Pitch_Deck.pdf` included.
- [x] `SentinelT_Bill_of_Materials.xlsx` included.
- [x] A4 portrait `SentinelT_Holistic_Build_Document.pdf` included.
- [x] Holistic report includes title header, Robo Wars constraints and solution overview.
- [x] Holistic report includes mechanical, electronic and programming sections with visual evidence.
- [x] Holistic report includes BOM summary and implementation status.
- [x] Project Developer and signature included in formal reports.
- [ ] Final active-mechanism motor/controller procurement line - **will be finalized after hardware matching**.
- [ ] Final physical implementation cost - **will be verified after hardware implementation**.

## FQ&A Bonus

- [ ] FQ&A attendance bonus - **not claimed; no Facilitator Q&A session was attended**.
- [ ] Attendance screenshots - **not available because no FQ&A session was attended**.

## Physical Verification Remaining

The following checks require the actual built robot and will be completed after hardware implementation:

- [ ] calibrated physical mass measurement;
- [ ] E-Stop power-interruption test;
- [ ] RC signal-loss/failsafe bench test;
- [ ] drivetrain direction and response test;
- [ ] motor/ESC current and thermal test;
- [ ] battery runtime and voltage-under-load test;
- [ ] final fastener/guard inspection;
- [ ] final wiring, strain-relief and insulation inspection.
