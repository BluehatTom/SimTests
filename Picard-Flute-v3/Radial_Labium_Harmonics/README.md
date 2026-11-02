# Circular multi-labium harmonics — Picard flute v3

**Replacement MOUTHPIECES ONLY.** Fits the v3 flute's existing ribbed joint, including the seven-hole, thumb-hole, and chromatic bodies. Use the **original working v3 mouthpiece** as your acoustic reference.

## What is a "reed" on this flute?

The sound-producing parts are stationary **labia** (singular: labium), or whistle edges — NOT vibrating clarinet/oboe reeds. These heads each have a circular breathing opening at the top, a shared air-distribution chamber, multiple narrow windways located around the **inside circumference**, and individual labium windows cut at different angles around the outer barrel. All the labia feed the SAME resonating flute bore. Additional edges may change harmonic balance, note attack, breath pressure requirements or turbulence, but they **do not guarantee additional pitches**.

## Five interchangeable STL experiments

| STL | Jets / sounding edges | Intended comparison |
|---|---:|---|
| **01_RADIAL_2_OPPOSED.stl** | 2 opposite | Safest first trial of circumferential jets; relatively high airflow per opening |
| **02_RADIAL_3_STAGGERED.stl** | 3 at 120° | Asymmetric slot widths and edge distances for changed timbre |
| **03_RADIAL_4_ALTERNATING.stl** | 4 at 90° | Two pairs of alternate blade lengths / jet thicknesses |
| **04_RADIAL_6_MICRO.stl** | 6 at 60° | Maximum circumferential edge count; high risk of weak response from shared pressure |
| **05_RADIAL_3_PRIMARY_PLUS_SATELLITES.stl** | 1 dominant + 2 small | **Best first harmonic experiment:** main large jet surrounded by two smaller auxiliary jets |

**Recommended print sequence:** 05 → 01 → 02 → 03 → 04. If 05 is silent, compare 01 before deciding the multi-jet geometry does not work with your flute.

## Important printing changes

**Unlike your working v3 flat-back mouthpiece, these have whistle windows on several sides. Print them UPRIGHT on the wide, flat socket end.** Do not print them on the side — that can bury or distort one of the labium windows.

- All five models are **52 mm long** and have the **original 6.84 mm-radius v3 female socket** and 16.4 mm outside diameter.
- Suggested starting settings: PLA or PETG; **0.10-0.12 mm layers**, **0.4 mm nozzle**, 0.30-0.36 mm variable line width if your slicer supports it (Arachne-type thin walls), 3 walls, slow external perimeters and good cooling for PLA. A 0.2 mm nozzle may preserve the small blades better.
- An **8+ mm brim** helps prevent the narrow annular base from tipping.
- The central bore ends near the labium. Check slicer preview for the **~11 mm internal bridge/roof**. Use tuned bridging speed, fan and flow. Clean drooping strands via the 11 mm bore if necessary, without scratching the labia.
- **Never put supports inside the windways or the circular top air inlet.** Do not cut/sand the blade edge unless correcting obvious print artifacts.
- Blow through the large central circular opening, not directly into any of the narrow outside windows.
- Fit with the same v3 joint as your working mouthpiece; do not glue experimental heads until you know they work.

## How to make the test meaningful

1. With **all finger holes covered**, record your current working mouthpiece's note on a smartphone at a fixed microphone distance.
2. Swap to head **05**, then **01**. Start blowing gently. Gradually increase, noting whether it speaks, turns breathy, or jumps an octave.
3. Repeat at two other fixed fingerings. Record at comparable loudness and note frequency.
4. Use a basic audio spectrum app to estimate the **2nd, 3rd and 4th harmonic levels relative to the fundamental** at the SAME note, pressure and recording level. Do not compare raw loudness alone.
5. Try TEMPORARILY taping over one outside sound window (without inserting anything into the mouthpiece) to isolate interfering jets. Remove the tape before cleaning or storing the flute.
6. If your six-edge head hisses or refuses to start, that is a test result: feeding several jets from the same chamber reduces pressure available to each, and their oscillations may compete.

### Why this is experimental

A 11 mm-diameter bore at normal flute frequencies primarily supports an axial pressure wave. The multiple jets therefore usually lock to a shared fundamental (when they lock at all). Asymmetric blades may strengthen different partials, but **cannot be counted on to produce chords, independently tuned notes or specific harmonics**. The shape is informed by flue-instrument physics and the working v3 geometry, not by physical sound measurements of this new design.

**Acoustics references:** Dequand et al. (2003), *JASA* 113(3):1724-35, doi:10.1121/1.1543929; 2024 experimental organ-pipe airflow imaging: https://pmc.ncbi.nlm.nih.gov/articles/PMC10974865/ .

### Engineering checks

The build workflow validates that each mesh is watertight, manifold, one solid, and nonzero volume; that lower socket point samples match v3 exactly; that every modeled air channel and window is open; and that the central mouth inlet is separated from the bore by a solid baffle. See QA/mesh_validation.json for each version's nozzle geometry.

All of that is geometric validation, **not a guarantee of a sound-producing print**.

This fan-made instrument part is not an official Star Trek product.
