# def intersection(tetr,line):
#     a = 0
#     for i in tetr:
#         p = i[0]*line[0] + i[1]*line[1] + i[2]*line[2] + line[3]
#         a += p/abs(p)
#     if abs(a)==4: return True
#     return False

def intersectQ(p1, p2, line):
    a = p1[0] * line[0] + p1[1] * line[1] + p1[2] * line[2] + line[3]
    b = p2[0] * line[0] + p2[1] * line[1] + p2[2] * line[2] + line[3]
    if a * b == 0:
        return 0
    return a * b / abs(a * b)


def intersection_point(p1, p2, line):
    t = -(line[0] * p1[0] + line[1] * p1[1] + line[2] * p1[2] + line[3]) / (
                p2[0] + p2[1] + p2[2] - p1[0] - p1[1] - p1[2])
    x = (p2[0] - p1[0]) * t - p1[0]
    y = (p2[1] - p1[1]) * t - p1[1]
    z = (p2[2] - p1[2]) * t - p1[2]
    return [x, y, z]


def tetrahedral_division(p1, p2, p3, p4):
    return [[p1, p2], [p1, p3], [p1, p4], [p2, p3], [p2, p4], [p3, p4]]


def main():
    p1 = [0, 0, 0]
    p2 = [2, 0, 0]
    p3 = [0, 2, 0]
    p4 = [0, 0, 2]
    line = [1, 1, 1, -1]
    sides = tetrahedral_division(p1, p2, p3, p4)
    a = []
    for i in sides:
        if intersectQ(i[0], i[1], line) == -1:
            a.append(intersection_point(i[0], i[1], line))
    print(a)


if __name__ == "__main__":
    main()
