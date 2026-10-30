# Troubleshooting

**Outcome:** the failure modes the lab
actually met, in the order a new user
is likely to meet them, each with
the fix that worked or the honest
statement that none did.

**Check:** every error below appears
in `orcaslicer-lab/transcripts/t06-failures.txt`
or `t05-multicolor-attempts.txt`,
in the words the program printed.

## "Add G92 E0 to layer_gcode" — error −51

The slice refuses outright:

```text
Failed to load G-code data!
Relative extruder addressing requires resetting
the extruder position at each layer to prevent
loss of floating point accuracy.
Add "G92 E0" to layer_gcode.
(error -51)
```

The lab met this with two bundled
machine families (a Creality Ender-3 V2
trio and the Prusa XL trio) loaded as
raw files on the command line.
The cause, shown by `--export-settings`:
loaded raw, the preset's inherited
values are only partly resolved —
the layer-change script that the
*base* preset contributes arrives
empty, while relative-E stays on,
and the slicer's own safety check
(correctly) refuses the combination.

**Fix that worked:** copy the *process*
preset, give it a new `name`, drop its
`setting_id`, and add the missing key:

```json
"layer_change_gcode": "G92 E0"
```

Load the copy instead of the bundled
process file. The XL then sliced clean.
(The lab's copy is kept at
`orcaslicer-lab/xl-process-g92.json`.)
In the window this does not bite:
profiles resolve there fully.
Whether a future release fixes raw
loading is the project's business;
until then, copy-and-patch is the
working route — and *not* a licence
to ignore the warning on profiles
you write yourself, where the check
is protecting real accuracy.

## Error −3: a file that is not there

```text
can not find setting file Generic PLA @MK3S.json
return -3
No such file: models/nope.stl
return -3
```

Both directions — a preset path and
a model path — fail with the same
code and, helpfully, name the file.
Preset names change between releases
(the lab reached for a preset name
from an older version); list the
vendor folder and copy the name
exactly, spaces and `@` included,
and quote the path.

## Error −102: "unprintable area"

```text
"Found G-code in unprintable area of
multi-extruder printers after slicing."
```

The lab's two bars sat at the plate's
corner, where they fit — but their
skirt did not: it reached X = −2.2 mm,
off the plate. On multi-tool machines
the slicer rejects toolpaths outside
the printable area instead of
silently clipping. Moving the models
toward the plate centre — the window
does this when it places objects —
sliced with `return_code: 0`.
Lesson: place for the *whole*
toolpath, skirt and prime tower
included, not just the model.

## The multicolor slice that is not

The slice succeeds, the summary looks
plausible — and the part is one colour.
Detect it with chapter 6's habit:

```text
; filament: 1
```

in the header, one entry in the
per-filament totals, and no
tool-select or changer commands
in the file. On the command line in
2.4.2 this is the known limit
documented in chapter 8: assignment
belongs to the window. In the window,
the same symptom means the assignment
never took — re-check it in the
object list, and trust the coloured
preview over the dropdowns.

## "total filament used [g] = 0.00"

Not a broken scale: the filament
preset carries `"filament_density": 0`,
and grams are computed as volume
times density. Length and volume
in the same footer are still valid.
Set a real density in your copy
of the preset (about 1.24 for PLA)
if you want weights.

## The AppImage will not start

It names a missing host library
(OpenGL and friends). Install what
it names, or extract the AppImage
with `--appimage-extract` and run
the binary from the tree — the lab
did both the extraction and a
library workaround, recorded in
`t00-install.txt`. On machines with
a normal desktop this rarely appears;
on minimal and headless machines
it is the first thing you will meet.
