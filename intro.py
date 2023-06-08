
import pygame 
from settings import *
from support import *
from text_overlay import *

class Intro:
    def __init__(self, change_map):
        self.change_map = change_map
        self.running = True
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font('font/Almendra-Bold.ttf', 30)
        self.text_counter = 0
        self.step = 0
        self.text_overlay = text_overlay()
        self.music = pygame.mixer.Sound('audio/samples/Run As Fast As You Can.mp3')
        self.music.play(loops = -1)
        self.intro_animations = [
            intro1_animation(),
            intro2_animation(),
            intro3_animation(),
            intro4_animation(),
            intro5_animation()
        ]
        self.texts = [
             'In a world devastated by an apocalypse, the determined protagonist\nTom emerges from a bleak future,',
             'Driven by a mission to save humanity from the monstrous force\nthat triggered the cataclysm. ',
             'His weapon of choice is the legendary sword of salvation,\na fabled blade with unimaginable power. ',
             'However, the sword is fragmented, its components scattered across\nthree distinct timelines, posing a daunting challenge.',
             "Undeterred, Tom employs a time portal to traverse through the fabric\nof time itself, embarking on a perilous journey to retrieve the\nsword's missing pieces. "
        ]
    def input(self):
        pressed = pygame.key.get_pressed()
        skip = pressed[pygame.K_x]
        if self.step < len(self.texts):
            if int(self.text_counter) < len(self.texts[self.step]):
                self.text_counter += 0.6
            else:
                if skip:
                    self.intro_animations[self.step].kill()
                    self.text_counter = 0
                    self.step += 1
        if self.step == len(self.texts):
            if skip:
                self.change_map('main')
                self.music.stop()
    def draw(self, dt):
        if self.step < len(self.texts):
            self.draw_text(self.texts[self.step][0:int(self.text_counter)])
            self.intro_animations[self.step].update(dt)
            if int(self.text_counter) == len(self.texts[self.step]):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
    def draw_text(self, text):
        y = SCREEN_HEIGHT - 200
        lines = text.splitlines()
        for line in lines:
            text_surf = self.font.render(line, True, 'white')
            text_rect = text_surf.get_rect(topleft=(210, y))
            self.display_surface.blit(text_surf, text_rect)
            y += text_surf.get_height()
    def run(self, dt):
        self.display_surface.fill('black')
        self.input()
        self.draw(dt)
class intro1_animation(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.frames = []
        for i in range(0, 19):
            self.frames.append(pygame.image.load('graphics/TOM ATTACK/INTRO/INTRO 1/'+str(i)+'.png'))
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(midtop = (SCREEN_WIDTH /2, 40))
    def animate(self, dt):
        self.frame_index += 6 * dt
        if self.frame_index >= len(self.frames):
            self.frame_index =0
        else:
            self.image = self.frames[int(self.frame_index)]
    def update(self, dt):
        self.animate(dt)
        self.display_surface.blit(self.image, self.rect)
class intro2_animation(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.frames = []
        for i in range(0, 21):
            self.frames.append(pygame.image.load('graphics/TOM ATTACK/INTRO/INTRO 2/'+str(i)+'.png'))
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(midtop = (SCREEN_WIDTH /2, 40))
    def animate(self, dt):
        self.frame_index += 6 * dt
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        else:
            self.image = self.frames[int(self.frame_index)]
    def update(self, dt):
        self.animate(dt)
        self.display_surface.blit(self.image, self.rect)
class intro3_animation(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.frames = []
        for i in range(0, 19):
            self.frames.append(pygame.image.load('graphics/TOM ATTACK/INTRO/INTRO 3/'+str(i)+'.png'))
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(midtop = (SCREEN_WIDTH /2, 40))
    def animate(self, dt):
        self.frame_index += 6 * dt
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        else:
            self.image = self.frames[int(self.frame_index)]
    def update(self, dt):
        self.animate(dt)
        self.display_surface.blit(self.image, self.rect)
class intro4_animation(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.frames = []
        for i in range(0, 27):
            self.frames.append(pygame.image.load('graphics/TOM ATTACK/INTRO/INTRO 4/'+str(i)+'.png'))
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(midtop = (SCREEN_WIDTH /2, 40))
    def animate(self, dt):
        self.frame_index += 6 * dt
        if self.frame_index >= len(self.frames):
            self.frame_index = len(self.frames)
        else:
            self.image = self.frames[int(self.frame_index)]
    def update(self, dt):
        self.animate(dt)
        self.display_surface.blit(self.image, self.rect)
class intro5_animation(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.frames = []
        for i in range(0, 23):
            self.frames.append(pygame.image.load('graphics/TOM ATTACK/INTRO/INTRO 5/'+str(i)+'.png'))
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(midtop = (SCREEN_WIDTH /2, 40))
    def animate(self, dt):
        self.frame_index += 6 * dt
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        else:
            self.image = self.frames[int(self.frame_index)]
    def update(self, dt):
        self.animate(dt)
        self.display_surface.blit(self.image, self.rect)