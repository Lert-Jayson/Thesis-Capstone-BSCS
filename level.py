import pygame, json
from settings import *
from player import *
from sprites import *
from support import *
from pytmx.util_pygame import load_pygame
from overlay import *
from dialogue import *
from npc import *
from soil import SoilLayer
from particles import *
from transition import *
from text_overlay import text_overlay
from quest import *
from lesson import *
from progresbar import progressbar
from timer import Timer
from tutorial import tutorial
from review_q import review
from map import Map_toggle
from magic import MagicPlayer

class Level:
	def __init__(self, map_status, lesson_log):
		self.running = False
		
		# get the display surface
		self.display_surface = pygame.display.get_surface()
		self.timer = Timer(200)

		self.font = pygame.font.Font('font/Almendra-Bold.ttf', 24)

		# sprite groups
		self.all_sprites = CameraGroup()
		self.collision_sprites = pygame.sprite.Group()
		self.tree_sprites = pygame.sprite.Group()
		self.interaction_sprites = pygame.sprite.Group()
		self.wildboar_sprites = pygame.sprite.Group()
		self.waterjar_sprites = pygame.sprite.Group()
		self.npc_sprites = pygame.sprite.Group()

		self.quest_grass_sprites = pygame.sprite.Group()
		self.grass_sprites = pygame.sprite.Group()
		self.speech_sprites = pygame.sprite.Group()

		self.fireworks_sprites = pygame.sprite.Group()
#bago##############################################
		self.attack_sprites = pygame.sprite.Group()
		self.attackable_sprites = pygame.sprite.Group()
