# Picard-inspired Ressikan flute | v3 acoustic test kit

This is an **experimental, 3D-printable duct-flute design**, not a verified working musical instrument. The original screen-used prop was decorative. The earlier v2 print was silent and had loose joints. V3 reduces the number of joints, uses ribbed joints, and provides multiple integrated windway/labium geometries for testing.

## What to print FIRST

- **STL/00_NO_JOINT_SOUND_TEST_A_BALANCED.stl** - no-assembly test of the windway and blade.
- If A is silent: **STL/01_NO_JOINT_SOUND_TEST_B_EASY_START.stl** - wider/taller alternative.
- **STL/30_FIT_GAUGE_MALE.stl** and **STL/31_FIT_GAUGE_FEMALE.stl** to check joint fit before printing the full instrument.

## For the complete flute

1. **STL/01_FLUTE_BODY_ONE_PIECE.stl** - main body with six finger holes, 210 mm barrel plus tenon.
2. Choose ONE head: **STL/10_MOUTHPIECE_A_BALANCED.stl** through **STL/14_MOUTHPIECE_E_WIDE_WINDOW.stl** - removable 50 mm heads.
3. Total assembled length is about 249 mm after joint overlap.

The **20_SHORT_TEST_RESONATOR.stl** is a short hole-free tube for mouthpiece trials before committing to the full body.

## Acoustically varied heads

| Head | Windway height (mm) | Jet-to-labium distance (mm) | Tip offset (mm) |
| --- | ---: | ---: | ---: |
| A Balanced | 1.00 | 4.10 | 0.00 |
| B Easy Start | 1.20 | 4.50 | +0.12 |
| C Narrow Jet | 0.78 | 3.70 | -0.10 |
| D Short Window | 1.08 | 3.25 | 0.00 |
| E Wide Window | 1.00 | 4.85 | +0.06 |

## Suggested print / debugging

- Print test A before any body. Do not obstruct the air passage or sound window with supports.
- Start at 0.12 mm layer height and 0.4 mm nozzle. Inspect the thin blade edge under good light. Remove stringing carefully.
- A blocked windway, rounded labium, or incorrectly formed slot can cause silence. If a note only appears when a finger covers the foot, inspect air jet alignment.
- Fit the test coupons before the body. Printer dimensional error, filament shrinkage, and wall seams affect rib fit.
- Printed plastic may require cleaning before blowing into it. Do not inhale loose plastic particles.
- There is NO CLAIM of tested pitch, stable tuning, or guaranteed sound. Real playing trials are required.

## Source and build

CAD/build_flute.py generates STL files from CadQuery solids, checks watertightness using Trimesh, and writes them to STL/. A GitHub Actions workflow builds the files and commits them.

To build locally:

    python -m pip install cadquery trimesh
    python Picard-Flute-v3/CAD/build_flute.py

Units: millimeters. This is an independent fan-inspired object, not an official Star Trek product.
