import pygame
from settings import *
from entity import Entity
from support import *
from sprites import *

class monster(Entity):
    def __init__(self, monster_name, pos ,groups, collision_sprites, trigger_death_particles, essence_group, damage_player, key_group):
        super().__init__(groups)

        self.sprite_type = 'monster'

        #graphics setup
        self.import_graphics(monster_name)
        self.status = 'idle'
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)
        self.z = LAYERS['main']

         #movement
        self.pos = pygame.math.Vector2(self.rect.center)
        self.hitbox = self.rect.inflate(0, 0)
        self.collision_sprites = collision_sprites

          #stats
        self.monster_name = monster_name
        monster_info = monster_data[self.monster_name]
        self.health = monster_info['health']
        self.speed = monster_info['speed']
        self.attack_damage = monster_info['damage']
        self.resistance = monster_info['resistance']
        self.attack_radius = monster_info['attack_radius']
        self.notice_radius = monster_info['notice_radius']
        self.attack_type = monster_info['attack_type']

        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = 400

        #invincibility timer
        self.vulnerable = True
        self.hit_time = None
        self.invincibility_duration = 300

        self.trigger_death_particles = trigger_death_particles

         # sounds
        self.death_sound = pygame.mixer.Sound('audio/death.wav')
        self.hit_sound = pygame.mixer.Sound('audio/hit.wav')
        self.attack_sound = pygame.mixer.Sound(monster_info['attack_sound'])
        self.death_sound.set_volume(0.6)
        self.hit_sound.set_volume(0.6)
        self.attack_sound.set_volume(0.6)

        self.essence_group = essence_group
        self.key_group = key_group
        self.damage_player = damage_player

    def import_graphics(self, name):
        self.animations = {'idle':[], 'move':[], 'attack':[]}
        main_path = f'graphics/monsters/{name}/'
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)

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

        if distance <= self.attack_radius and self.can_attack:
            if self.status != 'attack':
                self.frame_index = 0
            self.status = 'attack'
        elif distance <= self.notice_radius:
            self.status = 'move'
        else:
            self.status = 'idle'
###########damage pra sa player################
    def actions(self, player):
        if self.status == 'attack':
            self.attack_time = pygame.time.get_ticks()
            self.damage_player(self.attack_damage,self.attack_type)
            if player.health <= 0:
                pass
            else:
                self.attack_sound.play()
        elif self.status == 'move':
            self.direction = self.get_player_distance_direction(player)[1]
        else: 
            self.direction = pygame.math.Vector2()

    def animate(self, dt):
        animation = self.animations[self.status]

        self.frame_index += 8 * dt
        if self.frame_index >= len(animation):
            if self.status == 'attack':
                self.can_attack = False
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

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
################################bago attacktype
    def get_damage(self, player, attack_type):
        if self.vulnerable:
            self.hit_sound.play()
            self.direction = self.get_player_distance_direction(player)[1]
           
            if attack_type == 'magic':
                self.health -= 1
            else:
                self.health -= 1

            self.hit_time = pygame.time.get_ticks()
            self.vulnerable = False

    def check_death(self):
        if self.health <= 0:
            if self.monster_name == 'spirit':
                essence([self.groups()[0], self.essence_group], (self.pos.x, self.pos.y))
                self.kill()
                self.trigger_death_particles(self.rect.center, self.monster_name)
                self.death_sound.play()
            elif self.monster_name == 'spirit1' or self.monster_name == 'raccoon1':
                keys([self.groups()[0], self.key_group], (self.pos.x, self.pos.y))
                self.kill()
                self.trigger_death_particles(self.rect.center, self.monster_name)
                self.death_sound.play()
            else:
                self.kill()
                self.trigger_death_particles(self.rect.center, self.monster_name)
                self.death_sound.play()

    def hit_reaction(self):
        if not self.vulnerable:
            self.direction *= -self.resistance
            
    def update(self, dt):
        self.hit_reaction()
        self.move( dt)
        self.animate(dt)
        self.cooldowns()
        self.check_death()

    def monster_update(self, player):
        self.get_status(player)
        self.actions(player)