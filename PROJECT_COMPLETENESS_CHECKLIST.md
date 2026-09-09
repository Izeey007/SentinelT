# SentinelT Project Completeness Checklist

**Project owner and designer:** Thato Glen Assegaai  
**Category:** Robo Wars - RC Combat

This checklist tracks the current engineering completeness of SentinelT.

## Repository and Project Identity

- [x] Root `README.md` identifies SentinelT and project ownership.
- [x] Repository map covers Source Code, Designs and Documentation.
- [x] No institution is used as project ownership or attribution.
- [x] SentinelT is described directly as a Robo Wars RC combat robot.

## Source Code

- [x] Robo Wars-specific control framework.
- [x] 2.4 GHz RC channel mapping.
- [x] Control flowchart.
- [x] Safe-state logic for startup, reset and RC loss.
- [x] Commented firmware skeleton.
- [ ] Final receiver protocol, hardware pin assignments and ESC calibration will be locked after bench testing.

## Mechanical Design

- [x] Blender CAD file.
- [x] Front, side, top and isometric renders.
- [x] 318.16 mm x 495.00 mm verified footprint.
- [x] Current CAD height recorded as 405.99 mm.
- [x] 180/180 footprint frames PASS; 0 failed frames.
- [x] Material/fabrication approach documented.
- [x] Internal component packaging layout prepared.
- [x] Exploded labelled component-layout view prepared.
- [x] 2.4 GHz transmitter presentation view prepared.

## Electronic and Safety Design

- [x] 3S power architecture documented.
- [x] 2.4 GHz RC system selected.
- [x] Drive motors and drive ESC selected.
- [x] Main ON/OFF isolation documented.
- [x] E-Stop and separate high-current power-disable stage documented.
- [x] RC-loss safe state documented.
- [ ] Final guarded active-mechanism motor/controller remains to be selected and electrically matched.

## Documentation

- [x] A4 portrait, white-page holistic build report.
- [x] A4 portrait, white-page 7-page pitch deck.
- [x] Project-owner photo and responsibilities included.
- [x] Bill of Materials spreadsheet with required procurement fields.
- [x] Final-total row highlighted in red.
- [ ] Final implementation total remains pending the guarded active-mechanism motor/controller selection.
- [ ] FQ&A attendance evidence is added only if genuine proof exists.

## Physical Verification Still Required

- [ ] Measured physical mass.
- [ ] Actual current draw.
- [ ] Battery runtime and temperature behaviour.
- [ ] Drivetrain response under load.
- [ ] E-Stop interruption test on completed hardware.
- [ ] Final physical internal packaging and cable-routing verification.
