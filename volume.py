def volume(a,b,c,d):
    import numpy as np
    ab = np.array(b) - np.array(a)
    ac = np.array(c) - np.array(a)
    ad = np.array(d) - np.array(a)
    return 1/6 *np.linalg.det(np.matrix([ab,ac,ad]))
