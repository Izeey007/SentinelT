# Physical commissioning record

**All tests: NOT RUN.** Fill actual results only after completing the test. Planned behavior is not a result. Use lab-approved conditions, keep mechanisms isolated for early tests and stop on unexpected motion, overheating, wiring damage or failed isolation.

For each test record: date/time; operator and lab witness if present; hardware and firmware revision; battery; radio model/configuration; instruments; setup/photo; measured result; pass/fail; defect; correction; retest reference. Agree measurable acceptance criteria with the lab and final rules before the test.

| ID | Check | Required behavior/evidence | Actual result |
|---|---|---|---|
| T01 | Unpowered inspection | Correct polarity, insulation, secure fasteners/guards, battery restraint and accessible switches | NOT RUN |
| T02 | Main isolation | OFF removes intended power; no USB/signal/auxiliary backfeed | NOT RUN |
| T03 | E-stop | Independently opens actuator power; record interruption and coast-down separately | NOT RUN |
| T04 | Restart interlock | Releasing E-stop, reconnecting power or rebooting does not automatically move actuators | NOT RUN |
| T05 | Startup with non-neutral controls | Outputs remain disabled until deliberate valid arming and required neutral conditions | NOT RUN |
| T06 | Radio off / loss of link | Drive and auxiliary commands go safe within agreed measured limit; recovery does not auto-arm | NOT RUN |
| T07 | Receiver unplug / stale or malformed data | Firmware rejects missing/stale/invalid commands | NOT RUN |
| T08 | MCU reset / watchdog | Outputs default safe; deliberate re-arm required | NOT RUN |
| T09 | Drive direction / neutral | Correct left/right response, stops at neutral; no unexpected mixed-channel behavior | NOT RUN |
| T10 | Control power under load | No unexplained reset or unsafe command during approved load changes | NOT RUN |
| T11 | Current / temperature / runtime | Stay inside validated ratings for required operating duration | NOT RUN |
| T12 | Mechanism and guard inspection | Lab-reviewed retention, support, locks and clearances before any authorized powered test | NOT RUN |
| T13 | Complete physical mass | Strictly below 5 kg in organizer-required configuration; record scale and uncertainty | NOT RUN |
| T14 | Physical footprint | Within 500 x 500 mm in required poses; record method and uncertainty | NOT RUN |
| T15 | Final regression | Repeat affected checks after last hardware, radio or firmware change | NOT RUN |

## Individual test entry template

- Test ID / date:
- Operator / witness:
- Hardware / firmware / radio revision:
- Acceptance criteria and source:
- Setup and instruments:
- Measurements and evidence files:
- Result: NOT RUN / PASS / FAIL
- Defect and correction:
- Retest reference:
