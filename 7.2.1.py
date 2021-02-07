def points():
    ex = []
    for x in [0,1]:
        for y in [0,1]:
            for z in [0,2]:
                ex += [(x,y,z)]
    return ex


def main():
    from meshpy.tet import MeshInfo, build
    from meshpy.geometry import GeometryBuilder
    geom = GeometryBuilder();
    geom.add_geometry(points())
    mesh_info = MeshInfo()
    geom.set(mesh_info)

    mesh = build(mesh_info)
    mesh.write_vtk("test.vtk")


if __name__ == "__main__":
    main()
