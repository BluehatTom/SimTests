#!/usr/bin/env python3
"""Test mouthpieces for the working Picard flute v3; units mm.
Retains EXACT v3 receiving socket. This is acoustic experimentation, not
physical proof of note quality. Built as individual support-free-print STLs.
"""
import json
from pathlib import Path
import cadquery as cq
import trimesh
from build_flute import cylinder,conic,rect_cut,yz_cut,make_head,R_OUT,R_BORE,R_SOCKET

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'Experimental_Mouthpieces'; DEST.mkdir(exist_ok=True)
QA=ROOT/'QA';QA.mkdir(exist_ok=True)

# name, kind, slot height, width, window length, edge offset,
# windway funnel z, exit chamfer, edge thickness, additional bore length
V=[
 ('01_STABLE_LONG_WINDWAY','single',1.02,6.45,4.35,0.00,45.0,.18,.21,0),
 ('02_WARM_GENTLE','single',.87,6.20,4.60,-.05,44.8,.12,.20,0),
 ('03_BRIGHT_HARMONICS','single',.86,6.80,3.55,.08,40.8,0,.13,0),
 ('04_BREATHY_OPEN','single',1.35,7.00,4.65,-.12,42.0,0,.20,0),
 ('05_EASY_OVERTONE','single',.82,6.50,3.28,.13,40.4,0,.14,0),
 ('06_TWIN_JET_SINGLE_EDGE','twin',1.05,6.5,4.05,0,43.0,.07,.16,0),
 ('07_TWIN_JET_DOUBLE_LABIUM','double',1.10,6.5,4.15,0,43.0,.06,.16,0),
 ('08_LOWER_PITCH_12MM','single',1.0,6.50,4.10,0,43.0,0,.16,12),
 ('09_LOWER_PITCH_24MM','single',1.0,6.50,4.10,0,43.0,0,.16,24)
]

def head(spec):
    name,kind,sh,sw,wd,off,funnel,chamfer,tip,ext=spec
    ze=25+ext; top=50+ext; fz=funnel+ext
    s=cylinder(R_OUT,0,top)
    socket=cylinder(R_SOCKET,.35,10.9).fuse(conic(R_SOCKET+.20,R_SOCKET,0,.35))
    s=s.cut(socket).cut(cylinder(R_BORE,10.9,ze-10.9+.04))
    if kind=='single':
        slots=[(0,sw)]; windows=[(0,sw+.35,wd,off)]; fw=sw+.8
    elif kind=='twin':
        slots=[(-1.86,2.70),(1.86,2.70)]; windows=[(0,7.0,wd,off)]; fw=7.0
    else:
        slots=[(-1.93,2.56),(1.93,2.56)]
        windows=[(-1.93,2.66,wd-.18,off-.06),(1.93,2.66,wd+.18,off+.06)];fw=7.25
    for x,w in slots:
        s=s.cut(rect_cut(w,sh,ze-.05,fz,5.9).translate((x,0,0)))
        if chamfer:
            lo=5.9-sh/2;hi=5.9+sh/2
            for polygon in [[(hi-.002,ze-.012),(hi+chamfer,ze-.012),(hi-.002,ze+.6)],
                            [(lo+.002,ze-.012),(lo-chamfer,ze-.012),(lo+.002,ze+.6)]]:
                s=s.cut(yz_cut(polygon,w).translate((x,0,0)))
    # Common lip entrance splits into 2 side-by-side ducts on twin variants.
    wlow=sw if kind=='single' else fw-.3
    plane1=cq.Workplane('XY').workplane(offset=fz).center(0,5.9).rect(wlow,sh).val()
    plane2=cq.Workplane('XY').workplane(offset=top+.15).center(0,5.17).rect(fw,sh+(.7 if name=='02_WARM_GENTLE' else .8)).val()
    s=s.cut(cq.Solid.makeLoft([plane1,plane2],ruled=True))
    for x,w,length,offset in windows:
        blade=ze-length;by=5.9+offset
        cuts=[yz_cut([(5.05,blade-.001),(9.5,blade-.001),(9.5,ze+.001),(5.05,ze+.001)],w),
              yz_cut([(by,blade-.002),(8.9,blade-2.6),(10.2,blade-2.6),
                      (10.2,ze+.3),(by,ze+.3)],w),
              yz_cut([(4.9,blade-3.8),(5.45,blade-3.8),
                      (by-tip,blade+.06),(4.9,blade+.06)],w)]
        for cut in cuts:s=s.cut(cut.translate((x,0,0)))
    s=s.cut(rect_cut(30,4,-1,top+1,ycenter=-9.58)).clean()
    assert s.isValid() and len(s.Solids())==1,name
    # Check both jets really reach the window and the shared flute bore.
    xs=[0] if kind=='single' else ([-1.86,1.86] if kind=='twin' else [-1.93,1.93])
    def empty(x,y,z):return not s.isInside(cq.Vector(x,y,z),.0001)
    for x in xs:
        for y,z in [(5.17,top-.5),(5.9,35+ext),(5.9,ze+.12),(6.65,ze-.5)]:
            assert empty(x,y,z),(name,'blocked',x,y,z)
    assert empty(0,0,13),name
    if kind!='single':
        assert not empty(0,5.9,35+ext),(name,'no central duct divider')
        if kind=='double':assert not empty(0,6.65,ze-.5),(name,'windows are not separated')
    # Validate receiving socket identical to confirmed-working v3.
    orig,_=make_head('reference')
    for x,y in [(0,0),(0,6.8),(0,7.5),(6.8,0),(0,-7.3)]:
        assert s.isInside(cq.Vector(x,y,5),.0001)==orig.isInside(cq.Vector(x,y,5),.0001)
    return s

def main():
    report={}
    for spec in V:
        name,kind,sh,sw,wd,off,funnel,chamfer,tip,ext=spec
        h=head(spec)
        print_ready=h.rotate((0,0,0),(1,0,0),90).translate((0,50+ext,7.58))
        fn=DEST/(name+'.stl')
        cq.exporters.export(print_ready,str(fn),exportType='STL',tolerance=.035,angularTolerance=.15)
        mesh=trimesh.load_mesh(str(fn),process=True)
        assert isinstance(mesh,trimesh.Trimesh) and mesh.is_volume and mesh.is_watertight
        assert mesh.is_winding_consistent and len(mesh.split(only_watertight=False))==1
        report[name]=dict(filename=fn.name,kind=kind,slot_height_mm=sh,slot_width_mm=sw,
                          window_length_mm=wd,edge_offset_mm=off,
                          exit_chamfer_mm=chamfer,extra_length_mm=ext,
                          volume_mm3=round(mesh.volume,1),triangles=len(mesh.faces),
                          bounds_mm=mesh.bounds.round(2).tolist(),fit_v3=True,air_channels_open=True)
        print('PASS',fn.name,'tris',len(mesh.faces),flush=True)
    (QA/'alternative_heads.json').write_text(json.dumps(report,indent=2)+'\n')
if __name__=='__main__':main()
