def leng(point1, point2):
    from math import sqrt
    return sqrt((point1[0]-point2[0])**2
                + (point1[1]-point2[1])**2
                + (point1[2]-point2[2])**2)


def max_index(pts):
    n = 0
    index = 0
    for i in range(len(pts)):
        if pts[i] > n:
            n = pts[i]
            index = i
    return index


def find_minimum(points, indexes):
    n = 10
    index = 0
    for i in range(len(indexes)):
        if points[indexes[i]][0] < n:
            n = points[indexes[i]][0]
            index = indexes[i]
    return index


def find_next(points, elems,ind):
    newelems =[]
    for i in range(len(elems)):
        if ind in elems[i]:
            newelems.append(i)
    newpoints = []
    for i in range(len(newelems)):
        for j in range(4):
            if elems[newelems[i]][j] != ind:
                newpoints.append(elems[newelems[i]][j])
    lenarray = [leng(points[newpoints[i]],[1/2,1/2,1/2]) for i in range(len(newpoints))]
    i1 = max_index(lenarray)
    return newpoints[i1]




# def find_boundary(points, facets):