########################################################
		self.soil_layer = SoilLayer(self.all_sprites)
		self.setup()

		self.overlay = Overlay(self.player)
		self.text_overlay = text_overlay()
		self.progress_bar = progressbar()

		self.start = True
		self.dialogue = dialogue_manager(self.display_surface)

		self.questlog = quest_log()
		self.lesson_log = lesson_log

		try:
			with open('load_file.txt') as load_file:
				secondload = json.load(load_file)
		except:
			secondload= {'animation_done':[]}
		self.animation_done = secondload['animation_done']
		

		#particles
		self.animation_player = AnimationPlayer()
		self.map_status = map_status
		self.transition = Transition(self.enter_cave, self.player)

		self.texts = [
			'Press Enter to speak',
			'Press Enter to enter cave',
			'Press Enter to get water'
		]

		self.game_paused = False
		self.lesson_active = False
		self.maptoggle_active = False

		self.map_toggle = Map_toggle('graphics/map_toggle.png')

		self.b_time = pygame.time.get_ticks()

		self.success = pygame.mixer.Sound('audio/success.wav')
		self.success.set_volume(0.3)

		self.tutorial_start = tutorial('start', 'graphics/tutorial/Tutorial Health.png')
		self.tutorial_trees = tutorial('quest_trees', 'graphics/tutorial/Tutorial_trees.png')
		self.tutorial_farm = tutorial('quest_farm', 'graphics/tutorial/Tutorial_farm.png')
		self.tutorial_water = tutorial('quest_water', 'graphics/tutorial/Tutorial_water.png')
		self.tutorial_hunt = tutorial('quest_hunt', 'graphics/tutorial/Tutorial_hunt.png')

		self.lessonlol = review("lesson_1","graphics/questlog/page copy.png",self.player)

		#Questssss
		self.main_objective1 = objectives('Gather all the missing parts of\nthe sword in the four timelines')
		self.main_objective2 = objectives('Defeat the monster that\ncaused the apocalypse')
		self.main_quest = quest('The Sword of Salvation', 'You have embarked on a journey through time\nto retrieve the missing fragments of a\npowerful sword.', [self.main_objective1,self.main_objective2])

		self.help_objective1 = objectives('Help the villagers from their own\nindividual task')
		self.help_objective2 = objectives('Go back to the chief after you help\nthe villagers')
		self.quest_chief = quest('The Chief', 'To gain the chief trust and learn the location\nof the sword fragments, you must follow\nthe chief instructions.', [self.help_objective1, self.help_objective2])
		
		self.trees_objective1 = objectives('Gather ten(10) woods by cutting trees')
		self.trees_objective2 = objectives('Deliver the gathered woods to\nmonkey')
		self.quest_trees = quest('Woods', 'The chief of the village said monkey needs\nhelp to cut some trees', [self.trees_objective1,self.trees_objective2])
	
		self.farm_objective1 = objectives('Clear all the Grass in a the\ngiven area')
		self.farm_objective2 = objectives('After you clear the grass, dig up\nthe soil in the given area')
		self.quest_farm = quest('Farming', 'You help chicken farmer clear up the land\nfor him to plant crops for\nthe village', [self.farm_objective1,self.farm_objective2])
		
		self.water_objective1 = objectives('Get the water from the river above\nand put it to the empty jar')
		self.quest_water = quest('Water', 'You help rabbit to get water for the village.\nYou must get water and pour it into the jar\nuntil it was all full', [self.water_objective1])
	
		self.hunt_objective1 = objectives('Your goal is to gather at least\n8 pieces of meat.')
		self.hunt_objective2 = objectives('Deliver it to the chicken hunter')
		self.quest_hunt = quest('Hunting', 'You have accepted the mission of aiding the\nchicken hunter in gathering meat for the village.', [self.hunt_objective1,self.hunt_objective2])
	
		#Lesson Group
		self.lesson1 = lesson_group('Lesson 1', self.lesson_log)
		self.lesson_log.add_lesson_group(self.lesson1)
		
		#Lessons
		self.scroll1 = Lessons('L1_Scroll_1', 'Lessons/Prelim/L1_Scroll_1.png', self.lesson1)
		self.scroll2 = Lessons('L1_Scroll_2', 'Lessons/Prelim/L1_Scroll_2.png', self.lesson1)
		self.scroll3 = Lessons('L1_Scroll_3', 'Lessons/Prelim/L1_Scroll_3.png', self.lesson1)
		self.scroll4 = Lessons('L1_Scroll_4', 'Lessons/Prelim/L1_Scroll_4.png', self.lesson1)
		self.scroll5 = Lessons('L1_Scroll_5', 'Lessons/Prelim/L1_Scroll_5.png', self.lesson1)
		self.scroll6 = Lessons('L1_Scroll_6', 'Lessons/Prelim/L1_Scroll_6.png', self.lesson1)
		self.scroll7 = Lessons('L1_Scroll_7', 'Lessons/Prelim/L1_Scroll_7.png', self.lesson1)
		self.scroll8 = Lessons('L1_Scroll_8', 'Lessons/Prelim/L1_Scroll_8.png', self.lesson1)



		self.trees_fireworks = fireworks_animation()
		self.trees_fireworks1 = fireworks_animation()
		self.farm_fireworks = fireworks_animation()
		self.farm_fireworks1 = fireworks_animation()
		self.water_fireworks = fireworks_animation()
		self.water_fireworks1 = fireworks_animation()
		self.hunt_fireworks = fireworks_animation()
		self.hunt_fireworks1 = fireworks_animation()

		self.tree_complete_animation = questcomplete_animation(self.display_surface)
		self.farm_complete_animation = questcomplete_animation(self.display_surface)
		self.water_complete_animation = questcomplete_animation(self.display_surface)
		self.hunt_complete_animation = questcomplete_animation(self.display_surface)

		self.main_new_animation = newquest_animation(self.display_surface)
		self.chief_new_animation = newquest_animation(self.display_surface)
		self.tree_new_animation = newquest_animation(self.display_surface)
		self.farm_new_animation = newquest_animation(self.display_surface)
		self.water_new_animation = newquest_animation(self.display_surface)
		self.hunt_new_animation = newquest_animation(self.display_surface)

		self.objective_complete_list = []

#bago#################
		self.magic_player = MagicPlayer(self.animation_player)
########################################################################
		self.music = pygame.mixer.Sound('audio/samples/Welcome Space Traveler.mp3')
		self.music.play(loops = -1)

		self.lesson_sound = pygame.mixer.Sound('audio/sound_effects/lesson.wav')
		self.quest_complete_sound = pygame.mixer.Sound('audio/sound_effects/quest_complete.wav')
		self.open_log = pygame.mixer.Sound('audio/sound_effects/open_log.mp3')
		
		self.transition_death = Transition_death(self.reset, self, self.player)
		self.player_dead = False
###################################################################	
		self.complete_animation_list = []
