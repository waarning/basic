#David Neundorfer
#9/24/2020
#





def Welcome():
    print("Welcome to CSU Airlines")
    print()
    print("Tickets are $300 each")
    print("Carry-on bags cost $25 per bag")
    print("Checked baggage costs $55 per bag")

#Helper functions
def carry_on_bags(x):
    total_carryon = x * 25
    return total_carryon

def checked_bags(x):
    total_checked_bags = x * 55
    return total_checked_bags

def sales_tax(subtotal):
    tax = subtotal * .08
    return tax

#Main function
def main():
    ask_carryon = int(input("How many carry-on bags do you have? "))
    carryons = carry_on_bags(ask_carryon)
    ask_checked = int(input("How many checked bags? "))
    checkedbags = checked_bags(ask_checked)
    subtotal = carryons + checkedbags
    sales = sales_tax(subtotal)
    total = subtotal + sales
    print("Your subtotal is $", subtotal)
    print("Your total is $", total)

main()
        
