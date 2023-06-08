import pygame
from settings import *
from support import *
from timer import Timer
from particles import *
from random import randint
from dialogue import *
from entity import Entity

class Player_cave(Entity):
	def __init__(self, pos, group, collision_sprites, monster, tower_rise, interaction, fire, essence, display_surface, key_sprites, create_magic):
		super().__init__(group)

		self.display_surface = display_surface

		self.frame_index = 0
		self.direction = pygame.math.Vector2()
		self.import_assets()
		self.status = 'down_idle'
		

		# general setup
		self.image = self.animations[self.status][self.frame_index]
		self.rect = self.image.get_rect(center = pos)
		self.z = LAYERS['main']

		# movement attributes
		self.direction = pygame.math.Vector2()
		self.pos = pygame.math.Vector2(self.rect.center)
		self.speed = 320		

		# collision
		self.collision_sprites = collision_sprites
		self.hitbox = self.rect.copy().inflate((-126,-70))

#BAGO KO PONG DAGDAG ^^V###########################
        #stats
		self.stats = {'health': 200, 'energy': 60, 'attack': 10, 'magic': 4}
		self.max_stats = {'health': 300, 'energy': 140, 'attack': 20, 'magic' : 10}
		self.health = self.stats['health']
		self.energy = self.stats['energy']
		self.speed = 280	

		# magic 
		self.attacking = False
		self.attack_cooldown = 300
		self.attack_time = None
		self.create_magic = create_magic
		self.magic_index = 0
		self.magic = list(magic_data.keys())[self.magic_index]
		self.can_switch_magic = True
		self.magic_switch_time = None	
		self.switch_duration_cooldown = 200
####################################################

        # timers 
		self.timers = {
			'tool use': Timer(300,self.use_tool),
			'tool switch': Timer(200)
		}

		# tools 
		self.tools = ['axe']
		self.tool_index = 0
		self.selected_tool = self.tools[self.tool_index]

		self.monster = monster
		self.tower_rise = tower_rise
		self.interaction = interaction
		self.fire = fire
		self.fire_collide = False
		self.fire1_collide = False	

		self.essence = essence
		self.key_sprites = key_sprites

		# inventory
		self.item_inventory = {
			'essence': 0,
			'gem': 0,
			'keys': 0
		}

		self.had_essence = False
		self.had_gem = False
		self.had_key = False

		self.vulnerable = True
		self.hurt_time = None
		self.invincibility_duration = 300

		self.change = False
		self.tower_writing1 = False

		self.dialogue = dialogue_manager(self.display_surface)

		self.success = pygame.mixer.Sound('audio/success.wav')

		self.fire_interaction = False
		self.fire1_interaction = False

		self.quest_tower = False
		self.questtower_gather = False
		self.questtower_complete = False

		self.quest_fire = False
		self.questfire_ignite = False
		self.questfire_ignite1 = False
		self.questfire_complete = False

		self.reviewtime= False
		self.continueanim = False

		self.for_lesson = False
		self.text_overlay = text_overlay()
##########bagong sound#################
		self.weapon_attack_sound = pygame.mixer.Sound('audio/sword.wav')
		self.weapon_attack_sound.set_volume(0.4)

		self.restoration = False
		self.tower_dialogue = False

		self.retry = False
		self.test = False

		self.passed =False
		self.failed = False
	

	def use_tool(self):
	
		if self.selected_tool == 'axe':
			for monster in self.monster.sprites():
				if monster.rect.colliderect(self.rect):
					monster.get_damage(self, 'axe')
##################nilagyan ng attack type sa get damage#####################

	def import_assets(self):
		self.animations = {'up': [],'down': [],'left': [],'right': [],
						   'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
						   'right_hoe':[],'left_hoe':[],'up_hoe':[],'down_hoe':[],
						   'right_axe':[],'left_axe':[],'up_axe':[],'down_axe':[],
							'right_attack':[],'left_attack':[],'up_attack':[],'down_attack':[]}
############################maydinagdag sa folder##################
		for animation in self.animations.keys():
			full_path = 'graphics/player/' + animation
			self.animations[animation] = import_folder(full_path)

	def animate(self,dt):
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

	def input(self):
		keys = pygame.key.get_pressed()

		if self.dialogue.dialogue is None:
			if not self.timers['tool use'].active:
				# directions 
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

				# tool use
				if keys[pygame.K_SPACE]:
########################################################					
					self.timers['tool use'].activate()
					self.weapon_attack_sound.play()
					self.direction = pygame.math.Vector2()
					self.frame_index = 0

				# change tool
				if keys[pygame.K_q] and not self.timers['tool switch'].active:
					self.timers['tool switch'].activate()
					self.tool_index += 1
					self.tool_index = self.tool_index if self.tool_index < len(self.tools) else 0
					self.selected_tool = self.tools[self.tool_index]

