# SentinelT Bill of Materials

The elimination-round BOM is stored in this folder as:

- `SentinelT_Bill_of_Materials.xlsx`

## Current Status

The workbook includes the competition-required columns:

- Component Name
- Quantity
- Cost per Unit
- Supplier Name
- Supplier Stock Code
- Direct URL / Link
- Total Cost

The final-total row is visually highlighted in red.

## Current Procurement Progress

The BOM now includes selected candidate data for the chassis/armor stock, drivetrain, 2.4 GHz RC system, battery, branch protection, main isolation, E-Stop components, power distribution, connectors, high-current wiring and serviceable fasteners. The selected direct-drive wheel system does not require separate drive bearings or axles.

Current priced candidate subtotal: **R8,039.15**.

This is **not yet the final implementation total** because the guarded active-mechanism motor/controller remains to be selected and electrically matched. Shipping/import charges and any fabrication-service charges are also not included unless explicitly listed.

## Important Engineering Notes

- The 6 mm HDPE armor panels are cut from the same purchased sheet as the chassis stock, so the material is not double-counted.
- The 10 mm² red/black silicone power wiring is rated by the supplier for high-current use, but final routing, termination and branch protection still require physical verification.
- The E-Stop pushbutton is not treated as the high-current interrupt device by itself; the design uses a separate high-current relay/contactor candidate.
- Final physical mass, actual current draw, thermal behaviour and E-Stop interruption performance must be verified on the completed robot.
