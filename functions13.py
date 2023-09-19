import math
def hypotenuse(a,b):
    a = a**2
    b = b**2
    c = math.sqrt(a+b)
    return round(c,2)
print(hypotenuse(10,14))
