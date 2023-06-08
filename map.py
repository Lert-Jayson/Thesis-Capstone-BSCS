import pygame, sys
from settings import *
from support import *
from sprites import *
from timer import Timer

class Map_toggle:
    def __init__(self, surf):
        
        self.display_surface = pygame.display.get_surface()
        self.surf = surf
        self.active = True
 
        self.image = pygame.image.load(surf).convert_alpha()
        self.rect = self.image.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

    def input(self):
        keys = pygame.key.get_pressed()
                     
    def display(self):
        if self.active:
            self.display_surface.blit(self.image, self.rect)
           