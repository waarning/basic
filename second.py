#David Neundorfer
#


def Welcome():
    print("Welcome to the animal fact automation program!")


def val_input():
    asking = int(input("Please enter a number between 1 and 5: "))
    while asking<1 or asking>5:
        print("Your input is invalid")
        asking = int(input("Please enter a number between 1 and 5: "))
    return asking

def statements(x):
    if x==1:
        print("blah blah")
    elif x==2:
        print("second")
    elif x==3:
        print("blahahahaha")
    


def main():
    q="y"
    while q=="y":
        Welcome()
        inp = val_input()
        statements(inp)
        q=input("Would you like to run the program again y/n? ")

main()
