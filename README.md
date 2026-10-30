# OrcaSlicer for Mere Mortals

A 3D model is not something a printer can use.
A printer needs instructions:
move here, heat this, push out this much plastic.
Turning the first into the second is called **slicing**,
because the model is cut into layers,
and each layer becomes a path.
**OrcaSlicer** is the program that does the cutting.
You give it a model.
It gives you a file of instructions — **G-code** —
that one specific printer can follow.

OrcaSlicer is free and open source.
It runs on your own machine.
It grew out of Bambu Studio,
which grew out of PrusaSlicer,
so it carries a large library of printer profiles
and a long-serving slicing engine.

One rule before anything else.
G-code is instructions to a real machine
that gets hot and moves.
A file sliced for the wrong printer
can command the wrong temperatures and motions.
Always check that the machine profile
matches the physical printer in front of you,
and read a new file before you send it.
The checks in this guide exist for that reason.

## What the lab work actually ran

The verification lab for this guide
downloaded the official OrcaSlicer 2.4.2 AppImage,
generated small test models with a script,
and sliced them through OrcaSlicer's
**command-line mode** — the same engine the window runs,
driven by commands instead of clicks.
Every claim tied to the software rests on output
transcribed in the `orcaslicer-lab` folder:

- A 20 mm cube sliced with a bundled generic
  printer profile, and the G-code **proved**
  afterwards: the layer count checked three
  independent ways (100 layers, all agreeing),
  and the filament total summed from the file's
  own extrusion moves and compared with the
  slicer's own footer.
- The same cube re-sliced at 0.12 mm layer height:
  166 layers, about a third more time,
  almost the same filament — the setting's effect
  shown in numbers, not adjectives.
- Four real attempts at a two-filament slice
  from the command line, on two different
  machine profiles. None of them applied the
  second filament. That failure is documented
  in full, with the evidence, and the multicolor
  chapter teaches the window workflow instead,
  labelled as such.

The window (GUI) itself could not run
in the lab's headless sandbox,
and no printer was involved at any point.
Window steps, printer-specific profiles,
multicolor painting, and sending prints
are **documented-only** in this guide —
written from OrcaSlicer's own documentation
and from the profile files the lab read in full —
and labelled plainly in each chapter
and in the [writing criteria](criteria.md).

## What this guide covers

- The slicing model: model, layers, paths, G-code.
- The three presets that decide everything:
  **machine**, **process**, and **filament** —
  and how they inherit from shared bases.
- Installing OrcaSlicer, and the check
  that proves the install works.
- Your first slice, in the window and
  from the command line.
- Proving the G-code: header, layer counts,
  extrusion totals, estimates — reading the file
  like an auditor, not a believer.
- The handful of settings that actually
  change the result, each with its check.
- Multicolor printing: painting, per-object
  filament assignment, filament changers
  and toolchangers, flush volumes and
  the prime tower — and the honest state
  of multicolor from the command line.
- Sending the print: files, cards, and
  printer hosts.
- Recipes, the neighbouring slicers,
  the limits, and troubleshooting —
  including the profile trap the lab hit
  that refuses some bundled presets
  on the command line.

## What this guide does not do

- **Design models.** Making the model in
  the first place belongs to the OpenSCAD
  and CAD guides. This guide starts
  with a finished model file.
- **Run a printer.** Profiles for specific
  machines, first-layer tuning on real
  hardware, and print-farm operation are
  beyond it. The lab had no printer.
- **Pretend the window was tested.**
  Where a chapter describes clicking,
  it says so, and the criteria say why.

## How to use this guide

Read the chapters in order the first time;
they build on each other.
After that, each stands alone —
especially **Proving the G-code**
and **Troubleshooting**,
which most people return to.
Commands are shown exactly as the lab ran them,
and every number quoted from a slice
can be traced to a transcript
in the `orcaslicer-lab` folder.

---

Part of the series:
[For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/)

Related guides:
[3D Printing for Mere Mortals](https://paulsullivan33-dev.github.io/3d-printing-for-mere-mortals/),
[OpenSCAD for Mere Mortals](https://paulsullivan33-dev.github.io/openscad-for-mere-mortals/),
[CAD for Mere Mortals](https://paulsullivan33-dev.github.io/cad-for-mere-mortals/),
and [Klipper for Mere Mortals](https://paulsullivan33-dev.github.io/klipper-for-mere-mortals/).

## License

Text: [CC BY 4.0](LICENSE) · Code: [MIT](LICENSE-CODE)
