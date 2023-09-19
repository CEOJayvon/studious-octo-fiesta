#print a welcome message that shows the prices of suitcases and carry-on
def welcome():
    print("""Welcome to CSU Airlines

      Tickets are $399.99 each
      Carry-on bags cost $34.99 per bag
      Checked baggage costs $59.99 per bag""")
#total cost of checkedbags
def costOfCheckedBags(x):
    b = x * 59.99
    return b
#total cost of carry-ons
def costOfCarryOns(y):
    c = y * 34.99
    return c

def main():
    welcome()
#prompts input for number of carry-ons
    carry_on=(int(input("How many carry-on bags do you have?")))
#prompts input for number of checked bags
    checked=(int(input("How many checked bags?")))
#adds checked bags and carryons together
    subtotal = costOfCheckedBags(checked) + costOfCarryOns(carry_on)
#multiply the subtotal by 0.09 for sales tax
    sales_tax = subtotal * 0.09
#adds subtotal and the sales tax    
    total = subtotal + sales_tax          
#displays Subtotal
    print("Subtotal:",round (subtotal,2))
#displays Sales tax
    print("Sales tax:",round (sales_tax,2))
#displays total
    print("Total:",round(total,2))
#calls when summoned     
if __name__ == "__main__":
    main()
    
    


