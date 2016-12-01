import sys
import random
import math
import os
import getopt
import pygame
from socket import *
from pygame.locals import *
class Bricks(pygame.sprite.Sprite):
	"""Bricks to be hit by football"""
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.width = 40
		self.height = 40
		schools = ['data/OSU.bmp', 'data/MSU.bmp', 'data/ND.bmp', 'data/Illinois.bmp', 'data/IU.bmp', 'data/Alabama.bmp', 'data/Florida.bmp', 'data/Iowa.bmp','data/Maryland.bmp', 'data/Miami.bmp','data/Northwestern.bmp', 'data/Texas.bmp', 'data/Wisconsin.bmp', 'data/UCLA.bmp', 'data/USc.bmp', 'data/LSU.bmp', 'data/Minnesota.bmp']
		school_size = []
		for image in schools:
			self.image = pygame.image.load(image)
			self.school_size.append(self.image)
		self.image = random.choice(self.school_size)
		self.image = pygame.transform.scale(self.image (self.width, self.height))
		self.rect = self.image.get_image()




pygame.init()
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption('Michigan Brick Breaker')
background = pygame.Surface(screen.get_size())
background = background.convert()
background = pygame.image.load('data/stadium.bmp')
background = pygame.transform.scale(background, (1200, 600))

brickssprite = pygame.sprite.RenderPlain(Bricks)

while not gameExit:
	sound.play() #plays music
	# Runs frames at 60 frames per second
	clock.tick(60)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True 

screen.blit(background, bricks.rect, bricks.rect)
