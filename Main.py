import sys
import pygame
from pygame import *
import cv2

pygame.init()

screen = pygame.display.set_mode((388, 404))

frame = 0

lib = ['map1.png']

Read = list(cv2.imread(lib[0]))

clock = pygame.time.Clock()
while True:
    screen.fill((15, 15, 15))
    frame+=1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    for i in range(len(Read)):#y coords
        for j in range(len(Read[i])):#x coords
            blue = list(Read[i][j])[0]
            green = list(Read[i][j])[0]
            red = list(Read[i][j])[0]
            #if blue > 240 and green > 240 and red > 240:
                #pygame.draw.rect(screen, (255,255,255), pygame.Rect(j, i, 32, 32))
            #else:
            #    pygame.draw.rect(screen, (0), pygame.Rect(j, i, 32, 32))
        
    pygame.display.update()
    clock.tick(120)
