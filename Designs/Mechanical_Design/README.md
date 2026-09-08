# Mechanical Design

SentinelT uses a compact armored chassis with protected drive areas, sloped external protection, a central serviceable body and an articulated upper structure.

## CAD Assets

- `CAD/SentinelT_Rob_v101_FINAL_COMPLIANT.blend` - current verified Blender model.
- `Renders/01_SentinelT_FRONT_FINAL.png`
- `Renders/02_SentinelT_SIDE_FINAL.png`
- `Renders/03_SentinelT_TOP_FINAL.png`
- `Renders/04_SentinelT_ISOMETRIC_FINAL.png`

## Verified CAD Dimensions

| Axis | Dimension |
|---|---:|
| X width | **318.16 mm** |
| Y length | **495.00 mm** |
| Z height | **255.41 mm** |

Robo Wars footprint limit: **500 mm x 500 mm**.

My Blender/Python audit checks frames 1-180. Current result: **180/180 frames PASS; 0 failed frames**.

## Mechanical Architecture

- enclosed lower chassis;
- protected wheel and drive areas;
- sloped front and side guards;
- removable top/service-panel concept;
- reinforced central upper-body mounting region;
- articulated upper structure;
- guarded front active-mechanism provision;
- modular access for battery, receiver, power distribution and motor controller.

## Material and Fabrication Plan

The current material plan uses **6 mm HDPE sheet** for the chassis/base and shared armor panels. Metal is retained where it is appropriate for load transfer and hardware, including gearmotor housings, shafts, terminals, brackets and fasteners.

Planned fabrication methods include:

- cut HDPE structural and armor panels;
- bolted M4 serviceable joints;
- replaceable external guards;
- metal brackets/shafts/hardware where required;
- 3D-printed non-critical covers or detail components where useful.

The next CAD revision will add simplified internal component models, wiring paths, a cutaway view and an exploded internal-layout view.

## Engineering Mass Budget

The subsystem design allocation is **4.650 kg**, leaving **0.350 kg** below 5.000 kg. This is not a measured physical mass; the completed robot will be weighed on a calibrated scale.
