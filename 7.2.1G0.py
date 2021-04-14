def main():
    import numpy
    from meshpy.tet import MeshInfo, build, Options
    from meshpy.geometry import GeometryBuilder, Marker,make_box,make_ball
    from volume import volume
    geom = GeometryBuilder();
    box_marker = Marker.FIRST_USER_MARKER
    points, facets, _, _ = make_ball(r = 0.25)
    for i in range(len(points)):
        a = [0,0,0]
        a = numpy.array(points[i]) + numpy.array([0.5,0.5,0.5])
        points[i] = tuple(a)

    geom.add_geometry(points, facets, facet_markers=box_marker)
    mesh_info = MeshInfo()
    geom.set(mesh_info)
    mesh = build(mesh_info, max_volume=0.01,
                 volume_constraints=True, attributes=True)
    mesh.element_volumes.setup()
    total = 0
    for i in range(len(mesh.elements)):
        # print(mesh.element_volumes[i])
        total+=mesh.element_volumes[i]
    print(total)
    tot = 0;
    for i in range(len(mesh.elements)):
        [p1,p2,p3,p4] = mesh.elements[i]
        [pt1,pt2,pt3,pt4] = [mesh.points[p1],mesh.points[p2],mesh.points[p3],mesh.points[p4]]
        tot += volume(pt1,pt2,pt3,pt4)
    print(tot)
    #mesh.write_vtk("G0.vtk")
    

if __name__ == "__main__":
    main()
