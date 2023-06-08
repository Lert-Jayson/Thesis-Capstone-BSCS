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
from player_modern import *
from transition import *
from text_overlay import text_overlay
from monster import monster

class Level_modern:
    def __init__(self,map_status):

        
        # get the display surface
        self.display_surface = pygame.display.get_surface()
        
        # sprite groups
        self.all_sprites = CameraGroup()
        self.collision_sprites = pygame.sprite.Group()
        self.grass_sprites = pygame.sprite.Group()
        self.tree_sprites = pygame.sprite.Group()
        self.interaction_sprites = pygame.sprite.Group()
        self.crow_sprites = pygame.sprite.Group()
        self.monster_sprites = pygame.sprite.Group()
        self.essence_sprites = pygame.sprite.Group()
        self.truck_sprites = pygame.sprite.Group()
       
        self.setup()
        self.overlay = Overlay(self.player)

        self.animation_player = AnimationPlayer()
        self.map_status=map_status
        self.transition4 = Transition(self.enter_school,self.player)
        self.transition5 = Transition(self.enter_sevenseven,self.player)
        self.transition6 = Transition(self.enter_ahamart,self.player)

        self.text_overlay = text_overlay()
        self.texts = [
            'Press Enter to go inside the school',
            'Press Enter to go inside Seven Seven',
            'Press Enter to go inside AhaMart'
        ]

    def setup(self):

        tmx_data = load_pygame('data/tmx/modern_world.tmx')

        portal_frames = []
        for i in range(0, 13):
            portal_frames.append(pygame.image.load('graphics/portal/'+str(i)+'.png'))
        for obj in tmx_data.get_layer_by_name('portal'):
            portal((obj.x, obj.y), portal_frames, self.all_sprites)

        # fountain
        fountain_frames = []
        for i in range(1, 16):
            fountain_frames.append(pygame.image.load('graphics/fountain_school/fountain_school'+str(i)+'.png'))
        for obj in tmx_data.get_layer_by_name('fountain'):
            self.fountain = fountain_animation((obj.x, obj.y), fountain_frames, [self.all_sprites, self.collision_sprites])

        # houses 
        for obj in tmx_data.get_layer_by_name('houses'):
            collisions_modern((obj.x, obj.y), obj.image, [self.all_sprites, self.collision_sprites])

        for obj in tmx_data.get_layer_by_name('houses2'):
            collisions_modern4((obj.x, obj.y), obj.image, [self.all_sprites, self.collision_sprites])   

        #establishment
        for obj in tmx_data.get_layer_by_name('establishment'):
            collisions_modern3((obj.x, obj.y), (obj.image), [self.all_sprites, self.collision_sprites])

        for obj in tmx_data.get_layer_by_name('establishment2'):
            collisions_modern4((obj.x, obj.y), (obj.image), [self.all_sprites, self.collision_sprites])
        
        # grass destructable
        for x, y, surf in tmx_data.get_layer_by_name('destructible grass').tiles():
            Generic((x * TILE_SIZE,y * TILE_SIZE), surf, [self.all_sprites, self.collision_sprites, self.grass_sprites])
        
        # #assets
        # for x, y, surf in tmx_data.get_layer_by_name('assets').tiles():
        #   Generic((x*TILE_SIZE ,y*TILE_SIZE), surf, [self.all_sprites, self.collision_sprites])

        #other objects
        for obj in tmx_data.get_layer_by_name('assets(collision)'):
            Generic((obj.x, obj.y), (obj.image), [self.all_sprites, self.collision_sprites])
        
        #stalls
        for obj in tmx_data.get_layer_by_name('stalls'):
            collisions_modern2((obj.x, obj.y), (obj.image), [self.all_sprites, self.collision_sprites])
        
        #trees
        for obj in tmx_data.get_layer_by_name('trees_decor'):
            Generic((obj.x, obj.y), (obj.image), [self.all_sprites, self.collision_sprites])

        #trees killable
        for obj in tmx_data.get_layer_by_name('trees'):
            Tree1((obj.x, obj.y), obj.image, [self.all_sprites, self.collision_sprites, self.tree_sprites], obj.name) # di ko alam bakit nonetype

        # truck
        for obj in tmx_data.get_layer_by_name('truck'):
            if obj.name == 'truck':
                self.truck = Truck((obj.x, obj.y), obj.image, [self.all_sprites, self.collision_sprites, self.truck_sprites], obj.name)
                                
        #collision
        for x, y, surf in tmx_data.get_layer_by_name('Constraints').tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE),pygame.Surface((TILE_SIZE, TILE_SIZE)) ,self.collision_sprites)
        
        # crow 
        for obj in tmx_data.get_layer_by_name('monsters'):
            if obj.name == 'crow':
                self.crow = crow(pos=(obj.x,obj.y), 
                                 groups=[self.all_sprites, self.crow_sprites],
                                 collision_sprites= self.collision_sprites, 
                                 trigger_death_particles= self.trigger_death_particles,  
                                 damage_player= self.damage_player)
        for obj in tmx_data.get_layer_by_name('monsters2'):
            if obj.name == 'mush': monster_name = 'mush'
            monster(monster_name= monster_name, 
	   				pos= (obj.x,obj.y), 
					groups= [self.all_sprites, self.monster_sprites], 
					collision_sprites= self.collision_sprites, 
					trigger_death_particles= self.trigger_death_particles, 
					essence_group= self.essence_sprites,
					damage_player= self.damage_player,
                    key_group=None)



        # Player 
        for obj in tmx_data.get_layer_by_name('player'):
            if obj.name == 'start':
                self.player = Player_modern(
                    pos = (obj.x,obj.y), 
                    group = self.all_sprites,
                    collision_sprites = self.collision_sprites,
                    interaction = self.interaction_sprites,
                    grass_sprites = self.grass_sprites,
                    tree_sprites = self.tree_sprites,
                    truck_sprites = self.truck_sprites,
                    crow= self.crow_sprites,
                    monster= self.monster_sprites,
                    display_surface= self.display_surface,
                    create_magic= self.create_magic)
                
            if obj.name == 'school_entry':
                Interaction((obj.x,obj.y), (obj.width,obj.height), self.interaction_sprites, obj.name)
            
            if obj.name == 'sevenseven_entry':
                Interaction((obj.x,obj.y), (obj.width,obj.height), self.interaction_sprites, obj.name)
            
            if obj.name == 'ahamart_entry':
                Interaction((obj.x,obj.y), (obj.width,obj.height), self.interaction_sprites, obj.name)
            
            if obj.name == 'truck':
                Interaction((obj.x,obj.y), (obj.width,obj.height), self.interaction_sprites, obj.name)
            

        Generic(
            pos = (0,0),
            surf = pygame.image.load('graphics/modern_world.png').convert_alpha(),
            groups = self.all_sprites,
            z = LAYERS['ground'])
    
    #bago######33333333333##########################		
	
    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprites = pygame.sprite.spritecollide(attack_sprite, self.attackable_sprites, False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        target_sprite.get_damage(self.player, 'magic')

    def create_magic(self, style, strength, cost):
        if style == 'heal':
            self.magic_player.heal(self.player, strength, cost, [self.all_sprites])
        
        if style == 'flame':
            self.magic_player.flame(self.player, cost, [self.all_sprites, self.attack_sprites])

    def indicator(self):
        collided_interaction_sprite = pygame.sprite.spritecollide(self.player,self.interaction_sprites,False)
        if collided_interaction_sprite:
            if collided_interaction_sprite[0].name == 'school_entry':
                    self.text_overlay.draw(self.texts[0],(self.display_surface.get_width() // 2, self.display_surface.get_height() - 250))
            if collided_interaction_sprite[0].name == 'sevenseven_entry':
                    self.text_overlay.draw(self.texts[1],(self.display_surface.get_width() // 2, self.display_surface.get_height() - 250))
            if collided_interaction_sprite[0].name == 'ahamart_entry':
                    self.text_overlay.draw(self.texts[2],(self.display_surface.get_width() // 2, self.display_surface.get_height() - 250))
                  
    def enter_school(self):
        self.map_status('school')
    def enter_ahamart(self):
        self.map_status('ahamart')
    def enter_sevenseven(self):
        self.map_status('sevenseven')

    def trigger_death_particles(self, pos, particle_type):
        self.animation_player.create_particles(particle_type, pos, self.all_sprites)
        
    def damage_player(self, amount ,attack_type):
        if self.player.vulnerable:
            self.player.health -= amount
            self.player.vulnerable = False
            self.player.hurt_time = pygame.time.get_ticks()
            self.animation_player.create_particles(attack_type, self.player.rect.center, [self.all_sprites])
                        
    def run(self,dt):

        self.display_surface.fill('black')
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.crow_update(self.player)
        self.all_sprites.monster_update(self.player)
        self.all_sprites.update(dt)
        self.overlay.display()

        if self.player.change==True and self.player.school_entrance==True:
            self.transition4.play()
        if self.player.change==True and self.player.sevenseven_entrance==True:
            self.transition5.play()
        if self.player.change==True and self.player.ahamart_entrance==True:
            self.transition6.play()
        
        
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

                    # # anaytics
                    # if sprite == player:
                    #   pygame.draw.rect(self.display_surface,'red',offset_rect,5)
                    #   hitbox_rect = player.hitbox.copy()
                    #   hitbox_rect.center = offset_rect.center
                    #   pygame.draw.rect(self.display_surface,'green',hitbox_rect,5)
                    #   target_pos = offset_rect.center + SPEAR_TOOL_OFFSET[player.status.split('_')[0]]
                    #   pygame.draw.circle(self.display_surface,'blue',target_pos,5)
    def crow_update(self, player):
        crow_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'crow']
        for crow in crow_sprites:
            crow.crow_update(player)
            return crow_sprites
    def monster_update(self, player):
        monster_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'monster']
        for monster in monster_sprites:
            monster.monster_update(player)
            return monster_sprites