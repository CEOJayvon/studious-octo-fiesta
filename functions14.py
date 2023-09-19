import math
def hypotenuse(a,b):
    a = a**2
    b = b**2
    c = math.sqrt(a+b)
    return round(c,2)

def main():
    a = float(input("Enter side 1:"))
    b = float(input("Enter side 2:"))
    print("The hypotenuse is:", hypotenuse(a,b))
if __name__=="__main__":
    main()
