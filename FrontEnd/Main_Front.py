import pygame
from Button_Module import *

#create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

#load button images
start_img = pygame.image.load('start_btn.png').convert_alpha()
exit_img = pygame.image.load('exit_btn.png').convert_alpha()

#create button instances
start_button = Button(100, 200, start_img, 0.8)
exit_button = Button(450, 200, exit_img, 0.8)

# game speed
clock = pygame.time.Clock()

#game loop
run = True
while run:
	# clock.tick()
	screen.fill((202, 228, 241))
	start_button.draw(screen)
	exit_button.draw(screen)
	

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if start_button.isClicked():
				print('START')
			if exit_button.isClicked():
				print('EXIT')


	pygame.display.update()

pygame.quit()