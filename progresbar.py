import pygame
from settings import *

class progressbar:
    def __init__(self):
        #Progress bar
        self.display_surface = pygame.display.get_surface()
        self.current_progress = 0
        self.target_progress = 0
        self.max_progress = 1000
        self.progress_bar_length = 255
        self.progress_ratio = self.max_progress / self.progress_bar_length
        self.progress_change_speed = 4

    def get_progress(self, amount):
        if self.target_progress < self.max_progress:
            self.target_progress += amount
        if self.target_progress > self.max_progress:
            self.target_progress = self.max_progress

    def draw(self):


        transition_width = 0
        transition_color = 'white'

        if self.current_progress < self.target_progress:
            self.current_progress += self.progress_change_speed
            transition_width = int((self.target_progress - self.current_progress) / self.progress_ratio)
            transition_color = 'white'

        if self.current_progress > self.target_progress:
            self.current_progress -= self.progress_change_speed 
            transition_width = int((self.target_progress - self.current_progress) / self.progress_ratio)
            transition_color = 'white'

        progress_bar_width = int(self.current_progress / self.progress_ratio)
        progress_bar = pygame.Rect(SCREEN_WIDTH-288,30,progress_bar_width,25)
        transition_bar = pygame.Rect(progress_bar.right,30,transition_width,25)

        pygame.draw.rect(self.display_surface,'#ffc900',progress_bar)
        pygame.draw.rect(self.display_surface,transition_color,transition_bar)	
        # pygame.draw.rect(self.display_surface,'#d27e2d',(SCREEN_WIDTH-300,23,self.progress_bar_length,25),4)

        surf = pygame.image.load('graphics/overlay/progress.png').convert_alpha()
        surf_rect = surf.get_rect(topright = (SCREEN_WIDTH + 212, -32))
        self.display_surface.blit(surf, surf_rect)	