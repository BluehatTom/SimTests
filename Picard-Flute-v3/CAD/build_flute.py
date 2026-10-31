#!/usr/bin/env python3
"""Picard-style playable duct flute v3.
Parametric CadQuery model, in millimeters. Acoustic performance has not
been physically verified; use the no-joint sound testers before full prints.
"""
from pathlib import Path
import cadquery as cq
import trimesh
import math
import json

OUT=Path(__file__).resolve().parent.parent
STL=OUT/"STL"
STL.mkdir(parents=True,exist_ok=True)

R_OUT=8.20
R_BORE=5.50
R_TENON=6.76
R_SOCKET=6.84
L_BODY=210.0
L_TENON=11.0
L_HEAD=50.0

def cylinder(r,z,h):
    return cq.Solid.makeCylinder(r,h,cq.Vector(0,0,z),cq.Vector(0,0,1))

def rect_cut(sx,sy,z0,z1,ycenter=0):
    return cq.Workplane("XY").box(sx,sy,z1-z0).translate((0,ycenter,(z0+z1)/2)).val()

def yz_cut(poly,width):
    return cq.Workplane("YZ",origin=(-width/2,0,0)).polyline(poly).close().extrude(width).val()

def conic(r0,r1,z0,z1):
    return cq.Solid.makeCone(r0,r1,z1-z0,cq.Vector(0,0,z0),cq.Vector(0,0,1))

def make_tenon(z):
    ten=cylinder(R_TENON,z,8.4).fuse(conic(R_TENON,6.64,z+8.4,z+11))
    # Narrow crush ribs compensate for variable printer tolerances.
    for i in range(4):
        t=i*math.pi/2+math.pi/4
        r0,r1,dt=6.66,6.99,0.070
        pts=[(r0*math.cos(t-dt),r0*math.sin(t-dt)),
             (r1*math.cos(t-dt),r1*math.sin(t-dt)),
             (r1*math.cos(t+dt),r1*math.sin(t+dt)),
             (r0*math.cos(t+dt),r0*math.sin(t+dt))]
        ten=ten.fuse(cq.Workplane("XY",origin=(0,0,z+1)).polyline(pts).close().extrude(7).val())
    return ten

def make_body(height=L_BODY,holes=True):
    part=cylinder(R_OUT,0,height).fuse(make_tenon(height))
    part=part.cut(cylinder(R_BORE,-0.3,height+L_TENON+0.6))
    if holes:
        for z,d in zip([40,59,73,92,108,124],[6.2,6.1,6.0,5.8,5.8,5.6]):
            drill=cq.Solid.makeCylinder(d/2,6.5,cq.Vector(0,4,z),cq.Vector(0,1,0))
            part=part.cut(drill)
    return part.clean()

def make_head(name,slot_height=1.0,slot_width=6.5,window_len=4.1,offset=0.0,loft_widen=0.8,standalone=False):
    # Blown end at z=50, air jet travels down to z=25 and meets blade below.
    ymid=5.90
    z_exit=25.0
    z_blade=z_exit-window_len
    blade_y=ymid+offset
    part=cylinder(R_OUT,0,L_HEAD)
    if standalone:
        part=part.cut(cylinder(R_BORE,-0.1,z_exit+0.14))
    else:
        socket=cylinder(R_SOCKET,0.35,10.9)
        socket=socket.fuse(conic(R_SOCKET+0.20,R_SOCKET,0,0.35))
        part=part.cut(socket)
        part=part.cut(cylinder(R_BORE,10.9,z_exit-10.9+0.04))
    # Fully integral windway; no separable block that can leak.
    part=part.cut(rect_cut(slot_width,slot_height,z_exit-0.05,43.0,ycenter=ymid))
    lo=cq.Workplane("XY").workplane(offset=43).center(0,ymid).rect(slot_width,slot_height).val()
    hi=cq.Workplane("XY").workplane(offset=50.15).center(0,5.17).rect(slot_width+0.8,slot_height+loft_widen).val()
    part=part.cut(cq.Solid.makeLoft([lo,hi],ruled=True))
    width=slot_width+0.35
    # Open sound window connects the jet to both room air and the resonator.
    part=part.cut(yz_cut([(5.05,z_blade-0.001),(9.5,z_blade-0.001),
                          (9.5,z_exit+0.001),(5.05,z_exit+0.001)],width))
    bevel_len=2.6
    part=part.cut(yz_cut([(blade_y,z_blade-0.002),(8.9,z_blade-bevel_len),
                          (10.2,z_blade-bevel_len),(10.2,z_exit+0.3),
                          (blade_y,z_exit+0.3)],width))
    # Interior relief leaves nominal 0.16 mm blade tip.
    part=part.cut(yz_cut([(4.9,z_blade-3.8),(5.45,z_blade-3.8),
                          (blade_y-0.16,z_blade+0.06),(4.9,z_blade+0.06)],width))
    # Flat rear datum for support-free mouthpiece printing.
    part=part.cut(rect_cut(30,4,-1,L_HEAD+1,ycenter=-9.58))
    return part.clean()

