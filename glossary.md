# Glossary

**3MF** — the project-friendly model
format. Carries objects, positions,
and settings, where STL carries
only the skin.

**AMF** — an older multi-material
model format. OrcaSlicer 2.4.2's
importer misread the lab's test file;
see Limits.

**AMS** — Bambu Lab's Automatic
Material System: the box that holds
several spools and swaps filament
into a single-nozzle printer on
command (the `M620` family of
commands in the G-code).

**AppImage** — a Linux distribution
format that packs a program into
one executable file. Extractable
with `--appimage-extract` when the
system cannot mount it.

**Extruder** — the mechanism that
pushes filament. Also, in slicer
vocabulary, a *numbered slot* a
model part can be assigned to —
extruder 1, extruder 2 — whether
the hardware realises it as a
toolhead or a changer feed.

**Filament preset** — the settings
for one plastic: temperatures,
cooling, flow, retraction.

**Flush (purge)** — pushing extra
plastic through the nozzle after a
filament change to clear the old
colour out. Controlled by the
flush-volume matrix.

**G-code** — the instruction file
a printer obeys: moves, temperatures,
fan and changer commands, in plain
text.

**Infill** — the interior lattice
of a part, described by a density
and a pattern. Sparse infill is
the ordinary kind; the rest of the
part is walls and solid layers.

**Inherits** — the preset file key
naming the base preset whose values
it builds on. Profiles are diffs,
not whole documents.

**Layer** — one horizontal slice
of the print, laid at one Z height.
Layer height is its thickness
and the process preset's headline
number.

**Machine preset** — the settings
for one physical printer and nozzle:
size, limits, start and end blocks.
Called *printer* in the window.

**Manifold** — watertight: the model
skin has no holes or open edges,
so inside and outside are defined.
`--info` reports it.

**Plate** — the virtual build surface
in the slicer, holding the objects
of one print job.

**Prime tower (wipe tower)** — a
sacrificial block printed beside
the part on multicolor jobs,
where freshly changed filament
settles before touching the part.

**Process preset** — the settings
for how this print is made:
layer height, walls, infill,
supports, speeds.

**Retraction** — pulling filament
back slightly before a travel move,
so it does not drool a string
across the part. The gap between
gross and net extrusion in
chapter 6 is largely retraction
traffic.

**Skirt** — a warmup loop printed
around (not touching) the part,
priming the nozzle before the
real first layer.

**Slicing** — turning a model into
layers and layers into printer
instructions.

**Toolchanger** — a printer with
several complete toolheads that
it swaps mechanically (the Prusa XL
pattern), making filament changes
cheap in waste and dear in hardware.

**Tool change** — any change of the
active extruder mid-print: a tool
select (`T1`, …) on a toolchanger,
or the cut-swap-flush script on a
single-nozzle changer machine.
