import pygame

#define colors
black = (0,0,0)
white = (255,255,255)
idk = (2,28,70)


pygame.init()

width=350
height = 350

screen = pygame.display.set_mode((width, height))

tokei= pygame.time.Clock()

pygame.draw.line(screen,idk, (1,30), (50,50))