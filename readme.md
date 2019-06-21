# VTK Legacy format

Python translations of the Ruby scripts in the following article (in Japanese)
* [Use VTK legacy format in Paraview Part 1](https://qiita.com/kaityo256/items/661833e9e2bfbac31d4b)
* [Use VTK legacy format in Paraview Part 2](https://qiita.com/kaityo256/items/851c559a8f4c43de329e)

In addition Voronoi cells are generated from random points on the sphere uwith the aid of `scipy.spatial.SphericalVoronoi`.
Note that `size` parameter in `CELLS` are the sum of the vertices of each cell plus the connection point i.e. add one for each cell. Otherwise ParaView terminates without error.

![random_sphere_cell.png]
