# Electronic Design

SentinelT's electronics are organised around safe human-operated **2.4 GHz RC control**, a 3S battery architecture and separated power/control paths.

## Functional Blocks

- 11.1 V 3S battery pack;
- branch fuse/protection;
- accessible main ON/OFF isolation;
- E-Stop pushbutton and high-current power-disable relay/contactor;
- power distribution;
- 2.4 GHz RC receiver;
- controller/interface logic;
- dual brushed drive ESC;
- two 12 V geared drive motors;
- auxiliary controller for the guarded active mechanism.

## Current Component Plan

The Bill of Materials currently identifies:

- FlySky FS-i6X transmitter + X6B receiver (2.4 GHz);
- HobbyWing QuicRun WP 880 dual brushed ESC;
- 2 x Pololu 4743 50:1 12 V 200 RPM 37D metal gearmotors;
- BEAT 5000 mAh 11.1 V 3S LiPo with XT60;
- 30 A branch fuse and fuse holder candidates;
- 12 V 100 A main battery isolator candidate;
- emergency pushbutton candidate;
- separate 12 V 80 A high-current relay/contactor candidate;
- 100 A 4-way power-distribution terminal block;
- 10 mm2 red/black silicone high-current wiring;
- XT60 power connector set.

The guarded active-mechanism motor/controller remains the final unresolved BOM subsystem. All selected ratings will be verified as a matched electrical system before physical operation.

## Safety

The detailed ON/OFF and E-Stop architecture is documented in:

`Designs/Schematics/SentinelT_Power_and_EStop.md`

The E-Stop is treated as a hardware safety function, not merely a software command.
