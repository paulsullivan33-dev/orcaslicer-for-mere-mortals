# Profiles — Machine, Process, Filament

**Outcome:** you can pick a preset trio
that makes sense, and you know where
the presets live and how to read one.

**Check:** open any preset file in a
text editor. It is JSON — plain text,
a name, what it inherits, and the keys
it changes. Nothing about it is magic.

## Where profiles live

The official download carries a library
of **system profiles** under
`resources/profiles/<Vendor>/`,
each vendor folder split into
`machine/`, `process/`, and `filament/`.
The lab used three files from it directly:

```text
Prusa/machine/Prusa MK3.5 0.4 nozzle.json
Prusa/process/0.20mm Speed @MK3.5.json
Prusa/filament/Prusa Generic PLA @MK3.5.json
```

Profiles you tune yourself become
**user profiles**, saved by the window
into your OrcaSlicer configuration folder.
A useful habit: change a setting,
and the preset name gains a marker
that it is modified; save it under your
own name rather than overwriting the
system preset, so the original stays
one dropdown away when an experiment
goes wrong.

## Reading a preset's name

Preset names are dense because they
have to be. Decoded:

- `Prusa MK3.5 0.4 nozzle` — machine:
  the printer, plus the nozzle fitted.
  A 0.6 nozzle is a *different machine
  preset*, not a settings tweak.
- `0.20mm Speed @MK3.5` — process:
  layer height first (0.20 mm),
  the flavour (Speed), then `@MK3.5`,
  the machine family it was tuned for.
- `Prusa Generic PLA @MK3.5` — filament:
  a generic PLA, tuned by the vendor
  for that machine family.

The `@` tail is a compatibility claim.
A process preset built for one machine
family may refuse — or worse, silently
misfit — another. The window greys out
incompatible combinations;
the command line does not,
which is one reason chapter 5's
first slice uses a matched trio
from one vendor folder.

## Inheritance, and why it matters

Open a machine preset and near the top
you will find something like:

```json
"inherits": "fdm_machine_common"
```

The preset is a *diff*.
Shared values live in base presets
(`fdm_process_common`,
`fdm_filament_common`, and vendor bases),
and each file overrides what makes
it specific. Three consequences:

1. A preset file alone does not tell
   you the full settings. The window —
   and the chapter 6 technique of
   reading a sliced file's config
   block — shows the resolved truth.
2. Copying a preset to edit it is normal
   and safe: the lab did exactly that
   to change one key. Give the copy
   its own `name`, and drop its
   `setting_id` line so the program
   treats it as yours.
3. Raw preset files loaded on the
   command line are only partly
   resolved in OrcaSlicer 2.4.2.
   Most values resolve; some inherited
   values come through empty —
   and two bundled machine families
   fail the command line's own checks
   because of it. That story, with
   the error text, is chapter 13's.

## Choosing a trio for a first print

- Machine: your exact printer and
  the nozzle actually fitted.
- Process: the layer height you want,
  in the vendor's balanced or standard
  flavour if one exists.
  Speed flavours trade surface quality
  for time.
- Filament: the material in the machine
  — generic PLA is the honest starting
  point for PLA, whatever the spool's
  brand, because brands differ less
  than materials do.

Then slice, and *read the result*
(chapter 6) before the file goes
anywhere near a printer.