# 	
# 	
	def setup(self):

		tmx_data = load_pygame('data/tmx/1stmap.tmx')
			
		portal_frames = []
		for i in range(0, 13):
			portal_frames.append(pygame.image.load('graphics/portal/'+str(i)+'.png'))
		for obj in tmx_data.get_layer_by_name('portal'):
			portal((obj.x, obj.y), portal_frames, self.all_sprites)

		# water 
		water_frames = import_folder('graphics/tilesets/water/')
		for x, y, surf in tmx_data.get_layer_by_name('water').tiles():
			Water((x * TILE_SIZE,y * TILE_SIZE), water_frames, self.all_sprites)

		# houses 
		for obj in tmx_data.get_layer_by_name('houses'):
			Generic((obj.x, obj.y), obj.image, [self.all_sprites, self.collision_sprites])	

		# statues 
		for obj in tmx_data.get_layer_by_name('statues'):
			Generic((obj.x, obj.y), obj.image, [self.all_sprites, self.collision_sprites])

		# plants
		for x, y, surf in tmx_data.get_layer_by_name('plants').tiles():
			Generic((x * TILE_SIZE,y * TILE_SIZE), surf, [self.all_sprites, self.collision_sprites])

		# grass destructable
		for x, y, surf in tmx_data.get_layer_by_name('Grass Destructable').tiles():
			grass((x * TILE_SIZE,y * TILE_SIZE), surf, [self.all_sprites, self.collision_sprites, self.grass_sprites, self.attackable_sprites])

		#quest farm
		for x, y, surf in tmx_data.get_layer_by_name('quest farm').tiles():
			grass_quest((x * TILE_SIZE,y * TILE_SIZE), surf, [self.all_sprites, self.collision_sprites, self.quest_grass_sprites, self.attackable_sprites])

		# fences 
		for obj in tmx_data.get_layer_by_name('fences'):
			Generic((obj.x, obj.y), obj.image, self.all_sprites)

		# trees 
		for obj in tmx_data.get_layer_by_name('trees decor'):
			Generic((obj.x, obj.y), obj.image, [self.all_sprites, self.collision_sprites])

		# trees killable
		for obj in tmx_data.get_layer_by_name('killable tree'):
			Tree((obj.x, obj.y), obj.image, [self.all_sprites, self.collision_sprites, self.tree_sprites], obj.name, self.player_add)
#############naglagay ako ng function sa parameters$#############################################
		# water jar
		for obj in tmx_data.get_layer_by_name('water jar'):
			if obj.name == 'waterjar':
				self.water_jar = WaterJar((obj.x, obj.y), obj.image, [self.all_sprites, self.collision_sprites, self.waterjar_sprites], obj.name, self.player_add)
########################################################################

		# collion tiles
		for x, y, surf in tmx_data.get_layer_by_name('collisions').tiles():
			collisions((x * TILE_SIZE, y * TILE_SIZE),pygame.Surface((TILE_SIZE, TILE_SIZE)) ,self.collision_sprites)

		# wild boar 
		for obj in tmx_data.get_layer_by_name('wildboar'):
			if obj.name == 'wildboar':
#may dinagdag sa groups ng wildboar############################################
				self.wildboar = wildboar(pos=(obj.x,obj.y), 
			     						groups=[self.all_sprites, self.wildboar_sprites, self.attackable_sprites],
										collision_sprites= self.collision_sprites, 
										trigger_death_particles= self.trigger_death_particles, 
										player_add= self.player_add, 
										damage_player= self.damage_player)


		# npc 
		for obj in tmx_data.get_layer_by_name('entities'):
			if obj.name == 'npc1': npc_name = 'monkey'
			elif obj.name == 'npc_guard': npc_name = 'koala'
			elif obj.name == 'npc_chief': npc_name = 'chief'
			elif obj.name == 'npc_farm': npc_name = 'chicken2'
			elif obj.name == 'npc_water': npc_name = 'rabbit'
			elif obj.name == 'npc_hunt': npc_name = 'chicken'
			else: npc_name = 'mammoth'

			self.npc = NPC(npc_name, (obj.x,obj.y),[ self.all_sprites, self.collision_sprites, self.npc_sprites], self.interaction_sprites)


		# Player 
		for obj in tmx_data.get_layer_by_name('player'):
			if obj.name == 'start':
				self.player = Player(	
					pos = (obj.x,obj.y), 
					group = self.all_sprites, 
					collision_sprites = self.collision_sprites,
					tree_sprites = self.tree_sprites,
					grass_sprites= self.grass_sprites,
					interaction = self.interaction_sprites,
					display_surface= self.display_surface, 
					soil_layer= self.soil_layer,
					wildboar= self.wildboar_sprites,  
					waterjar_sprites= self.waterjar_sprites, 
					quest_grass_sprites= self.quest_grass_sprites,
					create_magic= self.create_magic)
