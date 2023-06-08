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


class Player_school(Entity):
    def __init__(self, pos, group, collision_sprites, interaction,display_surface):
        super().__init__(group)
        load={
            'pos_x':1283.2,
            'pos_y':2374.35,
            'anim_status':'up_idle'
        }
        try:
            with open('schoolload_file.txt') as load_file:
                load = json.load(load_file)
        except:
            print('No file created yet')
        self.import_assets()
        self.status = load['anim_status']
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)
        self.z = LAYERS['main']
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.pos.x=load['pos_x']
        self.pos.y=load['pos_y']
        self.stats = {'health': 200, 'energy': 60, 'attack': 10, 'magic': 4}
        self.max_stats = {'health': 300, 'energy': 140, 'attack': 20, 'magic' : 10}
        self.health = self.stats['health']
        self.energy = self.stats['energy']
        self.speed = 280  
        self.attacking = False
        self.attack_cooldown = 300
        self.attack_time = None
        self.magic_index = 0
        self.magic = list(magic_data.keys())[self.magic_index]
        self.can_switch_magic = True
        self.magic_switch_time = None	
        self.switch_duration_cooldown = 200      
        self.hitbox = self.rect.copy().inflate((-126,-70))
        self.collision_sprites = collision_sprites
        self.timers = {
            'tool use': Timer(300,self.use_tool),
            'tool switch': Timer(200)
        }
        self.tools = ['axe', 'hoe', 'spear']
        self.tool_index = 0
        self.selected_tool = self.tools[self.tool_index]
        self.interaction = interaction
        self.display_surface = display_surface
        self.animation_player = AnimationPlayer()
        self.dialogue = dialogue_manager(self.display_surface)
        self.change = False
        self.school_entrance = False
        self.bosslib_entrance = False
        self.speaking = False
        self.weapon_attack_sound = pygame.mixer.Sound('audio/sword.wav')
        self.weapon_attack_sound.set_volume(0.4)
    def use_tool(self):
        pass
    def get_target_pos(self):
        self.target_pos = self.rect.center + PLAYER_TOOL_OFFSET[self.status.split('_')[0]]
        self.target_pos_spear = self.rect.center + SPEAR_TOOL_OFFSET[self.status.split('_')[0]]
    def import_assets(self):
        self.animations = {'up': [],'down': [],'left': [],'right': [],
                           'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
                           'right_hoe':[],'left_hoe':[],'up_hoe':[],'down_hoe':[],
                           'right_axe':[],'left_axe':[],'up_axe':[],'down_axe':[],
                           'right_spear':[],'left_spear':[],'up_spear':[],'down_spear':[]}
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
                if keys[pygame.K_RETURN]:
                        collided_interaction_sprite = pygame.sprite.spritecollide(self,self.interaction,False)
                        if collided_interaction_sprite:
                            if collided_interaction_sprite[0].name == 'school_entrance_exit':
                                    self.change = True
                                    self.school_entrance = True
                            if collided_interaction_sprite[0].name == 'bosslib_entry':
                                    self.change = True
                                    self.bosslib_entrance = True              
    def get_status(self):
        if self.direction.magnitude() == 0:
            self.status = self.status.split('_')[0] + '_idle'
        if self.timers['tool use'].active:
            self.status = self.status.split('_')[0] + '_' + self.selected_tool
    def update_timers(self):
        for timer in self.timers.values():
            timer.update()
    def update(self, dt):
        with open('schoolload_file.txt','w') as load_file:
            json.dump({"pos_x": self.pos.x,"pos_y": self.pos.y,"anim_status":self.status}, load_file)
        self.input(dt)
        self.get_status()
        self.update_timers()
        self.get_target_pos()
        self.move(dt)
        self.animate(dt)
