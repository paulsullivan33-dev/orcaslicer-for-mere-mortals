# Limits

**Outcome:** what this guide and its
subject cannot do, collected in one
place, as the series requires.

**Check:** every limit below is either
a lab observation you can re-run,
or is labelled as a boundary of the
lab itself.

## The lab's limits

- **No window was run.** The sandbox
  was headless. OrcaSlicer's GUI
  install, workflow, painting tools,
  and preview are described from the
  project's documentation, not from
  observed use. Where a chapter
  depends on the window, it says so.
- **No printer was involved.**
  Nothing in this guide proves a
  physical print succeeds. The lab
  proved files: that the G-code is
  internally consistent, correctly
  counted, and produced by the
  profiles named. Bed adhesion,
  stringing, and warping live on
  the far side of a real machine.
- **One release.** Everything was
  run on OrcaSlicer 2.4.2.
  Command-line behaviour in
  particular changes between
  releases; the multicolor finding
  below is a finding about 2.4.2.

## The command line's limits, observed

- **Multicolor assignment does not
  apply to plain model files.**
  Four attempts, two machine families
  — the second filament never reached
  the G-code. Evidence:
  `transcripts/t05-multicolor-attempts.txt`.
- **Some bundled presets refuse the
  command line** with error −51,
  because raw profile files load
  without parts of their inherited
  values (chapter 13). A hand-copied
  process preset repairs the case
  the lab met; the general gap
  remains the project's to close.
- **The AMF importer misread**
  a well-formed two-material file,
  reporting zero volume. STL and
  3MF are the reliable inputs.
- **Estimates are estimates.**
  The slicer's time and totals come
  from its plan. The lab's own sums
  from the emitted file differed
  by about 1.5% on filament —
  small, and a standing reminder
  that the file, not the summary,
  is the ground truth.

## The tool's limits

- **A slicer cannot fix a model.**
  Non-manifold skins, paper-thin
  walls, and floating geometry
  slice into flawed instructions
  with total confidence. `--info`
  and the preview are the early
  warnings; repair belongs
  upstream, in the design tools.
- **Profiles are somebody's printer.**
  A bundled preset encodes the
  vendor's test units and habits.
  Yours may differ — nozzle wear,
  a swapped hotend, a different
  build plate. The checks in this
  guide catch file-level surprises;
  machine-level truth still comes
  from your first careful prints.
- **G-code is not portable.**
  A file is bound to its machine
  preset: sizes, sensors, start
  sequences. Slicing again for
  another printer is not pedantry;
  it is the tool's core rule.
