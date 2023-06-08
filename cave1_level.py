from settings import *
from player import *
from sprites import *
from support import *
from pytmx.util_pygame import load_pygame
from dialogue import *
from overlay_cave import *
from particles import *
from player_cave1 import *
from transition import *
from monster import monster
from text_overlay import text_overlay
from quest import *
from lesson import *
from progresbar import progressbar
from tutorial import tutorial
from magic import MagicPlayer

class Level_cave1:
	def __init__(self, map_status, lesson_log):
		self.running = True

		
		# get the display surface
		self.display_surface = pygame.display.get_surface()

		# sprite groups
		self.all_sprites = CameraGroup()
		self.collision_sprites = pygame.sprite.Group()
		self.interaction_sprites = pygame.sprite.Group()

		self.monster_sprites = pygame.sprite.Group()
		self.essence_sprites = pygame.sprite.Group()
		self.chest_sprites = pygame.sprite.Group()
		self.keys_sprites = pygame.sprite.Group()
#bago##############################################
		self.attack_sprites = pygame.sprite.Group()
		self.attackable_sprites = pygame.sprite.Group()
########################################################

		self.setup()


		self.animation_player = AnimationPlayer()
		self.map_status = map_status
		self.transition = Transition(self.enter_cave, self.player)

		self.overlay = Overlay_cave(self.player)
		self.text_overlay = text_overlay()
		self.progress_bar = progressbar()
		self.progress_bar.get_progress(345)
#######################dinagdagan ko ng progress pra galing kunware sa kabila
		self.questlog = quest_log()
		self.lesson_log = lesson_log

		self.quest_log_active = False
		self.lesson_log_active = False

		self.lesson3 = lesson_group('Lesson 3', self.lesson_log)

		#Lessons2
		self.scroll_1 = Lessons('L3_Scroll_1', 'Lessons/Prelim/L3_Scroll_1.png', self.lesson3)
		self.scroll_2 = Lessons('L3_Scroll_2', 'Lessons/Prelim/L3_Scroll_2.png', self.lesson3)
		self.scroll_3 = Lessons('L3_Scroll_3', 'Lessons/Prelim/L3_Scroll_3.png', self.lesson3)
		self.scroll_4 = Lessons('L3_Scroll_4', 'Lessons/Prelim/L3_Scroll_4.png', self.lesson3)
		self.scroll_5 = Lessons('L3_Scroll_5', 'Lessons/Prelim/L3_Scroll_5.png', self.lesson3)

		self.fireworks_1 = fireworks_animation()
		self.fireworks_2= fireworks_animation()
		self.fireworks_3= fireworks_animation()
		self.fireworks_4= fireworks_animation()
		self.fireworks_5= fireworks_animation()
	

		#Questssss
		self.main_objective1 = objectives('Gather all the missing parts of\nthe sword in the four timelines')
		self.main_objective2 = objectives('Defeat the monster that\ncaused the apocalypse')
		self.main_quest = quest('The Sword of Salvation', 'You have embarked on a journey through time\nto retrieve the missing fragments of a\npowerful sword.', [self.main_objective1,self.main_objective2])
		self.questlog.add_primary_quest(self.main_quest)

		self.chest_objective1 = objectives('Get the key from the giant monster\nand open all the chest that you can find')
		self.quest_chest = quest('Treasure Chest', 'You find a treasure chest and once you open it\nstrength flows through you. ', [self.chest_objective1])

		self.new_animation = newquest_animation(self.display_surface)
		
		self.complete_animation = questcomplete_animation(self.display_surface)

		self.objective_complete_list = []

		self.tutorial = tutorial('quest_chest', 'graphics/tutorial/Tutorial_cave3.png')

