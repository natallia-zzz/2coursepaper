def main():
    from boundary import leng
    import numpy
    from meshpy.tet import MeshInfo, build, Options
    from meshpy.geometry import GeometryBuilder, Marker, make_box, make_ball
    import volume
    import math
    from scipy.spatial import ConvexHull
    import surface_intersection as si
    from intersection import tetrahedral_division
    import sys

    geom = GeometryBuilder()
    box_marker = Marker.FIRST_USER_MARKER
    points, facets, _, facet_markers = make_box(
        numpy.array([0, 0, 0]), numpy.array([1, 1, 2])
    )
    geom.add_geometry(points, facets, facet_markers=box_marker)
    mesh_info = MeshInfo()
    geom.set(mesh_info)
    mesh_info.regions.resize(1)
    mesh_info.regions[0] = ([0, 0, 0] + [1, 0.001, ])
    mesh = build(mesh_info, max_volume=0.01,
                 volume_constraints=True, attributes=True)

    surface = si.sphere
    in_circle = []
    in_sphere = []
    total = len(mesh.elements)
    for i in range(total):
        [p1, p2, p3, p4] = mesh.elements[i]
        [pt1, pt2, pt3, pt4] = [mesh.points[p1], mesh.points[p2], mesh.points[p3], mesh.points[p4]]
        sides = tetrahedral_division(pt1, pt2, pt3, pt4)
        print(str(int(100*i/total)) + '%')
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
        for j in sides:
            if si.intersectQ(j[0], j[1], surface) == -1:
                in_circle.append(si.intersection_point(j[0],j[1],surface))
                in_sphere.append(i)
    print(str(len(in_circle))+"/"+ str(len(mesh.elements)))
    hull = ConvexHull(numpy.array(in_circle))
    print("volume: " + str(hull.volume))
    print("sphericity: " + str(volume.sphericity(hull.area,hull.volume)))
    tot = 0
    d = [0, 0, 0]
    for i in range(len(in_sphere)):
        [p1, p2, p3, p4] = mesh.elements[in_sphere[i]]
        [pt1, pt2, pt3, pt4] = [mesh.points[p1], mesh.points[p2], mesh.points[p3], mesh.points[p4]]
        for j in range(3):
            d[j] += volume.centre_of_mass(pt1, pt2, pt3, pt4, j)
        tot+= volume.volume(pt1,pt2,pt3,pt4)

    print("center of mass: " + str(d/tot))


if __name__ == "__main__":
    main()
