import pygame, sys
from settings import *
from player import *
from sprites import *
from support import *
from pytmx.util_pygame import load_pygame
from dialogue import *
from overlay_cave import *
from particles import *
from player_cave import *
from transition import *
from monster import monster
from text_overlay import text_overlay
from quest import *
from lesson import *
from progresbar import progressbar
from tutorial import tutorial
from magic import MagicPlayer
from salitasabato import writings
from review_q import reviewc

class Level_cave:
	def __init__(self, map_status, lesson_log):
		# get the display surface
		self.display_surface = pygame.display.get_surface()
		self.b_time = pygame.time.get_ticks()

		# sprite groups
		self.all_sprites = CameraGroup()
		self.collision_sprites = pygame.sprite.Group()
		self.interaction_sprites = pygame.sprite.Group()
		self.rocks_sprites = pygame.sprite.Group()

		self.monster_sprites = pygame.sprite.Group()
		self.essence_sprites = pygame.sprite.Group()
		self.keys_sprites = pygame.sprite.Group()
#bago##############################################
		self.attack_sprites = pygame.sprite.Group()
		self.attackable_sprites = pygame.sprite.Group()
########################################################

		self.setup()
		self.overlay = Overlay_cave(self.player)

		self.animation_player = AnimationPlayer()
		self.map_status = map_status
		self.transition = Transition(self.enter_cave, self.player)

		self.text_overlay = text_overlay()
		self.progress_bar = progressbar()

		self.questlog = quest_log()
		self.lesson_log = lesson_log

		self.quest_log_active = False
		self.lesson_log_active = False

		self.lesson2 = lesson_group('Lesson 2', self.lesson_log)

		#Lessons2
		self.scroll_1 = Lessons('L2_Scroll_1', 'Lessons/Prelim/L2_Scroll_1.png', self.lesson2)
		self.scroll_2 = Lessons('L2_Scroll_2', 'Lessons/Prelim/L2_Scroll_2.png', self.lesson2)
		self.scroll_3 = Lessons('L2_Scroll_3', 'Lessons/Prelim/L2_Scroll_3.png', self.lesson2)

		self.writing = writings("writing_1","graphics/rock_tablet.png",self.player)


		self.fire_fireworks = fireworks_animation()
		self.fire_fireworks1 = fireworks_animation()
		self.tower_fireworks = fireworks_animation()
	

		#Questssss
		self.main_objective1 = objectives('Gather all the missing parts of\nthe sword in the four timelines')
		self.main_objective2 = objectives('Defeat the monster that\ncaused the apocalypse')
		self.main_quest = quest('The Sword of Salvation', 'You have embarked on a journey through time\nto retrieve the missing fragments of a\npowerful sword.', [self.main_objective1,self.main_objective2])
		self.questlog.add_primary_quest(self.main_quest)

		self.tower_objective1 = objectives('Gather 2 GEMS and place them on the\ntower to activate it')
		self.quest_tower = quest('Wizard\'s Tower', 'You find ancient scriptures in a hidden cave that\nspeak of the legendary Gem of Lightning.', [self.tower_objective1])

		self.fire_objective1 = objectives('Activate the fire on the ancient brazier\ngather 3 FIRE ESSENCE')
		self.fire_objective2 = objectives('Activate the fire on the ancient brazier\ngather 3 FIRE ESSENCE')
		self.quest_fire = quest('The Brazier', 'According to the ancient scriptures to get the\ngem you must lit up the fire in the ancient brazier', [self.fire_objective1, self.fire_objective2])
		

		self.tower_new_animation = newquest_animation(self.display_surface)
		self.fire_new_animation = newquest_animation(self.display_surface)

		self.tower_complete_animation = questcomplete_animation(self.display_surface)
		self.fire_complete_animation = questcomplete_animation(self.display_surface)

		self.objective_complete_list = []

		self.tutorial_tower = tutorial('quest_tower', 'graphics/tutorial/Tutorial_cave1.png')
		self.tutorial_fire = tutorial('quest_fire', 'graphics/tutorial/Tutorial_cave2.png')

