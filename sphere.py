grid = 10
dim = grid * 2 + 1
points = dim ** 3

r = 0.8

with open('sphere.vtk', 'w') as f:
    f.write(f"""\
# vtk DataFile Version 1.0
test
ASCII
DATASET STRUCTURED_POINTS
DIMENSIONS {dim} {dim} {dim}
ORIGIN 0.0 0.0 0.0
SPACING 1.0 1.0 1.0
POINT_DATA {points}
SCALARS intensity float
LOOKUP_TABLE default\n"""
    )

    for k in range(-grid, grid+1):
        for j in range(-grid, grid+1):
            for i in range(-grid, grid+1):
                x = i / grid
                y = j / grid
                z = k / grid
                v = r*r - (x*x + y*y + z*z)
                v = 0 if v < 0 else v
                f.write(f"{v}\n")
