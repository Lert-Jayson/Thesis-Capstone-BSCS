import pygame 
from settings import *
from player import *
from sprites import *
from support import *
from pytmx.util_pygame import load_pygame
from overlay_modern import Overlay
from dialogue import *
from npc import *
from particles import *
from player_minimarket import *
from transition import *
from text_overlay import text_overlay

class Level_sevenseven:
    def __init__(self,map_status):
        self.display_surface = pygame.display.get_surface()
        self.all_sprites = CameraGroup()
        self.collision_sprites = pygame.sprite.Group()
        self.interaction_sprites = pygame.sprite.Group()
        self.setup()
        self.overlay = Overlay(self.player)
        self.map_status=map_status
        self.transition10 = Transition(self.back_to_modern,self.player)
        self.text_overlay = text_overlay()
        self.texts = [
            'Press Enter to go back outside'
        ]
    def setup(self):
        tmx_data = load_pygame('data/tmx/interior_mini_market.tmx')
        for obj in tmx_data.get_layer_by_name('object_decor'):
            Generic((obj.x, obj.y), (obj.image), [self.all_sprites, self.collision_sprites])
        for x, y, surf in tmx_data.get_layer_by_name('constraints').tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE),pygame.Surface((TILE_SIZE, TILE_SIZE)) ,self.collision_sprites)
        for obj in tmx_data.get_layer_by_name('player'):
            if obj.name == 'start':
                self.player = Player_minimarket(pos = (obj.x,obj.y), 
                    group = self.all_sprites,
                    collision_sprites = self.collision_sprites,
                    interaction = self.interaction_sprites,
                    display_surface= self.display_surface)
            if obj.name == 'sevenseven_entrance_exit':
                Interaction((obj.x,obj.y), (obj.width,obj.height), self.interaction_sprites, obj.name)
        Generic(
            pos = (0,0),
            surf = pygame.image.load('graphics/interior_mini_market.png').convert_alpha(),
            groups = self.all_sprites,
            z = LAYERS['ground'])
    def indicator(self):
        collided_interaction_sprite = pygame.sprite.spritecollide(self.player,self.interaction_sprites,False)
        if collided_interaction_sprite:
            if collided_interaction_sprite[0].name == 'sevenseven_entrance_exit':
                    self.text_overlay.draw(self.texts[0],(self.display_surface.get_width() // 2, self.display_surface.get_height() - 250))       
    def back_to_modern(self):
        self.map_status('modern')
    def run(self,dt):
        self.display_surface.fill('black')
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(dt)
        self.overlay.display()
        if self.player.change == True:
            self.transition10.play()
        self.indicator()
class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2
        for layer in LAYERS.values():
            for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)