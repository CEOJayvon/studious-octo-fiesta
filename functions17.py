import math
def areaTriangle(a,b):
    k = .5 * (a*b)
    return round(k,2)

def areaRectangle(c,d):
    h = c*d
    return round(h,2)

def areaCircle(f):
    j = math.pi*f**2
    return round(j,2)
