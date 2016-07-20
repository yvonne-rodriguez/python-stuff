 from turtle import *


def square(color, side):
    pendown()
    pencolor(color)
    delay(30)
    for i in range(4):
        left(90)
        forward(side)
        
        
def move(space):
    penup()
    back(space)

    
def triangle(color, side):
    pendown()
    pencolor(color)
    delay(30)
    for i in range(3):
        left(120)
        forward(side)


def polygon(color, sides, length):
    pendown()
    pencolor(color)
    delay(30)
    for i in range(sides):
        left(360/sides)
        forward(length)









        
        
        
penup()       
goto(20, 60)        
        
square("red", 50)
move(60)
square("blue", 50)
move(60)
square("yellow", 50)


penup()
goto(20, 0)


triangle("yellow", 50)
move(60)
triangle("red", 50)
move(60)
triangle("blue", 50)

penup()
goto(140, -100)

polygon("red", 5, 40)
move(80)
polygon("orange", 6, 35)
move(80)
polygon("yellow", 7, 30)
move(80)
polygon("green", 8, 25)
move(80)
polygon("blue", 9, 20)
move(70)
polygon("purple", 10, 15)