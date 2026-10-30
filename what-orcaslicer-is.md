# What OrcaSlicer Is

**Outcome:** a clear picture of what a slicer
does and does not do, before you install anything.

**Check:** at the end you can say, in one sentence,
what goes in and what comes out.
Everything between the two is this guide.

## The one-sentence version

A slicer turns a 3D model
into a list of instructions for one printer.

The input is usually an **STL** or **3MF** file:
a skin of triangles that describes a shape,
and nothing else.
No temperatures. No speeds. No plastic.
The output is usually a **G-code** file:
thousands of lines like `G1 X42.0 Y17.5 E0.83`,
each one a small move, some of them
pushing filament out of a heated nozzle
as the head travels.

## Why slicing is a real job

The printer is not smart.
It follows the file.
So every decision hides in the slicing step:

- How thick is each layer?
- How fast may the head move, and where
  must it slow down?
- How hot are the nozzle and the bed?
- Which lines are walls, which are filling,
  which are support to be torn away?
- When two colours are wanted,
  when does the filament change,
  and what happens to the old colour
  still melted in the nozzle?

OrcaSlicer makes those decisions from
three presets working together —
machine, process, and filament —
which is the subject of the next chapter.

## Where OrcaSlicer comes from

OrcaSlicer is a fork of Bambu Studio,
Bambu Lab's slicer,
which is itself a fork of PrusaSlicer,
which descends from Slic3r.
Practically, that heritage means three things.

It slices the way PrusaSlicer slices:
the engine is mature and widely trusted.
It speaks Bambu fluently:
profiles for Bambu machines and their
filament changers are first class.
And it is not tied to one maker:
the official download ships profiles
for more than sixty printer vendors,
from Afinia to Z-Bolt,
including Creality, Prusa, Anycubic,
Elegoo, Voron, and many more.
The lab counted the vendor folders
inside the official 2.4.2 download —
67 of them; the list is long.

## What OrcaSlicer is not

It is **not a design tool**.
It will scale, rotate, cut, and paint a model,
but you do not model a part in it from nothing.
That work belongs to CAD —
see the OpenSCAD and CAD guides
in this series.

It is **not a printer driver** in the
plug-it-in sense.
It produces the file,
and can hand the file to several kinds
of printer host, but the print itself
runs from the file, not from OrcaSlicer.

And it is **not the final word**.
The file it produces is plain text.
You can read it, count things in it,
and refuse to trust an estimate
until the file itself confirms it.
Chapter 6 is built on exactly that idea.

## The safety rule, stated early

G-code commands a machine that heats
plastic until it melts and moves
in three axes. A file sliced for one
printer can be wrong — sometimes
dangerously wrong — for another:
different travel limits, different
temperature sensors, different start
sequences. Treat every G-code file
like a program you are about to run,
because it is one. Slice for the
printer you actually own,
with its own profile,
and skim any new file before it prints.
