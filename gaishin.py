import numpy as np

def gai(x, y, z):

    ra = np.array(x)
    rb = np.array(y)
    rc = np.array(z)

    A = np.dot(rb-rc,rb-rc)
    B = np.dot(rc-ra,rc-ra)
    C = np.dot(ra-rb,ra-rb)

    T = A*(B+C-A)
    U = B*(C+A-B)
    W = C*(A+B-C)

    rcc = (T*ra + U*rb + W*rc)/(T + U + W)

    return rcc