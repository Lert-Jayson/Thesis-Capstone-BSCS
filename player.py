import pygame,json
from settings import *
from support import *
from timer import Timer
from particles import *
from random import randint
from dialogue import *
from entity import Entity
from sprites import *
from text_overlay import text_overlay

class Player(Entity):
	def __init__(self, pos, group, collision_sprites, tree_sprites, grass_sprites,interaction, display_surface, soil_layer, wildboar,waterjar_sprites, quest_grass_sprites, create_magic):
		super().__init__(group)

		#load file
		try:
			with open('load_file.txt') as load_file:
				load = json.load(load_file)
		except:
			load={
			'pos_x':pos[0],
			'pos_y':pos[1],
			'anim_status':'down_idle',
			'dialogue_order':0,
			'main_quest':False,
			'chief_quest':False,
			'quest_trees':False,
			'tree_active':False,
			'tree_gather':False,
			'tree_deliver':False,
			'tree_complete':False,
			'quest_farm': False,
			'farmgrass_cleared':False,
			'farmsoil_cultivated':False,
			'farm_complete':False,
			'quest_waterjar':False,
			'have_water':False,
			'waterjar_complete':False,
			'quest_hunt':False,
			'chief_second_dia':False,
			'hunt_kill':False,
			'hunt_deliver':False,
			'hunt_complete':False,
			'farm_active':False,
			'water_active':False,
			'hunt_active':False,
			'water':False,
			'wood':0,
			'meat':0,
			'had_wood':False,
			'had_meat':False,
			'hurt_time':None,
			'vulnerable':True,
			'tool_index':0,
			'animation_done':[]
		}
		#end of load file

		self.import_assets()
		self.status = load['anim_status']
		

		# general setup
		self.image = self.animations[self.status][self.frame_index]
		self.rect = self.image.get_rect(center = pos)
		self.z = LAYERS['main']

		# movement attributes
		self.direction = pygame.math.Vector2()
		self.pos = pygame.math.Vector2(self.rect.center)
		self.pos.x = load['pos_x']
		self.pos.y = load['pos_y']

		# collision
		self.hitbox = self.rect.copy().inflate((-126,-70))
		self.collision_sprites = collision_sprites

#BAGO KO PONG DAGDAG ^^V###########################
		self.retry = False
        #stats
		self.stats = {'health': 100, 'energy': 60, 'attack': 10, 'magic': 4}
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
		self.tools = ['axe', 'hoe','water']
		self.tool_index = 0
		self.selected_tool = self.tools[self.tool_index]
		

		# interaction
		self.tree_sprites = tree_sprites
		self.grass_sprites = grass_sprites
		self.wildboar = wildboar
		self.waterjar_sprites = waterjar_sprites
		self.interaction = interaction
		self.display_surface = display_surface
		self.soil_layer = soil_layer
		self.quest_grass_sprites = quest_grass_sprites

		#particles
		self.animation_player = AnimationPlayer()
		self.text_overlay = text_overlay()

		self.dialogue = dialogue_manager(self.display_surface)
		self.water = load['water']
		self.change = False
		self.speaking = False
#########################dinagdagan ko###############################
		# inventory
		self.item_inventory = {
			'wood': load['wood'],
			'meat': load['meat'],
			'water':0
		}
