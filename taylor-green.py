from collections import namedtuple
from math import tau, sin, cos, atan2

grid = 21
c = grid / 2
points = grid**3

Velocity = namedtuple('Velocity', ('x', 'y', 'z'))

velocity = []
for k in range(grid):
    for j in range(grid):
        for i in range(grid):
            x = (i / grid + 0.25) * tau 
            y = (j / grid + 0.25) * tau
            z = (k / grid + 0.25) * tau 
            u = cos(x) * sin(y) * cos(z)
            v = -sin(x) * cos(y) * cos(z)
            w = 0.0
            velocity.append(Velocity(u, v, w))

with open('taylor-green.vtk', 'w') as f:
    f.write(f"""\
# vtk DataFile Version 2.0
test
ASCII
DATASET STRUCTURED_POINTS
DIMENSIONS {grid} {grid} {grid}
ORIGIN 0.0 0.0 0.0
SPACING 1.0 1.0 1.0

POINT_DATA {points}
VECTORS velocity float
""")
    for v in velocity:
        f.write(f"{v.x} {v.y} {v.z}\n")

    f.write("SCALARS angle float\n")
    f.write("LOOKUP_TABLE default\n")
    
    for v in velocity:
        f.write("%f\n" % atan2(v.y, v.x))