print("""Welcome to the CSU Taco Shop
Menu:
Barbeque beef taco       $2.90
Shimp and grits taco     $3.00
Cajun fish taco          $3.25
Chicken guacamole taco   $2.75
Caramelized onion lentil taco $2.50""")
def beef_taco(a):
    a = round(a*2.90,2)
    return a
def shrimp_taco(b):
    b = round(b*3.00,2)
    return b
def fish_taco(c):
    c = round(c*3.25,2)
    return c
def chicken_taco(d):
    d = round(d*2.75,2)
    return d
def lentil_taco(e):
    e = round(e*2.50,2)
    return e

def main():
    a =float(input("How many barbeque beef tacos would you like?"))
    b =float(input("How many shrimp and grits tacos would you like?"))
    c =float(input("How many cajun fish tacos would you like?"))
    d =float(input("How many chicken guacamole tacos would you like?"))
    e =float(input("How many caramelized onion tacos would you like?"))

    print("Your order is:")
    print(a,"Barbeque beef tacos")
    print(b,"Shrimp and grits tacos")
    print(c,"Cajun fish tacos")
    print(d,"Chicken guacamole tacos")
    print(e,"Caramelized onion lentil tacos")
    bTax = beef_taco(a) + shrimp_taco(b) + fish_taco(c) + chicken_taco(d) + lentil_taco(e)
    aTax = round(1.08 * bTax,2)
    print("Your total before tax is", bTax)
    print("Your total with tax is", aTax)
if __name__ == "__main__":
        main()
        
          
          
          


      
