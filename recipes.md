# Recipes

**Outcome:** working patterns for the
jobs that recur, built from the
commands and checks the lab verified.

**Check:** each recipe names the
transcript or chapter that backs it.

## Slice a model without opening the window

The chapter 5 command, as a pattern:

```console
$ orca-slicer \
    --load-settings "MACHINE.json;PROCESS.json" \
    --load-filaments "FILAMENT.json" \
    --outputdir OUTDIR \
    --slice 0 \
    MODEL.stl
```

Use a matched trio from one vendor
folder (chapter 4). Read the verdict
in `OUTDIR/result.json`
(`t02-first-slice.txt`).

## Slice a folder of models, unattended

Loop the pattern and keep the verdicts:

```console
$ for f in models/*.stl; do
    orca-slicer --load-settings "MACHINE.json;PROCESS.json" \
        --load-filaments "FILAMENT.json" \
        --outputdir "out-$(basename "$f" .stl)" \
        --slice 0 "$f"
  done
$ grep -H error_string out-*/result.json
```

The grep at the end is the recipe's
point: one line per model,
`Success.` or the error, no console
archaeology. The lab's failures
(chapter 13) all announced themselves
this way — including error −51,
which prints its real reason to the
console but is easiest to catch
in bulk from `result.json`.

## Prove a file before it travels

```console
$ python3 orcaslicer-lab/check_gcode.py plate_1.gcode
```

Header, layer counts two ways,
net and gross extrusion, tool changes.
Compare against the file's own footer
(chapter 6, `t03-proving-gcode.txt`).
Run it on every file a script produces;
a person slices carefully,
a script slices carelessly at scale.

## Try a setting without losing the original

Copy the process preset JSON.
In the copy: change its `name`,
delete the `setting_id` line,
edit the one key. Load the copy
in place of the original:

```console
$ orca-slicer \
    --load-settings "MACHINE.json;./my-process.json" \
    --load-filaments "FILAMENT.json" \
    --outputdir OUTDIR --slice 0 MODEL.stl
```

The layer-height experiment of
chapter 7 was exactly this
(`t04-layer-height.txt`), and the
same trick carries the chapter 13
fix for presets that refuse the
command line.

## Dump the settings a slice really used

```console
$ orca-slicer \
    --load-settings "MACHINE.json;PROCESS.json" \
    --load-filaments "FILAMENT.json" \
    --export-settings SETTINGS.json \
    MODEL.stl
```

Profiles inherit (chapter 4),
so the file on disk is the *diff*,
not the truth. The export is the
resolved truth for one load —
every key, every value.
The lab used it to show that a
two-filament load had collapsed
to one filament's values
(`t05-multicolor-attempts.txt`):
when something slices strangely,
dump first, theorise second.

## Keep a project, not just a file

Export the plate as a **3MF project**
(`--export-3mf project.3mf`, or the
window's save). It carries the models,
their positions, and the full settings —
the whole decision, reopenable.
A bare G-code file carries only
the outcome. Archive the project
beside the G-code for any print
you might repeat; re-slicing a year
later from the project beats
reconstructing your reasoning
from a footer.
