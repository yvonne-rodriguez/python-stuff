import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
colors = [BLACK, GREEN, BLUE, RED]

def random_color():
    return random.choice(colors)

# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Set the title of the window
pygame.display.set_caption("CityScroller")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



class Building():
   
    def __init__(self, x_point, y_point, width, height, color):
        self.x_point = x_point
        self.y_point = y_point
        self.width= width 
        self.height = height
        self.color=color

        
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x_point,self.y_point,self.width,self.height))

    def move(self):
        self.x_point+= 3 
            #A positive integer moves the building to the right 
            #A negative integer moves the building to the left  
        
    


#self.height=random.randint(300,450)
b_list=[]
class Scroller():

    def __init__(self,x_point, y_point, width, height, base, color, speed):
        self.width= width
        self.height=height
        self.base=base
        self.color=color
        self.speed=speed
        self.x_point=x_point
        self.y_point=y_point
        
        self.b_list=[]    #instance variable
        
    def adds(self):
        current_width=0
        
        while self.width <= current_width:
            self.add
            

    def add(self, x_location):
        self.height=random.randint(300,450)
        x_point=x_location
        self.b_list.append(Building(self.x_point, self.y_point, self.width,self.height,self.color))
        
    def draw(self):
        for item in self.b_list:
          item.draw()
            


    def move(self):
        self.x_point +=self.speed 
        if self.width>600: 
            self.width=0
    
    

FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (17, 9, 89)

random_height=random.randint(300,450)


front_scroller = Scroller(0, 500, SCREEN_WIDTH, 500, (SCREEN_HEIGHT), FRONT_SCROLLER_COLOR, 3)
middle_scroller = Scroller(0, 300, SCREEN_WIDTH, 200, (SCREEN_HEIGHT - 50), MIDDLE_SCROLLER_COLOR, 2)
back_scroller = Scroller(0, 100, SCREEN_WIDTH, 300, (SCREEN_HEIGHT - 100), BACK_SCROLLER_COLOR, 1)

    
building=Building(30, random_height, 200, random_height, FRONT_SCROLLER_COLOR)


#scroll= Scroller(30, 200,200,300,RED, 5)
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

   
    
    
    screen.fill(BLACK)
    front_scroller.add(300)
    front_scroller.draw()
    #middle_scroller.add(300)
    #middle_scroller.draw()
    
    
    # building.draw()
    # building.move()
    
   
    
    
    
    # back_scroller.draw()
    # back_scroller.move()
    # middle_scroller.draw()
    # middle_scroller.move()
    front_scroller.draw()
    front_scroller.move()


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
