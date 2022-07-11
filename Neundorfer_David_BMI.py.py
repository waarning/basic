# PART A
# Purpose: This program calculates and displays the body
# mass index for given weight and height and classifies
# a person based on the inputs
# Author: David Neundorfer
# Date: 10/17/2020



#function that calculates bmi and gives back the category


def calculateBMI(x, y):
    BMI = (x/y)*703
    if BMI <=20:
        print("BMI:", BMI, "UNDR")
    elif BMI >20 and BMI <25:
        print("BMI:", BMI, "NORM")
    elif BMI >25 and BMI <30:
        print("BMI:", BMI, "OVER")
    elif BMI>=30:
        print("BMI:", BMI, "OBES")
    else:
        print("None")
    round(BMI, 2)
    return BMI

#main function that asks for height and weight and reruns program if needed
def main():
    q = "y"
    while q=="y":
        ask_weight = int(input("Please enter weight in pounds: "))
        ask_height = int(input("Please enter height in inches: "))
        calculateBMI(ask_weight, ask_height)
        q = input("Run again? (y/n): ")
    if q!="n" or "y":
        print("Invalid input:", q)
        q = input("Run again? (y/n): ")


#PART B



main()