#bago#################
		self.magic_player = MagicPlayer(self.animation_player)
		
		self.music = pygame.mixer.Sound('audio/samples/Space travel.mp3')
		self.music.play(loops = -1)

		self.open_log = pygame.mixer.Sound('audio/sound_effects/open_log.mp3')

		self.tower_dialogue_finished = False
		self.fire_dialogue_finished = False

		self.spawn = False
		self.spawn_1 = False

		self.transition_death = Transition_death(self.reset, self, self.player)
		self.player_dead = False

		self.flame_on = False
		self.flame1_on = False
		
		self.reviewcave = reviewc("lesson_2","graphics/questlog/page copy.png",self.player)

	def setup(self):

		tmx_data = load_pygame('data/tmx/cave.tmx')
		
		# collion tiles
		for x, y, surf in tmx_data.get_layer_by_name('collisions').tiles():
			collisions_cave((x * TILE_SIZE, y * TILE_SIZE),pygame.Surface((TILE_SIZE, TILE_SIZE)) ,self.collision_sprites)

		#rocks
		for obj in tmx_data.get_layer_by_name('rocks'):
			self.rocks = rocks((obj.x, obj.y), obj.image , [self.all_sprites, self.collision_sprites, self.rocks_sprites])

		tower_frames = []
		for i in range(0, 42):
			tower_frames.append(pygame.image.load('graphics/Tower 2.0/'+str(i)+'.png'))
		for obj in tmx_data.get_layer_by_name('tower'):
			self.tower = tower((obj.x, obj.y), tower_frames, [self.all_sprites, self.collision_sprites])

		# fire
		for obj in tmx_data.get_layer_by_name('fire'):
			if obj.name == 'fire':
				self.fire = fire((obj.x, obj.y), obj.image, [self.all_sprites, self.collision_sprites])
			if obj.name == 'fire1':
				self.fire1 = fire1((obj.x, obj.y), obj.image, [self.all_sprites, self.collision_sprites])

		# monster 
		for obj in tmx_data.get_layer_by_name('monsters'):
			if obj.name == 'squid': monster_name = 'squid'
			elif obj.name == 'bamboo': monster_name = 'bamboo'
			elif obj.name == 'spirit1': monster_name = 'spirit1'
			else: monster_name = 'spirit'
#may dinagdag sa groups ng monster############################################
			monster(monster_name= monster_name, 
	   				pos= (obj.x,obj.y), 
					groups= [self.all_sprites, self.monster_sprites, self.attackable_sprites], 
					collision_sprites= self.collision_sprites, 
					trigger_death_particles= self.trigger_death_particles, 
					essence_group= self.essence_sprites,
					damage_player= self.damage_player,
					key_group= self.keys_sprites)

		# Player 
		for obj in tmx_data.get_layer_by_name('player'):
			if obj.name == 'start':
				self.player = Player_cave(pos = (obj.x,obj.y), 
					group = self.all_sprites, 
					collision_sprites= self.collision_sprites,
					monster= self.monster_sprites,
					tower_rise= self.tower_rise,
					interaction= self.interaction_sprites,
					fire= self.start_fire,
					essence= self.essence_sprites,
					display_surface= self.display_surface,
					key_sprites= self.keys_sprites,
					create_magic= self.create_magic)
