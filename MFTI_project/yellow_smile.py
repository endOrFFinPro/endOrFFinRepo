import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 600))

circle(screen, ('yellow'), (400, 300), 200, 0)
# left eye
circle(screen, ('red'), (300, 250), 50, 0)
circle(screen, ('black'), (300, 250), 50, 1)
circle(screen, ('black'), (300, 250), 25, 0)
# right eye
circle(screen, ('red'), (500, 250), 40, 0)
circle(screen, ('black'), (500, 250), 40, 1)
circle(screen, ('black'), (500, 250), 25, 0)

line(screen, ('white'), [250, 130], [380, 250], 15)
line(screen, ('white'), [420, 250], [550, 150], 15)

rect(screen, ('black'), [350, 400, 100, 20])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()