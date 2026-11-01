# Picard flute v3 — interchangeable mouthpiece experiments

**All parts in this folder are MOUTHPIECES ONLY.** Use your existing v3 flute body. Keep the original working v3 head as a reference. The original v3 socket dimensions are unchanged in every experiment.

These are **acoustic prototypes**, not physically sound-verified. The goal is to find a wider breath-pressure range, different timbres, and interesting overblowing effects. The twin designs use **two air jets**, not vibrating reeds. They may reinforce or interfere with one another; harmonics and two-note effects are not guaranteed.

## Print order

1. **01_STABLE_LONG_WINDWAY.stl** — first choice for improving a sensitive/finicky response. 20-mm windway, 0.18-mm exit chamfers, slightly more substantial blade edge.
2. **02_WARM_GENTLE.stl** — smaller 0.87-mm windway, longer window; trial for soft/rounded playing.
3. **03_BRIGHT_HARMONICS.stl** — shorter windway and narrower jet height; aims at brighter partials. Might overblow more easily.
4. **04_BREATHY_OPEN.stl** — taller duct (1.35 mm); trial for a breathier, open sound.
5. **05_EASY_OVERTONE.stl** — short window and narrow duct; tries to encourage high-register/overblow response.

## Dual-air-jet experiments

6. **06_TWIN_JET_SINGLE_EDGE.stl** — one mouth opening splits into **two separate windways**; the jets strike **one common labium** and common sound window. Simplest experiment for split-jet tone.
7. **07_TWIN_JET_DOUBLE_LABIUM.stl** — one mouth opening splits into two side-by-side windways, with **two separate windows and two sharp labium edges**. Those edges have slightly different distances from their jets (about 3.97 and 4.33 mm). Both feed the same flute bore. This is closest to the requested “double reeds,” but is technically a **double-labium flue head**, not a double-reed instrument. Expect possible sensitivity, competing oscillation, chuffing, or no additional harmonics.

## Longer heads for genuinely lower notes

8. **08_LOWER_PITCH_12MM.stl** — based on successful v3 geometry, with 12 mm more airway length from socket to sound window.
9. **09_LOWER_PITCH_24MM.stl** — same with 24 mm extra length.

The longer heads should lower the pitch to some degree, although the change will depend on open finger holes, effective acoustic length and breath pressure. Mouthpiece shape mostly affects *timbre and response*, not the tuning of the entire flute.

## Print setup

- These STLs are oriented **flat on their backs**, with the sound window facing UP, as in the working v3.
- Begin with **0.12-mm layer height**, a clean **0.4-mm nozzle**, and a smooth bed-facing rear surface. Avoid supports or infill in the air path. Check slicer previews for gaps/unsupported slot ceilings.
- Inspect the small windway slit under bright light. Clean any plastic hairs/stringing. Avoid damaging the thin sounding edge.
- A very small dimensional shift (0.1–0.2 mm) at a duct or edge can be significant. Use the **same printer, filament, slicer, and settings** as the version that worked.
- These heads use the **same original v3 female socket**. Do not force the fit; remove a tiny amount of seam flash if necessary.

## How to test objectively

Keep the same flute body, fingers, room and blowing distance. Record 5–10 seconds of each sound on the same phone position. For each head, record:
- Can a clean note start with gentle blowing?
- What is the range of breath pressure before the tone cracks or jumps an octave?
- Does it play more softly or brightly?
- Does it sound on all six holes closed? With the first upper hole opened?
- Does the twin head produce a stable sound or competing tones?

A phone tuner can measure pitch, and a spectrum/spectrogram app can help compare harmonic energy. Play at comparable loudness before judging harmonic richness.

## Acoustic rationale / further reading

The jet alternately feeds and draws air from the resonator. The bore length and open finger holes largely determine pitch. Windway length, jet thickness, chamfers and edge geometry determine how reliably the air jet locks to the resonator and how much overtone content is excited.

- Segoufin et al. (2000), experimental windway length and chamfers: https://research.tue.nl/en/publications/experimental-study-of-the-influence-of-the-mouth-geometry-on-soun/
- Dequand et al. (2003), mouth geometry and sound generation: https://pubmed.ncbi.nlm.nih.gov/12656404/
- Recorder maker Philippe Bolton, windway geometry: https://www.flute-a-bec.com/gros-plan-chanfreinsgb.html

**Files / reproducibility:** The source is in CAD/build_alt_heads_compact.py. GitHub Actions generates these checked binary STL models and QA/alternative_heads.json. All meshes are tested to be watertight and single-component with an open mouth-to-window air path. Actual acoustic performance still requires printing and listening.

Not an official Star Trek product.
