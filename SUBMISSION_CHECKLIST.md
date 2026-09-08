# SentinelT Robo Rumble - Submission Readiness Checklist

**Category:** Robo Wars - RC Combat  
**Designer:** Thato Glen Assegaai

This checklist maps the repository against the 120-point elimination rubric.

## 1. GitHub Structure & README - 10 Points

- [x] Root `README.md`
- [x] High-level SentinelT summary
- [x] Category clearly stated
- [x] Directory map
- [x] Verified dimensions and mass-design note

## 2. Source Code - 20 Points

- [x] Robo Wars-specific source-code folder
- [x] Programming/control architecture documented
- [x] Mermaid control flowchart
- [x] 2.4 GHz RC control mapping
- [x] Safety-state / signal-loss logic
- [x] Commented firmware skeleton
- [ ] Replace hardware TODOs with final receiver protocol, pin assignments and ESC calibration after component selection/testing

## 3. Designs - 40 Points

### Mechanical - 15
- [x] Blender CAD file
- [x] Front render
- [x] Side render
- [x] Top render
- [x] Isometric render
- [x] Fabrication approach documented
- [x] 318.16 mm x 495.00 mm footprint verified

### Electronic - 10
- [x] Electronic architecture documented
- [x] Candidate components identified
- [x] Power/control blocks explained
- [ ] Final motor, fuse, wire, switch/disconnect and battery ratings still require matched-system validation

### Safety - 15
- [x] MAIN ON/OFF explicitly annotated
- [x] E-STOP explicitly annotated
- [x] RC-loss safe-state documented
- [x] Startup/shutdown sequences documented
- [x] High-current E-Stop rating caveat documented
- [ ] Final physical E-Stop/disconnect hardware still requires electrical validation

### Simulation Bonus Evidence
- [x] Blender/Python footprint audit
- [x] 180/180 checked frames PASS
- [x] Repeatable audit script in repository
- [x] Engineering mass-budget script

## 4. Documentation - 30 Points

### Holistic Build Document - 10
- [x] Full technical report
- [x] Mechanical section
- [x] Electronic section
- [x] Programming/framework section
- [x] Safety/E-Stop section
- [x] Simulation and limitations
- [x] Final formatted PDF uploaded as `Documentation/Holistic_Build_Document/SentinelT_Holistic_Build_Document.pdf`

### Bill of Materials - 10
- [x] Required XLSX exists
- [x] Required competition columns included
- [x] Formula-driven totals
- [x] Final-total row highlighted red
- [x] Verified candidate supplier data added for selected items
- [ ] All remaining TBD rows must be priced/selected before claiming a final implementation total

### Pitch Deck - 10
- [x] Final PDF uploaded as `Documentation/Pitch_Deck/SentinelT_Pitch_Deck.pdf`
- [x] 7-slide maximum respected
- [x] Clean white-page presentation theme
- [x] Problem/constraints covered
- [x] Solution/buildability covered
- [x] CAD/simulation evidence included
- [x] Cost/mass section included
- [x] Individual-role slide included
- [x] Genuine photo of Thato Glen Assegaai included

## 5. Bonus - 20 Points

### FQ&A Attendance - up to 10
- [x] Correct attendance-log structure
- [x] `FQA_Proof/` folder
- [ ] Add only genuine attendance sessions and screenshots if available

### Technical Excellence / Simulation - up to 10
- [x] High-quality CAD renders
- [x] Repeatable footprint simulation/audit
- [x] Full animation-range footprint verification
- [x] Safety architecture and documented limitations

## Remaining Before Submission

1. Complete as many remaining BOM supplier/cost rows as possible. Do not call the current subtotal the final implementation cost until every required row is populated.
2. Add FQ&A attendance screenshots only if genuine proof exists.
3. Final physical mass, E-Stop operation, electrical load ratings and drivetrain testing remain physical-prototype verification tasks and should not be misrepresented as completed.

## Current Repository Status

The elimination-round repository structure, CAD, renders, source-code framework, simulation evidence, safety architecture, pitch-deck PDF and holistic-build PDF are all present. The main documentation weakness remaining is incomplete BOM procurement detail; FQ&A points depend on genuine attendance evidence.
