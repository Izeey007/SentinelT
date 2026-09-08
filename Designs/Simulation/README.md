# Simulation & Digital Verification

SentinelT uses Blender plus Python-based digital verification before physical fabrication.

## Footprint Audit

The CAD audit:

1. iterates through frames 1-180;
2. evaluates visible mesh world-space bounding boxes;
3. calculates overall X/Y/Z extents;
4. compares X and Y against the 500 mm x 500 mm footprint limit;
5. records failed frames and maximum dimensions.

### Final Result

- Maximum X: **318.16 mm**
- Maximum Y: **495.00 mm**
- Maximum Z: **255.41 mm**
- Frames checked: **180**
- Failed frames: **0**
- Result: **PASS**

Earlier design iterations failed the footprint audit. A diagnostic script identified geometry creating the excessive extent, after which the design was repackaged and re-audited.

## Mass Analysis

A Blender mass audit found that the CAD meshes did not contain verified physical mass metadata. Rather than claiming an invalid zero mass, the project records an explicit subsystem engineering budget of **4.650 kg** with **0.350 kg design margin**.

The physical robot must still be weighed on a calibrated scale.

## Files

- `SentinelT_Footprint_Audit.py` - repeatable Blender footprint audit.
- `SentinelT_Mass_Budget.py` - engineering mass-allocation report.

This digital-testing evidence supports the elimination-round simulation/technical-excellence section, while not replacing required physical verification.
