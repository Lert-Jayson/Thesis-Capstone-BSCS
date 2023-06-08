import pygame 
from settings import *
from support import *
from transition import *

class cutscene_gem:
	def __init__(self, change_map) :
                
		self.display_surface = pygame.display.get_surface()
		self.frames = []
		for i in range(1, 196):
			self.frames.append(pygame.image.load('graphics/cutscene/'+str(i)+'.png'))
		self.frame_index = 0
		self.image = self.frames[self.frame_index]
		self.rect = self.image.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
		self.change_map = change_map
		self.transition = Transition_boss_passed(self.change_map, 'modern')
		self.change = False
		self.music = pygame.mixer.Sound('audio/samples/Run As Fast As You Can.mp3')
		self.music.play(loops = -1)


	def animate(self, dt):
		self.frame_index += 4 * dt
		if self.frame_index >= len(self.frames):
			self.frame_index = len(self.frames)
			self.change = True   
			self.music.stop() 
		else:
			self.image = self.frames[int(self.frame_index)]

	def run(self, dt):
		self.display_surface.blit(self.image, self.rect)
		self.animate(dt)	
		if self.change:
			self.transition.play()