########################################################
		self.had_wood = load['had_wood']
		self.had_meat = load['had_meat']

		self.vulnerable = load['vulnerable']
		self.hurt_time = load['hurt_time']
		self.invincibility_duration = 300


		self.dialogue_order = load['dialogue_order']

		self.main_quest = load['main_quest']

		self.chief_quest = load['chief_quest']

		self.quest_trees = load['quest_trees']
		self.questtrees_gather = load['tree_gather']
		self.questtrees_deliver = load['tree_deliver']
		self.questtrees_complete = load['tree_complete']

		self.quest_farm = load['quest_farm']
		self.questfarm_grass_cleared = load['farmgrass_cleared']
		self.questfarm_soil_cutivated = load['farmsoil_cultivated']
		self.questfarm_complete = load['farm_complete']

		self.quest_waterjar = load['quest_waterjar']
		self.questwaterjar_have_water = load['have_water']
		self.questwaterjar_complete = load['waterjar_complete']

		self.quest_hunt = load['quest_hunt']
		self.questhunt_kill = load['hunt_kill']
		self.questhunt_deliver = load['hunt_deliver']
		self.questhunt_complete = load['hunt_complete']
		self.chief_second_dialogue_complete= load['chief_second_dia']

		self.tree_active = load['tree_active']
		self.farm_active = load['farm_active']
		self.water_active = load['water_active']
		self.hunt_active = load['hunt_active']

		self.moves = False

		self.weapon_attack_sound = pygame.mixer.Sound('audio/sword.wav')
		self.weapon_attack_sound.set_volume(0.4)

		self.watering = pygame.mixer.Sound('audio/water.mp3')
		self.watering.set_volume(0.2)

		self.restoration = False

	def use_tool(self):
		if self.selected_tool == 'water':
			if self.water == True:
				self.watering.play()
				for jar in self.waterjar_sprites.sprites():
					if jar.rect.collidepoint(self.target_pos):
						jar.water_jar()
						self.water = False

		if self.selected_tool == 'hoe':
			if self.farm_active:
				self.soil_layer.get_hit(self.target_pos)
		
		if self.selected_tool == 'axe':
			for tree in self.tree_sprites.sprites():
				if tree.rect.collidepoint(self.target_pos):
					if self.tree_active and not self.questtrees_complete:
						tree.damage()
					
			for grass in self.grass_sprites.sprites():
				if grass.rect.colliderect(self.rect):
					pos = grass.rect.center
					offset = pygame.math.Vector2(0, 75)
					for leaf in range(randint(3, 6)):
						self.animation_player.create_grass_particles(pos - offset, [self.groups()[0]])
					grass.kill()

			if self.farm_active:
				for grass_quest in self.quest_grass_sprites.sprites():
					if grass_quest.rect.colliderect(self.rect):
						pos = grass_quest.rect.center
						offset = pygame.math.Vector2(0, 75)
						for leaf in range(randint(3, 6)):
							self.animation_player.create_grass_particles(pos - offset, [self.groups()[0]])
						grass_quest.destroy()
			if self.hunt_active:
				for wildboar in self.wildboar.sprites():
					if wildboar.rect.colliderect(self.rect): 
						wildboar.get_damage(self, 'axe')
##########################################bago sa parameters ng get_damage#############

	def get_target_pos(self):

		self.target_pos = self.rect.center + PLAYER_TOOL_OFFSET[self.status.split('_')[0]]

		self.target_pos_spear = self.rect.center + SPEAR_TOOL_OFFSET[self.status.split('_')[0]]


	def import_assets(self):
		self.animations = {'up': [],'down': [],'left': [],'right': [],
						   'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
						   'right_hoe':[],'left_hoe':[],'up_hoe':[],'down_hoe':[],
						   'right_axe':[],'left_axe':[],'up_axe':[],'down_axe':[],
						   'right_attack':[],'left_attack':[],'up_attack':[],'down_attack':[],
						   'right_water':[],'left_water':[],'up_water':[],'down_water':[],}
#MAY BAGO DIN SA FOLDER

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

	def input(self, dt):
		keys = pygame.key.get_pressed()
		
		if self.dialogue.dialogue is None:

			if not self.timers['tool use'].active:
				# directions 
				if keys[pygame.K_UP]:
					self.direction.y = -1
					self.status = 'up'
					self.moves = True
				elif keys[pygame.K_DOWN]:
					self.direction.y = 1
					self.status = 'down'
					self.moves = True
				else:
					self.direction.y = 0

				if keys[pygame.K_RIGHT]:
					self.direction.x = 1
					self.status = 'right'
					self.moves = True
				elif keys[pygame.K_LEFT]:
					self.direction.x = -1
					self.status = 'left'
					self.moves = True
				else:
					self.direction.x = 0

				# tool use
				if keys[pygame.K_SPACE]:
