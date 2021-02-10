
def main():
    import numpy
    from meshpy.tet import MeshInfo, build, Options
    from meshpy.geometry import GeometryBuilder, Marker,make_box
    geom = GeometryBuilder();
    points, facets, _, facet_markers = make_box(
        numpy.array([0,0,0]), numpy.array([1, 1, 2])
    )
    box_marker = Marker.FIRST_USER_MARKER
    geom.add_geometry(points, facets, facet_markers=box_marker)
    mesh_info = MeshInfo()
    geom.set(mesh_info)
    mesh_info.regions.resize(1)
    mesh_info.regions[0] = ([0, 0, 0] + [1,0.001,])
    mesh = build(mesh_info, max_volume=0.01,
            volume_constraints=True, attributes=True,options = Options('pq1.4'))
    mesh.write_vtk("test.vtk")


if __name__ == "__main__":
    main()
