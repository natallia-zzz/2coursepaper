def main():
    from meshpy.tet import MeshInfo, build
    from meshpy.geometry import GeometryBuilder
    geom = GeometryBuilder();
    # geom.add_geometry(points())
    mesh_info = MeshInfo()
    #geom.set(mesh_info)
    mesh_info.set_points(
        [
            (0, 0, 0),
            (1, 0, 0),
            (1, 1, 0),
            (0, 1, 0),
            (0, 0, 2),
            (1, 0, 2),
            (1, 1, 2),
            (0, 1, 2),
        ]
    )

    mesh_info.set_facets(
        [
            [0, 1, 2, 3],
            [4, 5, 6, 7],
            [0, 4, 5, 1],
            [1, 5, 6, 2],
            [2, 6, 7, 3],
            [3, 7, 4, 0],
        ]
    )

    mesh_info.save_nodes("bar")
    mesh_info.save_poly("bar")

    mesh = build(mesh_info)

    mesh.save_nodes("barout")
    mesh.save_elements("barout")
    mesh.save_faces("barout")

    mesh.write_vtk("test.vtk")


if __name__ == "__main__":
    main()
