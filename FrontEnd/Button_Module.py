import pygame

#button class
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

	def isClicked(self)->bool:
		# return pygame.mouse.get_pressed()[0] == 1 and self.rect.collidepoint(pygame.mouse.get_pos())
		return self.rect.collidepoint(pygame.mouse.get_pos())