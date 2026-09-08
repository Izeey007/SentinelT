# SentinelT Power, Control and Emergency-Stop Architecture

**Project:** SentinelT Robo  
**Category:** Robo Wars – RC Combat  
**Designer:** Thato Glen Assegaai

## Safety Objective

SentinelT is designed with two separate operator-accessible safety functions:

1. **MAIN ON/OFF SWITCH**
2. **EMERGENCY STOP (E-STOP)**

The E-Stop is intended to disable actuator power immediately and does not rely only on normal software commands.

---

## Power Architecture

```mermaid
flowchart TD

BAT[Battery Pack]

FUSE[Main Fuse / Protection]

SW[MAIN ON/OFF SWITCH]

ESTOP[EMERGENCY STOP]

PDB[Power Distribution]

CTRL[Control Electronics]

RX[2.4 GHz RC Receiver]

DRV[Drive Motor Controller]

AUX[Active Mechanism Controller]

LM[Left Drive Motor]

RM[Right Drive Motor]

ACT[Guarded Active Mechanism]

BAT --> FUSE
FUSE --> SW
SW --> ESTOP
ESTOP --> PDB

PDB --> CTRL
PDB --> DRV
PDB --> AUX

RX --> CTRL

CTRL --> DRV
CTRL --> AUX

DRV --> LM
DRV --> RM

AUX --> ACT
