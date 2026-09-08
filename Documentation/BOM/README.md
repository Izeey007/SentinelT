# SentinelT Bill of Materials

The SentinelT Bill of Materials is stored in this folder as:

- `SentinelT_Bill_of_Materials.xlsx`

## Workbook Structure

The workbook includes:

- Component Name
- Quantity
- Cost per Unit
- Supplier Name
- Supplier Stock Code
- Direct URL / Link
- Total Cost

The final-total row is visually highlighted in red.

## Current Procurement Plan

The BOM includes selected candidate data for the chassis/armor stock, drivetrain, 2.4 GHz RC system, 3S battery, branch protection, main isolation, E-Stop components, high-current relay/contactor, power distribution, connectors, high-current wiring and serviceable fasteners.

The selected direct-drive wheel system does not require separate drive bearings or axles.

**Current priced component subtotal: R8,039.15.**

This is not yet the final implementation total because the guarded active-mechanism motor/controller remains to be selected and electrically matched. Shipping/import charges and fabrication-service charges are not included unless explicitly listed.

## Engineering Notes

- The 6 mm HDPE armor panels are cut from the same purchased sheet as the chassis stock, so material cost is not double-counted.
- The 10 mm2 red/black silicone power wiring is selected for the high-current distribution path; final routing and terminations will be physically verified.
- The E-Stop pushbutton is not treated as the full high-current interrupt device by itself; the architecture uses a separate high-current relay/contactor candidate.
- Final physical mass, actual current draw, thermal behaviour and E-Stop interruption performance will be verified on the completed robot.
