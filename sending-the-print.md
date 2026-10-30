# Sending the Print

**Outcome:** the routes a finished file
takes to a printer, and the checks
worth doing on each.

**Check:** whatever the route, the file
that leaves should be the file you
proved in chapter 6 — same name,
same size, same slicer header.

> **Documented-only.** The lab had no
> printer and sent nothing anywhere.
> This chapter is written from the
> project's documentation and general
> practice. The checks below are the
> guide's own, and they travel well.

## Route 1: the file, carried

The oldest route: export the G-code
(or, for Bambu machines, the sliced
3MF the printer expects), copy it to
the printer's SD card or USB stick,
and start the print at the machine.
Its virtues are real: no network,
no accounts, and the file on the card
is exactly the file on your computer.
Compare the byte size after copying —
a truncated copy is a classic cause
of prints that stop mid-air.

## Route 2: a printer host

Many printers run or accept a **host**:
software that receives files and
supervises the print. OrcaSlicer can
send to the common kinds —

- **Klipper** machines, through their
  web interfaces (Mainsail, Fluidd)
  or Moonraker API. See the Klipper
  guide in this series.
- **OctoPrint**, the long-serving
  Raspberry Pi print server.
- **PrusaLink / Prusa Connect**
  for Prusa machines.
- **Bambu machines** on the local
  network, in LAN mode or through
  Bambu's cloud, depending on
  the machine and your choices.

In the window this is the
**Print** button beside Export:
pick the host, send, and the host
takes the file from there.
On the command line there is no
send step — produce the file,
then hand it to the host's own
upload path (its web page or API).

## Route 3: the manufacturer's cloud

Bambu and Prusa both offer clouds
that carry the file and report
progress. Convenience is the offer;
the price is an account and your
print metadata leaving the house.
LAN modes exist on both ecosystems
for people who decline. This guide
takes no side — it only notes that
the *file* is identical either way,
and a file you have proved locally
behaves the same from a cloud.

## Before any print starts

Three checks, thirty seconds:

1. **Right machine.** The machine
   preset in the file's config block
   names the printer family it was
   sliced for. Read it. Chapter 1's
   rule lives here.
2. **Right plastic.** The filament
   the file assumes, versus the spool
   loaded — material and, for
   multicolor, slot order.
3. **Plausible numbers.** Time and
   filament from chapter 6's proof.
   A "20-minute" file for a part
   that took two hours last time
   is a question, not a bargain.

Then let it print.
The first layer is the review point:
watch it go down, or check the
first photograph the host offers,
before trusting the remaining hours.
