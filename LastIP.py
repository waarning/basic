# This program gives you a random backpack and gives you choices
# 11/20/2020
# David Neundorfer

import random


def Welcome():
    print("Welcome to the random backpack program!")
    print()
    
# Generates new backpack
def fillBackpack(listnumbers):
    for i in range(0,6):
        var = random.randint(0, 10)
        listnumbers[i]=var
    
#prints backpack
def printBackpack(listnames, listnumbers):
    print("Here is your backpack: ")
    for i in range(len(listnumbers)):
        print(listnumbers[i], listnames[i])
    print()
    
#adds items to the backpack     
def addItem(listnumbers):
    index = int(input("Enter what you would like to add: "))
    num = int(input("How many: "))
    listnumbers[index-1]+=num
    return listnumbers

#removes items from the backpack   
def rmItem(listnumbers):
    index = int(input("Enter what you would like to remove: "))
    num = int(input("How many: "))
    listnumbers[index-1] -=num

#prints main menu
def printMainMenu():
    print("Here are your options: ")
    print("Press 1 to get a new backpack")
    print("Press 2 to print your current backpack")
    print("Press 3 to add an item to your backpack")
    print("Press 4 to delete an item from your backpack")
    print("Press 5 to quit")
    print()


#prints second menu
def printItemMenu():

    print("Press 1 for magic items")
    print("Press 2 for clothes items")
    print("Press 3 for food items")
    print("Press 4 for armor items")
    print("Press 5 for fire creation items")
    print("Press 6 for weapon items")
    print("Press 7 for other items")
    print()

#calls to other functions
def main():
    listnames = ["magic items", "clothes items", "food items", "armor items", "fire creation items", "weapon items", "other items"]
    listnumbers = [10, 2, 1, 4, 5, 1, 8]
    
    Welcome()
    fillBackpack(listnumbers)
    printBackpack(listnames,listnumbers)
    
    printMainMenu()
    ask = int(input("Please enter your choice: "))
    
    while ask!=5:
        
        if ask==1:
            fillBackpack(listnumbers)
            printBackpack(listnames, listnumbers)
        elif ask==2:
            printBackpack(listnames, listnumbers)
        elif ask==3:
            printItemMenu()
            addItem(listnumbers)
            printBackpack(listnames, listnumbers)
        elif ask==4:
            printItemMenu()
            rmItem(listnumbers)
            printBackpack(listnames, listnumbers)
        else:
            print("Incorrect input")
        ask = int(input("Please enter your choice: "))


    
main()

    
