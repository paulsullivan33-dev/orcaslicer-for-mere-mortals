# Installing OrcaSlicer

**Outcome:** OrcaSlicer on your machine,
with a check that proves it runs —
not just that it downloaded.

**Check:** the version's help text prints.

```console
$ orca-slicer --help | head -3
OrcaSlicer is a powerful FDM slicer
designed for slicing 3D models for
FDM 3D printers…
```

## Get it from the project

Download OrcaSlicer from the project's
official GitHub releases page —
the `SoftFever/OrcaSlicer` repository.
Windows gets an installer or a portable zip.
macOS gets a disk image.
Linux gets an **AppImage**,
a single file that carries the program
and its private libraries.

Versions matter to this guide:
the lab work used **2.4.2**,
the official Ubuntu 24.04 AppImage,
SHA-256
`d12fb8c8eac1aecd2dfb6377acd48f994f8fa439ed5292fa532dd82880f029fd`.
Behaviour — especially command-line
behaviour — can shift between releases,
so if your version differs,
expect the broad strokes to match
and the edges to differ.

## Linux and the AppImage

On a normal desktop the AppImage
is the easy path: make it executable
and run it. Two wrinkles are worth knowing.

**No FUSE?** Some systems — containers,
minimal servers, remote shells — cannot
mount an AppImage. Extract it instead:

```console
$ ./OrcaSlicer.AppImage --appimage-extract
```

That unpacks a `squashfs-root/` folder
with the real binary inside
(`bin/orca-slicer`), and everything in
this guide works on the extracted tree.

**Missing host libraries.**
The AppImage bundles its own libraries
but links a few from the host —
OpenGL and friends for the window.
On a machine without a desktop stack,
even `--help` can refuse to start,
naming the missing library.
Install what it names from your
distribution (on Debian and Ubuntu,
`libopengl0` and `libglu1-mesa`
cover the common case) and try again.
The lab's sandbox could not install
packages at all, so it extracted the
library packages into a folder and
used `LD_LIBRARY_PATH` — the same idea,
done by hand, recorded in
`orcaslicer-lab/transcripts/t00-install.txt`.

> **Lab note.** The lab ran everything
> through the extracted tree on a
> headless machine, so the window
> itself was never opened there.
> Install steps for the window are
> the project's standard ones;
> everything command-line in this
> guide was run, not retold.

## First launch

On a desktop, the first launch offers
a setup flow: region, then a chance
to pick your printer from the profile
library, then filaments.
Take the offer if your printer is listed —
it sets the three presets of chapter 2
to a sane starting trio.
You can change every choice later,
and chapter 4 explains what the
choices actually are.

## The check that matters

However you installed it, end here:
a terminal, the help text, three lines.
If `--help` prints, the engine runs,
and every command-line recipe in this
guide is available to you —
including slicing a model with no
window involved at all.
