from math import tau
import numpy as np
from numpy import cos, sin, sqrt
from numpy.random import random
from scipy.spatial import SphericalVoronoi

n = 10000

z = random(n) * 2 - 1.0
s = random(n) * tau
r = sqrt(1 - z**2)
x = r * cos(s)
y = r * sin(s)
vp = np.column_stack((x, y, z))

centre = np.array([0.0, 0.0, 0.0])
radius = 1
sv = SphericalVoronoi(vp, radius, centre)
n_vertex = len(sv.vertices)
sv.sort_vertices_of_regions()
# sum of the number of vertices of each cell plus the connection
n_size = sum([len(c) + 1 for c in sv.regions])

with open('random_sphere_cell.vtk', 'w') as f:
    f.write(f"""\
# vtk DataFile Version 2.0
test
ASCII
DATASET UNSTRUCTURED_GRID
POINTS {n_vertex} float
""")
    for p in sv.vertices:
        f.write("%f %f %f\n" % tuple(p.tolist()))
    f.write(f"CELLS {n} {n_size}\n") 
    for c in sv.regions:
        f.write(f"{len(c)} ")
        f.write(' '.join(map(str, c)))
        f.write('\n')
    f.write(f"CELL_TYPES {n}\n")
    f.write('\n'.join(['7'] * n))
    f.write('\n')

    f.write(f"CELL_DATA {n}\n")
    f.write("VECTORS vector float\n")
    for v in vp:
        f.write(f"{v[1]} {-v[0]} 0\n")
    
    f.write("SCALARS z float\n")
    f.write("LOOKUP_TABLE default\n")
    for v in vp:
        f.write(f"{v[2]}\n")
