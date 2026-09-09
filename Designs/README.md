# Designs - SentinelT Robo Wars

This folder contains the mechanical, electronic, safety and simulation design work for SentinelT.

## Mechanical Design

`Mechanical_Design/` contains:

- the canonical Blender CAD model;
- front, side, top and isometric renders;
- internal packaging, exploded-layout and 2.4 GHz transmitter views;
- fabrication and fastening approach;
- verified CAD dimensions and footprint results.

**Verified CAD envelope:** 318.16 mm x 495.00 mm x 405.99 mm  
**Footprint audit:** 180/180 checked frames PASS; 0 failed frames.

## Electronic Design

`Electronic_Design/` documents the selected 3S power architecture, 2.4 GHz RC link, drive motors, drive ESC, fuse/protection, main isolation, E-Stop control, high-current relay/contactor, power distribution and wiring plan.

## Schematics

`Schematics/SentinelT_Power_and_EStop.md` explicitly identifies:

- **MAIN ON/OFF SWITCH**;
- **EMERGENCY STOP / power-disable stage**;
- battery and fuse path;
- 2.4 GHz RC receiver;
- drive and auxiliary controllers;
- RC-loss safe-state behaviour.

## Simulation and Digital Verification

`Simulation/` contains repeatable Blender/Python tools and recorded evidence for:

- 500 mm x 500 mm footprint verification across frames 1-180;
- engineering mass-budget reporting.

The 4.650 kg value is an engineering allocation rather than a measured physical mass. Final physical weighing and electrical/mechanical validation will be performed on the fabricated robot.
