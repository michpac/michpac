import pygame
import random
import sys
import math
import os
import getopt
from pygame.locals import *
from socket import *

White = (255,255,255)
Black = (0,0,0)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Football_Green = (50, 180, 50)
clock = pygame.time.Clock()

'''
def load_png(name):
	""" Load image and return image object"""
	fullname = os.path.join('data', name)
	try:
		image = pygame.image.load(fullname)
		if image.get_alpha() is None:
			image = image.convert()
		else:
			image = image.convert_alpha()
	except pygame.error as message:
        	print ('Cannot load image:'), fullname
        	raise SystemExit(message)
	return image, image.get_rect()


class Helmet(pygame.sprite.Sprite):
	"""Main pacman that is the helmet"""
	def __init__(self, vector):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_png('Michigan.png')
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
		self.vector = vector

	def update(self):
		newpos = self.calcnewpos(self.rect,self.vector)
		self.rect = newpos

	def calcnewpos(self,rect,vector):
		(angle,z) = vector
		(dx,dy) = (z*math.cos(angle),z*math.sin(angle))
		return rect.move(dx,dy)


Michigan=pygame.image.load('Michigan.png')
pygame.display.set_icon(Michigan)
'''

def main():
	# Initialise screen
	pygame.init()
	screen = pygame.display.set_mode((1200, 750))
	pygame.display.set_caption('Michigan Pacman Game')

	# Fill background
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill(Football_Green)

	# Display some text
	font = pygame.font.Font(None, 36)
	score = 0
	score_text = font.render("Score: " + str(score), 1, Red)
	textpos = score_text.get_rect()
	textpos.bottomleft = background.get_rect().bottomleft
	background.blit(score_text, textpos)

	lives = 0
	lives_text = font.render("Lives: " + str(lives), 1, Red)
	textpos = lives_text.get_rect()
	textpos.bottomright = background.get_rect().bottomright
	background.blit(lives_text, textpos)

	font = pygame.font.Font(None, 80)
	lives_text = font.render("MICHIGAN PACMAN", 1, Blue)
	textpos = lives_text.get_rect()
	textpos.midbottom = background.get_rect().midbottom
	background.blit(lives_text, textpos)

	# Blit everything to the screen
	screen.blit(background, (0, 0))
	pygame.display.flip()


	# Event loop
	while 1:
		for event in pygame.event.get():
			if event.type == QUIT:
				return
		screen.blit(background, (0, 0))
		pygame.display.flip()
		x_pos = 0
		y_pos = 0
		x_delta = 0
		y_delta = 0
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
		x_pos += x_delta
		y_pos += y_delta
		screen.blit(background, (0, 0))
		pygame.display.flip()
		screen.fill(Blue, rect=[x_pos,y_pos, 20,20])
		pygame.display.update()		
		clock.tick(60)

if __name__ == '__main__': main()