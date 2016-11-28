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

#original positions
x_pos = 0
y_pos = 0
x_delta = 0
y_delta = 0

#plays music
# pygame.mixer.music.load('pacman.wav')
# pygame.mixer.music.play(5)        
# pygame.mixer.music.queue('pacman.wav')

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

class Helmet(pygame.sprite.Sprite):
	"""Main pacman that is the helmet"""
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('Michigan2.bmp')
		self.rect = self.image.get_rect()
		#self.image, self.rect = (blue, rect=[x_pos,y_pos, 20,20])
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
		self.speed = 10
		self.state = "still"
		self.reinit()

	def reinit(self):
		self.state = "still"
		self.movepos = [600,575]

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

	def moveup(self):
		self.movepos[1] = self.movepos[1] - (self.speed)
		self.state = "moveup"

	def movedown(self):
		self.movepos[1] = self.movepos[1] + (self.speed)
		self.state = "movedown"
'''
class Wall(pygame.sprite.Sprite):
	"""Setting up walls"""
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_png('WallA.png')
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
		self.state = "still"
		self.pos = [100,100]
'''
'''class Ghost(pygame.sprite.Sprite):
	"""Main pacman that is the helmet"""
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_png('NotreDameHelmet.png')
		#self.image, self.rect = (blue, rect=[x_pos,y_pos, 20,20])
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
		self.speed = 10
		self.state = "still"
		self.reinit()

	def reinit(self):
		self.state = "still"
		self.movepos = [600,450]

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

	def moveup(self):
		self.movepos[1] = self.movepos[1] - (self.speed)
		self.state = "moveup"

	def movedown(self):
		self.movepos[1] = self.movepos[1] + (self.speed)
		self.state = "movedown"'''

def main():
	# Initialise screen
	pygame.init()
	screen = pygame.display.set_mode((1200, 750))
	pygame.display.set_caption('Michigan Pacman Game')

	global helmet
	# global wall
	# global ghost
	helmet = Helmet()
	# wall = Wall()
	# ghost = Ghost()

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

	helmetsprite = pygame.sprite.RenderPlain(helmet)

	# Blit everything to the screen
	screen.blit(background, (0, 0))
	pygame.display.flip()


	# Event loop
	gameExit = False
	while not gameExit:
		# Make sure game doesn't run at more than 60 frames per second
		clock.tick(60)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			elif event.type == KEYDOWN:
				x_delta = 0;
				y_delta = 0;
				if event.key == pygame.K_RIGHT:
					helmet.moveright()
				if event.key == pygame.K_LEFT:
					helmet.moveleft()
				if event.key == pygame.K_DOWN:
					helmet.moveup()
				if event.key == pygame.K_UP:
					helmet.movedown()
			elif event.type == KEYUP:
				if event.key == K_RIGHT or event.key == K_LEFT:
					helmet.movepos = [0,0]
					helmet.state = "still"

		screen.blit(background, helmet.rect, helmet.rect)
		#screen.blit(background, wall.rect, wall.rect)
		#screen.blit(background, ghost.rect, ghost.rect)
		helmetsprite.update()
		#ghostsprite.update()
		helmetsprite.draw(screen)
		#ghostsprite.draw(screen)
		pygame.display.flip()
	pygame.quit()
	quit()	

if __name__ == '__main__': main()

