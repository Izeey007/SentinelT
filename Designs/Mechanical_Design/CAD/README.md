# SentinelT CAD Simulation & Animation Controls

**Build:** SentinelT  
**Category:** Robo Wars RC Combat  
**Project Developer:** TG Assegaai  
**Blender file:** `SentinelT_Rob.blend`

## Purpose

This README explains how to open, animate and control the SentinelT Blender model for digital simulation and review. The `.blend` contains the mechanical CAD, articulated mechanisms, wheel-drive animation, cutter animation, hammer animation, upper-body rotation and a non-rendering control object named `SentinelT_Controls`.

The animation system uses the robot's existing Blender hierarchy and control pivots. The working control setup does not require re-parenting the SentinelT mechanical assemblies.

## Open the Simulation

1. Open `SentinelT_Rob.blend` in Blender 5.2 LTS or a compatible version.
2. Use the `SentinelT_Engineering` scene.
3. Set the timeline to **Frame 0** for the original neutral/rest position.
4. Switch to the **Animation** workspace.
5. Select the object named `SentinelT_Controls`.
6. Press **Spacebar** to play or stop the demonstration animation.
7. Use the Timeline/Dope Sheet to move directly to a required frame.

`SentinelT_Controls` is a Blender Empty used only as a control panel. It is not a physical robot component and is not intended to appear in rendered evidence.

## Neutral / Rest Position

Frame **0** is the reference position for inspection:

- drive stopped;
- wheels at their home position;
- cutter stopped;
- left and right hammers at home;
- upper body centered and facing forward;
- SentinelT remains in its original mechanical position.

To return the model to the reference position, set the timeline to **Frame 0**.

## Master Control Object

Select `SentinelT_Controls`, then open **Object Properties -> Custom Properties**. The control channels are:

| Control | Function |
|---|---|
| `Drive_Enable` | Drive command/status flag used by the demonstration sequence. |
| `Drive_Distance_m` | Actual forward/reverse chassis displacement command. Wheel rotation is linked to this value. |
| `Cutter_On` | Cutter command/status flag used by the timeline. |
| `Cutter_Angle_rad` | Actual cutter rotation angle used by the cutter driver. |
| `Cutter_RPM` | Reference visual cutter speed; current demonstration value is 1800 RPM. |
| `Hammer_Enable` | Hammer command/status flag. |
| `Hammer_Swing` | Actual hammer position command: `0` = home and `1` = maximum permitted outward swing. |
| `Body_Rotation_Deg` | Upper-body yaw command in degrees. |

The status flags identify the intended command state. The continuous motion properties (`Drive_Distance_m`, `Cutter_Angle_rad`, `Hammer_Swing`, and `Body_Rotation_Deg`) are the values that directly drive the animated mechanisms.

## Demonstration Timeline

The file contains a 60 fps demonstration sequence over Frames **1-180**. The key sequence is:

| Frame range / marker | Demonstration behavior |
|---|---|
| `0` | Original neutral/rest position. |
| `1-50` | Forward drive; wheels rotate; cutter runs. |
| `50-70` | Drive stops. |
| `61-90` | Cutter stopped. |
| `71-120` | Reverse drive; wheel rotation reverses. |
| `91-180` | Cutter runs again. |
| Throughout | Hammers perform repeated safe outward swings and return home. |
| Throughout | Upper body performs small left/right rotations and returns to center. |
| `180` | Demonstration ends in a stopped state. |

Timeline markers are included to identify the principal drive, cutter, hammer and body-control events.

## Drive and Wheel Control

The main robot motion uses the existing object:

`SentinelT_COMPLIANCE_ROOT`

The wheel meshes are:

- `Wheel.004`
- `Wheel.005`
- `Wheel.006`
- `Wheel.007`

The matching hubs are:

- `Wheel hub.004`
- `Wheel hub.005`
- `Wheel hub.006`
- `Wheel hub.007`

