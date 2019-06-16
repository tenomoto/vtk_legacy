import random
from collections import namedtuple
from math import tau, cos, sin, sqrt

Point = namedtuple('Point', ('x', 'y', 'z'))

n = 10000

vp = []
for i in range(n):
    z = random.random() * 2 - 1.0
    s = random.random() * tau
    r = sqrt(1 - z**2)
    x = r * cos(s)
    y = r * sin(s)
    vp.append(Point(x, y, z))

with open('random_sphere.vtk', 'w') as f:
    f.write(f"""\
# vtk DataFile Version 2.0
test
ASCII
DATASET UNSTRUCTURED_GRID
POINTS {n} float
""")
    for v in vp:
        f.write(f"{v.x} {v.y} {v.z}\n")

    f.write(f"POINT_DATA {n}\n")
    f.write("VECTORS vector float\n")
    for v in vp:
        f.write(f"{v.y} {-v.x} {0}\n")
    
    f.write("SCALARS z float\n")
    f.write("LOOKUP_TABLE default")
    for v in vp:
        f.write(f"{v.z}\n")
