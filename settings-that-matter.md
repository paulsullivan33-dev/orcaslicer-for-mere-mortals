# Settings That Matter

**Outcome:** the short list of settings
that visibly change a print, each with
the check that shows its effect.

**Check:** one is demonstrated end-to-end
below — same cube, one key changed,
the difference counted in the output.

A slicer exposes hundreds of settings.
Most are fine at their preset values
for a long time. These are the ones
worth learning first, in the order
they bite.

## Layer height

The thickness of each layer, and the
single biggest quality-versus-time lever.
Thinner layers: smoother curved surfaces,
more layers, more time.

The lab's demonstration
(transcript `t04-layer-height.txt`):
the chapter 5 cube, re-sliced with a
copy of the process preset carrying
one edit — `"layer_height": "0.12"`.

| | 0.20 mm | 0.12 mm |
|---|---|---|
| Layers | 100 | 166 |
| Time estimate | 46 m 34 s | 1 h 1 m 20 s |
| Filament, net | 1321.7 mm | 1325.4 mm |
| Filament, gross | 1592.9 mm | 1730.2 mm |

The arithmetic closes: a 0.2 mm first
layer plus 165 × 0.12 mm is exactly
the cube's 20 mm. The lessons generalise:
time scales with layer count,
filament barely moves (same part!),
and the gross figure climbs because
each extra layer is another
retract-and-repush cycle.
Layer height changes *how* the part
is built, not *how much* it is.

## Walls (wall loops)

How many solid outlines each layer gets
before infill begins. Walls carry most
of a part's strength and all of its
surface. The lab's preset used 2,
and the type table in chapter 6 proved
it: an outer-wall and an inner-wall
path on every one of the 100 layers.
Thin-walled parts may be *all* wall;
check the preview before assuming
infill exists.

## Infill density and pattern

The interior lattice. 20% is the common
default — the lab's cube showed
sparse infill on 94 of 100 layers,
the rest being solid bottom and top.
Density is a strength-and-weight dial,
and the pattern (grid, gyroid, lines,
and more) changes how the part flexes
and how it prints. Check: the type
table again — `Sparse infill` lines
present, solid layers only at the
bottom, the top, and under overhangs.

## First layer settings

The first layer decides whether anything
else happens. Presets typically print
it slower, sometimes thicker or hotter,
for bed adhesion. The lab's footer
gave the game away: 21 m 47 s of the
46 m 34 s estimate was the *first layer*
— this preset takes its first layer
very slowly. When prints detach,
this family of settings, and a clean
bed, are where to look — in that order.

## Support

Structures printed under overhangs,
torn away afterwards. The cube needs
none — vertical walls support
themselves — and the type table agreed:
no support types appear. For models
with overhangs, the choices that
matter are the overhang angle that
triggers support, and tree (organic)
versus grid structures. Supports are
documented-only in this guide:
no lab model needed them,
so no transcript pretends otherwise.

## Temperature and speed

These live mostly in the filament
preset (nozzle and bed temperature)
and the process preset (speeds).
Treat the preset values as the
vendor's tested answer.
When you change one, change only one,
and keep the chapter 6 checks as your
before-and-after — a print that merely
*looks* different proves little;
a layer count, a time, and a filament
total that moved as predicted
proves the change did what you meant.

## The rule of the chapter

One setting at a time,
with the file checked afterwards.
Two settings at once is how
"the slicer update broke it"
mysteries are born.
