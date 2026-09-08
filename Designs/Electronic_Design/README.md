# Electronic Design

SentinelT's electronics are organised around safe 2.4 GHz human-operated RC control and separated power/control paths.

## Proposed Functional Blocks

- battery pack;
- main fuse/protection;
- accessible main ON/OFF isolation;
- E-Stop / actuator-power-disable stage;
- power distribution;
- 2.4 GHz RC receiver;
- embedded controller / interface logic;
- dual drive motor controller;
- drive motors;
- auxiliary controller for the guarded active mechanism.

## Candidate Components Identified

The BOM currently includes verified supplier data for several candidate items, including:

- FlySky FS-i6X transmitter + X6B receiver (2.4 GHz);
- HobbyWing QuicRun WP 880 dual brushed ESC;
- 2S 5000 mAh LiPo candidate;
- emergency pushbutton candidate;
- fuse holder candidate;
- XT60 connector candidate.

These are **procurement candidates**, not a final electrically validated system. Final voltage/current ratings, wire gauges, fusing, motor selection and disconnect implementation must be verified as a matched system before physical operation.

## Safety

The detailed ON/OFF and E-Stop architecture is in:

`Designs/Schematics/SentinelT_Power_and_EStop.md`

The E-Stop is treated as a hardware safety function, not merely a software command.