The wheels and hubs are driven from `Drive_Distance_m`. Their origins are centered on their geometry so the wheels rotate around their own axles rather than orbiting or detaching from the chassis.

For manual inspection, change `Drive_Distance_m` gradually and observe both chassis translation and synchronized wheel rotation.

## Cutter Control

The cutter assembly uses the existing pivot:

`spinner.001`

The cutter rings and triangular teeth are children of this pivot. The demonstration uses a visual reference speed of **1800 RPM**. The actual visible rotation is driven by `Cutter_Angle_rad`; `Cutter_On` records the intended ON/OFF state in the timeline.

To inspect the cutter safely in Blender:

1. Keep the robot at Frame 0 or another stationary frame.
2. Select `SentinelT_Controls`.
3. Change `Cutter_Angle_rad` gradually to inspect cutter rotation.
4. Use the timeline to view the prepared fast-spin sequence.

This is a digital kinematic animation and does not represent physical impact energy or motor-load physics.

## Hammer Control and Body-Collision Protection

The hammer pivots are:

- `hammer_L.001`
- `hammer_R.001`

The hammer meshes remain children of these existing pivots. `Hammer_Swing` drives both hammer mechanisms from home to their permitted outward position.

The hammer animation includes local `LIMIT_ROTATION` constraints so the demonstration is restricted to the outward side of the existing pivot range. The current demonstration swing is approximately **14 degrees** from the home position. The purpose of this limit is to prevent the hammer animation from passing inward through the torso geometry.

If hammer motion is edited, do not remove the SentinelT hammer safety limits without re-checking the complete motion path.

## Upper-Body Rotation

Upper-body rotation uses the existing control pivot:

`ST05 TORSO rotation`

`Body_Rotation_Deg` drives the torso yaw. The prepared animation uses small movements of approximately `+4 deg` to `-4 deg`, while the local body-rotation constraint limits the permitted range to approximately **+/-5 degrees**.

Frame 0 is the centered straight-forward orientation.

## Simulation Scope

The Blender model provides **kinematic design verification and mechanism demonstration**. It can be used to inspect:

- chassis and articulated geometry;
- wheel rotation and forward/reverse movement;
- cutter ON/OFF animation;
- hammer motion and motion limits;
- upper-body rotation;
- component clearances;
- footprint behavior across animation frames;
- presentation views and mechanical layout.

The model does **not** claim full rigid-body combat physics, measured motor torque, real cutter impact energy, real battery runtime, tire traction, structural impact failure or measured E-Stop interruption time. Those items require physical hardware implementation and testing.

## Footprint Verification

The verified engineering baseline is **318.16 mm x 495.00 mm** in plan view, within the 500 mm x 500 mm Robo Wars footprint. The digital audit previously checked 180 frames with 0 failed frames.

After changing any wheel, hammer, cutter, body or drive animation, rerun the footprint audit in `Designs/Simulation/` before treating the modified `.blend` as the submission model.

## Important Editing Rules

To preserve the working model:

- do not re-parent the SentinelT mechanical hierarchy for animation;
- use the existing control pivots listed above;
- keep Frame 0 as the neutral reference position;
- keep the hammer and torso rotation-limit constraints active;
- save a backup before changing drivers or animation curves;
- rerun the footprint audit after geometry or animation edits;
- keep the remote-control presentation geometry separate from the physical robot footprint audit.

## Quick Judge / Reviewer Test

For a fast review of the digital model:

1. Open `SentinelT_Rob.blend`.
2. Confirm Frame 0 shows SentinelT in the neutral straight-forward position.
3. Select `SentinelT_Controls`.
4. Press Spacebar to play Frames 1-180.
5. Observe synchronized wheel/drive motion, cutter ON/OFF behavior, safe hammer swings and upper-body rotation.
6. Return to Frame 0 after inspection.

---

**Project Developer:** TG Assegaai
