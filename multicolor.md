# Multicolor Printing

**Outcome:** how multicolor printing works
in OrcaSlicer — the assignment, the change,
the waste — and an honest account of
what the lab could and could not make
the command line do.

**Check:** the evidence for this chapter's
central claim is one transcript,
`orcaslicer-lab/transcripts/t05-multicolor-attempts.txt`.
Read it before believing the claim.

> This chapter is **documented-only**
> for its window workflow, and it is the
> one chapter where that label carries
> a story: the lab tried hard to slice
> multicolor for real, four different
> ways, and OrcaSlicer 2.4.2's command
> line would not apply a second filament.
> What follows teaches the real workflow
> and reports the real failure,
> side by side.

## How multicolor works

A multicolor print is still one print.
The slicer plans it; the printer performs it.

1. **More than one filament is loaded**
   in the preset list — filament 1,
   filament 2, and so on, each with its
   own material and colour.
2. **Every part of the model is assigned**
   a filament. Assignment happens three ways:
   per **object** (this object prints in
   filament 2), by **painting** (this region
   of the surface, down to a height or a
   brush stroke, prints in filament 2),
   or by **layer** (everything above
   a height changes filament).
3. **The slicer inserts filament changes**
   wherever consecutive paths disagree.
   What a change *is* depends on the machine:
   - A **toolchanger** (like the Prusa XL)
     parks one toolhead and picks up another.
     The G-code carries tool-select commands.
   - A **single-nozzle machine with a
     filament changer** (Bambu's AMS and
     its relatives) cuts the filament,
     retracts it, feeds the next one,
     and **flushes** — pushes extra plastic
     through to purge the old colour.
     The lab read this script in full:
     it sits in the Bambu profile's
     change-filament block inside every
     sliced file's config section,
     built around the `M620` changer
     commands, with explicit flush
     and wipe moves.
4. **The waste is managed, not eliminated.**
   Flushed plastic goes to a purge spot,
   a **prime (wipe) tower** — a sacrificial
   block printed beside the part where
   changes finish and pressure settles —
   or, optionally, into the part's own
   infill. The settings OrcaSlicer exposes
   are the **flush volumes**: a matrix of
   how much to purge going from each
   filament to each other (the lab saw
   the 4 × 4 matrix in a project file).
   Dark-to-light changes need the most;
   that asymmetry is real money and time
   on big multicolour prints.

## Doing it in the window

The workflow the documentation describes,
and the one to use:

1. Set up two or more filaments in
   the filament list, in the slots
   your machine will actually have
   loaded, in order.
2. Select the object. In the object list,
   set its filament, or open the painting
   tools and paint regions with the
   filament brush.
3. Slice, and **use the preview**:
   the preview is coloured by filament,
   and the summary breaks time and
   filament down per filament,
   flush included. If the preview
   shows one colour, the assignment
   did not take — whatever the
   object list seemed to say.
4. Check the change count.
   Every change costs time and purge
   plastic; a model that changes
   filament on most layers — the lab's
   two-bar test piece was designed
   to be exactly that worst case —
   is the expensive end of multicolor.

## What the lab found on the command line

The command line accepts the pieces:
`--load-filaments` takes several presets,
`--load-filament-ids` claims to assign
them to objects. In 2.4.2, for models
loaded as plain STL files, the assignment
does not survive. Four attempts,
two printer families, same result:

- Both objects sliced with filament 1.
  The output header says `; filament: 1`,
  and there are no tool-select commands
  anywhere in the file.
- Dumping the resolved settings showed
  both filament *names* loaded, but the
  per-filament values — colour,
  temperature — collapsed to one entry.
- Exporting a project file showed the
  same thing from inside: its object
  list recorded **both objects on
  extruder 1**. Editing the second
  object to extruder 2 by hand and
  slicing the project produced G-code
  identical to the unedited project,
  timestamp aside — the command-line
  slicing path ignores that record too.
- The older AMF format, which carries
  materials per volume, was misread
  by the importer (zero volume),
  closing the last route.

So: **multicolor assignment is,
in practice today, a window operation.**
The command line slices one filament
per plate, reliably and well.
Script the single-colour work;
do the colour work in the window;
and use chapter 6's method on any
multicolor file — header, per-filament
totals, change count — before it prints,
because exactly these numbers are
the ones that silently collapse to one.
