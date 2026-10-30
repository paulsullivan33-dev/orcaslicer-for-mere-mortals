#!/usr/bin/env python3
"""Write the two bars as one AMF file with two materials.

AMF is the older multi-material interchange format: each volume
names a material id, and slicers in the Prusa lineage map material
ids to extruders when the file is loaded. The lab generated this
file to test whether OrcaSlicer's command line would accept
multicolor input this way. In 2.4.2 it does not - the importer
misreads the geometry (see transcripts/t05-multicolor-attempts.txt).
The script is kept so the attempt can be repeated exactly.
"""
import importlib.util
import sys

spec = importlib.util.spec_from_file_location(
    "mm", __file__.replace("make_amf.py", "make_models.py"))
mm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mm)


def corners(x0, y0, z0, x1, y1, z1):
    return [(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0),
            (x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)]


def object_xml(obj_id, box_args, materialid):
    verts = corners(*box_args)
    idx = {v: i for i, v in enumerate(verts)}
    vxml = "\n".join(
        "        <vertex><coordinates>"
        f"<x>{v[0]}</x><y>{v[1]}</y><z>{v[2]}</z>"
        "</coordinates></vertex>" for v in verts)
    tris = "\n".join(
        f'        <triangle v1="{idx[t[0]]}" v2="{idx[t[1]]}" '
        f'v3="{idx[t[2]]}"/>' for t in mm.box(*box_args))
    return (f'  <object id="{obj_id}">\n    <mesh>\n      <vertices>\n'
            f"{vxml}\n      </vertices>\n"
            f'      <volume materialid="{materialid}">\n{tris}\n'
            "      </volume>\n    </mesh>\n  </object>")


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "bars-two-material.amf"
    amf = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<amf unit="millimeter" version="1.1">\n'
           '  <material id="0">\n'
           '    <metadata type="name">Filament A</metadata>\n'
           "  </material>\n"
           '  <material id="1">\n'
           '    <metadata type="name">Filament B</metadata>\n'
           "  </material>\n"
           + object_xml(0, (170, 175, 0, 180, 185, 6), 0) + "\n"
           + object_xml(1, (180, 175, 0, 190, 185, 6), 1) + "\n"
           "</amf>\n")
    open(out, "w").write(amf)
    print(f"wrote {out}")
