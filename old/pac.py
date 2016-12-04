import random
import sys
import pygame
from pygame.locals import *

# Some place I reference code from
#http://www.pygame.org/docs/tut/tom/games2.html



x_pos = 0
y_pos = 0
x_delta = 0
y_delta = 0

White = (255,255,255)
Black = (0,0,0)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Football_Green = (50, 180, 50)
background_color = Football_Green

#MICHIGAN_HELMET = pygame.image.load("Michigan.png").convert_alpha()
MICHIGAN_HELMET = Blue
Lines = White
Dots = White

#gameDisplay = pygame.display.set_mode((1200	,600))

#everything = pygame.sprite.Group()



def main():
	# Initialise screen
	pygame.init()
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((1200, 800))
	pygame.display.set_caption('Michigan Pacman Game')

	# Fill background
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill(Football_Green)

	# Display some text
	font = pygame.font.Font(None, 36)
	score_text = font.render("Score: ", 1, (10, 10, 10))
	textpos = score_text.get_rect()
	textpos.centerx = background.get_rect().centerx
	background.blit(text, textpos)

	# Blit everything to the screen
	screen.blit(background, (0, 0))
	pygame.display.flip()

	# Event loop
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return
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
		screen.blit(background, (0, 0))
		pygame.display.flip()
		gameDisplay.fill(MICHIGAN_HELMET, rect=[x_pos,y_pos, 20,20])
		pygame.display.update()		
		clock.tick(60)

if __name__ == '__main__': main()


#required
#pygame.quit()
#quit()		



