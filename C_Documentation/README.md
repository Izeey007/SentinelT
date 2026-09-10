# Folder C - Documentation

**Project Developer:** TG Assegaai  
**Build:** SentinelT

## Purpose

This folder contains the formal SentinelT submission documents: the pitch deck, Bill of Materials, holistic build report, completeness checklist and Facilitator Q&A attendance record.

## 1. Pitch Deck

Location: `Pitch_Deck/SentinelT_Pitch_Deck.pdf`

The pitch deck is limited to seven pages and covers SentinelT, Robo Wars design constraints, solution/buildability, CAD/simulation evidence, electronic control and safety, implementation cost, and Project Developer responsibilities.

## 2. Bill of Materials / Funding Procurement List

Location: `BOM/SentinelT_Bill_of_Materials.xlsx`

Supporting readable procurement files are also stored in `BOM/` so the funding list can be inspected directly from GitHub.

The revised procurement plan covers the complete intended hardware set rather than only the earlier partial component list. It includes:

- raw 6 mm HDPE and mild-steel fabrication stock;
- four 12 V drive gearmotors and four wheels;
- independent left/right Cytron MDD20A drive control;
- 3S robot battery and power wiring;
- RadioMaster Boxer 2.4 GHz transmitter, receiver and transmitter battery;
- embedded controller/interface hardware;
- cutter motor and controller candidate;
- two hammer actuators plus torso-rotation actuator;
- servo interface and control wiring;
- main ON/OFF isolator;
- normally-closed E-Stop control switch;
- separate high-current actuator-isolation relay/contactor candidate;
- fuse protection, XT60 connectors and insulation;
- fastening, telemetry/status and battery-restraint hardware;
- LiPo charging equipment.

The current revised funding total is **R15,985.04**. Supplier prices were checked during September 2026 and must be reconfirmed when purchasing because stock and pricing can change. Every funded hardware line identifies a supplier/model or stock code and a buying/source link in the procurement list.

The procurement plan corrects the earlier drivetrain mismatch: SentinelT now budgets **four 12 V 160 RPM 37 mm motors**, with two motors per side controlled by the independent channels of a **Cytron MDD20A**. The previous linked-output WP-880 concept is not used as the final differential-drive funding architecture.

## 3. Holistic Build Document

Location: `Holistic_Build_Document/SentinelT_Holistic_Build_Document.pdf`

The A4 report ties SentinelT together as a single technical build and covers the Robo Wars constraints, solution overview, mechanical design, electronics, E-Stop integration, programming framework, simulation, mass planning and BOM summary.

A fresh footprint audit of the current submitted Blender model records approximately **316.10 mm x 466.11 mm x 405.99 mm**, with **204 engineering mesh objects**, Frames **0-180**, and **0 failed footprint frames** against the 500 mm x 500 mm limit.

## 4. Project Completeness Checklist

Location: `PROJECT_COMPLETENESS_CHECKLIST.md`

The checklist separates completed digital evidence from tests that require the fabricated robot. Hardware-stage items remain explicitly scheduled for implementation and testing rather than being represented as already measured.

## 5. FQ&A Attendance

`FQA_Attendance_Log.md` records that no Facilitator Q&A session was attended. No FQ&A bonus or attendance screenshot is claimed.

## Physical Hardware Implementation Statement

The physical SentinelT build will follow the same CAD packaging, 2.4 GHz RC architecture, power isolation, E-Stop arrangement and mechanism intent documented in this repository. Physical verification will be completed during hardware implementation, including:

- calibrated robot mass measurement, with the completed robot kept **strictly below 5 kg**;
- final overall footprint within **500 mm x 500 mm**;
- main ON/OFF accessibility and isolation;
- E-Stop actuator-power interruption;
- receiver binding, channel mapping and failsafe behavior;
- drivetrain direction, current and thermal behavior;
- final fuse, relay/contactor, connector and wire ratings;
- battery restraint, insulation and runtime;
- mechanism clearance, guard and fastener inspection.

If a physical measurement differs from a digital assumption, the hardware will be adjusted before operation until the applicable Robo Wars constraints are met.
