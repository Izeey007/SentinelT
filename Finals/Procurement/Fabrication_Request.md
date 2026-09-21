# SentinelT: materials and fabrication request for TUT review

Individual entrant: TG Assegaai. No components or raw materials owned or purchased. Lab access for steel work is confirmed by the participant; technician supervision, available stock and processes still need confirmation. Use with `Component_Request.xlsx`; its **R11,370.84 priced subtotal is not the cost of a complete build**.

Participant clarification: the rear cutter and pointed front part must be real steel, not cosmetic metallic material. The front feature is recorded as a pointed steel part; powered actuation has not been specified. Retain the hammer assemblies in the review. Prefer lower delivered cost only among parts that meet the reviewed requirements for fit, durability, mass and reliability.

The public event information supplied by the participant states a 10 kg maximum, while the submitted SentinelT engineering documentation has been developed around a stricter **sub-5 kg target**. Until the final-round technical rulebook is confirmed, this request keeps the **5 kg engineering target** because it provides additional compliance margin.

## Recommended physical construction

SentinelT should **not** be fabricated as an all-steel shell. An all-steel body would consume too much of the 5 kg engineering allowance before the drivetrain, battery, controls and mechanisms are installed. The recommended physical build is a hybrid structure: lightweight structural material for the body and real steel only where impact, wear or shaft loading justifies it.

| Assembly | Recommended material / construction | Target installed mass |
|---|---|---:|
| Main lower chassis | Approx. 2 mm 6082-T6 aluminium plate or lab-approved equivalent, locally reinforced | 0.55-0.70 kg |
| Side armour | 6 mm HDPE; PE500/HMWPE/UHMWPE may be substituted where locally available and mass/cost are acceptable | 0.35-0.50 kg |
| Top/service panels | 4-6 mm HDPE, removable for service access | 0.15-0.25 kg |
| Chassis rails/stiffeners | Aluminium angle/flat, sized by workshop review | 0.15-0.25 kg |
| Pointed front part | **Real steel**, preferably a small replaceable 2.5-3 mm wear/impact-resistant part selected by the lab | 0.15-0.25 kg |
| Rear cutter | **Real steel**, workshop-selected wear-resistant/hardenable grade; final geometry/supports remain subject to rules and technician review | 0.20-0.35 kg |
| Cutter shaft/supports | Steel shaft with reviewed bearings; aluminium/steel supports as required by loading | 0.15-0.25 kg |
| Hammer impact/pivot areas | Steel only where required; lightweight arms/support structure elsewhere | 0.15-0.25 kg |
| Brackets/guards | Aluminium by default, steel only at concentrated-load or wear points | 0.15-0.25 kg |

Suitable steel candidates for workshop discussion include small offcuts of wear-resistant plate such as Hardox/AR-class material or a workshop-approved medium-carbon steel such as EN8/C45/1045. These are **candidate material classes, not released specifications**. If unavailable, mild steel may be used for an early prototype/test part, but should not be represented as equivalent to hardened wear-resistant steel.

The existing B01 6 mm HDPE procurement line remains useful. B02/B03 mild-steel bars stay on **design hold** until the lab produces an approved cut list; do not automatically buy full 6 m bars if smaller offcuts or cut-to-size material will satisfy the final drawings.

## Mass-control requirement

The submitted engineering mass allocation is:

| System | Allocation |
|---|---:|
| Chassis and lower armour | 1.10 kg |
| Drive motors and gearboxes | 0.75 kg |
| Wheels, hubs and shafts | 0.30 kg |
| Battery and power system | 0.60 kg |
| RC electronics, motor drivers and wiring | 0.25 kg |
| Guarded active mechanism + drive/mount | 0.70 kg |
| Upper structure, arms and outer shells | 0.50 kg |
| Bearings, brackets and fasteners | 0.25 kg |
| Contingency allowance | 0.20 kg |
| **Engineering total** | **4.65 kg** |
| **Margin to 5.00 kg** | **0.35 kg** |

The 4.65 kg figure is a design allocation, not a measured robot mass. For fabrication, aim for an actual complete mass of approximately **4.50-4.60 kg** where practical so that final guards, wiring, fasteners and fabrication tolerances do not push the robot over 5 kg. The finished robot must be weighed after every major assembly change.

## Requested fabrication scope

Please review and quote both the purchased components and the fabrication work needed to turn the submitted CAD concept into a working robot.

| Assembly | Purchased parts / material | Workshop deliverable needed |
|---|---|---|
| Body and chassis | HDPE/HMWPE-family panels, aluminium chassis/stiffeners and local steel reinforcement | Dimensioned panels, holes, brackets, battery restraint and removable covers |
| Four-wheel drive | Four matched motors, mounts, four shaft-compatible wheels and suitable motor controller(s) | Confirm mounting pattern, wheel clearance, shaft loading, retention and fasteners |
| RC and control | Matched FlySky transmitter/receiver, controller board and interfaces | Secure mounting, wiring and firmware integration; recorded radio-loss and restart tests |
| Power and isolation | Battery, charger, main isolator, E-stop, reviewed switching device, fuses and wiring | Reviewed circuit, complete harness and measured isolation/restart checks |
| Hammer assemblies | Material, actuator, supports, pivots and retention selected as a complete assembly | Load and mass review before purchase; fabrication drawing and quote |
| Front and rear features | Real-steel rear cutter and pointed steel front part | Agree configuration, permitted materials/mechanisms, supports, guarding and transport locks before issuing a cut list |
| Assembly and testing | Fasteners, insulation, strain relief, charging containment and consumables | Assembly, measured complete mass and envelope, staged testing and recorded results |

