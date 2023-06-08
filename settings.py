from pygame.math import Vector2
# screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
TILE_SIZE = 64

PLAYER_TOOL_OFFSET = {
	'left': Vector2(-50,40),
	'right': Vector2(50,40),
	'up': Vector2(0,-10),
	'down': Vector2(0,50)
}

SPEAR_TOOL_OFFSET = {
	'left': Vector2(-80,20),
	'right': Vector2(80,20),
	'up': Vector2(0,-50),
	'down': Vector2(0,70)
}


LAYERS = {
	'water': 0,
	'ground': 1,
	'soil': 2,
	'soil water': 3,
	'rain floor': 4,
	'ground plant': 5,
	'main': 6,
	'rain drops': 7
}

BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 250
ENERGY_BAR_WIDTH = 200
ITEM_BOX_SIZE = 80

WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE' 

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'


# upgrade menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

# overlay positions 
OVERLAY_POSITIONS = {
	'tool' : (50, SCREEN_HEIGHT - 70), 
	'gem': (SCREEN_WIDTH - 230, SCREEN_HEIGHT - 70),
    'essence': (SCREEN_WIDTH - 100, SCREEN_HEIGHT - 70),
    'keys': (SCREEN_WIDTH - 100, SCREEN_HEIGHT - 190)}

	# magic
magic_data = {
	'flame': {'strength': 5,'cost': 20,'graphic':'graphics/particles/flame/fire.png'},
	'heal' : {'strength': 20,'cost': 10,'graphic':'graphics/particles/heal/heal.png'}}

# enemy
monster_data = {
	'squid': {'health': 4,'damage':20, 'attack_type': 'slash', 'attack_sound':'audio/attack/slash.wav', 'speed': 180, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
	'raccoon': {'health': 8,'damage':40, 'attack_type': 'claw',  'attack_sound':'audio/attack/claw.wav','speed': 120, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
    'raccoon1': {'health': 8,'damage':40, 'attack_type': 'claw',  'attack_sound':'audio/attack/claw.wav','speed': 120, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
	'spirit': {'health': 3,'damage':8, 'attack_type': 'thunder', 'attack_sound':'audio/attack/fireball.wav', 'speed': 200, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
    'spirit1': {'health': 3,'damage':8, 'attack_type': 'thunder', 'attack_sound':'audio/attack/fireball.wav', 'speed': 200, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
	'bamboo': {'health': 2,'damage':6, 'attack_type': 'leaf_attack', 'attack_sound':'audio/attack/slash.wav', 'speed': 180, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300},
    'mush': {'health': 3, 'damage':6, 'attack_type': 'leaf_attack', 'attack_sound':'audio/attack/slash.wav', 'speed': 180, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}}

