#!/usr/bin/env python3
"""Experimental multi-labium circular whistle heads for working Picard v3.
Five acoustic trials: 2/3/4/6 circumferential labia, plus dominant+satellites.
These are flue air jets and stationary sounding edges, not vibrating reeds.
All dimensions in mm. Acoustic functionality requires print and playing tests.
"""
from pathlib import Path
import math, json, sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/"CAD"))
import cadquery as cq
import trimesh
from build_flute import cylinder,conic,rect_cut,yz_cut,R_OUT,R_BORE,R_SOCKET,make_head

ROOT=Path(__file__).resolve().parents[1]
STL=ROOT/'STL';STL.mkdir(exist_ok=True)
QA=ROOT/'QA';QA.mkdir(exist_ok=True)
Z_EXIT=25.0
TOP=52.0
R_JET=6.03
PLENUM_RADIUS=6.20

# (angle in degrees, tangential jet width, radial jet thickness,
#  jet to labium length, radial labium offset, tip thickness)
HEADS={
 '01_RADIAL_2_OPPOSED':[
    (0,4.60,1.05,4.10,0.00,.28),(180,3.60,.85,4.22,.04,.30)],
 '02_RADIAL_3_STAGGERED':[
    (0,4.75,1.01,4.05,0.00,.28),
    (120,2.80,.80,3.62,.14,.28),
    (240,2.55,.88,4.52,-.10,.28)],
 '03_RADIAL_4_ALTERNATING':[
    (0,3.00,.92,4.10,0.00,.28),
    (90,2.55,.77,3.51,.12,.27),
    (180,2.85,.92,4.68,-.08,.28),
    (270,2.45,.86,3.82,.03,.27)],
 '04_RADIAL_6_MICRO':[
    (0,1.95,.75,4.00,0.00,.28),
    (60,1.90,.73,3.53,.11,.28),
    (120,2.00,.80,4.44,-.10,.28),
    (180,1.95,.75,4.10,.03,.28),
    (240,1.85,.78,3.70,.12,.28),
    (300,2.00,.76,4.50,-.09,.28)],
 '05_RADIAL_3_PRIMARY_PLUS_SATELLITES':[
    (0,6.00,1.00,4.10,0.00,.27),
    (128,2.00,.73,3.73,.14,.28),
    (232,2.00,.75,4.60,-.12,.28)],
}

def radial_cut(shape,angle,sx,sy,z0,z1,y0=R_JET):
    void=rect_cut(sx,sy,z0,z1,ycenter=y0)
    return shape.cut(void.rotate((0,0,0),(0,0,1),angle))

def polygon_cut(shape,angle,vertices,width):
    void=yz_cut(vertices,width).rotate((0,0,0),(0,0,1),angle)
    return shape.cut(void)

def mouthpiece(config):
    """Circular, one-piece mouthpiece with shared inlet and separate jets."""
    obj=cylinder(R_OUT,0,TOP)
    # Same v3 receiving socket; keep the already-working flute body unchanged.
    socket=cylinder(R_SOCKET,0.35,10.9).fuse(conic(R_SOCKET+.20,R_SOCKET,0,.35))
    obj=obj.cut(socket)
    obj=obj.cut(cylinder(R_BORE,10.9,Z_EXIT-10.9+.05))

    # Mouth inlet above solid central baffle; only wall jets meet sounding bore.
    obj=obj.cut(cylinder(PLENUM_RADIUS,41.0,11.5))
    obj=obj.cut(conic(PLENUM_RADIUS,6.42,TOP-1.5,TOP+.05))
    for angle,width,height,gap,edge_offset,tip_thickness in config:
        blade_z=Z_EXIT-gap
        blade_r=R_JET+edge_offset
        obj=radial_cut(obj,angle,width,height,Z_EXIT-.055,44.5)
        window_width=width+.30
        # Opening connects the jet to outside air and the existing tube bore.
        obj=polygon_cut(obj,angle,
                        [(5.04,blade_z-.003),(9.50,blade_z-.003),
                         (9.50,Z_EXIT+.003),(5.04,Z_EXIT+.003)],
                        window_width)
        # Outward-facing bevel producing the labium, as in the v3 whistle head.
        obj=polygon_cut(obj,angle,
                        [(blade_r,blade_z-.004),(8.85,blade_z-2.6),
                         (10.10,blade_z-2.6),(10.10,Z_EXIT+.28),
                         (blade_r,Z_EXIT+.28)],window_width)
        # Inward relief leaving a slim-but-printable labium tip.
        obj=polygon_cut(obj,angle,
                        [(4.85,blade_z-3.6),(5.45,blade_z-3.6),
                         (blade_r-tip_thickness,blade_z+.08),
                         (4.85,blade_z+.08)],window_width)
    return obj.clean()

def is_air(shape,x,y,z):
    return not shape.isInside(cq.Vector(x,y,z),.00005)

def check_geometry(body,name,specs):
    assert body.isValid() and len(body.Solids())==1,(name,"invalid solid")
    ref=make_head('v3_reference')
    if isinstance(ref,tuple): ref=ref[0]
    # Compare original v3 socket material/void classifications at 300 points.
    for z in (.2,2,5,9,10.7):
        for deg in range(0,360,30):
            for radius in (5.3,6.4,6.79,6.87,7.0):
                x=radius*math.cos(math.radians(deg))
                y=radius*math.sin(math.radians(deg))
                assert body.isInside(cq.Vector(x,y,z),.00005)==ref.isInside(cq.Vector(x,y,z),.00005),(name,'socket misfit')
    assert is_air(body,0,0,TOP-.5)
    assert not is_air(body,0,0,35)
    assert is_air(body,0,0,17)
    for angle,width,height,gap,edge_offset,tip_thickness in specs:
        t=math.radians(angle)
        x=-R_JET*math.sin(t)
        y= R_JET*math.cos(t)
        for z in (Z_EXIT+.25,32,41,43.1):
            assert is_air(body,x,y,z),(name,'blocked windway',angle,z)
        blade_z=Z_EXIT-gap
        for z in (blade_z+.4,blade_z+gap*.75):
            x1=-7.9*math.sin(t);y1=7.9*math.cos(t)
            assert is_air(body,x1,y1,z),(name,'blocked labium window',angle,z)

def main():
    audit={}
    for name,specs in HEADS.items():
        body=mouthpiece(specs)
        check_geometry(body,name,specs)
        path=STL/(name+".stl")
        cq.exporters.export(body,str(path),exportType="STL",tolerance=.035,angularTolerance=.15)
        mesh=trimesh.load_mesh(str(path),process=True)
        assert isinstance(mesh,trimesh.Trimesh) and mesh.is_volume and mesh.is_watertight
        assert mesh.is_winding_consistent and len(mesh.split(only_watertight=False))==1
        audit[name]={"number_of_labia":len(specs),"file":path.name,
                     "bytes":path.stat().st_size,"triangles":len(mesh.faces),
                     "volume_mm3":round(mesh.volume,1),
                     "bounds_mm":mesh.bounds.round(2).tolist(),
                     "matches_original_v3_joint":True,"passages_open":True,
                     "physically_sound_tested":False,
                     "design":[{"angle_deg":a,"windway_width_mm":w,"windway_height_mm":h,
                                "jet_to_labium_mm":g,"edge_offset_mm":off,
                                "blade_tip_mm":th} for a,w,h,g,off,th in specs]}
        print("PASS",name,len(specs),"labia",flush=True)
    (QA/"mesh_validation.json").write_text(json.dumps(audit,indent=2)+"\n")

if __name__=="__main__":main()
