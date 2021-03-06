def analysis(radius, scalar, center, n):
    import numpy
    from meshpy.tet import MeshInfo, build, Options
    from meshpy.geometry import GeometryBuilder, Marker, make_box, make_ball
    import volume
    geom = GeometryBuilder()
    box_marker = Marker.FIRST_USER_MARKER
    points, facets, _, _ = make_ball(r=radius)
    for i in range(len(points)):
        a = numpy.array(points[i])
        a[2] *= scalar
        a += numpy.array(center)
        points[i] = tuple(a)
    area = 0
    for i in range(len(facets)):
        if len(facets[i][0]) == 4:
            [[p1, p2, p3, p4]] = facets[i]
            [pt1, pt2, pt3, pt4] = [points[p1], points[p2], points[p3], points[p4]]
            area += volume.area_of_quadrelateral(pt1, pt2, pt3, pt4)
        elif len(facets[i][0]) == 3:
            [[p1, p2, p3]] = facets[i]
            [pt1, pt2, pt3] = [points[p1], points[p2], points[p3]]
            area += volume.area_of_triangle(pt1, pt2, pt3)
    print("area: " + str(area))
    geom.add_geometry(points, facets, facet_markers=box_marker)
    mesh_info = MeshInfo()
    geom.set(mesh_info)
    mesh = build(mesh_info, max_volume=0.01,
                 volume_constraints=True, attributes=True)
    mesh.element_volumes.setup()
    # volume count
    tot = 0
    for i in range(len(mesh.elements)):
        [p1, p2, p3, p4] = mesh.elements[i]
        [pt1, pt2, pt3, pt4] = [mesh.points[p1], mesh.points[p2], mesh.points[p3], mesh.points[p4]]
        tot += volume.volume(pt1, pt2, pt3, pt4)
    print("volume: " + str(tot))
    #center of mass count
    d = [0, 0, 0]
    for i in range(len(mesh.elements)):
        [p1, p2, p3, p4] = mesh.elements[i]
        [pt1, pt2, pt3, pt4] = [mesh.points[p1], mesh.points[p2], mesh.points[p3], mesh.points[p4]]
        for j in range(3):
            d[j] += volume.centre_of_mass(pt1, pt2, pt3, pt4, j)

    print("center of mass: " + str(d / tot))
    #sphericity count
    print("spherical: " + str(volume.sphericity(area, tot)))
    # file write
    # mesh.write_vtk("G"+str(n)+".vtk")


def main():
    a = []
    for i in range(10):
        a.append(1/(i+1))
    for i in range(len(a)):
        print("ellipse"+str(i+1))
        analysis(1,a[i],[0,0,0], i+1)
        print("====================")
        

if __name__ == "__main__":
    main()
