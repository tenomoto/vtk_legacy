from math import exp

def export_vtk(filename, p):
    print(filename)
    grid = 10
    dim = grid*2 + 1
    points = dim**3
    with open(filename, 'w') as f:
        f.write(f"""\
# vtk DataFile Version 1.0
Wave function
ASCII
DATASET STRUCTURED_POINTS
DIMENSIONS {dim} {dim} {dim}
ORIGIN 0.0 0.0 0.0
SPACING 1.0 1.0 1.0
POINT_DATA {points}
SCALARS scalars float
LOOKUP_TABLE default\n""")
        for k in range(-grid, grid+1):
            for j in range(-grid, grid+1):
                for i in range(-grid, grid+1):
                    x = i / grid
                    y = j / grid
                    z = k / grid
                    r = (x*x + y*y + z*z) ** 0.5
                    f.write(f"{p(x, y, z, r)}\n")


p_2pz = lambda x, y, z, r: exp(-r * 3.0) * (z)
p_3dz2 = lambda x, y, z, r: exp(-r * 4.0) * (3 * z**2 - r**2)
p_3dzx = lambda x, y, z, r: exp(-r*4.0) * (z * x)

export_vtk("2pz.vtk", p_2pz)
export_vtk("3dz.vtk", p_3dz2)
export_vtk("3dzx.vtk", p_3dzx)