def taxiFare(a,b,c):
    totalFare = a+b*c
    return round(totalFare,2)
def main():
    a = float(input("Enter base rate:"))
    b = float(input("Enter cost per mile:"))
    c = float(input("Enter nymber of miles traveled:"))
    print("Your fare is:", taxiFare(a,b,c))
if __name__ =="__main__":
    main()
