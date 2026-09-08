# SentinelT Pitch Deck - 7 Slide Content Source

## Slide 1 - SentinelT Robo Wars

**SentinelT Robo Wars Combat Robot**  
Robo Rumble 2026 - Elimination Round  
**Designer:** Thato Glen Assegaai  
**Category:** Robo Wars - RC Combat

Key statement: Compact, armored and digitally verified for the Robo Wars elimination constraints.

Visual: final isometric CAD render.

---

## Slide 2 - Problem & Constraints

### Engineering Challenge
Build a remote-controlled combat robot that can be maneuvered reliably while meeting strict competition packaging, mass, communication and safety requirements.

### Mandatory Constraints
- Maximum footprint: **500 mm x 500 mm**
- Physical mass: **strictly below 5 kg**
- Human-operated control: **2.4 GHz RC only**
- Accessible **ON/OFF** switch
- Mandatory **Emergency Stop**
- No projectiles, flames or liquids

---

## Slide 3 - SentinelT Solution

SentinelT combines:
- compact armored lower chassis;
- protected drive areas;
- sloped frontal/side protection;
- removable service cover;
- articulated upper structure;
- guarded active-mechanism provision;
- 2.4 GHz RC architecture;
- safe-state control philosophy.

Visual: front/isometric render.

---

## Slide 4 - CAD Compliance & Simulation

### Verified CAD Dimensions
- X: **318.16 mm**
- Y: **495.00 mm**
- Z: **255.41 mm**

### Digital Verification
- Frames checked: **180**
- Failed frames: **0**
- Footprint status: **PASS**

Custom Blender/Python audit scripts are included in `Designs/Simulation/`.

Visual: top/side render plus compliance callout.

---

## Slide 5 - Electronics, RC & Safety

### Control
Human-operated **2.4 GHz RC** transmitter/receiver architecture.

### Safety Chain
Battery -> Fuse -> **MAIN ON/OFF** -> **E-STOP / power-disable** -> Power Distribution -> Controllers -> Actuators

### Fail-safe Logic
- startup outputs disabled;
- lost/invalid RC signal disables commands;
- E-Stop is a hardware safety layer;
- auxiliary actuation defaults OFF.

---

## Slide 6 - Buildability, Mass & Cost

### Engineering Mass Allocation
- Planned design mass: **4.650 kg**
- Remaining design margin: **0.350 kg**
- Physical weighing still required after fabrication.

### Current BOM Status
- No components are owned.
- Verified candidate subtotal: **R3,622.15**
- Remaining motor, wheel, chassis/armor, wiring, isolation and hardware rows are still TBD.

The candidate subtotal must not be presented as the final implementation cost until the BOM is complete.

---

## Slide 7 - Individual Entrant

### Thato Glen Assegaai
Individual entrant / project designer

Responsibilities:
- concept development;
- CAD modelling;
- mechanical architecture;
- Blender scripting and footprint auditing;
- electronic/control architecture;
- programming framework;
- safety documentation;
- GitHub repository and submission documentation.

**MANDATORY:** Insert a genuine individual photo on this slide before final submission.
