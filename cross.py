def cross(a, b, c, d):
    s = a - b
    t = c - d
    ab = numpy.cross(a, b)
    cd = numpy.cross(c, d)
    st = numpy.cross(s, t)
    if st == 0:
        return None
    x = (t[0] * ab - s[0] * cd) / st
    y = (t[1] * ab - s[1] * cd) / st
    return numpy.array([x, y])

def inside(a, b, x):
    if numpy.dot(a-x, b-x) <= 0:
        return True
    else: return False

def cross_inside(a, b, c, d):
    x = cross(a, b, c, d)
    if x is not None:
        if inside(a, b, x) and inside(c, d, x): return True
    return False