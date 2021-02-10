def leng(point1, point2):
    from math import sqrt
    return sqrt((point1[0]-point2[0])**2
                + (point1[1]-point2[1])**2
                + (point1[2]-point2[2])**2)
    
def main():
    import numpy
    from meshpy.tet import MeshInfo, build, Options
    from meshpy.geometry import GeometryBuilder, Marker,make_box,make_ball
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
    mesh.write_vtk("test.vtk")


if __name__ == "__main__":
    main()
