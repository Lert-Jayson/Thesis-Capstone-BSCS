import pygame
from settings import *

class Transition:
	def __init__(self, change_map, player):
		
		# setup
		self.display_surface = pygame.display.get_surface()
		self.change_map = change_map
		self.player = player

		# overlay image
		self.image = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))
		self.color = 255
		self.speed = -5

	def play(self):
		self.color += self.speed
		if self.color <= 0:
			self.speed *= -1
			self.color = 0
			self.change_map()
	
		if self.color > 255:
			self.color = 255
			self.player.change = False
			try:
				self.player.school_entrance=False
				self.player.sevenseven_entrance=False
				self.player.ahamart_entrance=False
			except:
				print("Not applicable here")

			self.speed = -2

		self.image.fill((self.color,self.color,self.color))
		self.display_surface.blit(self.image, (0,0), special_flags = pygame.BLEND_RGBA_MULT)

class Transition_boss_failed:
	def __init__(self,change_map,reset, boss , map):
		
		# setup
		self.display_surface = pygame.display.get_surface()
		self.change_map = change_map
		self.reset = reset
		self.boss = boss
		self.map = map

		

		# overlay image
		self.image = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))
		self.color = 255
		self.speed = -5

	def play(self):
		self.color += self.speed
		if self.color <= 0:
			self.speed *= -1
			self.color = 0
			self.change_map(self.map)
			self.reset()
			self.boss.reset()
			
	
		if self.color > 255:
			self.color = 255

		self.image.fill((self.color,self.color,self.color))
		self.display_surface.blit(self.image, (0,0), special_flags = pygame.BLEND_RGBA_MULT)

class Transition_boss_passed:
	def __init__(self,change_map, map):
		
		# setup
		self.display_surface = pygame.display.get_surface()
		self.change_map = change_map
		self.map = map

		
		# overlay image
		self.image = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))
		self.color = 255
		self.speed = -5

	def play(self):
		self.color += self.speed
		if self.color <= 0:
			self.speed *= -1
			self.color = 0
			self.change_map(self.map)
			
	
		if self.color > 255:
			self.color = 255

		self.image.fill((self.color,self.color,self.color))
		self.display_surface.blit(self.image, (0,0), special_flags = pygame.BLEND_RGBA_MULT)

class Transition_death:
	def __init__(self, reset,level, player):
		
		# setup
		self.display_surface = pygame.display.get_surface()
		self.reset = reset
		self.level = level
		self.player = player



		# overlay image
		self.image = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))
		self.color = 255
		self.speed = -2

	def play(self):
		self.color += self.speed
		if self.color <= 0:
			self.speed *= -1
			self.color = 0
			self.reset()

		if self.color > 255:
			self.color = 255
			self.speed = -2
			self.level.player_dead = False

		self.image.fill((self.color,self.color,self.color))
		self.display_surface.blit(self.image, (0,0), special_flags = pygame.BLEND_RGBA_MULT)





