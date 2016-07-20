import pygame
import random

# Define some colors
black  = (0, 0, 0)
white  = (255, 255, 255)
green  = (0, 255, 0)
red    = (255, 0, 0)
blue   = (0, 0, 255)
x      = 20
y      = 20 

colors= ["black", "white", "green", "red", "blue"]

pygame.init()

height = 450
width = 650
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball")

done = False

clock = pygame.time.Clock()

random_num= random.randint(0,15)
random_num1= random.randint(0,15)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    x = x + random_num
    y = y + random_num1
    
    if x>width or x<0 : 
        random_num= random_num * -1
    if y>height or y<0:
        random_num1= random_num1 * -1
        
    
    screen.fill(green)
    pygame.draw.circle(screen, blue, (x, y),50)

    pygame.display.flip()

    clock.tick(60)

    #CODE
    
    

    
pygame.quit()
exit() # Needed when using IDLE

