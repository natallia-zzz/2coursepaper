def main():
    import numpy
    from meshpy.tet import MeshInfo, build, Options
    from meshpy.geometry import GeometryBuilder, Marker,make_box,make_ball
    geom = GeometryBuilder();
    box_marker = Marker.FIRST_USER_MARKER
    points, facets, _, _ = make_ball(r = 0.5)
    for i in range(len(points)):
        a = [0,0,0]
        a = numpy.array(points[i]) + numpy.array([0.5,0.5,0.5])
        points[i] = tuple(a)
    geom.add_geometry(points, facets, facet_markers=box_marker)
    mesh_info = MeshInfo()
    geom.set(mesh_info)
    mesh_info.regions.resize(1)
    mesh_info.regions[0] = ([0, 0, 0] + [1,0.001,])
    mesh = build(mesh_info)
    mesh.write_vtk("G0.vtk")


if __name__ == "__main__":
    main()
