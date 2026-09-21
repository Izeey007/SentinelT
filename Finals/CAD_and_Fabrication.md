# CAD and fabrication control

Keep the elimination Blender file unchanged until actual hardware dimensions and scope are confirmed. Work on a revision copy under the finals branch; record the original and new hashes. Do not stretch the existing model merely to make supplier parts appear to fit.

| Decision | Required information | Status |
|---|---|---|
| Wheel fit | 125 mm supplier diameter, width, hub/shaft fit, motion envelope versus nominal CAD wheel | Open |
| Motor mounts | Exact motor drawing, screw lengths/pattern, bracket material and measured mass | Open |
| Chassis panels | Material grade, 6 mm thickness, nesting, panel dimensions, holes and fastening stack-up | Open |
| Metal parts | Grade, thickness, cut lengths and lab availability; raw stock not assumed owned | Open |
| Shaft retention | Reconcile 5 mm cutter/bearing dimensions with 6 mm collars in submitted BOM | Open |
| Mechanisms | Load-rated support, actuator fit, travel limits, guarding and organizer approval | Open |
| Electronics bay | Actual dimensions, service access, battery restraint, insulated terminals and harness routing | Open |
| Isolation access | Main switch/E-stop mounting and operation without hazardous reach | Open |

For each fabricated part issue a drawing ID/revision, material, thickness, quantity, dimensions, holes, tolerances, fasteners and installed mass estimate. Ask the lab to review before cutting. Buy stock quantities based on the approved nesting/cut list, not the robot's silhouette.

Change record: date; reason; baseline part; new part; cost/mass effect; drawing/model hash; digital recheck; affected physical tests; approval if organizer required. No new fabrication geometry has been released in this setup.
