# SentinelT Bill of Materials

Primary workbook: `SentinelT_Bill_of_Materials.xlsx`

## Competition Fields Included

The spreadsheet contains:

- Component Name
- Quantity
- Cost per Unit (R)
- Supplier Name
- Supplier Stock Code
- Direct URL / Link
- Total Cost (R)

The **FINAL TOTAL COST** row is highlighted in red, matching the elimination-round requirement.

## Procurement Status

No components are currently owned. Several components are still being selected, so the workbook distinguishes between:

- **TBD** - not yet selected/priced;
- **Candidate** - supplier/product data has been identified but the component is not yet physically validated as part of the complete system;
- **Verified/Purchased** - reserved for later confirmed hardware.

Current supplier-verified candidate rows include the 2.4 GHz RC set, dual brushed ESC, LiPo battery, E-Stop pushbutton, fuse holder and XT60 connector.

The current priced-candidate subtotal is **R3,622.15**. This is **not the final implementation cost** because motors, wheels, chassis/armor, fasteners, wiring, main isolation hardware and final auxiliary hardware are still TBD.

## Safety Note

Supplier current/voltage ratings must be checked against the final measured load. In particular, the E-Stop pushbutton must not automatically be assumed to interrupt the full traction/auxiliary current directly; a properly rated disconnect/contactor may be required.
