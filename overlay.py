import pygame
from settings import *

class Overlay:
	def __init__(self,player):

		# general setup
		self.display_surface = pygame.display.get_surface()
		self.player = player
		self.font = pygame.font.Font('font/LycheeSoda.ttf', 32)
		self.font1 = pygame.font.Font('font/Almendra-Bold.ttf', 22)

		# imports 
		overlay_path = 'graphics/overlay/'
		self.tools_surf = {tool: pygame.image.load(f'{overlay_path}{tool}.png').convert_alpha() for tool in player.tools}

		#jar water
		self.imageJ = pygame.image.load('graphics/overlay/water_vase.png').convert_alpha()
		self.rectJ = self.imageJ.get_rect(midbottom = (SCREEN_WIDTH - 85 , SCREEN_HEIGHT - 35))

		#wood
		self.imageW = pygame.image.load('graphics/overlay/wood.png').convert_alpha()
		self.rectW = self.imageW.get_rect(midbottom = (SCREEN_WIDTH - 85 , SCREEN_HEIGHT - 15))

		#meat
		self.imageM = pygame.image.load('graphics/overlay/meat.png').convert_alpha()
		self.rectM = self.imageM.get_rect(midbottom = (SCREEN_WIDTH - 85 , SCREEN_HEIGHT - 15))

		self.hud = pygame.image.load('graphics/overlay/gui.png').convert_alpha()
		self.hud_rect = self.hud.get_rect(topleft = (0,0))

#bago#####################################################
		#bar setup
		self.health_bar_rect = pygame.Rect(113,58,HEALTH_BAR_WIDTH,BAR_HEIGHT)
		self.energy_bar_rect = pygame.Rect(113,80,ENERGY_BAR_WIDTH,BAR_HEIGHT)

		 #convert magic dictionary
		self.magic_graphics = []
		for magic in magic_data.values():
			path = magic['graphic']
			magic = pygame.image.load(path).convert_alpha()
			self.magic_graphics.append(magic)

	def show_bar(self, current, max_amount, bg_rect, color):
        #draw bg
		pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)

        #Converting stat to a pixel
		ratio = current / max_amount
		current_width = bg_rect.width * ratio
		current_rect = bg_rect.copy()
		current_rect.width = current_width

        #Drawing a bar
		pygame.draw.rect(self.display_surface, color, current_rect)
		pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)
	
	def selection_box(self ,left , top, has_switched):
		bg_rect = pygame.Rect(left, top, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
		pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)
		if has_switched:
			pygame.draw.rect(self.display_surface, UI_BORDER_COLOR_ACTIVE, bg_rect, 3)
		else:
			pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)
		return bg_rect

	def weapon_overlay(self,  has_switched):
		bg_rect = self.selection_box(10,SCREEN_HEIGHT - 150, has_switched) #weapon
		weapon_surf = self.tools_surf[self.player.selected_tool]
		weapon_rect = weapon_surf.get_rect(center = bg_rect.center)

		self.display_surface.blit(weapon_surf, weapon_rect)

	def magic_overlay(self, magic_index, has_switched):
		bg_rect = self.selection_box(80,635, has_switched) #weapon
		magic_surf = self.magic_graphics[magic_index]
		magic_rect = magic_surf.get_rect(center = bg_rect.center)

		self.display_surface.blit(magic_surf, magic_rect)
	
	def display(self ):


		self.show_bar(self.player.health, self.player.stats['health'], self.health_bar_rect, HEALTH_COLOR)
		self.show_bar(self.player.energy, self.player.stats['energy'], self.energy_bar_rect, ENERGY_COLOR)
		
		self.display_surface.blit(self.hud, self.hud_rect)
		self.weapon_overlay(self.player.timers['tool switch'].active)
		self.magic_overlay(self.player.magic_index, not self.player.can_switch_magic)
#######d2 ko nilagay pra umibabaw#######################
	
		if self.player.water:
			self.display_surface.blit(self.imageJ, self.rectJ)
###################bago###################################################
		if self.player.water_active and not self.player.questwaterjar_complete:
			vase = pygame.image.load('graphics/overlay/water.png').convert_alpha()
			vase_rect = vase.get_rect(midbottom = ((SCREEN_WIDTH / 2) + 40 , SCREEN_HEIGHT -5))

			num_vase = self.font.render('/ 6', False, 'white')
			num_vase_rect = num_vase.get_rect(midbottom = ((SCREEN_WIDTH / 2) - 10, SCREEN_HEIGHT - 35))

			water_vase_num = self.player.item_inventory['water']
			vase_num = self.font.render(str(water_vase_num) , False, 'white')
			vase_num_rect = vase_num.get_rect(midbottom = ((SCREEN_WIDTH / 2) - 50 , SCREEN_HEIGHT - 35))

			vase_bg = pygame.image.load('graphics/overlay/water_bg.png').convert_alpha()
			vase_bg_rect = vase_bg.get_rect(topleft = (0,0))

			self.display_surface.blit(vase_bg,vase_bg_rect)
			self.display_surface.blit(vase,vase_rect)
			self.display_surface.blit(num_vase, num_vase_rect)
			self.display_surface.blit(vase_num, vase_num_rect)
###############################################################################################
		if self.player.had_wood:
			numw = self.player.item_inventory['wood']
			numw_surf = self.font.render(str(numw) , False, 'white')
			numw_rect = numw_surf.get_rect(midbottom = (SCREEN_WIDTH - 80 , SCREEN_HEIGHT - 28))

			self.display_surface.blit(self.imageW, self.rectW)
			self.display_surface.blit(numw_surf, numw_rect)

		if self.player.had_meat:
			numm = self.player.item_inventory['meat']
			numm_surf = self.font.render(str(numm) , False, 'white')
			numm_rect = numm_surf.get_rect(midbottom = (SCREEN_WIDTH - 50 , SCREEN_HEIGHT - 30))

			self.display_surface.blit(self.imageM, self.rectM)
			self.display_surface.blit(numm_surf, numm_rect)

		if self.player.restoration:
			self.player.restore_life()

		text_q = self.font1.render('Q', False, 'white')
		text_q_rect = text_q.get_rect(topleft = (65,SCREEN_HEIGHT-105))
		self.display_surface.blit(text_q, text_q_rect)

		text_e = self.font1.render('E', False, 'white')
		text_e_rect = text_e.get_rect(topleft = (140,SCREEN_HEIGHT-35))
		self.display_surface.blit(text_e, text_e_rect)


		

		