# This program recommends a restaurant based off users input
# by David Neundorfer
# 10/16/2020


#Welcome message
def Welcome():
    print("Welcome! Let's find a restaurant for you.")

    
#Supporting function
def ask():
    asking = input("Please enter the cuisine you want (BBQ, Chinese or Mexican): ")
    if asking=="BBQ":
        ask2 = input("Please enter what you're willing to spend ($, $$ or $$$): ")
        if ask2 == "$":
            print("You should try Columbus BBQ.")
        elif ask2=="$$":
            print("You should try uptown BBQ.")
        else:
            print(ask2, "is not a valid choice")
    
    elif asking=="Chinese":
        ask3= input("Please enter what you're willing to spend ($, $$ or $$$): ")
        if ask3== "$":
            print("You should try Lucky Day.")
        elif ask3=="$$":
            print("You should try Chinese Buffet.")
        elif ask3=="$$$":
            print("You should try Gourmet Chinese.")
        else:
            print(ask3, "is not a valid choice")
    elif asking=="Mexican":
        ask4= input("Please enter what you're willing to spend ($, $$ or $$$): ")
        if ask4=="$":
            print("You should try El Restaurante.")
        elif ask=="$$":
            print("You should try La Casa.")
        else:
            print(ask4, "is not a valid choice")
    else:
        print(asking, "is not a valid choice")
        

    

#main function

def main():
    Welcome()
    print()
    ask()


#call to main
main()
