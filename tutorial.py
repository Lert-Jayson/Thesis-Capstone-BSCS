import pygame, json
from settings import *
from support import *
from sprites import *
from timer import Timer

class tutorial:
    def __init__(self, name , surf):
        self.font = pygame.font.Font('font/LycheeSoda.ttf', 35)
        self.display_surface = pygame.display.get_surface()
        self.name = name
        self.surf = surf
        self.active = True
 
        self.image = pygame.image.load(surf).convert_alpha()
        self.rect = self.image.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

    def input(self):
        keys = pygame.key.get_pressed()
         #load 
        load={
			'tutorial_done':[]
		}
        try:
            with open('tutorialload_file.txt') as load_file:
                load = json.load(load_file)
        except:
            pass
        self.tutorial_done=load['tutorial_done']     
		#end of load file
        if keys[pygame.K_x]:
            self.active = False
            self.tutorial_done.append(self.name)
            with open('tutorialload_file.txt','w') as load_file:
               json.dump({'tutorial_done':self.tutorial_done},load_file)
           
          
    def display(self):
        self.input()
        if self.active:
            self.display_surface.blit(self.image, self.rect)
            exit_text = self.font.render('Back[x]', True, 'white')
            exit_rect = exit_text.get_rect(bottomright = (SCREEN_WIDTH-120, SCREEN_HEIGHT-80))
            self.display_surface.blit(exit_text, exit_rect)