#bago#################
		self.magic_player = MagicPlayer(self.animation_player)
		self.music = pygame.mixer.Sound('audio/samples/Space travel.mp3')
		self.music.play(loops = -1)

		self.open_log = pygame.mixer.Sound('audio/sound_effects/open_log.mp3')

		self.transition_death = Transition_death(self.reset, self, self.player)
		self.player_dead = False
	
		
	def setup(self):

		tmx_data = load_pygame('data/tmx/cave1.tmx')
		
                #Chest
		for obj in tmx_data.get_layer_by_name('chest'):
			Treasure_chest((obj.x, obj.y), obj.image , [self.all_sprites, self.collision_sprites, self.chest_sprites], obj.name)

		eyes_frames = []
		for i in range(0, 19):
			eyes_frames.append(pygame.image.load('graphics/cave/eyes/'+str(i)+'.png'))
		for obj in tmx_data.get_layer_by_name('eyes'):
			Eyes((obj.x, obj.y), eyes_frames, self.all_sprites)


		# collision tiles
		for x, y, surf in tmx_data.get_layer_by_name('collisions').tiles():
			collisions_cave((x * TILE_SIZE, y * TILE_SIZE),pygame.Surface((TILE_SIZE, TILE_SIZE)) ,self.collision_sprites)

        		#rocks
		for obj in tmx_data.get_layer_by_name('rocks'):
			self.rocks = Generic((obj.x, obj.y), obj.image , [self.all_sprites, self.collision_sprites])

        # cliff tiles
		for x, y, surf in tmx_data.get_layer_by_name('cliff_decor').tiles():
			Generic((x * TILE_SIZE, y * TILE_SIZE),surf ,self.all_sprites, z = LAYERS['soil water'])

        # bridge tiles
		for x, y, surf in tmx_data.get_layer_by_name('bridge').tiles():
			Generic((x * TILE_SIZE, y * TILE_SIZE),surf ,self.all_sprites, z = LAYERS['ground plant'])


 		# monster 
		for obj in tmx_data.get_layer_by_name('monsters'):
			if obj.name == 'squid': monster_name = 'squid'
			elif obj.name == 'bamboo': monster_name = 'bamboo'
			elif obj.name == 'raccoon': monster_name = 'raccoon'
			elif obj.name == 'raccoon1': monster_name = 'raccoon1'
			else: monster_name = 'spirit'

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
				self.player = Player_cave1(pos = (obj.x,obj.y), 
					group = self.all_sprites, 
					collision_sprites= self.collision_sprites,
					monster= self.monster_sprites,
					interaction= self.interaction_sprites,
					essence= self.essence_sprites,
		            chest_sprites= self.chest_sprites, 
					display_surface= self.display_surface, 
					key_sprites= self.keys_sprites,
					create_magic= self.create_magic)
				
			if obj.name == 'finalboss':
				Interaction((obj.x,obj.y), (obj.width,obj.height), self.interaction_sprites, obj.name)
				
			if obj.name == 'chest1':
				Interaction((obj.x,obj.y), (obj.width,obj.height), self.interaction_sprites, obj.name)
			if obj.name == 'chest2':
				Interaction((obj.x,obj.y), (obj.width,obj.height), self.interaction_sprites, obj.name)
			if obj.name == 'chest3':
				Interaction((obj.x,obj.y), (obj.width,obj.height), self.interaction_sprites, obj.name)
			if obj.name == 'chest4':
				Interaction((obj.x,obj.y), (obj.width,obj.height), self.interaction_sprites, obj.name)
			if obj.name == 'chest5':
				Interaction((obj.x,obj.y), (obj.width,obj.height), self.interaction_sprites, obj.name)


		Generic(
			pos = (0,0),
			surf = pygame.image.load('data/cave1.png').convert_alpha(),
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

########################################
		
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
		self.map_status('boss1')
		self.music.stop()

	def take_quest(self, dt):
		if self.player.quest_chest:
			if self.quest_chest not in self.questlog.quests:
				self.questlog.add_quest(self.quest_chest)
			self.new_animation.update(dt)
			if self.new_animation.finished:
				self.tutorial.display()

	def opened_chest(self, dt):
		if self.player.chest1_open:
			self.fireworks_1.update(dt)
			if self.fireworks_1.finished:
				self.scroll_1.display()
				if self.scroll_1 not in self.lesson3.lessons: 
					self.lesson3.add_lesson(self.scroll_1)
					self.progress_bar.get_progress(115)

		if self.player.chest2_open:
			self.fireworks_2.update(dt)
			if self.fireworks_2.finished:
				self.scroll_2.display()
				if self.scroll_2 not in self.lesson3.lessons: 
					self.lesson3.add_lesson(self.scroll_2)
					self.progress_bar.get_progress(115)

		if self.player.chest3_open:
			self.fireworks_3.update(dt)
			if self.fireworks_3.finished:
				self.scroll_3.display()
				if self.scroll_3 not in self.lesson3.lessons: 
					self.lesson3.add_lesson(self.scroll_3)
					self.progress_bar.get_progress(115)

		if self.player.chest4_open:
			self.fireworks_4.update(dt)
			if self.fireworks_4.finished:
				self.scroll_4.display()
				if self.scroll_4 not in self.lesson3.lessons: 
					self.lesson3.add_lesson(self.scroll_4)
					self.progress_bar.get_progress(115)

		if self.player.chest5_open:
			self.fireworks_5.update(dt)
			if self.fireworks_5.finished:
				self.scroll_5.display()
				if self.scroll_5 not in self.lesson3.lessons: 
					self.lesson3.add_lesson(self.scroll_5)
					self.progress_bar.get_progress(115)

	def check_quest(self):
		if self.player.questchest_complete:
			self.chest_objective1.complete()

	def toggle_questlog(self):
		self.open_log.play()
		self.quest_log_active = not self.quest_log_active

	def show_lesson(self):
		self.open_log.play()
		self.lesson_log_active = not self.lesson_log_active

##############binago ko lang ang position##########################
	def quest_indicator(self):
		if self.questlog.new_quest:
			img = pygame.image.load('graphics/overlay/new.png').convert_alpha()
			img_rect = img.get_rect(midtop = (53, SCREEN_HEIGHT/2 - 160))

			self.c_time = pygame.time.get_ticks()
			if ((self.c_time - self.b_time) % 1000) < 500 :
				self.display_surface.blit(img, img_rect)
###################################################
	def player_death(self):
		if self.player.health <= 0:
			for sprite in self.monster_sprites.sprites():
				sprite.direction.x = 0
				sprite.direction.y = 0
				
			self.player.kill()
			self.player_dead = True
			

	def reset(self):
		self.lesson3.remove_lesson()
		self.player.restoration = True
		for sprite in self.monster_sprites.sprites():
			sprite.kill()
		self.monster_sprites.empty()

		for chest_sprite in self.chest_sprites.sprites():
			chest_sprite.kill()
		self.chest_sprites.empty()

		for key in self.keys_sprites.sprites():
			key.kill()
		self.keys_sprites.empty()

		for essence in self.essence_sprites.sprites():
			essence.kill()
		self.essence_sprites.empty()


		tmx_data = load_pygame('data/tmx/cave1.tmx')

		for obj in tmx_data.get_layer_by_name('player'):
			if obj.name == 'spawn':
				self.player = Player_cave1(pos = (obj.x,obj.y), 
					group = self.all_sprites, 
					collision_sprites= self.collision_sprites,
					monster= self.monster_sprites,
					interaction= self.interaction_sprites,
					essence= self.essence_sprites,
		            chest_sprites= self.chest_sprites, 
					display_surface= self.display_surface, 
					key_sprites= self.keys_sprites,
					create_magic= self.create_magic)
		
		# monster 
		for obj in tmx_data.get_layer_by_name('monsters'):
			if obj.name == 'squid': monster_name = 'squid'
			elif obj.name == 'bamboo': monster_name = 'bamboo'
			elif obj.name == 'raccoon': monster_name = 'raccoon'
			elif obj.name == 'raccoon1': monster_name = 'raccoon1'
			else: monster_name = 'spirit'

			monster(monster_name= monster_name, 
	   				pos= (obj.x,obj.y), 
					groups= [self.all_sprites, self.monster_sprites, self.attackable_sprites], 
					collision_sprites= self.collision_sprites, 
					trigger_death_particles= self.trigger_death_particles, 
					essence_group= self.essence_sprites,
					damage_player= self.damage_player,
					key_group= self.keys_sprites)
			
		for obj in tmx_data.get_layer_by_name('chest'):
			Treasure_chest((obj.x, obj.y), obj.image , [self.all_sprites, self.collision_sprites, self.chest_sprites], obj.name)

		for chest in self.chest_sprites.sprites():
			if chest.name == 'chest1':
				chest.open()
			
		self.player.item_inventory['keys'] = 0
		self.player.chest1_open = True
		self.overlay = Overlay_cave(self.player)
		self.fireworks_2= fireworks_animation()
		self.fireworks_3= fireworks_animation()
		self.fireworks_4= fireworks_animation()
		self.fireworks_5= fireworks_animation()
		self.scroll_2 = Lessons('L3_Scroll_2', 'Lessons/Prelim/L3_Scroll_2.png', self.lesson3)
		self.scroll_3 = Lessons('L3_Scroll_3', 'Lessons/Prelim/L3_Scroll_3.png', self.lesson3)
		self.scroll_4 = Lessons('L3_Scroll_4', 'Lessons/Prelim/L3_Scroll_4.png', self.lesson3)
		self.scroll_5 = Lessons('L3_Scroll_5', 'Lessons/Prelim/L3_Scroll_5.png', self.lesson3)

		self.progress_bar.target_progress = 345
					
	def retry(self):
		for sprite in self.monster_sprites.sprites():
			sprite.kill()
		self.monster_sprites.empty()

		for chest_sprite in self.chest_sprites.sprites():
			chest_sprite.open()


		tmx_data = load_pygame('data/tmx/cave1.tmx')

		for obj in tmx_data.get_layer_by_name('player'):
			if obj.name == 'retry':
				self.player = Player_cave1(pos = (obj.x,obj.y), 
					group = self.all_sprites, 
					collision_sprites= self.collision_sprites,
					monster= self.monster_sprites,
					interaction= self.interaction_sprites,
					essence= self.essence_sprites,
		            chest_sprites= self.chest_sprites, 
					display_surface= self.display_surface, 
					key_sprites= self.keys_sprites,
					create_magic= self.create_magic)
		
		self.player.chest1_open = True
		self.player.chest2_open = True
		self.player.chest3_open = True
		self.player.chest4_open = True
		self.player.chest5_open = True
										
		

	def run(self,dt):
			
		if self.lesson3 not in self.lesson_log.lesson_groups:
			self.lesson_log.add_lesson_group(self.lesson3)

		self.display_surface.fill('#0a0909')
		self.all_sprites.custom_draw(self.player)
		self.player_death()
		self.overlay.display()
		
		if self.player_dead:
			self.transition_death.play()

		self.take_quest(dt)
		self.progress_bar.draw()
		self.opened_chest(dt)
		self.check_quest()
		self.player_attack_logic()
		
		if self.quest_log_active:
			self.questlog.display()
		elif self.lesson_log_active:
			self.lesson_log.display()
		else:
			self.all_sprites.update(dt)
			self.all_sprites.monster_update(self.player)
		
		if self.player.change:
			self.transition.play()
	


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



	