def make_gauges():
    male=cylinder(R_OUT,0,6).fuse(make_tenon(6))
    male=male.cut(cylinder(R_BORE,-0.5,18))
    female=cylinder(R_OUT,0,13)
    female=female.cut(cylinder(R_SOCKET,0.35,10.9).fuse(conic(R_SOCKET+0.20,R_SOCKET,0,0.35)))
    female=female.cut(cylinder(R_BORE,10.9,2.5))
    return male.clean(),female.clean()

def export(part,name):
    path=STL/name
    cq.exporters.export(part,str(path),exportType="STL",tolerance=0.035,angularTolerance=0.15)
    m=trimesh.load_mesh(str(path),process=True)
    assert isinstance(m,trimesh.Trimesh),name
    assert m.is_watertight,name
    assert m.is_winding_consistent,name
    assert m.volume>0,name
    return {"file":name,"triangles":len(m.faces),"volume_mm3":round(m.volume,1),
            "bounds_mm":m.bounds.round(2).tolist()}

def main():
    report={}
    report["body"]=export(make_body(),"01_FLUTE_BODY_ONE_PIECE.stl")
    variants=[
      ("A_BALANCED",1.00,6.5,4.1,0.00,0.8),
      ("B_EASY_START",1.20,6.8,4.5,0.12,1.0),
      ("C_NARROW_JET",0.78,6.5,3.7,-0.10,0.75),
      ("D_SHORT_WINDOW",1.08,7.0,3.25,0.00,0.85),
      ("E_WIDE_WINDOW",1.00,6.8,4.85,0.06,0.8),
    ]
    for i,(name,h,w,g,off,taper) in enumerate(variants):
        head=make_head(name,h,w,g,off,taper)
        # Print on flat rear face, sound window upward.
        head=head.rotate((0,0,0),(1,0,0),90).translate((0,50,7.58))
        report[name]=export(head,f"1{i}_MOUTHPIECE_{name}.stl")
    report["resonator"]=export(make_body(height=120,holes=False),"20_SHORT_TEST_RESONATOR.stl")
    for i,(name,h,w,g,off,taper) in enumerate(variants[:2]):
        head=make_head(name,h,w,g,off,taper,standalone=True)
        tube=cylinder(R_OUT,-145,145).cut(cylinder(R_BORE,-145.2,145.4))
        pure=head.fuse(tube).clean()
        pure=pure.cut(rect_cut(30,4,-145.1,0.1,ycenter=-9.58)).clean()
        pure=pure.rotate((0,0,0),(1,0,0),90).translate((0,50,7.58))
        report["sound_test_"+name]=export(pure,f"0{i}_NO_JOINT_SOUND_TEST_{name}.stl")
    a,b=make_gauges()
    report["fit_male"]=export(a,"30_FIT_GAUGE_MALE.stl")
    report["fit_female"]=export(b,"31_FIT_GAUGE_FEMALE.stl")
    (OUT/"geometry_report.json").write_text(json.dumps(report,indent=2)+"\n")
    for k,x in report.items():
        print(k,x["file"],x["triangles"],"triangles",x["volume_mm3"],"mm3")
if __name__=="__main__": main()
