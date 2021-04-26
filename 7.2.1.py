def leng(point1, point2):
    from math import sqrt
    return sqrt((point1[0]-point2[0])**2
                + (point1[1]-point2[1])**2
                + (point1[2]-point2[2])**2)
    
def main():
    import numpy
    from meshpy.tet import MeshInfo, build, Options
    from meshpy.geometry import GeometryBuilder, Marker,make_box,make_ball
    import volume
    geom = GeometryBuilder();
    box_marker = Marker.FIRST_USER_MARKER
    points, facets, _, facet_markers = make_box(
        numpy.array([0,0,0]), numpy.array([1, 1, 2])
    )
    geom.add_geometry(points, facets, facet_markers=box_marker)
    mesh_info = MeshInfo()
    geom.set(mesh_info)
    mesh_info.regions.resize(1)
    mesh_info.regions[0] = ([0, 0, 0] + [1,0.001,])
    mesh = build(mesh_info, max_volume=0.01,
                 volume_constraints=True, attributes=True)

    in_circle = []
    for i in range(len(mesh.elements)):
        [p1,p2,p3,p4] = mesh.elements[i]
        [pt1,pt2,pt3,pt4] = [mesh.points[p1],mesh.points[p2],mesh.points[p3],mesh.points[p4]]
        if(leng(pt1,[1/2,1/2,1/2]) <= 1/4 and leng(pt2,[1/2,1/2,1/2]) <= 1/4 and leng(pt3,[1/2,1/2,1/2]) <= 1/4 and leng(pt4,[1/2,1/2,1/2]) <= 1/4):
            in_circle.append(i)

    print(len(in_circle))

    tot = 0;
    for i in range(len(in_circle)):
        [p1,p2,p3,p4] = mesh.elements[in_circle[i]]
        [pt1,pt2,pt3,pt4] = [mesh.points[p1],mesh.points[p2],mesh.points[p3],mesh.points[p4]]
        tot += volume.volume(pt1,pt2,pt3,pt4)
    print("volume: " +  str(tot))
    d = [0,0,0]
    for i in range(len(in_circle)):
        [p1,p2,p3,p4] = mesh.elements[in_circle[i]]
        [pt1,pt2,pt3,pt4] = [mesh.points[p1],mesh.points[p2],mesh.points[p3],mesh.points[p4]]
        for i in range(3):
            d[i]+= volume.centre_of_mass(pt1,pt2,pt3,pt4,i)

    print("center of mass: " + str(d/tot))
    
    #mesh.write_vtk("test.vtk")


if __name__ == "__main__":
    main()