#########################dinagdag ang create magic##########################
			if obj.name == 'tower':
				Interaction((obj.x,obj.y), (obj.width,obj.height), self.interaction_sprites, obj.name)

			if obj.name == 'fire':
				Interaction((obj.x,obj.y), (obj.width,obj.height), self.interaction_sprites, obj.name)
			if obj.name == 'fire1':
				Interaction((obj.x,obj.y), (obj.width,obj.height), self.interaction_sprites, obj.name)
			
			if obj.name == 'change_map':
				Interaction((obj.x,obj.y), (obj.width,obj.height), self.interaction_sprites, obj.name)
			
			if obj.name == 'savepoint':
				Interaction((obj.x,obj.y), (obj.width,obj.height), self.interaction_sprites, obj.name)
			if obj.name == 'savepoint1':
				Interaction((obj.x,obj.y), (obj.width,obj.height), self.interaction_sprites, obj.name)

		
 
		Generic(
			pos = (0,0),
			surf = pygame.image.load('data/cave.png').convert_alpha(),
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



	def tower_rise(self, player):
		self.tower.tower_animation(player)

	def start_fire(self):
		if self.player.fire_collide:
			self.fire.start_fire()
			

		if self.player.fire1_collide:
			self.fire1.start_fire()	

	def destroy_rocks(self):
		for rocks in self.rocks_sprites.sprites():
			rocks.particles()
			rocks.kill()

	def trigger_death_particles(self, pos, particle_type):

		self.animation_player.create_particles(particle_type, pos, self.all_sprites)

#may dinagdag ##################################
	def damage_player(self, amount ,attack_type):
		if self.player.vulnerable:
			self.player.health -= amount
			self.player.vulnerable = False
			self.player.hurt_time = pygame.time.get_ticks()
			self.animation_player.create_particles(attack_type, self.player.rect.center, [self.all_sprites])
			
	def enter_cave(self):
		self.map_status('cave1')
		self.music.stop()

	def toggle_questlog(self):
		self.open_log.play()
		self.quest_log_active = not self.quest_log_active

	def show_lesson(self):
		self.open_log.play()
		self.lesson_log_active = not self.lesson_log_active

	def take_quest(self, dt):
		if self.player.quest_tower:
			self.tower_dialogue_finished = True
			if self.quest_tower not in self.questlog.primary_quest:
				self.questlog.add_primary_quest(self.quest_tower)
			self.tower_new_animation.update(dt)
			if self.tower_new_animation.finished:
				self.tutorial_tower.display()
		
		if self.player.quest_fire:
			self.fire_dialogue_finished = True
			if self.quest_fire not in self.questlog.quests:
				self.questlog.add_quest(self.quest_fire)
			self.fire_new_animation.update(dt)
			if self.fire_new_animation.finished:
				self.tutorial_fire.display()

	def check_quest_objectives(self, dt):
		
		if self.player.questtower_gather:
			self.tower_objective1.complete()
			if self.tower_objective1.description not in self.objective_complete_list:
				self.objective_complete_list.append(self.tower_objective1.description)
				self.progress_bar.get_progress(115)
################################### binago ko sa pag show nila ng lesson$$$$$$$$$$$$$$$$$$$#########
		if self.player.questfire_ignite:
			self.flame_on = True
			self.fire_objective1.complete()
			if self.fire_objective1.description not in self.objective_complete_list:
				self.objective_complete_list.append(self.fire_objective1.description)
				self.progress_bar.get_progress(115)
			self.fire_fireworks.update(dt)
			if self.fire_fireworks.finished:
				if not self.player.questfire_ignite1:
					self.scroll_2.display()
					if self.scroll_2 not in self.lesson2.lessons: 
						self.lesson2.add_lesson(self.scroll_2)
				else:
					self.scroll_3.display()
					if self.scroll_3 not in self.lesson2.lessons: 
						self.lesson2.add_lesson(self.scroll_3)
					
		if self.player.questfire_ignite1:
			self.flame1_on = True
			self.fire_objective2.complete()
			if self.fire_objective2.description not in self.objective_complete_list:
				self.objective_complete_list.append(self.fire_objective2.description)
				self.progress_bar.get_progress(115)
			self.fire_fireworks1.update(dt)
			if self.fire_fireworks1.finished:
				if not self.player.questfire_ignite:
					self.scroll_2.display()
					if self.scroll_2 not in self.lesson2.lessons: 
						self.lesson2.add_lesson(self.scroll_2)
				else:
					self.scroll_3.display()
					if self.scroll_3 not in self.lesson2.lessons: 
						self.lesson2.add_lesson(self.scroll_3)
#####################################################################################
		if self.player.for_lesson:
			self.tower_fireworks.update(dt)
			if self.tower_fireworks.finished:
				self.scroll_1.display()
				if self.scroll_1 not in self.lesson2.lessons: 
					self.lesson2.add_lesson(self.scroll_1)


	def check_quest(self,dt):
		if self.player.questtower_complete:
			self.tower_complete_animation.update(dt)
		
		if self.player.questfire_complete:
			self.fire_complete_animation.update(dt)
			
##############binago ko lang ang position##########################
	def quest_indicator(self):
		if self.questlog.new_quest:
			img = pygame.image.load('graphics/overlay/new.png').convert_alpha()
			img_rect = img.get_rect(midtop = (53, SCREEN_HEIGHT/2 - 160))

			self.c_time = pygame.time.get_ticks()
			if ((self.c_time - self.b_time) % 1000) < 500 :
				self.display_surface.blit(img, img_rect)
###################################################

	def save_interaction(self):
		collided_interaction_sprite = pygame.sprite.spritecollide(self.player,self.interaction_sprites,False)
		if collided_interaction_sprite:
			if collided_interaction_sprite[0].name == 'savepoint':
				self.spawn = True
			if collided_interaction_sprite[0].name == 'savepoint1':
				self.spawn_1 = True


		if self.flame_on and not self.flame1_on:
			self.spawn_1 = False
		if self.flame1_on and not self.flame_on:
			self.spawn = False


	def player_death(self):
		if self.player.health <= 0:
			for sprite in self.monster_sprites.sprites():
				sprite.direction.x = 0
				sprite.direction.y = 0
				
			self.player.kill()
			self.player_dead = True
			

	def reset(self):
		self.player.restoration = True
		for sprite in self.monster_sprites.sprites():
			sprite.kill()
		self.monster_sprites.empty()

		for essence in self.essence_sprites.sprites():
			essence.kill()
		self.essence_sprites.empty()

		for key in self.keys_sprites.sprites():
			key.kill()
		self.keys_sprites.empty()

		tmx_data = load_pygame('data/tmx/cave.tmx')

		if self.spawn:
			for obj in tmx_data.get_layer_by_name('player'):
				if obj.name == 'spawn':
					self.player = Player_cave(pos = (obj.x,obj.y), 
						group = self.all_sprites, 
						collision_sprites= self.collision_sprites,
						monster= self.monster_sprites,
						tower_rise= self.tower_rise,
						interaction= self.interaction_sprites,
						fire= self.start_fire,
						essence= self.essence_sprites,
						display_surface= self.display_surface,
						key_sprites= self.keys_sprites,
						create_magic= self.create_magic)	
			
				
		if self.spawn_1:
			for obj in tmx_data.get_layer_by_name('player'):
				if obj.name == 'spawn1':
					self.player = Player_cave(pos = (obj.x,obj.y), 
						group = self.all_sprites, 
						collision_sprites= self.collision_sprites,
						monster= self.monster_sprites,
						tower_rise= self.tower_rise,
						interaction= self.interaction_sprites,
						fire= self.start_fire,
						essence= self.essence_sprites,
						display_surface= self.display_surface,
						key_sprites= self.keys_sprites,
						create_magic= self.create_magic)
			

		# monster 
		for obj in tmx_data.get_layer_by_name('monsters'):
			if obj.name == 'squid': monster_name = 'squid'
			elif obj.name == 'bamboo': monster_name = 'bamboo'
			elif obj.name == 'spirit1': monster_name = 'spirit1'
			else: monster_name = 'spirit'
#
			monster(monster_name= monster_name, 
					pos= (obj.x,obj.y), 
					groups= [self.all_sprites, self.monster_sprites, self.attackable_sprites], 
					collision_sprites= self.collision_sprites, 
					trigger_death_particles= self.trigger_death_particles, 
					essence_group= self.essence_sprites,
					damage_player= self.damage_player,
					key_group= self.keys_sprites)
			
		self.overlay = Overlay_cave(self.player)
		self.reviewcave = reviewc("lesson_2","graphics/questlog/page copy.png",self.player)
		self.player.tower_dialogue = True
		self.player.fire1_interaction = True
		self.player.fire1_interaction = True

		if self.flame_on and not self.flame1_on:
			self.player.questfire_ignite = True
			self.player.item_inventory['gem'] += 1
			self.player.item_inventory['keys'] += 1
			# self.spawn_1 = False
		if self.flame1_on and not self.flame_on:
			self.player.questfire_ignite1 = True
			self.player.item_inventory['gem'] += 1
			# self.spawn = False
		
	def review_question(self):
		if self.player.test:
			self.reviewcave.active = True

		if self.player.passed:
			self.destroy_rocks()

	def run(self,dt):
	
		self.running = True
		if self.lesson2 not in self.lesson_log.lesson_groups:
			self.lesson_log.add_lesson_group(self.lesson2)

		self.display_surface.fill('#0a0909')
		self.all_sprites.custom_draw(self.player)
####################################
		self.player_death()
		self.save_interaction()
###################################
		self.overlay.display()
		self.progress_bar.draw()


		if self.quest_log_active:
			self.questlog.display()
		elif self.lesson_log_active:
			self.lesson_log.display()
		elif self.reviewcave.active:
			self.reviewcave.display()
		else:
			self.all_sprites.update(dt)
			self.all_sprites.monster_update(self.player)
	
		if self.player.change:
			self.transition.play()
		
		if self.player_dead:
			self.transition_death.play()
			
		self.take_quest(dt)
		self.quest_indicator()
		self.player_attack_logic()
		self.check_quest_objectives(dt)
		self.review_question()
	


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
					# 	target_pos = offset_rect.center + SPEAR_TOOL_OFFSET[player.status.split('_')[0]]
					# 	pygame.draw.circle(self.display_surface,'blue',target_pos,5)

	def monster_update(self, player):
		monster_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'monster']
		for wildboar in monster_sprites:
			wildboar.monster_update(player)
		return monster_sprites


