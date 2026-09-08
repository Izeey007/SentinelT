# SentinelT_Robo

**Designer:** Thato Glen Assegaai  
**Category:** Robo Wars – RC Combat  
**Competition:** Robo Rumble

## Project Summary

SentinelT is a compact remotely controlled combat robot designed for the
Robo Wars category of the Robo Rumble competition.

The design combines a low-profile armored mobile chassis, protected drive
system, sloped frontal protection, articulated upper structure, and a guarded
active-mechanism concept.

The robot is designed around the mandatory competition constraints including:

- Maximum footprint: 500 mm × 500 mm
- Maximum mass: strictly below 5 kg
- 2.4 GHz remote-control communication
- Accessible main ON/OFF switch
- Emergency Stop system
- No projectiles, flames, or liquids

## Verified CAD Compliance

Final CAD dimensions:

- X width: 318.16 mm
- Y length: 495.00 mm
- Z height: 255.41 mm

Footprint requirement:

500 mm × 500 mm maximum

CAD audit result:

**PASS**

Animation/compliance frames checked:

**180 / 180 PASS**

## Engineering Mass Budget

Maximum permitted mass:

5.000 kg

Planned engineering mass:

4.650 kg

Remaining design margin:

0.350 kg

**Engineering mass-budget status: PASS**

> The 4.650 kg value is a design estimate. Final physical mass must be
> verified using a calibrated weighing scale before competition.

## Control Method

SentinelT is manually controlled using a 2.4 GHz RC communication system,
in accordance with Robo Wars regulations.

## Safety

The electrical architecture includes:

- Main ON/OFF power isolation
- Emergency Stop mechanism
- Power isolation for the active mechanism
- Clearly labelled shutdown controls

Detailed circuit diagrams and E-Stop annotations are provided under
`Designs/Schematics/`.

## Repository Structure

### Source_Code
Firmware, RC-control logic, programming architecture and flowcharts.

### Designs
Mechanical CAD, renders, fabrication information, electronic design,
schematics, E-Stop integration and simulation evidence.

### Documentation
Pitch deck, Bill of Materials, holistic technical report and FQ&A
attendance records.