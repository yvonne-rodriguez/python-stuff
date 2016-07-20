import pygame
import random


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
 



pygame.init()


SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ball Game")

done = False

clock = pygame.time.Clock()


possible_ball_colors = [BLACK, WHITE, GREEN, RED, BLUE, GREY]


class BouncingBall(): 
    def   __init__(self, x_location, y_location, x_speed, y_speed, ball_size):  
        self.x_location = x_location
        self.y_location = y_location  
        self.x_speed = x_speed
        self.y_speed = y_speed 
        self.ball_size = ball_size
      

    def flashBounce(self, screen, colors, screen_width, screen_height):

        ball_color = random.choice(colors) # This is outside because of variable scoping.

        if self.x_location >= screen_width - self.ball_size or self.x_location < self.ball_size:
            self.x_speed = self.x_speed * -1

        if self.y_location >= screen_height - self.ball_size or self.y_location < self.ball_size:
            self.y_speed = self.y_speed * -1

        self.x_location += self.x_speed 
        self.y_location += self.y_speed 

        pygame.draw.circle(screen, ball_color, [self.x_location, self.y_location], self.ball_size)

ball=BouncingBall(250,350,5,5,50)
ball2=BouncingBall(250,350,5,5,30)
ball3=BouncingBall(250,350,5,5,20)
ball4=BouncingBall(250,350,5,5,10)
ball5=BouncingBall(250,350,5,5,40)
ball6=BouncingBall(250,350,5,5,60)
ball7=BouncingBall(250,350,5,5,70)
ball8=BouncingBall(250,350,5,5,80)
ball9=BouncingBall(250,350,5,5,90)
ball10=BouncingBall(250,350,5,5,100)



while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    # --- Game logic should go here

    
    
    
    
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(GREEN) 
    
    # --- Drawing code should go here
    ball.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    ball2.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    ball3.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    ball4.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    ball5.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    ball6.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    ball7.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    ball8.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    ball9.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    ball10.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE


 