################d2 ko nilagay ung attack sound###############					
					self.timers['tool use'].activate()
					if self.selected_tool == 'axe':
						self.weapon_attack_sound.play()
					self.direction = pygame.math.Vector2()
					self.frame_index = 0
				
				#MAGIC INPUT


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
################################################################################			

				if keys[pygame.K_RETURN]:
						#
						#dialogues
						collided_interaction_sprite = pygame.sprite.spritecollide(self,self.interaction,False)
						if collided_interaction_sprite:
							if collided_interaction_sprite[0].name == 'npc1':
								if self.dialogue_order == 0:
									self.speaking = True
									self.dialogue.start_dialogue(dialogue_npc1(self))
									self.dialogue_order = 1
								elif self.dialogue_order == 2:
									self.speaking = True
									self.dialogue.start_dialogue(dialogue_npc1_2(self))
									self.dialogue_order = 3
									self.tree_active = True
								else:
									if self.questtrees_gather and self.dialogue_order == 3:
										self.speaking = True
										self.dialogue.start_dialogue(dialogue_npc1_3(self))
										self.questtrees_deliver = True
										self.item_inventory['wood'] = 0		
										self.dialogue_order = 4

							if collided_interaction_sprite[0].name == 'npc_guard':
								if self.dialogue_order == 2:
									self.speaking = True
									self.dialogue.start_dialogue(dialogue_npcGuard_1(self))
								elif self.dialogue_order == 4:
									self.speaking = True
									self.dialogue.start_dialogue(dialogue_npcGuard_2(self))
								elif self.dialogue_order == 8:
									self.speaking = True
									self.dialogue.start_dialogue(dialogue_npcGuard_3(self))

						
						collided_interaction_sprite = pygame.sprite.spritecollide(self,self.interaction,False)
						if collided_interaction_sprite:
							if collided_interaction_sprite[0].name == 'npc_chief':
								if self.dialogue_order == 1:
									self.speaking = True
									self.dialogue.start_dialogue(dialogue_npcChief(self))
									self.dialogue_order = 2

								elif self.dialogue_order == 2:
									self.dialogue.start_dialogue(dialogue_npcChief_(self))
								
								if self.questhunt_deliver and self.dialogue_order == 10:
									self.speaking = True
									self.dialogue.start_dialogue(dialogue_npcChief1(self))
								# if self.dialogue_order == 11:
								# 	self.dialogue.start_dialogue(dialogue_npcChief2(self))
								# if self.dialogue_order == 12:
								# 	self.dialogue.start_dialogue(dialogue_npcChief3(self))
								# 	self.dialogue_order=10

								# if self.retry:
								# 	self.dialogue.dialogue_complete.remove("Chief1")
								# 	if "Chief3" in self.dialogue.dialogue_complete:
								# 		self.dialogue.dialogue_complete.remove("Chief3")
								# 		self.retry = False
									

						collided_interaction_sprite = pygame.sprite.spritecollide(self,self.interaction,False)
						if collided_interaction_sprite:
							if collided_interaction_sprite[0].name == 'npc_farm':
								if self.dialogue_order == 4:
									self.speaking = True
									self.dialogue.start_dialogue(dialogue_npcChicken1(self))
									self.dialogue_order = 5
									self.farm_active = True
								if self.questfarm_soil_cutivated and self.dialogue_order == 5:
									self.speaking = True
									self.dialogue.start_dialogue(dialogue_npcChicken1_1(self))
									self.dialogue_order = 6

						collided_interaction_sprite = pygame.sprite.spritecollide(self,self.interaction,False)
						if collided_interaction_sprite:
							if collided_interaction_sprite[0].name == 'npc_water':
								if self.dialogue_order == 6:
									self.speaking = True
									self.dialogue.start_dialogue(dialogue_npcRabbit(self))
									self.dialogue_order = 7
									
								if self.questwaterjar_have_water and self.dialogue_order == 7:
									self.speaking = True
									self.dialogue.start_dialogue(dialogue_npcRabbit_1(self))
									self.dialogue_order = 8

								
						collided_interaction_sprite = pygame.sprite.spritecollide(self,self.interaction,False)
						if collided_interaction_sprite:
							if collided_interaction_sprite[0].name == 'npc_hunt':
								if self.dialogue_order == 8 :
									self.speaking = True
									self.dialogue.start_dialogue(dialogue_npcChicken(self))
									self.hunt_active = True
									self.dialogue_order = 9

								if self.questhunt_kill and self.dialogue_order == 9:
									self.speaking = True
									self.dialogue.start_dialogue(dialogue_npcChicken_1(self))
									self.questhunt_deliver = True
									self.item_inventory['meat'] = 0
									self.dialogue_order = 10

						
						#Getwater
						collided_interaction_sprite = pygame.sprite.spritecollide(self,self.interaction,False)
						if collided_interaction_sprite:
							if collided_interaction_sprite[0].name == 'water_jar':
								if self.water_active and not self.questwaterjar_complete:
									self.water = True

						collided_interaction_sprite = pygame.sprite.spritecollide(self,self.interaction,False)
						if collided_interaction_sprite:
							if collided_interaction_sprite[0].name == 'cave':
									self.change = True
		
	def check_objectives(self):
		#quest trees
		if self.item_inventory['wood'] >= 10:
			self.questtrees_gather = True

		#quest farm
		if all(grass.killed == True for grass in self.quest_grass_sprites.sprites()):
			self.questfarm_grass_cleared = True
		if self.all_farmable_tiles_occupied(self.soil_layer):
			self.questfarm_soil_cutivated = True

		#quest water jar
		if all(jar.have_water == True for jar in self.waterjar_sprites.sprites()):
			self.questwaterjar_have_water = True
			

		#quest hunt
		if self.item_inventory['meat'] >= 8:
			self.questhunt_kill = True

	def all_farmable_tiles_occupied(self,soil_layer):
		for row in soil_layer.grid:
			for cell in row:
				if 'F' in cell and 'X' not in cell:
					return False
		return True

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

	def check_inventory(self):
		if self.item_inventory['wood'] >= 1:
			self.had_wood = True
		else:
			self.had_wood = False
		
		if self.item_inventory['meat'] >= 1:
			self.had_meat = True
		else:
			self.had_meat = False

	def guard_dialogue(self):
		collided_interaction_sprite = pygame.sprite.spritecollide(self,self.interaction,False)
		if collided_interaction_sprite:
			if collided_interaction_sprite[0].name == 'npc_guard':
				self.direction.x = 0
				self.direction.y = 0
				self.dialogue.start_dialogue(dialogue_npcGuard())

	def start_actions(self):
		collided_interaction_sprite = pygame.sprite.spritecollide(self,self.interaction,False)
		if collided_interaction_sprite:
			if collided_interaction_sprite[0].name == 'starting':
				self.direction.x = 0
				self.direction.y = 0
				self.dialogue.start_dialogue(dialogue_self(self))

	def text_indicator(self):
		if self.dialogue_order == 11:
			self.dialogue.start_dialogue(dialogue_npcChief2(self))
		if self.dialogue_order == 12:
			self.dialogue.start_dialogue(dialogue_npcChief3(self))
			self.dialogue_order=10

		if self.retry:
			self.dialogue.dialogue_complete.remove("Chief1")
			if "Chief3" in self.dialogue.dialogue_complete:
				self.dialogue.dialogue_complete.remove("Chief3")
				self.retry = False
		
		collided_interaction_sprite = pygame.sprite.spritecollide(self,self.interaction,False)
		if collided_interaction_sprite:
			if collided_interaction_sprite[0].name == 'npc1':
				if self.dialogue_order == 0:
					if not self.speaking:
						self.text_overlay.draw('Interact[Enter]', (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 250))
				if self.dialogue_order == 2:
					if not self.speaking:
						self.text_overlay.draw('Interact[Enter]', (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 250))
				if self.questtrees_gather and self.dialogue_order == 3	:
					if not self.speaking:
						self.text_overlay.draw('Interact[Enter]', (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 250))	
			
			if collided_interaction_sprite[0].name == 'npc_chief':
				if self.dialogue_order == 1:
					if not self.speaking:
						self.text_overlay.draw('Interact[Enter]', (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 250))

			if collided_interaction_sprite[0].name == 'npc_farm':
				if self.dialogue_order == 4:
					if not self.speaking:
						self.text_overlay.draw('Interact[Enter]', (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 250)) 

				if self.questfarm_soil_cutivated and self.dialogue_order == 5:
					if not self.speaking:
						self.text_overlay.draw('Interact[Enter]', (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 250)) 


			if collided_interaction_sprite[0].name == 'npc_water':
				if self.dialogue_order == 6:
					if not self.speaking:
						self.text_overlay.draw('Interact[Enter]', (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 250))
				if self.questwaterjar_have_water and self.dialogue_order == 7:
					if not self.speaking:
						self.text_overlay.draw('Interact[Enter]', (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 250))



			if collided_interaction_sprite[0].name == 'npc_hunt':
				if self.dialogue_order == 8 :
					if not self.speaking:
						self.text_overlay.draw('Interact[Enter]', (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 250))
				if self.questhunt_kill and self.dialogue_order == 9:
					if not self.speaking:
						self.text_overlay.draw('Interact[Enter]', (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 250))
#bago###############################################################
			if collided_interaction_sprite[0].name == 'water_jar':
				if self.water_active and not self.questwaterjar_complete and not self.water:
					self.text_overlay.draw('Get Water[Enter]', (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 250))
#############################################################

	def energy_recovery(self):
		if self.energy < self.stats['energy']:
			self.energy += 0.01 * self.stats['magic']
		else:
			self.energy = self.stats['energy']
	
	def restore_life(self):
		self.health = self.stats['health']
		self.energy = self.stats['energy']

	def update(self, dt):
		
		self.input(dt)
		self.get_status()
		self.update_timers()
		self.get_target_pos()
		self.check_inventory()
		self.cooldowns()
		self.check_objectives()
		self.energy_recovery()

		self.move(dt)
		self.animate(dt)

		self.start_actions()
		self.guard_dialogue()
		self.dialogue.update()
		self.dialogue.draw()
		self.text_indicator()

		

	