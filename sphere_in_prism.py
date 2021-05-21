def main():
    import numpy
    from meshpy.tet import MeshInfo, build, Options
    from meshpy.geometry import GeometryBuilder, Marker, make_box
    import volume
    import math
    from scipy.spatial import ConvexHull
    import surface_intersection as si
    from intersection import tetrahedral_division
    import sys
    import time
    #mesh generation
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
    #finding intersection points
    surface = si.function
    in_region = []
    in_region_tetr = []
    total = len(mesh.elements)
    start_time = time.time()
    for i in range(total):
        [p1, p2, p3, p4] = mesh.elements[i]
        [pt1, pt2, pt3, pt4] = [mesh.points[p1], mesh.points[p2], mesh.points[p3], mesh.points[p4]]
        sides = tetrahedral_division(pt1, pt2, pt3, pt4)
        print(str(int(100*i/total)) + '%')
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
        for j in sides:
            if si.intersectQ(j[0], j[1], surface) == -1:
                in_region.append(si.intersection_point(j[0],j[1],surface))
                in_region_tetr.append(i)
    print("timing: %s seconds" % (time.time() - start_time))
    #counting number of intersected tetrahedrons
    print(str(len(in_region))+"/"+ str(len(mesh.elements)))
    hull = ConvexHull(numpy.array(in_region))
    # volume, area and sphericity
    print("volume: " + str(hull.volume))
    print("area: " + str(hull.area))
    print("sphericity: " + str(volume.sphericity(hull.area,hull.volume)))
    tot = 0
    d = [0, 0, 0]
    for i in range(len(in_region_tetr)):
        [p1, p2, p3, p4] = mesh.elements[in_region_tetr[i]]
        [pt1, pt2, pt3, pt4] = [mesh.points[p1], mesh.points[p2],mesh.points[p3], mesh.points[p4]]
        for j in range(3):
            d[j] += volume.centre_of_mass(pt1, pt2, pt3, pt4, j)
        tot+= volume.volume(pt1,pt2,pt3,pt4)
    #center of mass
    print("center of mass: " + str(d/tot))
    print("timing: %s seconds" % (time.time() - start_time))


if __name__ == "__main__":
    main()
