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

BACKGROUND_COLOR = (17, 9, 89)

def random_color():
    return random.choice(colors)

# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Set the title of the window
pygame.display.set_caption("CityScroller")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

x_location=350


class Building():
   
    def __init__(self, x_point, y_point, width, height, color):
        self.x_point = x_point
        self.y_point = y_point
        self.width= width 
        self.height = height
        self.color=color
        
    def draw(self):
        pygame.draw.rect(screen, self.color, (200,150,100,50), self.width)

    def move(self, speed):
        x_point+=speed 
            #A positive integer moves the building to the right 
            #A negative integer moves the building to the left  
            
building=Building(350, 250, 100, 100, BLACK)
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    
    
    
    screen.fill(BACKGROUND_COLOR)

    # --- Drawing code should go here
    building.draw()
    
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit()