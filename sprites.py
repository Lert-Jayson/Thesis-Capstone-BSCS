import pygame
from settings import *
from support import *

class Generic(pygame.sprite.Sprite):
	def __init__(self, pos, surf, groups, z = LAYERS['main']):
		super().__init__(groups)
		self.image = surf
		self.rect = self.image.get_rect(topleft = pos)
		self.z = z
		self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.5, -self.rect.height * 0.70)

class collisions(Generic):
	def __init__(self, pos, surf, groups, z=LAYERS['main']):
		super().__init__(pos, surf, groups, z)
		self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.5, -self.rect.height * 0.40)

class collisions_cave(Generic):
	def __init__(self, pos, surf, groups, z=LAYERS['main']):
		super().__init__(pos, surf, groups, z)
		self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.5, -50)

class collisions_modern(Generic):
	def __init__(self, pos, surf, groups, z=LAYERS['main']):
		super().__init__(pos, surf, groups, z)
		self.hitbox = self.rect.copy().inflate(-45, -self.rect.height * 0.35)

class collisions_modern2(Generic):
	def __init__(self, pos, surf, groups, z=LAYERS['main']):
		super().__init__(pos, surf, groups, z)
		self.hitbox = self.rect.copy().inflate(-45, -self.rect.height * 0.70)

class collisions_modern3(Generic):
	def __init__(self, pos, surf, groups, z=LAYERS['main']):
		super().__init__(pos, surf, groups, z)
		self.hitbox = self.rect.copy().inflate(-350, -self.rect.height * 0.35)

class collisions_modern4(Generic):
	def __init__(self, pos, surf, groups, z=LAYERS['main']):
		super().__init__(pos, surf, groups, z)
		self.hitbox = self.rect.copy().inflate(-150, -self.rect.height * 0.35)

class grass(Generic):
	def __init__(self, pos, surf, groups, z=LAYERS['main']):
		super().__init__(pos, surf, groups, z)
		self.sprite_type = 'grass'

class grass_quest(Generic):
	def __init__(self, pos, surf, groups, z=LAYERS['main']):
		super().__init__(pos, surf, groups, z)
		self.killed = False
		self.sprite_type = 'grass_quest'

	def destroy(self):
		self.killed = True
		self.kill()
				
class Interaction(Generic):
	def __init__(self, pos, size, groups, name):
		surf = pygame.Surface(size)
		super().__init__(pos, surf, groups)
		self.name = name

class Water(Generic):
	def __init__(self, pos, frames, groups):

		#animation setup
		self.frames = frames
		self.frame_index = 0

		# sprite setup
		super().__init__(
				pos = pos, 
				surf = self.frames[self.frame_index], 
				groups = groups, 
				z = LAYERS['water']) 

	def animate(self,dt):
		self.frame_index += 5 * dt
		if self.frame_index >= len(self.frames):
			self.frame_index = 0
		self.image = self.frames[int(self.frame_index)]

	def update(self,dt):
		self.animate(dt)

class Particle(Generic):
	def __init__(self, pos, surf, groups, z, duration = 200):
		super().__init__(pos, surf, groups, z)
		self.start_time = pygame.time.get_ticks()
		self.duration = duration

		# white surface 
		mask_surf = pygame.mask.from_surface(self.image)
		new_surf = mask_surf.to_surface()
		new_surf.set_colorkey((0,0,0))
		self.image = new_surf

	def update(self,dt):
		current_time = pygame.time.get_ticks()
		if current_time - self.start_time > self.duration:
			self.kill()
		
class Tree(Generic):
	def __init__(self, pos, surf, groups, name, player_add):
		super().__init__(pos, surf, groups)

		# tree attributes
		self.health = 5
		self.alive = True
		stump_path = f'graphics/stumps/{"wood1" if name == "wood1" else "wood2"}.png'
		self.stump_surf = pygame.image.load(stump_path).convert_alpha()
		self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.8, -self.rect.height * 0.80)

		self.player_add = player_add

		self.axe_sound = pygame.mixer.Sound('audio/axe.mp3')


	def damage(self):
		
		# damaging the tree
		self.health -= 1
		self.axe_sound.play()


	def check_death(self):
		if self.health <= 0:
			Particle(self.rect.topleft, self.image, self.groups()[0], LAYERS['rain drops'], 300)
			self.image = self.stump_surf
			self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
			self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.8, -self.rect.height * 0.80)
			self.alive = False
			self.player_add('wood')

	def update(self,dt):
		if self.alive:
			self.check_death()

class Tree1(Generic):
	def __init__(self, pos, surf, groups, name):
		super().__init__(pos, surf, groups)

		# tree attributes
		self.health = 5
		self.alive = True
		stump_path = f'graphics/stumps/{"wood1" if name == "wood1" else "wood2"}.png'
		self.stump_surf = pygame.image.load(stump_path).convert_alpha()

		self.axe_sound = pygame.mixer.Sound('audio/axe.mp3')

	def damage(self):
		
		# damaging the tree
		self.health -= 1
		self.axe_sound.play()


	def check_death1(self):
		if self.health <= 0:
			Particle(self.rect.topleft, self.image, self.groups()[0], LAYERS['rain drops'], 300)
			self.image = self.stump_surf
			self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
			self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.8, -self.rect.height * 0.80)
			self.alive = False


	def update(self,dt):
		if self.alive:
			self.check_death1()

######################may dinagdag sa sprite na to ######################################
class WaterJar(Generic):
	def __init__(self, pos, surf, groups, name, player_add):
		super().__init__(pos, surf, groups)


		# waterjar_path = 'graphics/new obj/vase2 (1).png'
		waterjar_path = f'graphics/new obj/{"vase2 (1)" if name == "waterjar" else "waterjar"}.png'
		self.waterjar_surf = pygame.image.load(waterjar_path).convert_alpha()
		self.have_water = False
		self.player_add = player_add

	def water_jar(self):
		if not self.have_water:
			self.player_add('water')
			self.have_water = True
			Particle(self.rect.topleft, self.image, self.groups()[0], LAYERS['rain drops'], 300)
			self.image = self.waterjar_surf
			self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
###########################################################################################	
class tower(Generic):
	def __init__(self, pos, frames, groups):
		self.pos = pos
		self.frames = frames
		self.image = self.frames[1]
		self.rect = self.image.get_rect(topleft = pos)

		super().__init__(pos = pos, surf = self.image, groups = groups, z = LAYERS['main'])

		self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.5, -self.rect.height * 0.5)

	def tower_animation(self, player):
		tower_animation(self.pos, self.frames, self.groups(), player)
		self.kill()	

class tower_animation(Generic):
	def __init__(self, pos, frames, groups, player):

		#animation setup
		self.frames = frames
		self.frame_index = 1

		# sprite setup
		super().__init__(
				pos = pos, 
				surf = self.frames[int(self.frame_index)], 
				groups = groups, 
				z = LAYERS['main']) 
		
		self.player = player
		self.animation_done = False
		

	def animate(self,dt):
		self.frame_index += 8 * dt
		if self.frame_index >= len(self.frames):
			self.frame_index = 41
			self.player.reviewtime = True
			
		self.image = self.frames[int(self.frame_index)]
		self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.5, -self.rect.height * 0.5)
		

	def update(self,dt):
		self.animate(dt)

class fire(Generic):
	def __init__(self, pos, surf, groups, z=LAYERS['main']):
		super().__init__(pos, surf, groups, z)

		self.frames = import_folder('graphics/fire_cave/fire_animation/')
		self.pos = pos

	def start_fire(self):
		fire_animation(self.pos, self.frames, self.groups())
		self.kill()

class fire1(Generic):
	def __init__(self, pos, surf, groups, z=LAYERS['main']):
		super().__init__(pos, surf, groups, z)

		self.frames = import_folder('graphics/fire_cave/fire_animation/')
		self.pos = pos

	def start_fire(self):
		fire_animation(self.pos, self.frames, self.groups())
		self.kill()		

class fire_animation(Generic):
	def __init__(self, pos, frames, groups):

		#animation setup
		self.frames = frames
		self.frame_index = 0

		# sprite setup
		super().__init__(
				pos = pos, 
				surf = self.frames[self.frame_index], 
				groups = groups, 
				z = LAYERS['main']) 

	def animate(self,dt):
		self.frame_index += 5 * dt
		if self.frame_index >= len(self.frames):
			self.frame_index = 0
		self.image = self.frames[int(self.frame_index)]

	def update(self,dt):
		self.animate(dt)

class rocks(Generic):
	def __init__(self, pos, surf, groups):
		super().__init__(pos, surf, groups, z=LAYERS['main'])
		self.hitbox = self.rect.copy().inflate(0, -self.rect.height * 0.5)

	def particles(self):
		Particle(self.rect.topleft, self.image, self.groups()[0], LAYERS['rain drops'], 300)

class essence(pygame.sprite.Sprite):
	def __init__(self, groups,  pos, z = LAYERS['main']) :
		super().__init__(groups)
		self.z = z
		self.frames = import_folder('graphics/essence/')
		self.frame_index = 0

		self.image = self.frames[self.frame_index]
		self.rect = self.image.get_rect(center = pos)

	def animate(self, dt):
		self.frame_index += 5 * dt
		if self.frame_index >= len(self.frames):
			self.frame_index = 0
		self.image = self.frames[int(self.frame_index)]

	def update(self,dt):
		self.animate(dt)

class Truck(Generic):
	def __init__(self, pos, surf, groups, name):
		super().__init__(pos, surf, groups)


		# waterjar_path = 'graphics/new obj/vase2 (1).png'
		truck_path = f'graphics/objects_modern/{"truck_emptyr" if name == "truck" else "truck"}.png'
		self.truck_surf = pygame.image.load(truck_path).convert_alpha()
		self.no_boxes = False

	def truck_empty(self):
		self.no_boxes = True
		Particle(self.rect.topleft, self.image, self.groups()[0], LAYERS['rain drops'], 300)
		self.image = self.truck_surf
		self.rect = self.image.get_rect(midbottom = self.rect.midbottom)

class fountain_animation(Generic):
	def __init__(self, pos, frames, groups):

		#animation setup
		self.frames = frames
		self.frame_index = 0

		# sprite setup
		super().__init__(
				pos = pos, 
				surf = self.frames[self.frame_index], 
				groups = groups, 
				z = LAYERS['main']) 

	def animate(self,dt):
		self.frame_index += 5 * dt
		if self.frame_index >= len(self.frames):
			self.frame_index = 0
		self.image = self.frames[int(self.frame_index)]

	def update(self,dt):
		self.animate(dt)
		
class dialogue_indicator(pygame.sprite.Sprite):
	def __init__(self, groups, pos, z = LAYERS['main']):
		super().__init__(groups)
		self.z = z
	
		self.frames = import_folder('graphics/speech_indicator/')
		self.frame_index = 0
		self.image = self.frames[self.frame_index]
		self.rect = self.image.get_rect(midbottom = pos)
	
	def animate(self,dt):
		self.frame_index += 4 * dt
		if self.frame_index >= len(self.frames):
			self.frame_index = 0
		self.image = self.frames[int(self.frame_index)]

	def update(self, dt):
		
		self.animate(dt)

class newquest_animation(pygame.sprite.Sprite):
	def __init__(self, display_surface) :
		super().__init__()
		self.display_surface = display_surface
		self.finished = False

		self.frames = []
		for i in range(0, 18):
			self.frames.append(pygame.image.load('graphics/questlog/newquest/'+str(i)+'.png'))
		self.frame_index = 0

		self.image = self.frames[0]
		self.rect = self.image.get_rect(topleft = (0,0))

	def animate(self, dt):
		self.frame_index += 8 * dt
		if self.frame_index >= len(self.frames):
			self.kill()
			self.image = None
			self.finished = True
		else:
			self.image = self.frames[int(self.frame_index)]

	def update(self, dt):
		if self.image is not None:
			self.display_surface.blit(self.image, self.rect)
		self.animate(dt)

class questcomplete_animation(pygame.sprite.Sprite):
	def __init__(self, display_surface) :
		super().__init__()
	
		self.display_surface = display_surface
		self.frames = []
		for i in range(0, 19):
			self.frames.append(pygame.image.load('graphics/questlog/questcomplete/'+str(i)+'.png'))
		self.frame_index = 0

		self.image = self.frames[0]
		self.rect = self.image.get_rect(topleft = (0,0))

		self.animation_complete = False

	def animate(self, dt):
		self.frame_index += 8 * dt
		if self.frame_index >= len(self.frames):
			self.animation_complete = True
			self.kill()
			self.image = None
			
		else:
			self.image = self.frames[int(self.frame_index)]

	def update(self, dt):
		if self.image is not None:
			self.display_surface.blit(self.image, self.rect)
		self.animate(dt)

class fireworks_animation(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.finished = False
		
		self.frames = []
		for i in range(0, 22):
			self.frames.append(pygame.image.load('graphics/fireworks/'+str(i)+'.png'))
		self.frame_index = 0

		self.image = self.frames[self.frame_index]
		self.rect = self.image.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

	def animate(self, dt):
		self.frame_index += 8 * dt
		if self.frame_index >= len(self.frames):
			self.finished = True
			self.kill()
			self.image = None
		else:
			self.image = self.frames[int(self.frame_index)]

	def update(self, dt):
		if self.image is not None:
			self.display_surface.blit(self.image, self.rect)
		self.animate(dt)
			
class Treasure_chest(Generic):
	def __init__(self, pos, surf, groups, name):
		super().__init__(pos, surf, groups)

		self.name = name
		self.chest_open = pygame.image.load('graphics/cave/chest/chest open.png').convert_alpha()
		

	def open(self):
		Particle(self.rect.topleft, self.image, self.groups()[0], LAYERS['rain drops'], 300)
		self.image = self.chest_open
		self.rect = self.image.get_rect(midbottom = self.rect.midbottom)

class Eyes(Generic):
	def __init__(self, pos, frames, groups):

		#animation setup
		self.frames = frames
		self.frame_index = 0

		# sprite setup
		super().__init__(
				pos = pos, 
				surf = self.frames[self.frame_index], 
				groups = groups, 
				z = LAYERS['soil']) 

	def animate(self,dt):
		self.frame_index += 5 * dt
		if self.frame_index >= len(self.frames):
			self.frame_index = 0
		self.image = self.frames[int(self.frame_index)]

	def update(self,dt):
		self.animate(dt)

class keys(pygame.sprite.Sprite):
	def __init__(self, groups,  pos, z = LAYERS['main']) :
		super().__init__(groups)
		self.z = z
		self.frames = import_folder('graphics/cave/keys/')
		self.frame_index = 0

		self.image = self.frames[self.frame_index]
		self.rect = self.image.get_rect(center = pos)

	def animate(self, dt):
		self.frame_index += 5 * dt
		if self.frame_index >= len(self.frames):
			self.frame_index = 0
		self.image = self.frames[int(self.frame_index)]

	def update(self,dt):
		self.animate(dt)

class portal(Generic):
	def __init__(self, pos, frames, groups):

		#animation setup
		self.frames = frames
		self.frame_index = 0

		# sprite setup
		super().__init__(
				pos = pos, 
				surf = self.frames[self.frame_index], 
				groups = groups, 
				z = LAYERS['soil']) 

	def animate(self,dt):
		self.frame_index += 5 * dt
		if self.frame_index >= len(self.frames):
			self.frame_index = 0
		self.image = self.frames[int(self.frame_index)]

	def update(self,dt):
		self.animate(dt)