## Budget-reduced finals route

The preferred request to Kyle is now the reduced list in [`Component_Request_Lean.md`](Component_Request_Lean.md). It keeps the core drive, RC, safety, battery/charging and rear-cutter systems while deferring the hammer/torso servo package and avoiding full-sheet/full-bar purchases before the lab cut list exists.

- Reduced online component subtotal: **R6,256.41**
- Desired TUT material/fabrication allowance: **R1,000-R1,500**, only if suitable lab stock/offcuts and workshop access are available
- **Target complete build request: approximately R7,300-R7,800**
- Optional budget-radio fallback could lower the online subtotal to about **R5,262.41**, but only after satisfactory range/failsafe/reliability testing

The earlier R19,460.84 planning figure is retained below only as a historical full-scope estimate. It is **not** the recommended amount to request from Kyle.

## Historical full-scope provisional completion allowance

The **R11,370.84** in `Component_Request.md` remains the currently priced component subtotal. The following amounts are **engineering planning allowances only** so the request has a realistic complete-build budget before formal supplier/lab quotations arrive.

| Remaining scope | Planning allowance |
|---|---:|
| 4 AA transmitter cells | R80 |
| Additional branch fuse holders / correct fuses | R180 |
| Arming/reset and relay/contactor suppression hardware | R250 |
| Insulated distribution blocks, terminals and covers | R250 |
| Additional power cable, lugs, ferrules and sleeves | R450 |
| Servo/control wiring and connectors | R250 |
| Pico headers, data cable and secure mounting | R120 |
| Structural bolts, nyloc nuts, washers and spacers | R500 |
| Grommets, P-clips, cable ties and strain relief | R150 |
| Correct shafts, bearings, collars/couplings and support hardware | R650 |
| Mechanism guards, retention and transport locks | R400 |
| Battery tray, padding and restraint extras | R180 |
| LiPo fire-resistant charging/storage containment | R180 |
| Delivery and essential spare hardware allowance | R600 |
| Aluminium chassis plate/offcut allowance | R600 |
| Aluminium rails/stiffeners allowance | R250 |
| Tough steel offcuts for front/rear impact parts | R650 |
| Cutting, drilling, CNC/machining and tapping allowance | R1,200 |
| Mechanism/bracket fabrication allowance | R700 |
| Welding/fit-up allowance where actually required | R450 |
| **Provisional completion allowance** | **R8,090.00** |

### Planning total

- Existing priced component subtotal: **R11,370.84**
- Provisional completion/material/fabrication allowance: **R8,090.00**
- **Complete planning total: R19,460.84**
- Recommended funding ceiling for planning/approval: **approximately R20,500**, leaving roughly R1,039 contingency for supplier substitutions, delivery changes and small fabrication revisions.

The **R19,460.84 and R20,500 figures are not supplier quotations**. They are provisional engineering budget figures for planning only. Replace allowance values with actual lab/supplier quotes as they are received. Where an allowance replaces an existing held BOM item, avoid double purchasing and update the total accordingly.

## Material and process decisions

- Cosmetic metallic finishes are not structural steel. Select materials by documented properties, installed mass and role.
- Use real steel selectively at the pointed front feature, rear cutter, shafts, pivots and other concentrated-load/wear locations.
- Use aluminium and engineering plastic for the majority of the chassis/armour to preserve the 5 kg mass target.
- The submitted mild-steel bars are provisional raw-stock entries, not a specification for finished impact parts or cutters.
- Request suitable offcuts or cut-to-size stock when economical. Include grade, thickness, quantity, drawing revision and price on each quote.
- The workshop should select cutting, drilling, machining and joining processes for the actual material.
- Welding is not assumed necessary everywhere; accessible bolted assemblies can simplify maintenance and repair.
- No active-mechanism performance claim is made until the physical mechanism, guards, retention and power system are tested.
- The 1800 RPM value in the Blender animation is a visual simulation reference only and is not a released physical cutter operating speed.

## Information needed before final purchase release

1. Final-round Robo Wars technical rules and mechanism approval.
2. Workshop technician review of the front, rear-cutter and hammer assemblies.
3. Actual supplier dimensions and measured/declared component masses.
4. Approved fabrication drawings/cut list and material grades.
5. Final shaft/bearing/collar compatibility.
6. Electrical protection and isolation ratings based on measured hardware current.
7. Current supplier stock, delivery dates and formal workshop/material quotation.
8. Updated complete mass roll-up with a practical margin below the chosen competition limit.

Nothing has been ordered through this document. Physical construction and testing remain pending until procurement and workshop review are complete.
