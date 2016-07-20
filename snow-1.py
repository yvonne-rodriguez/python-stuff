import pygame
import random
import sys

#colors
WHITE = (255, 255, 255)
PGREEN= (152,251,152)
PTURQUOISE=(175,238,238)
LightSkyBlue = (135,206,250)
LightPink= (255,182,193)
LightYellow=(255,255,224)
LightGray=(211,211,211)
possible_colors= [WHITE,PGREEN,PTURQUOISE, LightPink,LightSkyBlue,LightYellow,LightGray]


pygame.init()

#screen
size = (700, 500)
screen = pygame.display.set_mode(size)
back = pygame.image.load("mount.jpg")
backRect= back.get_rect()
size= back.get_size()

pygame.display.set_caption("Snow")


#SnowFlake class
class SnowFlake():
    
    def __init__(self, x_location, y_location, y_speed, ball_size):  
        self.x_location = x_location
        self.y_location = y_location  
        self.y_speed = y_speed 
        self.ball_size = ball_size
        
    def fall(self,colors, item):
        ball_color = random.choice(colors) 

        self.y_location += self.y_speed 
        pygame.draw.circle(screen, ball_color, item, self.ball_size)\
    

        
            

random_x=random.randint(0,700)
#ranColors=random.randint
random_size=random.randint(2,5)

done = False
clock = pygame.time.Clock()

speed = 1


snow_list2 = []
snow_list = []
for i in range(150):
    x=random.randint(0,700)
    y=random.randint(0,500)
    snow_list.append([x,y])

for i in range(100):
    x=random.randint(0,700)
    y=random.randint(0,500)
    snow_list2.append([x,y])

snow=SnowFlake(350, 0, speed,3)


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

 
    screen.blit(back, backRect)

#falling snow DIAGONALLY

    for item in snow_list:
        item[1] +=1        
        item[0] +=1
        snow.fall(possible_colors, item)
        
        if item[1] > 500:
            item[1]=0
            item[0]=random.randint(0,700)

        if item[0]>700:
            item[0]=0
    
#falling snow STRAIGHT 

    for item in snow_list2:       
        item[1]+=1
        snow.fall(possible_colors, item)
        
        if item[1] > 500:
            item[1]=0
      

        if item[0]>700:
            item[0]=0
        
            
    pygame.display.flip()

    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() 
