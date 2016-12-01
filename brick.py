import sys
import random
import math
import os
import getopt
import pygame
from socket import *
from pygame.locals import *

White = (255,255,255)
Black = (0,0,0)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Football_Green = (50, 180, 50)


class Football(pygame.sprite.Sprite):
	"""This is going to be the football that bounces back and fourth"""
	def __init__(self, vector):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('data/football.bmp')
		self.rect = self.image.get_rect()
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
		self.vector = vector
		self.lives = 3

	def update(self):
		newpos = self.calcnewpos(self.rect,self.vector)
		self.rect = newpos
		(angle,z) = self.vector
		self.hit = 0	
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
			if br == True and bl == True: 
				self.lives -= 1
				return self.lives

		else:
			if self.rect.colliderect(paddle.rect) == True and not self.hit:
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
	"""Paddle (Michigan Football Helmets) on the bottom"""

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('data/Michigan.bmp')
		self.rect = self.image.get_rect()		
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
		self.speed = 10
		self.state = "still"
		self.reinit()

	def reinit(self):
		self.state = "still"
		self.movepos = [600, 475]

	def update(self):
		newpos = self.rect.move(self.movepos)
		if self.area.contains(newpos):
			self.rect = newpos
		pygame.event.pump()

	#positions paddle can move
	def moveleft(self):
		self.movepos[0] = self.movepos[0] - (self.speed)
		self.state = "move left"

	def moveright(self):
		self.movepos[0] = self.movepos[0] + (self.speed)
		self.state = "move right"

class Bricks(pygame.sprite.Sprite):
	"""Bricks to be hit by football"""
	def __init__(self, image, groups):

		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('data/OSU.bmp')
		self.image = pygame.Surface([brick_width, brick_height])
		self.rect = self.image.get_rect()
		#self.rect.center = (50, 50)
		self.rect.x = 50
		self.rect.y = 50
		#self.add(groups)
		#self.score = 0

	'''def update(self):
		if self.rect.colliderect(football.rect):
			self.kill()
			self.score +=1
			return score'''

# Initialise screen
pygame.init()
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption('Michigan Brick Breaker')


# Fill background
background = pygame.Surface(screen.get_size())
background = background.convert()
background = pygame.image.load('data/stadium.bmp')
background = pygame.transform.scale(background, (1200, 600))

# Initialize players
global paddle
paddle = Paddle()

# Initialise ball
speed = 13
rand = ((0.1 * (random.randint(5,8))))
football = Football((0.47, speed))

#Initialize Bricks
bricks = pygame.sprite.Group()
schools = ['data/OSU.bmp', 'data/MSU.bmp', 'data/ND.bmp',
 'data/Illinois.bmp','data/IU.bmp', 'data/Alabama.bmp', 
 'data/Florida.bmp', 'data/Iowa.bmp','data/Maryland.bmp', 
 'data/Miami.bmp','data/Northwestern.bmp', 'data/Texas.bmp', 
 'data/Wisconsin.bmp', 'data/UCLA.bmp', 'data/USC.bmp', 
 'data/LSU.bmp', 'data/Minnesota.bmp']
for item in schools:
	Bricks(item, bricks)

# Initialise sprites
paddlesprite = pygame.sprite.RenderPlain(paddle)
footballsprite = pygame.sprite.RenderPlain(football)
brickssprite =pygame.sprite.RenderPlain(bricks)

#music
sound = pygame.mixer.Sound('victors.wav')

#fonts on bottom
score = 0
font = pygame.font.Font(None, 36)
score_text = font.render("Score: " + str(score), 1, Red)
textpos = score_text.get_rect()
textpos.bottomleft = background.get_rect().bottomleft
background.blit(score_text, textpos)

font = pygame.font.Font(None, 80)
lives_text = font.render("MICHIGAN BrickBreaker", 1, Blue)
textpos = lives_text.get_rect()
textpos.midbottom = background.get_rect().midbottom
background.blit(lives_text, textpos)

#lives = 3
font = pygame.font.Font(None, 36)
lives_text = font.render("Lives: " + str(football.lives), 1, Red)
textpos = lives_text.get_rect()
textpos.bottomright = background.get_rect().bottomright
background.blit(lives_text, textpos)

# Blit everything to the screen
screen.blit(background, (0, 0))
pygame.display.flip()

# Initialise clock
clock = pygame.time.Clock()

#Creating rows
# b = pygame.sprite.Bricks()
# y_pos = 10
# number_blocks = 10
# brick_width =40
# brick_height = 40
# for row in range (0,5):
# 	for column in range(0, number_blocks):
# 		dems = Bricks(column * (brick_width * 2) + 1, y_pos)
# 		b.add(dems)
# 	y_pos += brick_height +1


# Event loop
gameExit = False
while not gameExit:
	sound.play() #plays music
	# Runs frames at 60 frames per second
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
	#screen.blit(background, bricks.rect, bricks.rect)
	footballsprite.update()
	paddlesprite.update()
	#brickssprite.update()
	footballsprite.draw(screen)
	paddlesprite.draw(screen)
	#brickssprite.draw(screen)
	pygame.display.flip()
#print (score)
pygame.quit()
quit()	


if __name__ == '__main__': main()

