import pygame


class Button:
	def __init__(self, height, width, color):

		self.image = pygame.Surface([width, height])
		self.image.fill([0, 0, 0])
		self.image.set_colorkey([0, 0, 0])
		pygame.draw.rect(self.image, color, [0, 0, width, height])
		self.rect = self.image.get_rect()
		self.clicked = False

	def draw(self, surface):
		action = False

		# get mouse position
		pos = pygame.mouse.get_pos()

		# check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if self.clicked == False and pygame.mouse.get_pressed()[0] == 1:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		# draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action
