from turtle import *


def square(side,color):
    pendown()
    pencolor(color)
    delay(30)
    for i in range(4):
        forward(side)
        left(90)

        
def move(side):
    penup()
    right(180)
    forward(side)
    

    
def triangle():
    pendown()
    pencolor("black")
    delay(50)
    right(60)
    forward(side)
    for i in range(2):
        left(120)
        forward(side)
        
        

square(50, "red")

move(10)

square(50,"red")
        


    
    
    
    
    
    
    
    
    
    
