import sys, pygame
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import random
import os


pygame.init()

size = width, height = 500, 100
speed = [2, 2]
black = 255, 255, 255
BLACK = (0,0,0)
BLUE = (0,0,1)



screen = pygame.display.set_mode(size)

ball = pygame.image.load("YAK.png")
ballrect = ball.get_rect()
clock = pygame.time.Clock()
n = 0
# pos = [[((abs(df.Latitude[0])/maxX)-1.0)*20000000., ((abs(df.Longitude[0])/maxY)-1.0)*20000000.]]
pos = [[0.,50.]]

# print(pos)
x = 0.
y = 50.
signx = 1.0
signy = 1.0
while 1:
    n+=1
    
    if x > width:
        break
        signx = -1.0

    if y > height:
        signy = -1.0

    if x < 0:
        signx = 1.0

    if y < 0 :
        signy = 1.0
    

    x+= signx *  random.normalvariate(1.0, 1.0)
    y+= signy * random.normalvariate(0.0, 1.0)


    clock.tick(100)
    pos.append([x, y])
    # pos.append([((abs(df.Latitude[n])/maxX)-1.0)*20000000., ((df.Longitude[n]/maxY)-1.0)*20000000.])
    # if(n%20. == 0.0):
        # print(pos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]


    screen.fill(black)
    pygame.draw.circle(screen, (200,0,0), [int(x), int(y)], 5)
    pygame.draw.lines(screen, BLACK, False, pos, 1)

    pygame.image.save(screen, './x0/'+"{:03d}".format(n)+".jpg")
    
    # screen.blit(ball, ballrect)
    pygame.display.flip()

