# Designs - SentinelT Robo Wars

This folder contains the mechanical, electronic, safety and simulation design work for SentinelT.

## Mechanical Design

`Mechanical_Design/` contains:

- the Blender CAD model;
- front, side, top and isometric renders;
- fabrication and fastening approach;
- verified CAD dimensions and footprint results.

**Verified CAD envelope:** 318.16 mm x 495.00 mm x 255.41 mm  
**Footprint audit:** 180/180 checked frames PASS.

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

`Simulation/` contains repeatable Blender/Python tools for:

- 500 mm x 500 mm footprint verification;
- engineering mass-budget reporting.

The 4.650 kg value is an engineering allocation rather than a measured physical mass. Final physical weighing and electrical/mechanical validation will be performed on the fabricated robot.
