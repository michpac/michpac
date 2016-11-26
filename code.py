#Frames per second manipulation

#required 
import pygame
import os
pygame.init();
Football_Green = (50, 180, 50)
#create colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#position vars
x_pos = 0
y_pos = 0
x_delta = 0
y_delta = 0
clock = pygame.time.Clock()

#create a surface
gameDisplay = pygame.display.set_mode((1200,800)) #initialize with a tuple

#lets add a title, aka "caption"
pygame.display.set_caption("Frames per second")
pygame.display.update()		#only updates portion specified

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

helmet = load_png('Michigan.png')

gameExit = False
while not gameExit:
	gameDisplay.fill(Football_Green)

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
	gameDisplay.fill(helmet)
	pygame.display.update()		
	clock.tick()



#required
pygame.quit()
quit()				#exits python