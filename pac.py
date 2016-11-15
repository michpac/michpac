import random
import sys
import pygame
from pygame.locals import *
pygame.init();

X_MAX = 800
Y_MAX = 600

x_pos = 0
y_pos = 0
x_delta = 0
y_delta = 0

White = (255,255,255)
Black = (0,0,0)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)

background_color = Green
lines = White
Dots = White

gameDisplay = pygame.display.set_mode((800,600))

everything = pygame.sprite.Group()
clock = pygame.time.Clock()
pygame.display.set_caption("Michigan Pacman")
pygame.display.update()	

gameExit = False
while not gameExit:
	gameDisplay.fill(Green)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

	if event.type == pygame.KEYDOWN:
		x_delta=0;
		y_delta=0;
		if event.key == pygame.K_LEFT:
			x_delta -= 10
		if event.key == pygame.K_RIGHT:
			x_delta += 10
		if event.key == pygame.K_UP:
			y_delta -= 10
		if event.key == pygame.K_DOWN:
			y_delta += 10
	
	x_pos +=x_delta
	y_pos +=y_delta
	gameDisplay.fill(blue, rect=[x_pos,y_pos, 20,20])
	pygame.display.update()		
	clock.tick(30)
gameDisplay.fill(blue, rect=[x_pos,y_pos, 20,20])




