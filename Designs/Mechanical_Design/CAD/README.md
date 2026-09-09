# SentinelT CAD Simulation & Animation Controls

**Build:** SentinelT  
**Category:** Robo Wars RC Combat  
**Project Developer:** TG Assegaai  
**Blender file:** `SentinelT_Rob.blend`

## Purpose

This README is the operating guide for the SentinelT Blender simulation model. It explains how a reviewer can open the CAD, return the robot to its neutral position, play the prepared demonstration sequence, and manually inspect the drive, wheels, cutter, hammers and upper-body rotation.

The simulation uses the robot's existing Blender hierarchy and control pivots. The animation system does **not** require re-parenting the mechanical assemblies.

## Open the Simulation

1. Open `SentinelT_Rob.blend` in Blender 5.2 LTS or a compatible version.
2. Select the `SentinelT_Engineering` scene.
3. Set the Timeline to **Frame 0** for the original neutral/rest position.
4. Open the **Animation** workspace.
5. Select the Blender Empty named `SentinelT_Controls`.
6. Press **Spacebar** to play or stop the prepared demonstration.
7. Drag the Timeline or use the Dope Sheet to inspect individual frames.

`SentinelT_Controls` is a non-physical Blender control object. It is used only to expose simulation controls and is not intended to appear in rendered evidence or physical footprint measurements.

## Neutral / Rest Position

Frame **0** is the official reference position:

- drive stopped;
- robot at its original chassis position;
- wheels at home position;
- cutter stopped;
- both hammers at home;
- upper body centered and facing straight forward.

To reset SentinelT after testing, return the Timeline to **Frame 0**.

## SentinelT Controls

Select `SentinelT_Controls`, then open **Object Properties -> Custom Properties**.

| Control | Function |
|---|---|
| `Drive_Enable` | Drive command/status indicator used by the demonstration. |
| `Drive_Distance_m` | Forward/reverse chassis displacement command. Wheel rotation is linked to this value. |
| `Cutter_On` | Cutter ON/OFF command/status indicator. |
| `Cutter_Angle_rad` | Actual cutter rotation angle used by the cutter driver. |
| `Cutter_RPM` | Reference visual cutter speed. Current prepared value: **1800 RPM**. |
| `Hammer_Enable` | Hammer command/status indicator. |
| `Hammer_Swing` | Hammer position command. `0` = home and `1` = maximum permitted outward swing. |
| `Body_Rotation_Deg` | Upper-body yaw command in degrees. |

The continuous controls that directly move geometry are `Drive_Distance_m`, `Cutter_Angle_rad`, `Hammer_Swing` and `Body_Rotation_Deg`.

## Prepared Demonstration Timeline

The simulation runs at **60 fps** over Frames **1-180**.

| Frame range / marker | Demonstration behavior |
|---|---|
| `0` | Original neutral/rest position. |
| `1-50` | Forward drive; wheels rotate; cutter runs. |
| `50-70` | Drive stopped. |
| `61-90` | Cutter stopped. |
| `71-120` | Reverse drive; wheel rotation reverses. |
| `91-180` | Cutter runs again. |
| Throughout | Hammers perform repeated safe outward swings and return home. |
| Throughout | Upper body performs small left/right rotations and returns to center. |
| `180` | Demonstration ends in a stopped state. |

Timeline markers identify the main drive, cutter, hammer and body-control events.

## Drive and Wheel Simulation

The chassis movement uses the existing control root:

`SentinelT_COMPLIANCE_ROOT`

The wheel meshes are:

- `Wheel.004`
- `Wheel.005`
- `Wheel.006`
- `Wheel.007`

The matching wheel hubs are:

- `Wheel hub.004`
- `Wheel hub.005`
- `Wheel hub.006`
- `Wheel hub.007`

The wheel/hub origins are centered on their own geometry so each wheel rotates around its axle instead of orbiting or detaching from the chassis. Forward/reverse wheel rotation is driven from `Drive_Distance_m`.

For manual inspection, change `Drive_Distance_m` gradually while `SentinelT_Controls` is selected. The chassis displacement and wheel rotation should remain synchronized.

## Cutter Simulation