###################dinagdag ang create magic########################				
			if obj.name == 'starting':
				Interaction((obj.x,obj.y), (obj.width,obj.height), self.interaction_sprites, obj.name)
			
			if obj.name == 'npc1':
				Interaction((obj.x,obj.y), (obj.width,obj.height), self.interaction_sprites, obj.name)

			if obj.name == 'npc_guard':
				Interaction((obj.x,obj.y), (obj.width,obj.height), self.interaction_sprites, obj.name)

			if obj.name == 'npc_chief':
				Interaction((obj.x,obj.y), (obj.width,obj.height), self.interaction_sprites, obj.name)
			
			if obj.name == 'npc_water':
				Interaction((obj.x,obj.y), (obj.width,obj.height), self.interaction_sprites, obj.name)

			if obj.name == 'npc_farm':
				Interaction((obj.x,obj.y), (obj.width,obj.height), self.interaction_sprites, obj.name)

			if obj.name == 'npc_hunt':
				Interaction((obj.x,obj.y), (obj.width,obj.height), self.interaction_sprites, obj.name)


			if obj.name == 'cave':
				Interaction((obj.x,obj.y), (obj.width,obj.height), self.interaction_sprites, obj.name)

			if obj.name == 'water_jar':
				Interaction((obj.x,obj.y), (obj.width,obj.height), self.interaction_sprites, obj.name)

		Generic(
			pos = (0,0),
			surf = pygame.image.load('data/mapa.png').convert_alpha(),
			groups = self.all_sprites,
			z = LAYERS['ground'])
#bago######33333333333##########################		
	def player_attack_logic(self):
		if self.attack_sprites:
			for attack_sprite in self.attack_sprites:
				collision_sprites = pygame.sprite.spritecollide(attack_sprite, self.attackable_sprites, False)
				if collision_sprites:
					for target_sprite in collision_sprites:
						if target_sprite.sprite_type == 'grass':
							pos = target_sprite.rect.center
							offset = pygame.math.Vector2(0, 75)
							for leaf in range(randint(3, 6)):
								self.animation_player.create_grass_particles(pos - offset, [self.all_sprites])
							target_sprite.kill()
						elif target_sprite.sprite_type == 'grass_quest':
							if self.player.farm_active:
								pos = target_sprite.rect.center
								offset = pygame.math.Vector2(0, 75)
								for leaf in range(randint(3, 6)):
									self.animation_player.create_grass_particles(pos - offset, [self.all_sprites])
								target_sprite.destroy()
						else:
							target_sprite.get_damage(self.player, 'magic')


	def create_magic(self, style, strength, cost):
		if style == 'heal':
			self.magic_player.heal(self.player, strength, cost, [self.all_sprites])

		if style == 'flame':
			self.magic_player.flame(self.player, cost, [self.all_sprites, self.attack_sprites])

