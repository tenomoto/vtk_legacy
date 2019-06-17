from math import sqrt, exp
grid = 50
dim = grid * 2 + 1
points = dim ** 2

ep = 5

with open(f'ga_ep{ep}.vtk', 'w') as f:
    f.write(f"""\
# vtk DataFile Version 1.0
test
ASCII
DATASET STRUCTURED_GRID
DIMENSIONS {dim} {dim} 1
POINTS {points} float
"""
    )

    for j in range(-grid, grid+1):
        for i in range(-grid, grid+1):
            x = i / grid
            y = j / grid
            r = sqrt(x*x + y*y)
            z = exp(-(ep * r**2))
            f.write(f"{x} {y} {z}\n")
