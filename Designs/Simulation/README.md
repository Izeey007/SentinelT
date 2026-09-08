# Simulation and Digital Verification

I use Blender and Python-based verification to test SentinelT before physical fabrication.

## Footprint Audit

The CAD audit:

1. iterates through frames 1-180;
2. evaluates visible mesh world-space bounding boxes;
3. calculates overall X/Y/Z extents;
4. compares X and Y with the 500 mm x 500 mm Robo Wars footprint;
5. records failed frames and maximum dimensions.

### Verified Result

- Maximum X: **318.16 mm**
- Maximum Y: **495.00 mm**
- Maximum Z: **255.41 mm**
- Frames checked: **180**
- Failed frames: **0**
- Result: **PASS**

Earlier design iterations exceeded the footprint. I used diagnostic scripts to identify the geometry causing the excessive extent, repackaged the design and repeated the audit until all checked frames passed.

## Mass Analysis

The CAD meshes do not contain verified physical mass metadata. Instead of claiming a false simulated mass, SentinelT uses an explicit engineering subsystem budget of **4.650 kg**, leaving a **0.350 kg** design margin below 5.000 kg.

The completed physical robot will be weighed on a calibrated scale.

## Files

- `SentinelT_Footprint_Audit.py` - repeatable Blender footprint audit.
- `SentinelT_Mass_Budget.py` - engineering mass-allocation report.

This folder documents SentinelT's pre-fabrication digital testing and repeatable engineering checks.