The cutter assembly uses the existing pivot:

`spinner.001`

The cutter rings and triangular teeth are children of this pivot. The prepared demonstration uses a visual reference speed of **1800 RPM**.

- `Cutter_On` records the intended ON/OFF state.
- `Cutter_Angle_rad` directly drives visible cutter rotation.
- Frames `61-90` demonstrate the cutter stopped.
- Frames `1-60` and `91-180` demonstrate the cutter running.

For manual inspection, keep SentinelT stationary and change `Cutter_Angle_rad` gradually.

This is a kinematic simulation. It does not claim measured cutter impact energy, physical motor load or structural impact physics.

## Hammer Simulation and Collision Protection

The existing hammer pivots are:

- `hammer_L.001`
- `hammer_R.001`

The hammer geometry remains parented to those original pivots. `Hammer_Swing` moves the hammers between home and the prepared outward strike position.

The current animation uses local rotation-limit constraints so the hammers are restricted to an outward-safe motion range and do not swing inward through the torso geometry. The prepared maximum swing is approximately **14 degrees** from home.

If the hammer animation is edited, keep the SentinelT hammer safety limits active and inspect the full motion path before saving a new submission model.

## Upper-Body Rotation

Upper-body rotation uses the existing pivot:

`ST05 TORSO rotation`

`Body_Rotation_Deg` controls torso yaw. The prepared demonstration uses small rotations of approximately `+4 deg` to `-4 deg`, with a local safety limit of approximately **+/-5 degrees**.

At Frame 0 the upper body is centered and faces straight forward.

## Manual Simulation Test

A reviewer can test individual mechanisms without playing the full animation:

1. Go to **Frame 0**.
2. Select `SentinelT_Controls`.
3. Change one control at a time.
4. Use `Drive_Distance_m` to test chassis/wheel movement.
5. Use `Cutter_Angle_rad` to inspect cutter rotation.
6. Use `Hammer_Swing` between `0` and `1` to inspect hammer travel.
7. Use `Body_Rotation_Deg` within the permitted range to inspect torso rotation.
8. Return all controls to neutral or return to **Frame 0** when finished.

## Simulation Scope

The Blender model provides digital kinematic design verification and mechanism demonstration for:

- mechanical CAD geometry;
- forward/reverse chassis movement;
- synchronized wheel rotation;
- cutter ON/OFF and rotation;
- hammer travel and motion limits;
- upper-body rotation;
- component-clearance inspection;
- footprint behavior across animated frames;
- reviewer presentation and design verification.

The model does **not** claim full rigid-body combat physics, measured motor torque, measured cutter impact energy, real tire traction, measured battery runtime, structural impact failure or measured E-Stop interruption time. Those items require physical hardware implementation and testing.

## Footprint Verification

The verified engineering baseline is **318.16 mm x 495.00 mm** in plan view, within the required 500 mm x 500 mm Robo Wars footprint.

The digital audit checked **180 frames with 0 failed frames** before the latest simulation-control refinement. After changing geometry or animation, rerun the footprint audit in `Designs/Simulation/` before treating the modified `.blend` as the submission model.

## Important Editing Rules

To preserve the working SentinelT model:

- do not re-parent the mechanical hierarchy for animation;
- use the existing pivots documented above;
- keep Frame 0 as the original neutral reference position;
- keep hammer and torso rotation-limit constraints active;
- keep wheel origins centered on their geometry;
- save a backup before editing drivers or animation curves;
- rerun the footprint audit after geometry or animation changes;
- keep non-physical controls and remote presentation geometry outside the physical footprint audit.

## Quick Judge / Reviewer Test

1. Open `SentinelT_Rob.blend`.
2. Confirm Frame 0 shows SentinelT in the neutral straight-forward position.
3. Select `SentinelT_Controls`.
4. Press **Spacebar** to play Frames 1-180.
5. Observe forward/reverse drive and synchronized wheel motion.
6. Observe cutter ON/OFF behavior and fast rotation.
7. Observe both hammers moving within their safe outward limits.
8. Observe the upper body rotate slightly and return to center.
9. Return the Timeline to Frame 0 after inspection.

---

**Project Developer:** TG Assegaai
