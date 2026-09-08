# Designs - SentinelT Robo Wars

This folder contains the physical/electronic design evidence required for the Robo Rumble elimination round.

## Mechanical Design

`Mechanical_Design/`

Contains:
- final Blender CAD model;
- front, side, top and isometric renders;
- fabrication approach;
- verified CAD dimensions and footprint results.

**Verified CAD:** 318.16 mm x 495.00 mm x 255.41 mm.  
**Footprint audit:** 180/180 checked frames PASS.

## Electronic Design

`Electronic_Design/`

Documents the planned battery, fuse, power isolation, E-Stop, RC receiver, control electronics, drive controller and auxiliary-control architecture.

## Schematics

`Schematics/SentinelT_Power_and_EStop.md`

Explicitly identifies:
- **MAIN ON/OFF SWITCH**;
- **EMERGENCY STOP / power-disable stage**;
- battery and fuse path;
- 2.4 GHz RC receiver;
- drive and auxiliary controllers;
- RC-loss safe-state behaviour.

## Simulation / Digital Verification

`Simulation/`

Contains repeatable Blender/Python audit scripts for:
- 500 mm x 500 mm footprint verification;
- engineering mass-budget reporting.

The 4.650 kg mass figure is an engineering allocation rather than a measured physical mass. Final physical weighing and electrical/mechanical validation are still required before competition use.
