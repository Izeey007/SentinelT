# SentinelT Procurement Notes

**Project Developer:** TG Assegaai  
**Build:** SentinelT  
**Category:** Robo Wars - RC Combat

The funding BOM lists the hardware and raw materials intended for the physical SentinelT implementation. Prices were checked during September 2026 and should be reconfirmed when procurement is authorized because stock and retail pricing can change.

## Drivetrain correction

The physical drivetrain is budgeted around **four 12 V 160 RPM 37 mm brushed gearmotors** and a **Cytron MDD20A dual-channel motor driver**. Two motors are assigned to each side. This replaces the earlier WP-880 concept because independent left/right control is required for differential steering.

## Safety procurement

The BOM separately funds:

- an accessible main ON/OFF battery isolator;
- an E-Stop mushroom switch used in a low-current normally-closed safety loop;
- a separate high-current relay/contactor candidate that removes actuator power when the E-Stop loop opens;
- main/branch fuse protection;
- XT60 power connectors and 12 AWG cable assemblies;
- insulation and battery restraint hardware.

Final fuse value, relay/contactor rating, cable rating and interruption performance are verified against measured hardware current before powered operation.

## Mechanical materials

Raw HDPE and mild-steel stock are budgeted because the physical robot must be fabricated from purchased material. Laboratory cutting/machining access can be used for shaping and finishing, but the raw material itself is included in the procurement request.

## Active mechanisms

The funding list includes a candidate 775 brushed motor and high-current H-bridge for the cutter, plus three high-torque ST3215 serial-bus servos for the two hammer mechanisms and torso rotation. Their final mounting, mechanical load, current draw, guards and motion limits are verified during hardware implementation before operation.

## Physical compliance statement

The current submitted Blender model has a fresh digital footprint audit of approximately **316.10 mm x 466.11 mm x 405.99 mm**, with **204 engineering mesh objects**, Frames **0-180**, and **0 failed footprint frames**. This is digital geometry evidence, not a claim of completed physical testing.

The physical SentinelT build will follow the same documented Robo Wars architecture and constraints. During implementation, the completed robot will be measured and adjusted as necessary so that:

- physical mass is strictly below 5 kg;
- overall footprint remains within 500 mm x 500 mm;
- the RC system operates at 2.4 GHz;
- the main ON/OFF switch remains accessible;
- the E-Stop removes actuator power through the separate high-current isolation stage;
- no prohibited projectiles, flames or liquids are used.