#################################################################################
	def take_quest(self, dt):
		load= {'tutorial_done':[]}
		try:
			with open('tutorialload_file.txt') as load_file:
				load = json.load(load_file)
		except:
			pass
		
		if self.player.main_quest:
			if self.main_quest not in self.questlog.primary_quest:
				self.questlog.add_primary_quest(self.main_quest)
			if 'main' not in self.animation_done:
				self.main_new_animation.update(dt)
			if self.main_new_animation.finished and self.tutorial_start.name not in load['tutorial_done']:
				self.tutorial_start.display()
				if 'main' not in self.animation_done:
					self.animation_done.append('main')

		if self.player.chief_quest:
			if self.quest_chief not in self.questlog.primary_quest:
				self.questlog.add_primary_quest(self.quest_chief)
			if 'chief' not in self.animation_done:
				self.chief_new_animation.update(dt)
				if 'main' not in self.animation_done:
					self.animation_done.append('chief')

		if self.player.quest_trees:
			if self.quest_trees not in self.questlog.quests:
				self.questlog.add_quest(self.quest_trees)
			if 'trees' not in self.animation_done:
				self.tree_new_animation.update(dt)
			if self.tree_new_animation.finished and self.tutorial_trees.name not in load['tutorial_done']:
				self.tutorial_trees.display()
				if 'trees' not in self.animation_done:
					self.animation_done.append('trees')

		if self.player.quest_farm:
			if self.quest_farm not in self.questlog.quests:
				self.questlog.add_quest(self.quest_farm)
			if 'farm' not in self.animation_done:
				self.farm_new_animation.update(dt)
			if self.farm_new_animation.finished and self.tutorial_farm.name not in load['tutorial_done']:
				self.tutorial_farm.display()
				if 'farm' not in self.animation_done:
					self.animation_done.append('farm')

		if self.player.quest_waterjar:
			if self.quest_water not in self.questlog.quests:
				self.questlog.add_quest(self.quest_water)
			if 'water' not in self.animation_done:
				self.water_new_animation.update(dt)
			if self.water_new_animation.finished and self.tutorial_water.name not in load['tutorial_done']:
				self.tutorial_water.display()
				if 'water' not in self.animation_done:
					self.animation_done.append('water')

		if self.player.quest_hunt:
			if self.quest_hunt not in self.questlog.quests:
				self.questlog.add_quest(self.quest_hunt)
			if 'hunt' not in self.animation_done:
				self.hunt_new_animation.update(dt)
			if self.hunt_new_animation.finished and self.tutorial_hunt.name not in load['tutorial_done']:
				self.tutorial_hunt.display()
				if 'hunt' not in self.animation_done:
					self.animation_done.append('hunt')

	def check_quest_objectives(self, dt):
		load= {'lesson_done':[]}
		try:
			with open('lessonload_file.txt') as load_file:
				load = json.load(load_file)
		except:
			pass
		#quest trees
		if self.player.questtrees_gather:
			self.trees_objective1.complete()
			if self.trees_objective1.description not in self.objective_complete_list:
				self.objective_complete_list.append(self.trees_objective1.description)
				self.progress_bar.get_progress(115)
				self.lesson_sound.play()
			self.trees_fireworks.update(dt)
			if self.trees_fireworks.finished and self.scroll1.name not in load['lesson_done']:
				self.scroll1.display()
				if self.scroll1 not in self.lesson1.lessons: 
					self.lesson1.add_lesson(self.scroll1)
			
		if self.player.questtrees_deliver:
			self.trees_objective2.complete()
			if self.trees_objective2.description not in self.objective_complete_list:
				self.objective_complete_list.append(self.trees_objective2.description)
				self.progress_bar.get_progress(115)
		
		#quest farm 
		if self.player.questfarm_grass_cleared:
			self.farm_objective1.complete()
			if self.farm_objective1.description not in self.objective_complete_list:
				self.objective_complete_list.append(self.farm_objective1.description)
				self.progress_bar.get_progress(115)
				self.lesson_sound.play()
			self.farm_fireworks.update(dt)
			if self.farm_fireworks.finished and self.scroll3.name not in load['lesson_done']:
				self.scroll3.display()
				if self.scroll3 not in self.lesson1.lessons: 
					self.lesson1.add_lesson(self.scroll3)
		if self.player.questfarm_soil_cutivated:
			self.farm_objective2.complete()
			if self.farm_objective2.description not in self.objective_complete_list:
				self.objective_complete_list.append(self.farm_objective2.description)
				self.progress_bar.get_progress(115)
				self.lesson_sound.play()
			self.farm_fireworks1.update(dt)
			if self.farm_fireworks1.finished and self.scroll4.name not in load['lesson_done']:
				self.scroll4.display()
				if self.scroll4 not in self.lesson1.lessons: 
					self.lesson1.add_lesson(self.scroll4)

		if self.player.questwaterjar_have_water:
			self.water_objective1.complete()
			if self.water_objective1.description not in self.objective_complete_list:
				self.objective_complete_list.append(self.water_objective1.description)
				self.progress_bar.get_progress(115)
				self.lesson_sound.play()
			self.water_fireworks.update(dt)
			if self.water_fireworks.finished and self.scroll5.name not in load['lesson_done']:
				self.scroll5.display()
				if self.scroll5 not in self.lesson1.lessons: 
					self.lesson1.add_lesson(self.scroll5)

		#quest hunt
		if self.player.questhunt_kill:
			self.hunt_objective1.complete()
			if self.hunt_objective1.description not in self.objective_complete_list:
				self.objective_complete_list.append(self.hunt_objective1.description)
				self.progress_bar.get_progress(115)
				self.lesson_sound.play()
			self.hunt_fireworks.update(dt)
			if self.hunt_fireworks.finished and self.scroll7.name not in load['lesson_done']:
				self.scroll7.display()
				if self.scroll7 not in self.lesson1.lessons: 
					self.lesson1.add_lesson(self.scroll7)
		if self.player.questhunt_deliver:
			self.hunt_objective2.complete()
			if self.hunt_objective2.description not in self.objective_complete_list:
				self.objective_complete_list.append(self.hunt_objective2.description)
				self.progress_bar.get_progress(115)
			self.help_objective1.complete()
			if self.help_objective1.description not in self.objective_complete_list:
				self.objective_complete_list.append(self.help_objective1.description)
				self.progress_bar.get_progress(115)

		if self.player.chief_second_dialogue_complete:
			self.lessonlol.active = True	

				
	def check_quest(self,dt):
		load= {'lesson_done':[]}
		try:
			with open('lessonload_file.txt') as load_file:
				load = json.load(load_file)
		except:
			pass
		
		if self.player.questtrees_complete:
			self.tree_complete_animation.update(dt)
			if self.tree_complete_animation.animation_complete:
				if self.tree_complete_animation not in self.complete_animation_list:
					self.complete_animation_list.append(self.tree_complete_animation)
					self.lesson_sound.play()
				self.trees_fireworks1.update(dt)
				if self.trees_fireworks1.finished and self.scroll2.name not in load['lesson_done']:
					self.scroll2.display()
					if self.scroll2 not in self.lesson1.lessons: 
						self.lesson1.add_lesson(self.scroll2)
			
		if self.player.questfarm_complete:
			self.farm_complete_animation.update(dt)
			
		if self.player.questwaterjar_complete:
			self.water_complete_animation.update(dt)
			if self.water_complete_animation.animation_complete:
				if self.water_complete_animation not in self.complete_animation_list:
					self.complete_animation_list.append(self.water_complete_animation)
					self.lesson_sound.play()
				self.water_fireworks1.update(dt)
				if self.water_fireworks1.finished and self.scroll6.name not in load['lesson_done']:
					self.scroll6.display()
					if self.scroll6 not in self.lesson1.lessons: 
						self.lesson1.add_lesson(self.scroll6)

		if self.player.questhunt_complete:
			self.hunt_complete_animation.update(dt)
			if self.hunt_complete_animation.animation_complete:
				if self.hunt_complete_animation not in self.complete_animation_list:
					self.complete_animation_list.append(self.hunt_complete_animation)
					self.lesson_sound.play()
				self.hunt_fireworks1.update(dt)
				if self.hunt_fireworks1.finished and self.scroll8.name not in load['lesson_done']:
					self.scroll8.display()
					if self.scroll8 not in self.lesson1.lessons: 
						self.lesson1.add_lesson(self.scroll8)
			
		
	def trigger_death_particles(self, pos, particle_type):

		self.animation_player.create_particles(particle_type, pos, self.all_sprites)

	def enter_cave(self):
		self.map_status('cave')
		self.music.stop()


	def player_add(self,item):

		self.player.item_inventory[item] += 1
		self.success.play()

