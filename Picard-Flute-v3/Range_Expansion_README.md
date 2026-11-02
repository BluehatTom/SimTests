# Extra playable notes — Picard flute v3

Keep your **working v3 mouthpiece**. This expansion is a set of replacement BODIES and optional lower-end extensions. They all retain the original v3 ribbed top joint (11 mm bore, 16.4 mm nominal outside diameter). Do not mix with v2.

## What to print

| File | Role | Print this when… |
|---|---|---|
| 01_7HOLE_SIMPLE_NO_THUMB.stl | One extra front hole, no thumb hole | You want the lowest-risk first test |
| **02_7HOLE_THUMB_3MM.stl** | **Seven front holes + 3 mm thumb register vent** | **You want a wider musical range; print this first** |
| 03_7HOLE_THUMB_SMALL_2_2MM.stl | Smaller 2.2 mm thumb hole | The regular vent weakens low notes or is too strong |
| **04_CHROMATIC_SPLIT_LOW_7HOLE_THUMB_3MM.stl** | **Same layout, but two pairs of split low finger holes** | **You want G and A half steps without delicate half-holing** |
| 05_FOOT_EXTENSION_25MM.stl | Slip-on lower extension, +25 mm nominal | Try a lower all-closed note |
| 05_FOOT_EXTENSION_45MM.stl | Slip-on lower extension, +45 mm nominal | Try an even lower all-closed note |

**You only need one body and the mouthpiece you already own.** The foot extensions are optional; neither replaces the body.

### Geometry and fingers

Front hole numbering goes **from the mouthpiece to the foot**. Hole 1 is nearest your face; hole 7 is nearest the lower end. Use the **left hand for 1–3 and the right hand for 4–7**, as on a recorder. The **rear thumb vent** is behind the upper end of the body.

The original v3 flute body had six holes and no thumb vent. The new model has seven holes at the following heights above the foot (mm), from lowest to highest:

- **#7** 36 mm / 6.2 mm bore (or split into 5.67 mm + 2.5 mm)
- **#6** 55 mm / 6.3 mm bore (or split into 5.54 mm + 3.0 mm)
- **#5** 70 mm / 5.2 mm bore
- **#4** 86 mm / 5.8 mm bore
- **#3** 103 mm / 5.8 mm bore
- **#2** 117 mm / 6.0 mm bore
- **#1** 132 mm / 3.0 mm bore
- **Thumb vent**, on back: 163 mm above foot, diameter 3.0 mm or 2.2 mm

The very small uppermost front hole is intentional: it limits an overly sharp high note in our simplified model. Whether it vents strongly enough for a reliable tone must be established on a print.

## Printing

- **Bodies:** Print upright on the flat open foot, 0.12–0.16 mm layers; use a sturdy brim. Height approximately **221 mm including the original tenon**. A 245-mm Z printer can accommodate this.
- **Extensions:** Print upright, with a brim. The sleeve has 15 mm insertion depth and shallow grip ribs. Fit must be checked with your filament; lightly sand the grip ribs if too tight. For airtightness, a thin removable tape wrap on the flute foot is preferable to glue.
- No supports INSIDE the central bore, thumb vent, or finger holes. Remove all stringing before blowing.
- Print the new body in the SAME settings, material, and orientation as the version that succeeded.
- Check front-hole and thumb-hole sealing. A tiny leak from an uncovered thumbhole can spoil low notes, so cover it fully with the soft pad of your thumb for first-register tests. If needed, temporarily tape it over during diagnosis.
- Do not use small loose plugs inside a wind instrument.

## First register — STARTER fingering chart

**Prototype only.** These are the first register's *theoretical* approximate pitches from a simplified 1D acoustic model, **not measured pitches**. We cannot promise any pitch label until you play each note with a tuner.

- **X** = fully covered, **O** = open.
- **s** = on the split-hole body, leave ONLY the small member of that pair open (cover its large neighbor). On the normal body, experiment with approximately half-covering that hole.
- Patterns list holes **1–7**, mouth-to-foot. Keep **rear thumb fully covered** for the basic scale.

| Intended note | Front 1–7 | Model, Hz | Technique |
|---|---|---:|---|
| F#5 | XXXXXXX | 745 | all covered |
| G5 | XXXXXXs | ~784 | small half-step hole 7 |
| G#5 | XXXXXXO | 833 | open both holes of 7 |
| A5 | XXXXXsO | ~879 | small half-step hole 6 |
| A#5 | XXXXXOO | 922 | open holes 6 and 7 |
| B5 | XXXXOOO | 997 | normal |
| C6 | XXXOXXO | ~1060 | cross-fingering experiment |
| C#6 | XXXOOOO | 1103 | normal |
| D6 | XXOXXOX | ~1176 | cross-fingering experiment |
| D#6 | XXOOOOO | 1236 | normal |
| E6 | XOXXOOO | ~1308 | cross-fingering experiment |
| F6 | XOOOOOO | 1385 | normal |
| F#6 | OOOOOOO | 1478 | normal |

The actual pitch may differ by a semitone or more, especially for cross-fingerings, depending on mouthpiece voicing, printed diameters, leaks, the shape of split holes, and blowing pressure.

### Additional upper notes — thumb register test

Once you have a stable low register, **crack the thumb vent partially open** while keeping most holes covered and increase air pressure slightly. A recorder's thumbhole is a *register vent*: it can suppress the fundamental and help the flute select a higher resonance. Full thumb uncovering is usually NOT the same as cracking it open.

Try the original seven patterns in sequence with a barely opened thumb vent, log any pitch with a tuner, and reject fingerings that only hiss or squeal. **No upper-register range is guaranteed**, especially because this is not yet a professionally voiced recorder.

## Why these holes differ

The **first open tone hole** controls the effective acoustic length of the air column, but because its air has inertia and its opening is finite, the effective end does NOT stop exactly at the center of that hole. Closing holes below the first open hole changes pitch further, giving "cross-fingered" semitones.

The six-hole working version modeled close to F#5–F#6. This seven-hole pattern was designed for an approximate eight-step major scale plus two extra split-hole half steps and some cross-fingered semitones. **This is a theoretical design target, not a tuning guarantee.**

References:
- [Acoustics Today — A Close Look at Flutes](https://acousticstoday.org/issues/2018AT/Spring2018/files/basic-html/page56.html) — tone-hole inertance, cross-fingerings, and register venting.
- [Woodwind Fingering Guide — Recorder](https://www.wfg.woodwind.org/recorder/rec_fing.html) — thumbhole partial coverage.
- [Euphonics — The end correction of a single tone-hole](https://euphonics.org/11-1-3-the-end-correction-of-a-single-tone-hole/) — why hole size affects effective length.

## Practical tuning workflow

1. Record your **known working six-hole flute** with a phone tuner (all closed, then open one hole at a time).
2. Put on your old working mouthpiece and print **02_7HOLE_THUMB_3MM**.
3. Record each fingering from the table, with steady blowing and thumb completely covered.
4. Try a slightly opened thumbhole and log which upper notes settle cleanly. If none, try **03**, the smaller vent.
5. Print **04** if you want reliable G/A semitones from paired holes rather than half-covering a single circle.
6. Save recordings and actual pitches. If an individual note is too flat, enlarging its relevant hole very gradually may sharpen it. If a note is too sharp, use reversible tape first rather than drilling. The hole changes interact.
7. Only after finding a reliable baseline try the 25/45 mm foot extensions for lower tones.

*This is an independent fan-inspired instrument, not an official Star Trek product.*
