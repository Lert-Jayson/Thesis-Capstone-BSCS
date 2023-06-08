import pygame
import json
from settings import *
from support import *
from timer import Timer
from particles import *
from random import randint
from dialogue import *
from entity import Entity
from sprites import *

class Player_modern(Entity):
    def __init__(self, pos, group, collision_sprites, interaction, grass_sprites, tree_sprites,truck_sprites, crow, monster, display_surface, create_magic):
        super().__init__(group)
        #load file
        load={
            'pos_x':1599,
            'pos_y':1314.50,
            'anim_status':'down_idle'
        }
        try:
            with open('modernload_file.txt') as load_file:
                load = json.load(load_file)
        except:
            print('No file created yet')
        self.frame_index = 0
        self.import_assets()
        self.status = load['anim_status']
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)
        self.z = LAYERS['main']
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.pos.x=load['pos_x']
        self.pos.y=load['pos_y']
        self.speed = 320        
        self.hitbox = self.rect.copy().inflate((-126,-70))
        self.collision_sprites = collision_sprites
        self.grass_sprites = grass_sprites
        self.tree_sprites = tree_sprites
        self.truck_sprites = truck_sprites
        self.stats = {'health': 200, 'energy': 60, 'attack': 10, 'magic': 4}
        self.max_stats = {'health': 300, 'energy': 140, 'attack': 20, 'magic' : 10}
        self.health = self.stats['health']
        self.energy = self.stats['energy']
        self.speed = 280	
        self.attacking = False
        self.attack_cooldown = 300
        self.attack_time = None
        self.create_magic = create_magic
        self.magic_index = 0
        self.magic = list(magic_data.keys())[self.magic_index]
        self.can_switch_magic = True
        self.magic_switch_time = None	
        self.switch_duration_cooldown = 200 
        self.timers = {
            'tool use': Timer(300,self.use_tool),
            'tool switch': Timer(200)
        } 
        self.tools = ['axe']
        self.tool_index = 0
        self.selected_tool = self.tools[self.tool_index]
        self.crow = crow
        self.monster = monster
        self.interaction = interaction
        self.display_surface = display_surface
        self.animation_player = AnimationPlayer()
        self.dialogue = dialogue_manager(self.display_surface)
        self.change = False
        self.speaking = False
        self.school_entrance= False
        self.sevenseven_entrance = False
        self.ahamart_entrance = False
        self.weapon_attack_sound = pygame.mixer.Sound('audio/sword.wav')
        self.weapon_attack_sound.set_volume(0.4)
        self.vulnerable = True
        self.hurt_time = None
        self.invincibility_duration = 300
        self.success = pygame.mixer.Sound('audio/success.wav')
    def use_tool(self):
        if self.selected_tool == 'axe':
            for tree in self.tree_sprites.sprites():
                if tree.rect.collidepoint(self.target_pos):
                    tree.damage()             
            for grass in self.grass_sprites.sprites():
                if grass.rect.collidepoint(self.target_pos):
                    pos = grass.rect.center
                    offset = pygame.math.Vector2(0, 75)
                    for leaf in range(randint(3, 6)):
                        self.animation_player.create_grass_particles(pos - offset, [self.groups()[0]])
                    self.weapon_attack_sound.play()
                    grass.kill()
            for crow in self.crow.sprites():
                if crow.rect.colliderect(self.rect): 
                    crow.get_damage(self, 'axe')
            for monster in self.monster.sprites():
                if monster.rect.colliderect(self.rect):
                    monster.get_damage(self, 'axe')    
    def get_target_pos(self):
        self.target_pos = self.rect.center + PLAYER_TOOL_OFFSET[self.status.split('_')[0]]
        self.target_pos_spear = self.rect.center + SPEAR_TOOL_OFFSET[self.status.split('_')[0]]
    def import_assets(self):
        self.animations = {'up': [],'down': [],'left': [],'right': [],
                           'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
                           'right_axe':[],'left_axe':[],'up_axe':[],'down_axe':[],
                           'right_water':[],'left_water':[],'up_water':[],'water':[]}
        for animation in self.animations.keys():
            full_path = 'graphics/player/' + animation
            self.animations[animation] = import_folder(full_path)
    def animate(self,dt):
        self.frame_index += 8 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]
    def input(self, dt):
        keys = pygame.key.get_pressed()   
        if self.dialogue.dialogue is None:
            if not self.timers['tool use'].active:
                if keys[pygame.K_UP]:
                    self.direction.y = -1
                    self.status = 'up'
                elif keys[pygame.K_DOWN]:
                    self.direction.y = 1
                    self.status = 'down'
                else:
                    self.direction.y = 0
                if keys[pygame.K_RIGHT]:
                    self.direction.x = 1
                    self.status = 'right'
                elif keys[pygame.K_LEFT]:
                    self.direction.x = -1
                    self.status = 'left'
                else:
                    self.direction.x = 0
                if keys[pygame.K_SPACE]:
                    self.timers['tool use'].activate()
                    self.direction = pygame.math.Vector2()
                    self.frame_index = 0
                if keys[pygame.K_q] and not self.timers['tool switch'].active:
                    self.timers['tool switch'].activate()
                    self.tool_index += 1
                    self.tool_index = self.tool_index if self.tool_index < len(self.tools) else 0
                    self.selected_tool = self.tools[self.tool_index]
                if keys[pygame.K_LCTRL] and not self.attacking:	
                    self.attacking = True
                    self.attack_time = pygame.time.get_ticks()
                    style = list(magic_data.keys())[self.magic_index]
                    strength = list(magic_data.values())[self.magic_index]['strength'] + self.stats['magic']
                    cost = list(magic_data.values())[self.magic_index]['cost']
                    self.create_magic(style, strength, cost)   
                if keys[pygame.K_e] and self.can_switch_magic:
                    self.can_switch_magic = False
                    self.magic_switch_time = pygame.time.get_ticks()
                    if self.magic_index < len(list(magic_data.keys())) - 1:
                        self.magic_index += 1
                    else:
                        self.magic_index = 0
                        self.magic = list(magic_data.keys())[self.magic_index]
                if keys[pygame.K_RETURN]:
                        collided_interaction_sprite = pygame.sprite.spritecollide(self,self.interaction,False)
                        if collided_interaction_sprite:
                            if collided_interaction_sprite[0].name == 'school_entry':
                                    self.change = True
                                    self.school_entrance = True
                            if collided_interaction_sprite[0].name == 'sevenseven_entry':
                                    self.change = True
                                    self.sevenseven_entrance = True
                            if collided_interaction_sprite[0].name == 'ahamart_entry':
                                    self.change = True
                                    self.ahamart_entrance = True
                            if collided_interaction_sprite[0].name == 'truck':
                                for truck in self.truck_sprites.sprites():
                                    if truck.rect.collidepoint(self.target_pos):
                                        truck.truck_empty()              
    def get_status(self):
        if self.direction.magnitude() == 0:
            self.status = self.status.split('_')[0] + '_idle'
        if self.timers['tool use'].active:
            self.status = self.status.split('_')[0] + '_' + self.selected_tool
        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle','_attack')
                else:
                    self.status = self.status + '_attack'
            else:
                if 'attack' in self.status:
                    self.status = self.status.replace('_attack','')
    def update_timers(self):
        for timer in self.timers.values():
            timer.update()
    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if not self.vulnerable:
            if current_time - self.hurt_time >= self.invincibility_duration:
                self.vulnerable = True
        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False  
        if not self.can_switch_magic:
            if current_time - self.magic_switch_time >= self.switch_duration_cooldown:
                self.can_switch_magic = True          
    def hit_reaction(self):
        if not self.vulnerable:
            self.direction *= -3
    def energy_recovery(self):
        if self.energy < self.stats['energy']:
            self.energy += 0.01 * self.stats['magic']
        else:
            self.energy = self.stats['energy']	
    def update(self, dt):
        with open('modernload_file.txt','w') as load_file:
            json.dump({"pos_x": self.pos.x,"pos_y": self.pos.y,"anim_status":self.status}, load_file)
        self.input(dt)
        self.get_status()
        self.update_timers()
        self.get_target_pos()
        self.move(dt)
        self.hit_reaction()
        self.cooldowns()
        self.animate(dt)
