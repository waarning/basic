# Program description: Turtle graphics for you to look at
# Author: David Neundorfer
# Date: 9/12/2020


#Basics
import turtle

#Turtle 1 settings
one = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
one.color("white")
one.pensize(3)
one.speed(5)


#Triangle
one.penup()
one.right(90)
one.forward(100)
one.pendown()
one.right(90)
one.forward(200)
one.back(400)
one.right(60)
one.forward(400)
one.left(120)
one.forward(400)


#big circle
one.fillcolor("lightblue")
one.penup()
one.goto(-95, 80)
one.pendown()
one.circle(110)
one.hideturtle()

#turtle 2 settings
second = turtle.Turtle()
second.color("lightblue")
second.pensize(3)
second.speed(5)


#clock small circle (filled)
second.penup()
second.goto(0, 10)
second.pendown()
second.fillcolor("lightblue")
second.begin_fill()
second.circle(10)
second.end_fill()


#clock small arrow
second.right(90)
second.forward(80)


#turtle 3 settings
third = turtle.Turtle()
third.color("lightblue")
third.pensize(3)


#clock big arrow
third.penup()
third.goto(5, 27)
third.pendown()
third.left(45)
third.forward(100)


#right bubble
bob = turtle.Turtle()
bob.color("yellow")
bob.fillcolor("red")
bob.begin_fill()
bob.pensize(3)
bob.penup()
bob.goto(150, 100)
bob.pendown()
bob.circle(25)
bob.end_fill()

#left bubble
bob.penup()
bob.goto(-150, 100)
bob.pendown()
bob.fillcolor("lightblue")
bob.begin_fill()
bob.circle(30)
bob.end_fill()

#bottom bubble
bob.penup()
bob.goto(0, -200)
bob.pendown()
bob.fillcolor("Yellow")
bob.begin_fill()
bob.circle(35)
bob.end_fill()



#top caption
caption = turtle.Turtle()
caption.penup()
caption.goto(-55, 265)
caption.pendown()
caption.color("white")
caption.write("Dream Big !", font=("Arial", 20, "normal"))
caption.hideturtle()


#bottom signature
caption.penup()
caption.goto(135, -260)
caption.write("David Neundorfer", font=("Arial", 15, "normal"))



#exit on click
screen.exitonclick()




