import pygame
from settings import *
from entity import Entity
from support import *
from timer import Timer
from particles import *
from sprites import *
from text_overlay import text_overlay

class NPC(pygame.sprite.Sprite):
    def __init__(self, npc_name, pos,  groups, interaction):
        super().__init__(groups)

        #graphics setup
        self.import_graphics(npc_name)
        self.status = 'idle'
        self.frame_index = 0
        self.npc_name = npc_name
        
		# general setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)
        self.z = LAYERS['main']

        # collision
        self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.5, -self.rect.height * 0.70)
  
        self.interaction = interaction
        self.text_indicator = text_overlay()

    def import_graphics(self, name):
        self.animations = {'idle': [], 'left': [],'right': []}
        
        for animation in self.animations.keys():
            main_path = f'graphics/NPC/{name}/' + animation
            self.animations[animation] = import_folder(main_path)

    def animate(self, dt):
        self.frame_index += 8 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0

        self.image = self.animations[self.status][int(self.frame_index)]

        
    def update(self, dt):
        self.animate(dt)
  

class wildboar(Entity):
    def __init__(self, pos,  groups , collision_sprites, trigger_death_particles, player_add, damage_player):
        super().__init__(groups)

        self.sprite_type = 'wildboar'

         #graphics setup
        self.import_graphics()
        self.status = 'Right'
        self.frame_index = 0
        
		# general setup
        self.image = self.animations[self.status][self.frame_index]
        self.z = LAYERS['main']
        self.rect = self.image.get_rect(center = pos)

        self.pos = pygame.math.Vector2(self.rect.center)
        self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.5, -self.rect.height * 0.70)
        self.collision_sprites = collision_sprites

        #stats
        self.health = 3
        self.speed = 180
    #nagdagdag###############
        self.attack_damage = 10
    ##########################
        self.attack_radius =50
        self.notice_radius = 300
        self.resistance = 3

        self.damage_player = damage_player

        self.direction = pygame.math.Vector2()

        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = 400

        #invincibility timer
        self.vulnerable = True
        self.hit_time = None
        self.invincibility_duration = 300

        self.trigger_death_particles = trigger_death_particles
        self.player_add = player_add

        self.death_sound = pygame.mixer.Sound('audio/death.wav')
        self.hit_sound = pygame.mixer.Sound('audio/hit.wav')
        self.attack_sound = pygame.mixer.Sound('audio/attack/claw.wav')
        self.death_sound.set_volume(0.6)
        self.hit_sound.set_volume(0.6)
        self.attack_sound.set_volume(0.6)

    def import_graphics(self):
        self.animations = {'Die': [],'Idle left': [],'Idle right': [],
						   'Left':[],'Right':[], 'left_attack':[], 'right_attack':[]}

        for animation in self.animations.keys():
            full_path = 'graphics/Wild Boar/' + animation
            self.animations[animation] = import_folder(full_path)

    def get_player_distance_direction(self, player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance = (player_vec - enemy_vec).magnitude()

        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        else:
            direction = pygame.math.Vector2()


        return (distance, direction)
    
    def get_status(self, player):
        distance = self.get_player_distance_direction(player)[0]
        direction_player = self.get_player_distance_direction(player)[1]

        
        if distance <= self.attack_radius and self.can_attack:
            if self.status != 'left_attack' and self.status != 'right_attack':
                self.frame_index = 0
            if direction_player.x < 0 :
                self.status = 'left_attack'
            elif direction_player.x > 0 :
                self.status = 'right_attack'
     
        elif distance <= self.notice_radius:
            if direction_player.x < 0 :
                self.status = 'Left'
            elif direction_player.x > 0 :
                self.status = 'Right'
            
  
        else:
            if direction_player.x < 0 :
                self.status = 'Idle left'
            elif direction_player.x > 0 :
                self.status = 'Idle right'
           

    def actions(self, player):
        if self.status == 'left_attack' or self.status == 'right_attack':
            self.attack_time = pygame.time.get_ticks()
        #pra sa damage ng player
            self.damage_player(self.attack_damage ,'claw')
            if player.health <= 0:
                pass
            else:
                self.attack_sound.play()
        elif self.status == 'Left':
            self.direction = self.get_player_distance_direction(player)[1]
        elif self.status == 'Right':
            self.direction = self.get_player_distance_direction(player)[1]
        else: 
            self.direction = pygame.math.Vector2()

    def animate(self, dt):
        self.frame_index += 8 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0

        self.image = self.animations[self.status][int(self.frame_index)]

    
        if not self.vulnerable:
            #flicker
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if not self.can_attack:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True

        if not self.vulnerable:
            if current_time - self.hit_time >= self.invincibility_duration:
                self.vulnerable = True

#maybago##################################################
    def get_damage(self, player, attack_type):
        if self.vulnerable:
            self.hit_sound.play()
            self.direction = self.get_player_distance_direction(player)[1]
           
            if attack_type == 'magic':
                self.health -= 2
            else:
                self.health -= 1

            self.hit_time = pygame.time.get_ticks()
            self.vulnerable = False
 #######################################################           
    def check_death(self):
        if self.health <= 0:
            self.death_sound.play()
            self.kill()
            self.trigger_death_particles(self.rect.center, 'boar')
            self.player_add('meat')

    def hit_reaction(self):
        if not self.vulnerable:
            self.direction *= -self.resistance


    def update(self, dt):
        self.hit_reaction()
        self.move(dt)
        self.animate(dt)
        self.cooldowns()
        self.check_death()

    def wildboar_update(self, player):
        self.get_status(player)
        self.actions(player)
class crow(Entity):
    def __init__(self, pos,  groups , collision_sprites, trigger_death_particles, damage_player):
        super().__init__(groups)

        self.sprite_type = 'crow'

        #graphics setup
        self.import_graphics()
        self.status = 'idle left'
        self.frame_index = 0
        
		# general setup
        self.image = self.animations[self.status][self.frame_index]
        self.z = LAYERS['main']
        self.rect = self.image.get_rect(center = pos)

        self.pos = pygame.math.Vector2(self.rect.center)
        self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.5, -self.rect.height * 0.70)
        self.collision_sprites = collision_sprites

        #stats
        self.health = 3
        self.speed = 180
        #nagdagdag###############
        self.attack_damage = 10
    ##########################
        self.attack_radius =50
        self.notice_radius = 300
        self.resistance = 3

        self.damage_player = damage_player

        self.direction = pygame.math.Vector2()

        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = 400

        #invincibility timer
        self.vulnerable = True
        self.hit_time = None
        self.invincibility_duration = 300

        self.trigger_death_particles = trigger_death_particles

        self.death_sound = pygame.mixer.Sound('audio/death.wav')
        self.hit_sound = pygame.mixer.Sound('audio/hit.wav')
        self.attack_sound = pygame.mixer.Sound('audio/attack/claw.wav')
        self.death_sound.set_volume(0.6)
        self.hit_sound.set_volume(0.6)
        self.attack_sound.set_volume(0.6)

    def import_graphics(self):
        self.animations = {'attack left':[],'attack right':[],'fly left':[],'fly right':[],'idle left':[],'idle right':[],}

        for animation in self.animations.keys():
            full_path = 'graphics/Modern monsters/crow/' + animation
            self.animations[animation] = import_folder(full_path)

    def get_player_distance_direction(self, player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance = (player_vec - enemy_vec).magnitude()

        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        else:
            direction = pygame.math.Vector2()


        return (distance, direction)
    
    def get_status(self, player):
        distance = self.get_player_distance_direction(player)[0]
        direction_player = self.get_player_distance_direction(player)[1]

        
        if distance <= self.attack_radius and self.can_attack:
            if self.status != 'attack left' and self.status != 'attack right':
                self.frame_index = 0
            if direction_player.x < 0 :
                self.status = 'attack left'
            elif direction_player.x > 0 :
                self.status = 'attack right'
     
        elif distance <= self.notice_radius:
            if direction_player.x < 0 :
                self.status = 'fly left'
            elif direction_player.x > 0 :
                self.status = 'fly right'
            
  
        else:
            if direction_player.x < 0 :
                self.status = 'idle left'
            elif direction_player.x > 0 :
                self.status = 'idle right'
           

    def actions(self, player):
        if self.status == 'attack left' or self.status == 'attack right':
            self.attack_time = pygame.time.get_ticks()
            self.damage_player(self.attack_damage,'claw')
            self.attack_sound.play()
        elif self.status == 'fly left':
            self.direction = self.get_player_distance_direction(player)[1]
        elif self.status == 'fly right':
            self.direction = self.get_player_distance_direction(player)[1]
        else: 
            self.direction = pygame.math.Vector2()

    def animate(self, dt):
        self.frame_index += 8 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0

        self.image = self.animations[self.status][int(self.frame_index)]

    
        if not self.vulnerable:
            #flicker
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if not self.can_attack:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True

        if not self.vulnerable:
            if current_time - self.hit_time >= self.invincibility_duration:
                self.vulnerable = True

    #maybago##################################################
    def get_damage(self, player, attack_type):
        if self.vulnerable:
            self.hit_sound.play()
            self.direction = self.get_player_distance_direction(player)[1]
           
            if attack_type == 'magic':
                self.health -= 2
            else:
                self.health -= 1

            self.hit_time = pygame.time.get_ticks()
            self.vulnerable = False
 #######################################################   
            
    def check_death(self):
        if self.health <= 0:
            self.death_sound.play()
            self.kill()
            self.trigger_death_particles(self.rect.center, 'crow')

    def hit_reaction(self):
        if not self.vulnerable:
            self.direction *= -self.resistance


    def update(self, dt):
        self.hit_reaction()
        self.move(dt)
        self.animate(dt)
        self.cooldowns()
        self.check_death()

    def crow_update(self, player):
        self.get_status(player)
        self.actions(player)