#BAGO##################################################
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
######################################################################################

				if keys[pygame.K_RETURN]:
					collided_interaction_sprite = pygame.sprite.spritecollide(self,self.interaction,False)
					if collided_interaction_sprite:
						if collided_interaction_sprite[0].name == 'tower':
							if self.item_inventory['gem'] >= 2:
								self.questtower_complete = True
								self.tower_rise(self)
								self.item_inventory['gem'] -= 2
								self.questtower_gather = True
							
							if self.failed:
								self.dialogue.dialogue_complete.remove("Wizard tower_failed")
								self.test = True

						if collided_interaction_sprite[0].name == 'fire':
							if self.item_inventory['essence'] >= 3:
								self.fire_collide = True
								self.fire()
								self.item_inventory['essence'] -= 3
								self.item_inventory['gem'] += 1
								self.questfire_ignite = True
						
						if collided_interaction_sprite[0].name == 'fire1':
							if self.item_inventory['essence'] >= 3:
								self.fire1_collide = True
								self.fire()
								self.item_inventory['essence'] -= 3
								self.item_inventory['gem'] += 1
								self.questfire_ignite1 = True
					
						
				
	def get_status(self):
		
		# idle
		if self.direction.magnitude() == 0:
			self.status = self.status.split('_')[0] + '_idle'

		# tool use
		if self.timers['tool use'].active  and not self.attacking:
			self.status = self.status.split('_')[0] + '_' + self.selected_tool

#BAGO###########################################
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
##########################################################

	def update_timers(self):
		for timer in self.timers.values():
			timer.update()

	def get_essence(self):
		for essence in self.essence.sprites():
			if essence.rect.colliderect(self.hitbox):
				self.success.play()
				essence.kill()
				self.item_inventory['essence'] += 1

	def get_key(self):
		for key in self.key_sprites.sprites():
			if key.rect.colliderect(self.hitbox):
				self.success.play()
				key.kill()
				self.item_inventory['keys'] += 1

	def check_inventory(self):
		if self.item_inventory['essence'] >= 1:
			self.had_essence = True
		else:
			self.had_essence = False

		if self.item_inventory['gem'] >= 1:
			self.had_gem = True
		else:
			self.had_gem = False

		if self.item_inventory['keys'] >= 1:
			self.had_key = True
		else:
			self.had_key = False


	def cooldowns(self):
		current_time = pygame.time.get_ticks()
		if not self.vulnerable:
			if current_time - self.hurt_time >= self.invincibility_duration:
				self.vulnerable = True

#BAGO#################################################
		if self.attacking:
			if current_time - self.attack_time >= self.attack_cooldown:
				self.attacking = False
    

		if not self.can_switch_magic:
			if current_time - self.magic_switch_time >= self.switch_duration_cooldown:
				self.can_switch_magic = True
	
############################################################
	
	def hit_reaction(self):
		if not self.vulnerable:
			self.direction *= -3

	def change_map(self):
		collided_interaction_sprite = pygame.sprite.spritecollide(self,self.interaction,False)
		if collided_interaction_sprite:
			if collided_interaction_sprite[0].name == 'change_map':
				self.direction.x = 0
				self.direction.y = 0
				self.change = True

	def interaction_cave(self):
		collided_interaction_sprite = pygame.sprite.spritecollide(self,self.interaction,False)
		if collided_interaction_sprite:
			if collided_interaction_sprite[0].name == 'tower':

				if not self.tower_dialogue:
					self.tower_dialogue = True
					self.dialogue.start_dialogue(dialogue_cave_tower(self))
					self.direction.x = 0
					self.direction.y = 0


				

			if collided_interaction_sprite[0].name == 'fire':
				if not self.fire1_interaction and not self.fire_interaction:
					self.dialogue.start_dialogue(dialogue_brazier(self))
					self.fire_interaction = True
					self.direction.x = 0
					self.direction.y = 0

				if self.item_inventory['essence'] >= 3:
					if not self.fire_collide:
						self.text_overlay.draw('Interact[Enter]', (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 250))
			
			if collided_interaction_sprite[0].name == 'fire1':
				if not self.fire_interaction and not self.fire1_interaction:
					self.dialogue.start_dialogue(dialogue_brazier(self))
					self.fire1_interaction = True
					self.direction.x = 0
					self.direction.y = 0

				if self.item_inventory['essence'] >= 3:
					if not self.fire1_collide:
						self.text_overlay.draw('Interact[Enter]', (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 250))
			

			if collided_interaction_sprite[0].name == 'tower':
				if self.item_inventory['gem'] >= 2:
					if not self.questtower_gather:
						self.text_overlay.draw('Interact[Enter]', (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 250))
					
		if self.reviewtime:
			self.dialogue.start_dialogue(dialogue_wizard_tower(self))

		if self.continueanim:
			self.dialogue.start_dialogue(dialogue_wizard_tower_passed(self))

		if self.retry:
			self.dialogue.start_dialogue(dialogue_wizard_tower_failed(self))



##########bago to#######################			
	def energy_recovery(self):
		if self.energy < self.stats['energy']:
			self.energy += 0.01 * self.stats['magic']
		else:
			self.energy = self.stats['energy']
############################################
	def restore_life(self):
		self.health = self.stats['health']
		self.energy = self.stats['energy']
				
					
					
	def check_objectives(self):
		if self.fire_collide == True and self.fire1_collide == True:
			self.questfire_complete = True

		if self.item_inventory['essence'] >= 3:
			self.for_lesson = True
		
				
			
	def update(self, dt):
		self.input()
		self.get_status()
		self.update_timers()
		self.move(dt)
		self.hit_reaction()
		self.cooldowns()
		self.change_map()
		self.check_objectives()
		self.energy_recovery()

		self.animate(dt)
		self.get_essence()
		self.get_key()
		self.check_inventory()
		self.interaction_cave()

		self.dialogue.update()
		self.dialogue.draw()
