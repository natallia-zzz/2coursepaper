# surface
def function(x,y,z):
    return (x-0.5)**2 + (y-0.5)**2 + (z-0.5)**2 - 1/16


def main():
    import numpy
    from meshpy.tet import MeshInfo, build, Options
    from meshpy.geometry import GeometryBuilder, Marker, make_box, make_ball
    import volume
    import math
    import time
    # mesh generation
    start_time = time.time()
    geom = GeometryBuilder();
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

    in_region = []
    for i in range(len(mesh.elements)):
        [p1, p2, p3, p4] = mesh.elements[i]
        [pt1, pt2, pt3, pt4] = [mesh.points[p1], mesh.points[p2], mesh.points[p3], mesh.points[p4]]
        # selection of inside tetrahedra
        # if (function(pt1[0],pt1[1],pt1[2]) <= 0
        #         and function(pt2[0],pt2[1],pt2[2]) <= 0 and function(pt3[0],pt3[1],pt3[2]) <= 0
        #         and function(pt4[0],pt4[1],pt4[2] <= 0)):
        #     in_region.append(i)
        # selection of inside and intersecting tetrahedra
        if (function(pt1[0], pt1[1], pt1[2]) <= 0
                or function(pt2[0], pt2[1], pt2[2]) <= 0 or function(pt3[0], pt3[1], pt3[2]) <= 0
                or function(pt4[0], pt4[1], pt4[2] <= 0)):
            in_region.append(i)
    print(str(len(in_region)/len(mesh.elements)))
    tot = 0
    # volume
    for i in range(len(in_region)):
        [p1, p2, p3, p4] = mesh.elements[in_region[i]]
        [pt1, pt2, pt3, pt4] = [mesh.points[p1], mesh.points[p2], mesh.points[p3], mesh.points[p4]]
        tot += volume.volume(pt1, pt2, pt3, pt4)
    print("volume: " + str(tot))
    # center of mass
    d = [0, 0, 0]
    for i in range(len(in_region)):
        [p1, p2, p3, p4] = mesh.elements[in_region[i]]
        [pt1, pt2, pt3, pt4] = [mesh.points[p1], mesh.points[p2], mesh.points[p3], mesh.points[p4]]
        for j in range(3):
            d[j] += volume.centre_of_mass(pt1, pt2, pt3, pt4, j)
    print("center of mass: " + str(d / tot))
    # surface area for sphericity is counted by formula for a sphere
    print("sphericity: " + str(volume.sphericity(math.pi*0.25,tot)))
    print("timing: %s seconds" % (time.time() - start_time))
    

if __name__ == "__main__":
    main()
