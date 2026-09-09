# Mechanical Design

SentinelT uses a compact armored chassis with protected drive areas, sloped external protection, a central serviceable body and an articulated upper structure.

## CAD Assets

- `CAD/SentinelT_Rob.blend` - canonical verified Blender model.
- `Renders/01_SentinelT_FRONT_FINAL.png`
- `Renders/02_SentinelT_SIDE_FINAL.png`
- `Renders/03_SentinelT_TOP_FINAL.png`
- `Renders/04_SentinelT_ISOMETRIC_FINAL.png`
- `Renders/SentinelT_Internal_Layout.jpg` - internal electronics/drivetrain packaging layout.
- `Renders/SentinelT_Exploded_Layout.jpg` - labelled component-layout view.
- `Renders/SentinelT_Remote.jpg` - SentinelT with the 2.4 GHz transmitter concept.

## Verified CAD Dimensions

| Axis | Dimension |
|---|---:|
| X width | **318.16 mm** |
| Y length | **495.00 mm** |
| Z height | **405.99 mm** |

Robo Wars footprint limit: **500 mm x 500 mm**.

My Blender/Python audit checks frames 1-180. Current result: **180/180 frames PASS; 0 failed frames**.

The current audit evaluated **204 physical mesh objects**. The maximum X and Y values occurred at frame 1.

## Mechanical Architecture

- enclosed lower chassis;
- protected wheel and drive areas;
- sloped front and side guards;
- removable top/service-panel concept;
- reinforced central upper-body mounting region;
- articulated upper structure;
- guarded front active-mechanism provision;
- modular access for battery, receiver, power distribution and motor controller;
- internal packaging concept for drive motors, 3S LiPo battery, ESC, receiver, fuse, E-Stop relay, power distribution, XT60, main isolation and auxiliary control;
- separate 2.4 GHz transmitter presentation model.

## Material and Fabrication Plan

The current material plan uses **6 mm HDPE sheet** for the chassis/base and shared armor panels. Metal is retained where it is appropriate for load transfer and hardware, including gearmotor housings, shafts, terminals, brackets and fasteners.

Planned fabrication methods include:

- cut HDPE structural and armor panels;
- bolted M4 serviceable joints;
- replaceable external guards;
- metal brackets/shafts/hardware where required;
- 3D-printed non-critical covers or detail components where useful.

## Engineering Mass Budget

The subsystem design allocation is **4.650 kg**, leaving **0.350 kg** below 5.000 kg. This is not a measured physical mass; the completed robot will be weighed on a calibrated scale.
