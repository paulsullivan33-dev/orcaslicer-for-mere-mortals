#!/usr/bin/env python3
"""Generate this guide's test models as binary STL files.

Three solids, all axis-aligned boxes built from 12 triangles each:

- cube.stl        a 20 x 20 x 20 mm calibration cube
- bar-a.stl       a 10 x 10 x 6 mm bar standing on the bed (x 0..10)
- bar-b.stl       the same bar beside it              (x 10..20)

Sliced together, the two bars form one 20 x 10 x 6 mm block whose
left and right halves can be assigned to different filaments.
Coordinates are absolute, so the files only make sense printed
together with arranging turned off.
"""
import struct
import sys


def box(x0, y0, z0, x1, y1, z1):
    """Return the 12 triangles of an axis-aligned box as vertex tuples."""
    c = [(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0),
         (x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)]
    # faces as (a, b, c) corner indices, wound to face outwards
    faces = [(0, 2, 1), (0, 3, 2),      # bottom
             (4, 5, 6), (4, 6, 7),      # top
             (0, 1, 5), (0, 5, 4),      # front
             (1, 2, 6), (1, 6, 5),      # right
             (2, 3, 7), (2, 7, 6),      # back
             (3, 0, 4), (3, 4, 7)]      # left
    return [(c[a], c[b], c[cc]) for a, b, cc in faces]


def write_stl(path, triangles):
    with open(path, "wb") as f:
        f.write(b"\0" * 80)                      # header
        f.write(struct.pack("<I", len(triangles)))
        for tri in triangles:
            f.write(struct.pack("<3f", 0, 0, 0))  # normal (recomputed by readers)
            for v in tri:
                f.write(struct.pack("<3f", *v))
            f.write(struct.pack("<H", 0))         # attribute byte count
    print(f"wrote {path}: {len(triangles)} triangles")


if __name__ == "__main__":
    outdir = sys.argv[1] if len(sys.argv) > 1 else "."
    write_stl(f"{outdir}/cube.stl", box(0, 0, 0, 20, 20, 20))
    write_stl(f"{outdir}/bar-a.stl", box(0, 0, 0, 10, 10, 6))
    write_stl(f"{outdir}/bar-b.stl", box(10, 0, 0, 20, 10, 6))
