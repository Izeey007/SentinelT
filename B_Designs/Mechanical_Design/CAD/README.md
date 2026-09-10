# SentinelT CAD Simulation & Animation Controls

**Build:** SentinelT  
**Category:** Robo Wars RC Combat  
**Project Developer:** TG Assegaai  
**Blender file:** `SentinelT_Rob.blend`

## Purpose

This README is the operating guide for the SentinelT Blender simulation model. It explains how a reviewer can open the CAD, return the robot to its neutral position, play the prepared demonstration sequence, and inspect the drive, wheels, cutter, hammers and upper-body rotation.

The simulation uses SentinelT's existing Blender hierarchy and control pivots. The animation system does not require re-parenting the mechanical assemblies.

## Open the Simulation

1. Open `SentinelT_Rob.blend` in Blender 5.2 LTS or a compatible version.
2. Select the `SentinelT_Engineering` scene.
3. Set the Timeline to **Frame 0** for the original neutral/rest position.
4. Open the **Animation** workspace.
5. Select the Empty named `SentinelT_Controls`.
6. Press **Spacebar** to play or stop the prepared demonstration.
7. Drag the Timeline or use the Dope Sheet to inspect individual frames.

`SentinelT_Controls` is a non-physical Blender control object and is excluded from physical footprint interpretation.

## Neutral / Rest Position

Frame **0** is the reference position:

- drive stopped;
- robot at its original chassis position;
- wheels at home position;
- cutter stopped;
- both hammers at home;
- upper body centered and facing straight forward.

Return to Frame 0 after testing.

## SentinelT Controls

Select `SentinelT_Controls`, then open **Object Properties -> Custom Properties**.

| Control | Function |
|---|---|
| `Drive_Enable` | Drive command/status indicator. |
| `Drive_Distance_m` | Forward/reverse chassis displacement; wheel rotation follows this value. |
| `Cutter_On` | Cutter ON/OFF command/status indicator. |
| `Cutter_Angle_rad` | Cutter rotation angle used by the visible cutter driver. |
| `Cutter_RPM` | Visual cutter-speed reference; prepared value is 1800 RPM. |
| `Hammer_Enable` | Hammer command/status indicator. |
| `Hammer_Swing` | Hammer position; `0` = home and `1` = prepared outward swing. |
| `Body_Rotation_Deg` | Upper-body yaw command in degrees. |

## Prepared Demonstration Timeline

The simulation runs at **60 fps** over Frames **1-180**.

| Frame range | Demonstration behavior |
|---|---|
| `0` | Neutral/rest position. |
| `1-50` | Forward drive; wheels rotate; cutter runs. |
| `50-70` | Drive stopped. |
| `61-90` | Cutter stopped. |
| `71-120` | Reverse drive; wheel rotation reverses. |
| `91-180` | Cutter runs again. |
| Throughout | Hammers perform outward swings and return home. |
| Throughout | Upper body performs small left/right rotations and returns to center. |
| `180` | Demonstration ends stopped. |

## Drive and Wheel Simulation

The chassis movement uses `SentinelT_COMPLIANCE_ROOT`. The wheel meshes are `Wheel.004` through `Wheel.007`, with matching hubs `Wheel hub.004` through `Wheel hub.007`.

The wheel/hub origins are centered on their geometry so each wheel rotates around its axle instead of orbiting or detaching from the chassis. Forward/reverse wheel rotation is synchronized with `Drive_Distance_m`.

## Cutter Simulation

The cutter assembly uses pivot `spinner.001`. The cutter rings and triangular teeth are children of this pivot. The prepared animation uses a visual reference of **1800 RPM**.

`Cutter_On` represents the intended ON/OFF state and `Cutter_Angle_rad` drives visible cutter rotation. Frames 61-90 show the stopped state; Frames 1-60 and 91-180 show rotation.

This is a kinematic mechanism demonstration, not a claim of measured cutter impact energy, motor load or structural impact performance.

## Hammer Simulation

The hammer pivots are `hammer_L.001` and `hammer_R.001`. The hammer geometry remains parented to those original pivots. `Hammer_Swing` moves the hammers between home and the prepared outward position.

Local rotation limits restrict the animated hammers to an outward-safe range and prevent the prepared demonstration from swinging them inward through the torso geometry. Physical actuator torque and impact performance will be verified during hardware implementation.

## Upper-Body Rotation

Upper-body rotation uses `ST05 TORSO rotation`. `Body_Rotation_Deg` controls torso yaw. The prepared demonstration uses small rotations of approximately +/-4 degrees with a local limit of approximately +/-5 degrees.

At Frame 0 the upper body is centered and faces straight forward.

## Current Footprint Verification

A fresh audit of the current submitted `SentinelT_Rob.blend` model checked **204 engineering mesh objects** over **Frames 0-180**.

| Audit item | Result |
|---|---:|
| Maximum X | **316.10 mm** |
| Maximum Y | **466.11 mm** |
| Maximum Z | **405.99 mm** |
| Footprint limit | **500 mm x 500 mm** |
| Failed frames | **0** |
| Result | **PASS** |

The audit is digital geometry evidence. It does not replace physical weighing, fabrication-tolerance checks, current testing, structural verification or E-Stop interruption testing.

## Physical Hardware Implementation

The physical robot will be fabricated to follow the same CAD packaging, motion intent and Robo Wars constraints represented here. The completed hardware will be checked for the required sub-5 kg mass, maximum 500 mm x 500 mm footprint, mechanism clearances and safe operation. If a physical measurement differs from the digital design assumptions, the build will be adjusted before operation so it remains within the applicable limits.

## Quick Reviewer Test

1. Open `SentinelT_Rob.blend`.
2. Confirm Frame 0 shows the neutral straight-forward position.
3. Select `SentinelT_Controls`.
4. Play Frames 1-180.
5. Observe forward/reverse drive and synchronized wheel motion.
6. Observe cutter ON/OFF behavior.
7. Observe both hammer motions.
8. Observe the upper-body rotation.
9. Return to Frame 0.

---

**Project Developer:** TG Assegaai
