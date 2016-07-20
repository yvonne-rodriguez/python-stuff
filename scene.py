from turtle import*


    
def sun():
    fillcolor("yellow")
    begin_fill()  
    penup()
    goto(0, -450)  
    pendown()
    pencolor("orange")
    circle(150,360,50)    
    end_fill()
 
def cloud(x, y, sides):
    penup()
    goto(x, y)
    speed(0)
    for i in range(sides):
        fillcolor("light sky blue")
        begin_fill()
        pendown()
        pencolor("light sky blue")
        circle(30,360,50)
        penup()
        back(30)
        end_fill()

sun()
      
delay(30)
cloud(0, 200, 5)
cloud(50, 100, 3)
cloud(-100, 50, 5)
cloud(-150, -100, 4)
cloud(150, -50, 3)




