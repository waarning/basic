# This program gets user input and returns a tip from WHO to keep from
# spreading coronavirus
#
# David Neundorfer
# 10/29/2020

def Welcome():
    print("Welcome! Here is a public service announcement from the World Health Organization")
    print()
    print()
    
# A function that validates user input
def validateInput():
    ask = int(input("Please enter a number 1 to 5 or type 0 to quit: "))
    while ask<0 or ask>5:
        print("Invalid input", ask)
        ask = int(input("Please enter a number 1 to 5 or type 0 to quit: "))
    return ask


# a function that has all of the IF ELIF statements
def definitions(x):
    if x==1:
        print("HANDS Wash them often")
    elif x==2:
        print("ELBOW Cough into it")
    elif x==3:
        print("FACE Don't touch it")
    elif x==4:
        print("SPACE Keep safe distance")
    elif x==5:
        print("HOME Stay if you can")
    elif x==0:
        print("Stay safe!")
        exit()

        
# Main function that calls to other functions and repeats
def main():
    q=1
    Welcome()
    while q==1:
        val_inp = validateInput()
        definitions(val_inp)
        print()
    q+=1


main()
        
