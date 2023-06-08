import pygame, sys
from settings import *
from support import *
from sprites import *
from timer import Timer
from player_cave import *
from text_overlay import *

class writings:
    def __init__(self, name , surf, player):
        self.font = pygame.font.Font('font/LycheeSoda.ttf', 30)
        self.display_surface = pygame.display.get_surface()
        self.name = name
        self.surf = surf
        self.active = True
        self.player = player
        self.text_overlay = text_overlay()
 
        self.image = pygame.image.load(surf).convert_alpha()
        self.rect = self.image.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.step= 2

        self.text = {
            '2': "'Anyone who can read this is worthy of\nthe Gem of Lightning.'",
            '3': "It is located at the deepest part of the cave.",
            '4': "I am the great wizard who cast a spell on this\ncave to keep the monsters from wreaking havoc\non the outside world.", 
            '5': "And to keep the Gem of Lightning that is\nGuarded by many monsters",
            '6': "To go the Deepest part of the cave,\nYou must COLLECT 2 GEMS and put it on\nhere and this tower will activate",
            '7': "To collect the Gems, you must activate the\nfires on the braziers on both sides of the cave",
        }
        self.text_counter = 0
    
    def input(self):
        pressed = pygame.key.get_pressed()
        skip = pressed[pygame.K_x]
        skip_all = pressed[pygame.K_SPACE]
        if self.step == 2:
                    if int(self.text_counter) < len(self.text['2']):
                        if skip_all:
                            self.text_counter = len(self.text['2'])
                        else:
                            self.text_counter += 1
        if self.step == 3:
                    if int(self.text_counter) < len(self.text['3']):
                        if skip_all:
                            self.text_counter = len(self.text['3'])
                        else:
                            self.text_counter += 1
        if self.step == 4:
                    if int(self.text_counter) < len(self.text['4']):
                        if skip_all:
                            self.text_counter = len(self.text['4'])
                        else:
                            self.text_counter += 1
        if self.step == 5:
                    if int(self.text_counter) < len(self.text['5']):
                        if skip_all:
                            self.text_counter = len(self.text['5'])
                        else:
                            self.text_counter += 1
        if self.step == 6:
                    if int(self.text_counter) < len(self.text['6']):
                        if skip_all:
                            self.text_counter = len(self.text['6'])
                        else:
                            self.text_counter += 1
        if self.step == 7:
                    if int(self.text_counter) < len(self.text['7']):
                        if skip_all:
                            self.text_counter = len(self.text['7'])
                        else:
                            self.text_counter += 1
                    
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if self.step < len(self.text):
                    if event.key==pygame.K_x:
                        self.text_counter = 0
                        self.step += 1
                        
                

                if self.step >= len(self.text):
                    pass
               
    def display(self):
        if self.active:
            self.input()
            self.display_surface.blit(self.image, self.rect)
            if self.step < len(self.text):
                writing_text = self.font.render((self.text[str(self.step)][0:int(self.text_counter)]), True, 'white',None)
                writing_rect = writing_text.get_rect()
                writing_rect.center = (self.rect.centerx,150)
                self.display_surface.blit(writing_text, writing_rect)
                if int(self.text_counter) == len(self.text[str(self.step)]):
                    self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 435, SCREEN_HEIGHT - 220))

            if self.step >= len(self.text):
                if pygame.key.get_pressed()[pygame.K_x]:
                    self.player.quest_tower=True
                    self.active=False
    