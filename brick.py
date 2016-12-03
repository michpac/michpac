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
		self.lives = 2
		self.score = 0

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
				angle = -angle
				self.lives -= 1

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
		self.movepos = [500, 475]

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
	
	#def __init__(self, image, groups):
	def __init__(self, image, xpos, ypos):
		super(Bricks, self).__init__()
		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect()
		self.rect.center = (xpos, ypos)
		#self.groups = [groups]
		#self.score = 0
		#self.add(groups)
		#self.score = 0
	def update(self):
		self.rect.center = self.rect.center

	def destroy(self):
		super(Bricks, self).kill()

# Initialise screen
pygame.init()
screen = pygame.display.set_mode((1100, 600))
pygame.display.set_caption('Michigan Brick Breaker')

# Fill background
background = pygame.Surface(screen.get_size())
background = background.convert()
background = pygame.image.load('data/stadium.bmp').convert_alpha()
background = pygame.transform.scale(background, (1100, 600))

# Initialize players
global paddle
paddle = Paddle()

# Initialise ball
speed = 13
rand = ((0.1 * (random.randint(5,8))))
football = Football((0.47, speed))

#Initialize Bricks
schools = ['bricks/Alabama.bmp', 'bricks/Arizona.bmp', 'bricks/Duke.bmp', 'bricks/Florida.bmp', 'bricks/FSU.bmp', 'bricks/Georgetown.bmp', 'bricks/Illinois.bmp', 'bricks/Iowa.bmp','bricks/IU.bmp', 'bricks/Louisville.bmp', 'bricks/LSU.bmp', 'bricks/Maryland.bmp', 'bricks/Miami.bmp', 'bricks/Minnesota.bmp', 'bricks/MSU.bmp', 'bricks/ND.bmp','bricks/Nebraska.bmp', 'bricks/Northwestern.bmp', 'bricks/Oregon.bmp','bricks/OSU.bmp', 'bricks/OU.bmp', 'bricks/PSU.bmp','bricks/Purdue.bmp', 'bricks/Rutgers.bmp', 'bricks/Syracuse.bmp', 'bricks/Texas.bmp', 'bricks/UCLA.bmp', 'bricks/USC.bmp', 'bricks/Vandy.bmp','bricks/Wisconsin.bmp', 'bricks/Penn.bmp', 'bricks/Tulane.bmp', 'bricks/Virginia.bmp', 'bricks/CU.bmp', 'bricks/Kentucky.bmp']


brick1sprite =pygame.sprite.Group()
brick2sprite =pygame.sprite.Group()
brick3sprite =pygame.sprite.Group()
brick4sprite =pygame.sprite.Group()
brick5sprite =pygame.sprite.Group()
brick6sprite =pygame.sprite.Group()
for i in range(10):
	brick = Bricks(schools[i], (i+1)*100, 100)
	brick1sprite.add(brick)
for i in range(10):
	brick = Bricks(schools[i+10], (i+1)*100, 125)
	brick2sprite.add(brick)
for i in range(10):
	brick = Bricks(schools[i+20], (i+1)*100, 150)
	brick3sprite.add(brick)
for i in range(10):
	brick = Bricks(schools[i+25], (i+1)*100, 175)
	brick4sprite.add(brick)
for i in range(10):
	brick = Bricks(schools[i+7], (i+1)*100, 200)
	brick5sprite.add(brick)
for i in range(10):
	brick = Bricks(schools[i+14], (i+1)*100, 225)
	brick6sprite.add(brick)



# Initialise sprites
paddlesprite = pygame.sprite.RenderPlain(paddle)
footballsprite = pygame.sprite.RenderPlain(football)

#music
sound = pygame.mixer.Sound('music/victors.wav')

#fonts on bottom
# font = pygame.font.Font(None, 36)
# score_text = font.render("Score: " + str(football.score), 1, Red)
# textpos = score_text.get_rect()
# textpos.bottomleft = background.get_rect().bottomleft


font = pygame.font.Font(None, 80)
lives_text = font.render("MICHIGAN Eraser", 1, Blue)
textpos = lives_text.get_rect()
textpos.midbottom = background.get_rect().midbottom
background.blit(lives_text, textpos)


font = pygame.font.Font(None, 36)
lives_text = font.render("The game gives you 2 lives", 1, Red)
textpos = lives_text.get_rect()
textpos.midtop = background.get_rect().midtop
background.blit(lives_text, textpos)


# Blit everything to the screen
screen.blit(background, (0, 0))
pygame.display.flip()

# Initialise clock
clock = pygame.time.Clock()

 	
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

	hit1 = pygame.sprite.spritecollide(football, brick6sprite, True)
	for brick in hit1:
		brick.destroy()
		football.score +=1
	hit2 = pygame.sprite.spritecollide(football, brick5sprite, True)
	for brick in hit2:
		brick.destroy()
		football.score +=1
	hit3 = pygame.sprite.spritecollide(football, brick4sprite, True)
	for brick in hit3:
		brick.destroy()
		football.score +=1
	hit4 = pygame.sprite.spritecollide(football, brick3sprite, True)
	for brick in hit4:
		brick.destroy()
		football.score +=1
	hit5 = pygame.sprite.spritecollide(football, brick2sprite, True)
	for brick in hit5:
		brick.destroy()
		football.score +=1	
	hit6 = pygame.sprite.spritecollide(football, brick1sprite, True)
	for brick in hit6:
		brick.destroy()
		football.score +=1
	if football.lives == 0:
		gameExit = True 
		font = pygame.font.Font(None, 100)
		score_text = font.render("Score: " + str(football.score), 1, Red)
		textpos = score_text.get_rect()
		textpos.center = background.get_rect().center
		background.blit(score_text, textpos)
		screen.blit(background, (0, 0))
		pygame.display.update()
		pygame.time.delay(5000)
		break
	if football.score == 60:
		gameExit = True 
		font = pygame.font.Font(None, 100)
		score_text = font.render("You Won The Game. Score: " + str(football.score), 1, Red)
		textpos = score_text.get_rect()
		textpos.center = background.get_rect().center
		background.blit(score_text, textpos)
		screen.blit(background, (0, 0))
		pygame.display.update()
		pygame.time.delay(5000)
		break


	screen.blit(background, football.rect, football.rect)
	screen.blit(background, paddle.rect, paddle.rect)
	footballsprite.update()
	paddlesprite.update()
	brick1sprite.update()
	brick2sprite.update()
	brick3sprite.update()
	brick4sprite.update()
	brick5sprite.update()
	brick6sprite.update()
	footballsprite.draw(screen)
	paddlesprite.draw(screen)
	brick1sprite.draw(screen)
	brick2sprite.draw(screen)
	brick3sprite.draw(screen)
	brick4sprite.draw(screen)
	brick5sprite.draw(screen)
	brick6sprite.draw(screen)
	pygame.display.flip()
print ("Game over!!! You scored: " + str(football.score))
pygame.quit()
quit()	


if __name__ == '__main__': main()
