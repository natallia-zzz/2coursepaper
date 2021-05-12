def intersectQ(p1,p2,surface):
    a = surface(p1[0], p1[1],p1[2])
    b = surface(p2[0], p2[1], p2[2])
    if a * b == 0:
        return 0
    return a * b / abs(a * b)

def intersection_point(p1,p2,surface):
    from sympy import symbols, solve
    import numpy as np
    t = symbols('t')
    x = (p2[0] - p1[0]) * t + p1[0]
    y = (p2[1] - p1[1]) * t + p1[1]
    z = (p2[2] - p1[2]) * t + p1[2]
    sol = solve(surface(x,y,z))
    for i in sol:
        x = (p2[0] - p1[0]) * i + p1[0]
        y = (p2[1] - p1[1]) * i + p1[1]
        z = (p2[2] - p1[2]) * i + p1[2]
        if np.dot(np.array(p2) - np.array([x,y,z]),np.array([x,y,z]) - np.array(p1)) > 0:
            return [x,y,z]
        

def sphere(x,y,z):
    return (x-0.5)**2 + (y-0.5)**2 + (z-0.5)**2 - 1/16
    

def main():
    from intersection import tetrahedral_division
    p1 = [0, 0, 0]
    p2 = [2, 0, 0]
    p3 = [0, 2, 0]
    p4 = [0, 0, 2]
    surface = sphere
    sides = tetrahedral_division(p1, p2, p3, p4)
    a = []
    for i in sides:
        if intersectQ(i[0], i[1], surface) == -1:
            print(intersection_point(i[0],i[1],surface))


if __name__ == "__main__":
    main()
