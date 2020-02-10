
import pygame
import sys
pygame.init()
pygame.display.set_mode((600, 400))
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
#__________22222222____________________________________

play = True
while play:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            play = False

import pygame
pygame.init()
pygame.display.set_mode((600, 400))
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
            pygame.time.delay(20)

#________333333333______________________________________

import pygame
pygame.init()
pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
clock.tick(60)
clock = pygame.time.Clock()
FPS = 60
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
clock.tick(FPS)

#________4444444444444444_________________________________

import pygame

FPS = 60

pygame.iimnit()
pygame.display.set_mode((600, 400))
clock = pygame.te.Clock()

pygame.display.update()
while True:
    clock.tick(FPS)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

pygame.display.update()
#_________________5555555555____________________________________

import pygame
pygame.init()
sc = pygame.display.set_mode((300, 200))
# здесь будут рисоваться фигуры
pygame.display.update()
done = True
while done:
    pygame.time.delay(1000)
for i in pygame.event.get():
     if i.type == pygame.QUIT:
         done = False
pygame.quit()

#____________666666666666_________________________________________

import pygame
pygame.init()
sc = pygame.display.set_mode((300, 200))
pygame.draw.rect(sc, (255, 255, 255), (20, 20, 100, 75))
pygame.draw.rect(sc, (64, 128, 255), (150, 20, 100, 75), 8)
pygame.display.update()
done = True
while done:
    pygame.time.delay(1000)
for i in pygame.event.get():
    if i.type == pygame.QUIT:
        done = False
pygame.quit()

#_____________77777777777777777_____________________________________

import pygame
pygame.init()
sc = pygame.display.set_mode((300, 200))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (15, 20, 64)
YELLOW = (225, 225, 0)
PINK = (190, 47, 230)
r1 = pygame.Rect((150, 20, 100, 75))
pygame.draw.rect(sc, WHITE, (20, 20, 100, 75))
pygame.draw.rect(sc, LIGHT_BLUE, r1, 8)

pygame.display.update()
done = True
while done:
    pygame.time.delay(1000)
for i in pygame.event.get():
     if i.type == pygame.QUIT:
         done = False
pygame.quit()
