#may dinagdag ##################################
	def damage_player(self, amount ,attack_type):
		if self.player.vulnerable:
			self.player.health -= amount
			self.player.vulnerable = False
			self.player.hurt_time = pygame.time.get_ticks()
			self.animation_player.create_particles(attack_type, self.player.rect.center, [self.all_sprites])
			
	def indicator(self):
	

		collided_interaction_sprite = pygame.sprite.spritecollide(self.player,self.interaction_sprites,False)
		if collided_interaction_sprite:
			if collided_interaction_sprite[0].name == 'cave':
					self.text_overlay.draw(self.texts[1], (self.display_surface.get_width() // 2, self.display_surface.get_height() - 250))


	def toggle_questlog(self):
		self.open_log.play()
		self.game_paused = not self.game_paused

##############binago ko lang ang position##########################
	def quest_indicator(self):
		if self.questlog.new_quest:
			img = pygame.image.load('graphics/overlay/new.png').convert_alpha()
			img_rect = img.get_rect(midtop = (53, SCREEN_HEIGHT/2 - 160))

			self.c_time = pygame.time.get_ticks()
			if ((self.c_time - self.b_time) % 1000) < 500 :
				self.display_surface.blit(img, img_rect)
###################################################

	def show_lesson(self):
		self.open_log.play()
		self.lesson_active = not self.lesson_active

	def toggle_map(self):
		self.open_log.play()
		self.maptoggle_active = not self.maptoggle_active


	def tutorial_indicator(self):
		arrowkeys_img = pygame.image.load('graphics/overlay/arrowkeys.png').convert_alpha()
		arrowkeys_rect = arrowkeys_img.get_rect(bottomright = (SCREEN_WIDTH - 50,SCREEN_HEIGHT))

		text_arrow = self.font.render('Press any arrow keys to move', True, 'white')
		text_arrow_rect = text_arrow.get_rect(midbottom = (arrowkeys_rect.midtop))

		

		if not self.player.moves:
			self.c_time = pygame.time.get_ticks()
			if ((self.c_time - self.b_time) % 1000) < 500 :
				self.display_surface.blit(text_arrow, text_arrow_rect)
				self.display_surface.blit(arrowkeys_img, arrowkeys_rect)
		
	def player_death(self):
		if self.player.health <= 0:
			for sprite in self.wildboar_sprites.sprites():
				sprite.direction.x = 0
				sprite.direction.y = 0
				
			self.player.kill()
			self.player_dead = True
			

	def reset(self):
		# self.player.pos.x = 5477.33
		# self.player.pos.y = 2593.34
		self.player.restoration = True
		for sprite in self.wildboar_sprites.sprites():
			sprite.kill()
		
		self.wildboar_sprites.empty()

		tmx_data = load_pygame('data/tmx/1stmap.tmx')

		for obj in tmx_data.get_layer_by_name('player'):
			if obj.name == 'spawn':
				self.player = Player(	
					pos = (obj.x,obj.y), 
					group = self.all_sprites, 
					collision_sprites = self.collision_sprites,
					tree_sprites = self.tree_sprites,
					grass_sprites= self.grass_sprites,
					interaction = self.interaction_sprites,
					display_surface= self.display_surface, 
					soil_layer= self.soil_layer,
					wildboar= self.wildboar_sprites,  
					waterjar_sprites= self.waterjar_sprites, 
					quest_grass_sprites= self.quest_grass_sprites,
					create_magic= self.create_magic)
			
		for obj in tmx_data.get_layer_by_name('wildboar'):
			if obj.name == 'wildboar':
				self.wildboar = wildboar(pos=(obj.x,obj.y), 
			     						groups=[self.all_sprites, self.wildboar_sprites, self.attackable_sprites],
										collision_sprites= self.collision_sprites, 
										trigger_death_particles= self.trigger_death_particles, 
										player_add= self.player_add, 
										damage_player= self.damage_player)

		
		self.player.item_inventory['meat'] = 0
		self.player.dialogue_order = 9
		self.player.hunt_active = True
		self.overlay = Overlay(self.player)
		self.lessonlol = review("lesson_1","graphics/questlog/page copy.png",self.player)

	def run(self,dt):
		#creating and updating load file
		if not self.player_dead:
			with open('load_file.txt','w') as load_file:
				json.dump({"pos_x": self.player.pos.x,"pos_y": self.player.pos.y,"anim_status":self.player.status,"dialogue_order":self.player.dialogue_order,'main_quest':self.player.main_quest,'chief_quest':self.player.chief_quest,'quest_trees':self.player.quest_trees,'tree_active':self.player.tree_active,'tree_gather':self.player.questtrees_gather,'tree_deliver':self.player.questtrees_deliver,'tree_complete':self.player.questtrees_complete,'quest_farm':self.player.quest_farm,'farmgrass_cleared':self.player.questfarm_grass_cleared,'farmsoil_cultivated':self.player.questfarm_soil_cutivated,'farm_complete':self.player.questfarm_complete,'quest_waterjar':self.player.quest_waterjar,'have_water':self.player.questwaterjar_have_water,'waterjar_complete':self.player.questwaterjar_complete,'quest_hunt':self.player.quest_hunt,'hunt_kill':self.player.questhunt_kill,'hunt_deliver':self.player.questhunt_deliver,'hunt_complete':self.player.questhunt_complete,'chief_second_dia':self.player.chief_second_dialogue_complete,'farm_active':self.player.farm_active,'water_active':self.player.water_active,'hunt_active':self.player.hunt_active,'water':self.player.water,'wood':self.player.item_inventory['wood'],'meat':self.player.item_inventory['meat'],'had_wood':self.player.had_wood,'had_meat':self.player.had_meat,'hurt_time':self.player.hurt_time,'vulnerable':self.player.vulnerable,'tool_index':self.player.tool_index,'animation_done': self.animation_done}, load_file)
		else:
			with open('load_file.txt','w') as load_file:
				json.dump({"pos_x": 5477.33,"pos_y": 2593.34,"anim_status":'down_idle',"dialogue_order":self.player.dialogue_order,'main_quest':self.player.main_quest,'chief_quest':self.player.chief_quest,'quest_trees':self.player.quest_trees,'tree_active':self.player.tree_active,'tree_gather':self.player.questtrees_gather,'tree_deliver':self.player.questtrees_deliver,'tree_complete':self.player.questtrees_complete,'quest_farm':self.player.quest_farm,'farmgrass_cleared':self.player.questfarm_grass_cleared,'farmsoil_cultivated':self.player.questfarm_soil_cutivated,'farm_complete':self.player.questfarm_complete,'quest_waterjar':self.player.quest_waterjar,'have_water':self.player.questwaterjar_have_water,'waterjar_complete':self.player.questwaterjar_complete,'quest_hunt':self.player.quest_hunt,'hunt_kill':self.player.questhunt_kill,'hunt_deliver':self.player.questhunt_deliver,'hunt_complete':self.player.questhunt_complete,'chief_second_dia':self.player.chief_second_dialogue_complete,'farm_active':self.player.farm_active,'water_active':self.player.water_active,'hunt_active':self.player.hunt_active,'water':self.player.water,'wood':self.player.item_inventory['wood'],'meat':self.player.item_inventory['meat'],'had_wood':self.player.had_wood,'had_meat':self.player.had_meat,'hurt_time':self.player.hurt_time,'vulnerable':self.player.vulnerable,'tool_index':self.player.tool_index,'animation_done': self.animation_done}, load_file)
		
		
		#end of creating and updating load file
		self.display_surface.fill('black')
		self.all_sprites.custom_draw(self.player)
		self.player_death()
		self.overlay.display()
		self.progress_bar.draw()


		if self.game_paused:
			self.questlog.display()
		elif self.lesson_active:
			self.lesson_log.display()
		elif self.maptoggle_active:
			self.map_toggle.display()
		elif self.lessonlol.active:
			self.lessonlol.display()
		else:
			self.all_sprites.update(dt)
			self.all_sprites.wildboar_update(self.player)
		#bagodagdad##############
			self.player_attack_logic()

		if self.player.change:
			self.transition.play()
		
		if self.player_dead:
			self.transition_death.play()

		self.indicator()
		self.quest_indicator()
		self.take_quest(dt)
		self.check_quest_objectives(dt)
		self.check_quest(dt)
		self.tutorial_indicator()
	


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
					# 	pygame.draw.rect(self.display_surface,'red',offset_rect,5)
					# 	hitbox_rect = player.hitbox.copy()
					# 	hitbox_rect.center = offset_rect.center
					# 	pygame.draw.rect(self.display_surface,'green',hitbox_rect,5)
					# 	target_pos = offset_rect.center + PLAYER_TOOL_OFFSET[player.status.split('_')[0]]
					# 	pygame.draw.circle(self.display_surface,'blue',target_pos,5)

	def wildboar_update(self, player):
		wildboar_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'wildboar']
		for wildboar in wildboar_sprites:
			wildboar.wildboar_update(player)
		return wildboar_sprites
	

		


