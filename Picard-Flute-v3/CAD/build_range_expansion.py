#!/usr/bin/env python3
"""Expanded-note v3 Picard duct flute bodies. All units mm.
Keep the currently working v3 mouthpiece: socket/tenon is unchanged.
These are acoustic prototypes and require real pitch tests.
"""
import json
import math
from pathlib import Path
import cadquery as cq
import trimesh
from build_flute import R_OUT,R_BORE,cylinder,conic,make_tenon

ROOT=Path(__file__).resolve().parents[1]
STL=ROOT/"Range_Expansion_STLs";STL.mkdir(parents=True,exist_ok=True)
DOCS=ROOT/"Range_Expansion_Docs";DOCS.mkdir(parents=True,exist_ok=True)

# From FOOT to MOUTH; chosen using a 1D open-tone-hole impedance model.
FRONT_Z=[36,55,70,86,103,117,132]
FRONT_D=[6.20,6.30,5.20,5.80,5.80,6.00,3.00]
THUMB_Z=163.0
BODY_LEN=210.0

def drill(x,y,z,d,sign):
    return cq.Solid.makeCylinder(d/2,7.5,cq.Vector(x,y,z),cq.Vector(0,sign,0))

def make_body(thumb_d=3.,split=False):
    shape=cylinder(R_OUT,0,BODY_LEN).fuse(make_tenon(BODY_LEN))
    shape=shape.cut(cylinder(R_BORE,-.25,BODY_LEN+11.5))
    for i,(pos,d) in enumerate(zip(FRONT_Z,FRONT_D)):
        if split and i in (0,1):
            small=2.50 if i==0 else 3.00
            large=math.sqrt(d*d-small*small)
            # Double vents: combined area matches single round hole.
            shape=shape.cut(drill(-2.9,3.4,pos,large,+1))
            shape=shape.cut(drill(+2.9,3.4,pos,small,+1))
        else:
            shape=shape.cut(drill(0,3.4,pos,d,+1))
    if thumb_d:
        shape=shape.cut(drill(0,-3.4,THUMB_Z,thumb_d,-1))
    shape=shape.clean()
    assert shape.isValid() and len(shape.Solids())==1
    for z in (4,30,94,135,200,217):
        assert not shape.isInside(cq.Vector(0,0,z),.0001)
    for i,z in enumerate(FRONT_Z):
        xx=(-2.9,2.9) if split and i in (0,1) else (0,)
        for x in xx:
            assert not shape.isInside(cq.Vector(x,7.4,z),.0001),("closed front hole",x,z)
    if thumb_d:
        assert not shape.isInside(cq.Vector(0,-7.4,THUMB_Z),.0001),"closed thumb hole"
    return shape

def rib(angle):
    # Very shallow FDM-compliant grip on the existing smooth 16.4mm foot.
    low,high,half=8.11,8.39,.055
    p=[(r*math.cos(angle+t),r*math.sin(angle+t))
       for r,t in [(low,-half),(high,-half),(high,half),(low,half)]]
    return cq.Workplane("XY",origin=(0,0,3)).polyline(p).close().extrude(6).val()

def make_extension(extra):
    # Foot sleeve with 15mm insertion; continues the 11mm internal bore.
    insertion=15.0
    shape=cylinder(10.40,0,insertion+extra)
    shape=shape.cut(cylinder(R_OUT+.105,-.1,insertion+.11))
    shape=shape.cut(conic(R_OUT+.32,R_OUT+.105,0,.75))
    shape=shape.cut(cylinder(R_BORE,insertion-.03,extra+.20))
    for i in range(4):
        shape=shape.fuse(rib(i*math.pi/2+math.pi/4))
    shape=shape.clean()
    assert shape.isValid() and len(shape.Solids())==1
    assert not shape.isInside(cq.Vector(0,0,insertion+extra/2),.0001)
    return shape

def export(shape,name):
    fn=STL/name
    cq.exporters.export(shape,str(fn),exportType="STL",tolerance=.035,angularTolerance=.15)
    m=trimesh.load_mesh(str(fn),process=True)
    assert isinstance(m,trimesh.Trimesh) and m.is_volume and m.is_watertight
    assert m.is_winding_consistent and len(m.split(only_watertight=False))==1
    assert m.volume>0
    return dict(file=name,triangles=len(m.faces),mm3=round(m.volume,2),
                bounds_mm=m.bounds.round(2).tolist(),bytes=fn.stat().st_size)

def main():
    all_parts={}
    versions=[
      ("01_7HOLE_SIMPLE_NO_THUMB.stl",0,False),
      ("02_7HOLE_THUMB_3MM.stl",3.0,False),
      ("03_7HOLE_THUMB_SMALL_2_2MM.stl",2.2,False),
      ("04_CHROMATIC_SPLIT_LOW_7HOLE_THUMB_3MM.stl",3.0,True)
    ]
    for name,thumb,split in versions:
        all_parts[name]=export(make_body(thumb,split),name)
        print("PASS",name,flush=True)
    for ext in (25,45):
        name=f"05_FOOT_EXTENSION_{ext}MM.stl"
        all_parts[name]=export(make_extension(ext),name)
        print("PASS",name,flush=True)
    (DOCS/"mesh_qa.json").write_text(json.dumps(all_parts,indent=2)+"\n")

if __name__=="__main__":main()
