# Folder C - Documentation

**Project Developer:** TG Assegaai  
**Build:** SentinelT

## Purpose

This folder contains the formal SentinelT submission documents: the pitch deck, Bill of Materials, holistic build report, completeness checklist and Facilitator Q&A attendance record.

## 1. Pitch Deck

Location: `Pitch_Deck/SentinelT_Pitch_Deck.pdf`

The pitch deck is limited to 7 pages and covers:

- SentinelT introduction and Robo Wars constraints;
- solution and buildability;
- mechanical CAD and simulation evidence;
- electronic control, main ON/OFF and E-Stop safety;
- engineering mass allocation and current component cost;
- Project Developer responsibilities and signature.

## 2. Bill of Materials

Location: `BOM/SentinelT_Bill_of_Materials.xlsx`

The spreadsheet contains the required purchasing fields:

- Component Name;
- Quantity;
- Cost per Unit;
- Supplier;
- Supplier Stock Code;
- Direct URL;
- line and total cost information.

The current priced component subtotal is **R8,039.15**. Hardware-dependent procurement lines that are not yet physically locked are identified as such rather than represented as completed purchases.

## 3. Holistic Build Document

Location: `Holistic_Build_Document/SentinelT_Holistic_Build_Document.pdf`

This A4 portrait report ties SentinelT together as one technical build. Its title header identifies **SentinelT** and **Project Developer: TG Assegaai**, and the report ends with **Signature: Thato Glen Assegaai**.

The report includes:

1. Context and Robo Wars design constraints.
2. Solution overview describing what SentinelT is and how it is being built.
3. Mechanical design and fabrication approach.
4. Internal packaging/buildability evidence.
5. Electronic design and component choices.
6. Wiring and mandatory E-Stop integration.
7. Programming language, framework and operating logic.
8. Simulation and footprint verification.
9. Engineering mass budget.
10. BOM summary.
11. Current implementation status and physical-verification plan.

Recorded digital result: **318.16 mm x 495.00 mm x 405.99 mm**, **204 physical meshes**, **180/180 frames PASS**, **0 failed frames** for the documented audit baseline.

## 4. Project Completeness Checklist

Location: `PROJECT_COMPLETENESS_CHECKLIST.md`

The checklist maps the submission against the scoring areas and clearly separates completed digital evidence from tests that require the fabricated robot. Unchecked hardware items are marked for verification after hardware implementation.

## 5. FQ&A Attendance

`FQA_Attendance_Log.md` records that no Facilitator Q&A session was attended. Therefore:

- no FQ&A attendance bonus is claimed;
- no attendance screenshot is fabricated;
- `FQA_Proof/` is intentionally reserved without attendance images.

## Physical Verification Status

The formal documentation distinguishes digital results from hardware results. The following remain physically unverified and will be checked after hardware implementation:

- measured robot mass;
- measured current draw;
- battery runtime;
- drivetrain performance;
- thermal behavior;
- final receiver/ESC calibration;
- final cable routing and strain relief;
- physical E-Stop interruption performance.
