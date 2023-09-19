def costTaffy(t):
    x = round(t * 5.99,2)
    return x

def costFudge(f):
    y = round(f * 9.99,2)
    return y

def costPraline(p):
    z = round(p * 8.99,2)
    return z

def main():
    a = float(input("Enter weight of taffy in pounds:"))
    b = float(input("Enter weight of fudge in pounds:"))
    c = float(input("Enter weight of praline in pounds:"))
    n = costTaffy(x) + costFudge(y) + costPraline(z)
    print("Your total is:",round(n,2))
if __name__ == "__main__":
    main()


