import sys
import random
import math
import os
import getopt
import pygame
from socket import *
from pygame.locals import *

def load_png(name): #this was taken from pygame website on loading pngs
	""" Load image and return image object"""
	fullname = os.path.join('data', name)
	try:
		image = pygame.image.load(fullname)
		if image.get_alpha is None:
			image = image.convert()
		else:
			image = image.convert_alpha()
	except pygame.error as message:
		print ('Cannot load image:' + fullname)
		raise SystemExit
	return image, image.get_rect()

class Football(pygame.sprite.Sprite):
	"""This is going to be the football that bounces back and fourth"""
	def __init__(self, vector):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_png('Football.png')
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
		self.vector = vector
		self.hit = 0

	def update(self):
		newpos = self.calcnewpos(self.rect,self.vector)
		self.rect = newpos
		(angle,z) = self.vector

		if not self.area.contains(newpos):
			tl = not self.area.collidepoint(newpos.topleft)
			tr = not self.area.collidepoint(newpos.topright)
			bl = not self.area.collidepoint(newpos.bottomleft)
			br = not self.area.collidepoint(newpos.bottomright)
			if tl == True and bl == True:
				angle = math.pi - angle
			if tr == True and br == True:
				angle = math.pi - angle
			if tr == True and tl == True:
				angle = -angle
			#if br == True and bl == True: 
				#this will be a loss of life

		else:
			# Do ball and bat collide?
			# Note I put in an odd rule that sets self.hit to 1 when they collide, and unsets it in the next
			# iteration. this is to stop odd ball behaviour where it finds a collision *inside* the
			# bat, the ball reverses, and is still inside the bat, so bounces around inside.
			# This way, the ball can always escape and bounce away cleanly
			if self.rect.colliderect(paddle.rect) == 1 and not self.hit:
				angle = -angle
				self.hit = not self.hit
			elif self.hit:
				self.hit = not self.hit
		self.vector = (angle,z)

	def calcnewpos(self,rect,vector):
		(angle,z) = vector
		(dx,dy) = (z*math.cos(angle),z*math.sin(angle))
		return rect.move(dx,dy)

class Paddle(pygame.sprite.Sprite):
	"""Paddle on the bottom"""

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		#self.image, self.rect = load_png('Michigan.png')
		self.image, self.rect = (blue, rect=[x_pos,y_pos, 20,20])
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
		self.speed = 10
		self.state = "still"
		self.reinit()

	def reinit(self):
		self.state = "still"
		self.movepos = [0,0]

	def update(self):
		newpos = self.rect.move(self.movepos)
		if self.area.contains(newpos):
			self.rect = newpos
		pygame.event.pump()

	def moveleft(self):
		self.movepos[0] = self.movepos[0] - (self.speed)
		self.state = "move left"

	def moveright(self):
		self.movepos[0] = self.movepos[0] + (self.speed)
		self.state = "move right"

def main():
	# Initialise screen
	pygame.init()
	screen = pygame.display.set_mode((1200, 600))
	pygame.display.set_caption('Michigan Brick Breaker')

	# Fill background
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((50, 180, 50))

	# Initialise players
	global paddle
	paddle = Paddle()

	# Initialise ball
	speed = 13
	rand = ((0.1 * (random.randint(5,8))))
	football = Football((0.47, speed))

	# Initialise sprites
	paddlesprite = pygame.sprite.RenderPlain(paddle)
	footballsprite = pygame.sprite.RenderPlain(football)

	# Blit everything to the screen
	screen.blit(background, (0, 0))
	pygame.display.flip()

	# Initialise clock
	clock = pygame.time.Clock()

	# Event loop
	gameExit = False
	while not gameExit:
		# Make sure game doesn't run at more than 60 frames per second
		clock.tick(60)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			elif event.type == KEYDOWN:
				if event.key == pygame.K_RIGHT:
					paddle.moveright()
				if event.key == pygame.K_LEFT:
					paddle.moveleft()
			elif event.type == KEYUP:
				if event.key == K_RIGHT or event.key == K_LEFT:
					paddle.movepos = [0,0]
					paddle.state = "still"

		screen.blit(background, football.rect, football.rect)
		screen.blit(background, paddle.rect, paddle.rect)
		footballsprite.update()
		paddlesprite.update()
		footballsprite.draw(screen)
		paddlesprite.draw(screen)
		pygame.display.flip()
	pygame.quit()
	quit()	


if __name__ == '__main__': main()
