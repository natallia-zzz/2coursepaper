# объем
def volume(a,b,c,d):
    import numpy as np
    ab = np.array(b) - np.array(a)
    ac = np.array(c) - np.array(a)
    ad = np.array(d) - np.array(a)
    return 1/6 *np.linalg.det(np.matrix([ab,ac,ad]))


#составляющая центра масс для одного тетраэдра
def centre_of_mass(a,b,c,d, i):
    return 0.25*(a[i]+b[i]+c[i]+d[i])*volume(a,b,c,d)


# площадь треугольника   
def area_of_triangle(a,b,c):
    import numpy as np
    ab = np.array(b) - np.array(a)
    ac = np.array(c) - np.array(a)
    return 0.5*np.dot(ab,ac)

# площадь четырехугольника
def area_of_quadrelateral(a,b,c,d):
    return area_of_triangle(a,b,c) + area_of_triangle(a,c,d)


# сферичностьз
def sphericity(area, volume):
    import math
    return (math.pi**(1/3)) *((6*volume)**(2/3))/area
    
