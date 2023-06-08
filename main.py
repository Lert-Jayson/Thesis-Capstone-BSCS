import pygame, sys, json, mysql.connector, pygame_gui
from settings import *
from level import Level
from cave_level import Level_cave
from cave1_level import Level_cave1
from modern_level import Level_modern
from school_level import Level_school
from library_level import Level_library
from sevenseven_level import Level_sevenseven
from ahamart_level import Level_ahamart
from support import *
from lesson import *
from intro import *
from boss1 import *
from cutscene_gem import *

class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
		pygame.display.set_caption('Adventures of Tom')
		self.clock = pygame.time.Clock()
		try:
			with open('mainload_file.txt') as load_file:
				load = json.load(load_file)
		except:
			load={
			'map_status':'intro'
		}
		self.lesson_log = lesson_log()
		self.levels = {}       
		self.map_status = load['map_status']
	def change_map(self, map):
		self.map_status = map
	def cave_level_reset(self):
		if 'cave1' in self.levels:
			self.levels['cave1'].player.kill()
			self.levels['cave1'].retry()
	def map_manager(self, dt):
		if self.map_status not in self.levels:
			if self.map_status == 'intro':
				self.levels['intro'] = Intro(self.change_map)
			elif self.map_status == 'main':
				self.levels['main'] = Level(self.change_map, self.lesson_log)
			elif self.map_status == 'cave':
				self.levels['cave'] = Level_cave(self.change_map, self.lesson_log)
			elif self.map_status == 'cave1':
				self.levels['cave1'] = Level_cave1(self.change_map, self.lesson_log)
			elif self.map_status == 'boss1':
				self.levels['boss1'] = Boss1(self.change_map, self.cave_level_reset)
			elif self.map_status == 'modern':
				self.levels['modern'] = Level_modern(self.change_map)
			elif self.map_status == 'school':
				self.levels['school'] = Level_school(self.change_map)
			elif self.map_status == 'boss library':
				self.levels['boss library'] = Level_library(self.change_map)
			elif self.map_status == 'sevenseven':
				self.levels['sevenseven'] = Level_sevenseven(self.change_map)
			elif self.map_status == 'ahamart':
				self.levels['ahamart'] = Level_ahamart(self.change_map)
			elif self.map_status == 'cutscene_gem':
				self.levels['cutscene_gem'] = cutscene_gem(self.change_map)
		current_level = self.levels.get(self.map_status)
		if current_level:
			current_level.run(dt)
	def run(self):
		while True:
			with open('mainload_file.txt','w') as load_file:
				json.dump({"map_status":self.map_status},load_file)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					mydb=mysql.connector.connect(
					host="localhost",
					username="root",
					password="",
					database="adventures_of_tom"
					)
					mycursor=mydb.cursor
					with open('mainload_file.txt','r') as load_file:
						mainfile_contents = load_file.read()
					try:
						with open('load_file.txt','r') as load_file:
							mainprefile_contents = load_file.read()
					except:
						print("Intro Not Done")
					try:
						with open('caveload_file.txt','r') as load_file:
							cavefile_contents = load_file.read()
					except:
						print("Cave still not reached")
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_TAB:
						if 'main' in self.levels:
							self.levels['main'].toggle_questlog()
						if 'cave' in self.levels:
							self.levels['cave'].toggle_questlog()
						if 'cave1' in self.levels:
							self.levels['cave1'].toggle_questlog()
					if event.key == pygame.K_ESCAPE:
						if 'main' in self.levels:
							self.levels['main'].show_lesson()
						if 'cave' in self.levels:
							self.levels['cave'].show_lesson()
						if 'cave1' in self.levels:
							self.levels['cave1'].show_lesson()
					if event.key == pygame.K_m:
							if 'main' in self.levels:
								self.levels['main'].toggle_map()
			dt = self.clock.tick() / 1000
			self.map_manager(dt)	
			pygame.display.update()
class Button():
	def __init__(self, image, pos, hover):
		self.image = image
		self.hover = hover
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
	def update(self, screen):
		screen.blit(self.image, self.rect)
	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False
	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.image = self.hover
		else:
			self.image = self.image
class pixel_animation:
	def __init__(self) :
		self.frames = []
		for i in range(0, 77):
			self.frames.append(pygame.image.load('mainmenu/PIXELS 2.0/'+str(i)+'.png'))
		self.frame_index = 0
		self.image = self.frames[self.frame_index]
		self.rect = self.image.get_rect()
		self.rect.topleft = (0, 0)
	def animate(self, dt):
		self.frame_index += 15 * dt
		if self.frame_index >= len(self.frames):
			self.frame_index = 0
		self.image = self.frames[int(self.frame_index)]
	def update(self, dt):
		self.animate(dt)
		screen.blit(self.image, self.rect)
class title_animation:
	def __init__(self) :
		self.frames = import_folder('mainmenu/SWORD_LIGHTNING/')
		self.image = self.frames[0]
		self.rect = self.image.get_rect(topleft = (0, -40))
		self.frame_index = 0
	def animate(self, dt):
		self.frame_index += 10 * dt
		if self.frame_index >= len(self.frames):
			self.frame_index = 0
		self.image = self.frames[int(self.frame_index)]
	def update(self, dt):
		screen.blit(self.image, self.rect)
		self.animate(dt)
class tom_animation:
	def __init__(self) :
		self.frames = import_folder('mainmenu/TOM/')
		self.image = self.frames[0]
		self.rect = self.image.get_rect(midbottom = ((SCREEN_WIDTH // 2) + 30, SCREEN_HEIGHT+15))
		self.frame_index = 0
	def animate(self, dt):
		self.frame_index += 8 * dt
		if self.frame_index >= len(self.frames):
			self.frame_index = 0
		self.image = self.frames[int(self.frame_index)]
	def update(self, dt):
		screen.blit(self.image, self.rect)
		self.animate(dt)
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Adventures of Tom')
clock = pygame.time.Clock()
pixels = pixel_animation()
title = title_animation()
tom = tom_animation()
design = pygame.image.load("mainmenu/LIFE IS A JOURNEY/pic.png").convert_alpha()
design_rect = design.get_rect(center = (SCREEN_WIDTH/2,(SCREEN_HEIGHT/2)-40))
bg = pygame.image.load("mainmenu/BASE/base.png")
bg_rect = bg.get_rect(topleft = (0,0))
def mask_character(password):
	masked_password = "*" * len(password)
	return (masked_password, password)
def login():
	WIDTH, HEIGHT = 1280,720
	SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
	pygame.display.set_caption("Adventures of Tom Login Page")
	manager = pygame_gui.UIManager((1600,900))
	loginu_text = pygame.font.Font('font/LycheeSoda.ttf',30).render(f"Username", True, "maroon")
	loginu_text_rect = loginu_text.get_rect(center=(450,250))
	loginp_text = pygame.font.Font('font/LycheeSoda.ttf', 30).render(f"Password", True, "maroon")
	loginp_text_rect = loginp_text.get_rect(center=(450,350))
	user_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((390, 275), (450, 50)), manager=manager,
                                                object_id='#user_text_entry')
	pass_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((390, 375), (450, 50)), manager=manager,
                                                object_id='#pass_text_entry')
	login_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((490, 475), (250, 50)), text="Login", manager=manager,
                                                object_id='#loginbutton')
	register_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((490, 530), (250, 50)), text="Register", manager=manager,
                                                object_id='#registerbutton')
	back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((980, 665), (250, 50)), text="Back", manager=manager,
                                                object_id='#backbutton')
	clock = pygame.time.Clock() #di ko sure para saan
	def register():
		WIDTH, HEIGHT = 1280,720
		SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
		pygame.display.set_caption("Adventures of Tom Register Page")
		mydb = mysql.connector.connect(
				host="localhost",
				username="root",
				password="",
				database="adventures_of_tom"
			)
		mycursor =  mydb.cursor()
		manager = pygame_gui.UIManager((1600,900))
		program_option=['BSCS','BSIT','BSCOE']
		year_level = ['1','2','3','4']
		year_level2 = ['1','2','3','4','5']
		fname_text = pygame.font.Font('font/LycheeSoda.ttf',30).render(f"First Name", True, "maroon")
		fname_text_rect = fname_text.get_rect(center=(460,250))
		lname_text = pygame.font.Font('font/LycheeSoda.ttf',30).render(f"Last Name", True, "maroon")
		lname_text_rect = lname_text.get_rect(center=(460,350))
		program_text = pygame.font.Font('font/LycheeSoda.ttf',30).render(f"Program", True, "maroon")
		program_text_rect = program_text.get_rect(center=(445,450))
		year_text = pygame.font.Font('font/LycheeSoda.ttf',30).render(f"Year Level", True, "maroon")
		year_text_rect = program_text.get_rect(center=(685,450))
		stud_no_text = pygame.font.Font('font/LycheeSoda.ttf',30).render(f"Student No.", True, "maroon")
		stud_no_text_rect = program_text.get_rect(center=(445,550))
		program_dd = pygame_gui.elements.UIDropDownMenu(options_list=program_option,starting_option=program_option[0],relative_rect=pygame.Rect((390, 475), (225, 50)), manager=manager,
                                                object_id='#user_prog_for_approval')
		year_level_dd = pygame_gui.elements.UIDropDownMenu(options_list=year_level,starting_option=year_level[0],relative_rect=pygame.Rect((640, 475), (200, 50)), manager=manager,
                                                object_id='#user_yl_for_approval')
		registeru_text = pygame.font.Font('font/LycheeSoda.ttf',30).render(f"Username", True, "maroon")
		registeru_text_rect = registeru_text.get_rect(center=(450,150))
		registerp_text = pygame.font.Font('font/LycheeSoda.ttf', 30).render(f"Password", True, "maroon")
		registerp_text_rect = registerp_text.get_rect(center=(690,150))
		fname_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((390, 175), (210, 50)), manager=manager,
													object_id='#fname_text_entry')
		lname_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((630, 175), (210, 50)), manager=manager,
													object_id='#lname_text_entry')
		registeruser_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((390, 275), (450, 50)), manager=manager,
													object_id='#registeruser_text_entry')
		registerpass_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((390, 375), (450, 50)), manager=manager,
													object_id='#registerpass_text_entry')
		student_no_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((390, 575), (450, 50)), manager=manager,
													object_id='#student_no_text_entry')
		registerr_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((980, 615), (250, 50)), text="Register", manager=manager,
                                                object_id='#registerrbutton')
		back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((980, 665), (250, 50)), text="Back", manager=manager,
                                                object_id='#backbutton')
		clock = pygame.time.Clock() #di ko sure para saan
		while True:
			dt = clock.tick() / 1000
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#fname_text_entry'):
					manager.set_focus_set(lname_input)
				if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#lname_text_entry'):
					manager.set_focus_set(registeruser_input)
				if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#registeruser_text_entry'):
					manager.set_focus_set(registerpass_input)
				if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#registerpass_text_entry'):
					manager.set_focus_set(student_no_input)
				if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#student_no_text_entry'):
					manager.set_focus_set(registerr_button)
				if (event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == '#registerrbutton'):
					user=registeruser_input.get_text()
					passw=registerpass_input.get_text()
					fname=fname_input.get_text()
					lname=lname_input.get_text()
					full= user +" "+ passw
					rights='Student'
					prog=program_dd.selected_option
					year= year_level_dd.selected_option
					studno= student_no_input.get_text()
					mycursor.execute('''INSERT INTO administrator_pending VALUES(%s,%s,%s,%s,%s,%s,%s)''',(fname,lname,full,rights,prog,year,studno,))
					mydb.commit()
					print("Registered")
				if (event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == '#backbutton'):
					login()
				manager.process_events(event)
			SCREEN.fill("white")
			half_screen_x = SCREEN.get_width() // 2
			bg = pygame.image.load("mainmenu/LOGIN FORM/loginform.png")
			bg_rect = bg.get_rect(midbottom = (half_screen_x, SCREEN.get_height()))
			SCREEN.blit(bg,bg_rect)
			manager.update(dt)
			manager.draw_ui(SCREEN)
			SCREEN.blit(registeru_text, registeru_text_rect)
			SCREEN.blit(registerp_text,registerp_text_rect)
			SCREEN.blit(fname_text,fname_text_rect)
			SCREEN.blit(lname_text,lname_text_rect)
			SCREEN.blit(program_text,program_text_rect)
			SCREEN.blit(year_text,year_text_rect)
			SCREEN.blit(stud_no_text,stud_no_text_rect)
			pygame.display.update()
	def admin_window():
		WIDTH, HEIGHT = 1280,720
		SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
		pygame.display.set_caption("Adventures of Tom Admin Page")
		mydb = mysql.connector.connect(
				host="localhost",
				username="root",
				password="",
				database="adventures_of_tom"
			)
		mycursor =  mydb.cursor()
		for_approval_queue = ['--']
		mycursor.execute(''' SELECT full_name from administrator_pending''')
		myresult = mycursor.fetchall()
		mydb.commit()
		for row in myresult:
			for x in row:
				for_approval_queue.append(x)
		manager = pygame_gui.UIManager((1600,900))
		admin_window_student_approval = pygame_gui.elements.UIDropDownMenu(options_list=for_approval_queue,starting_option=for_approval_queue[0],relative_rect=pygame.Rect((150, 155), (550, 50)), manager=manager,
                                                object_id='#user_dd_for_approval')
		show_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 155), (250, 50)), text="Show", manager=manager,
                                                object_id='#showbutton')
		checku_text = pygame.font.Font('font/LycheeSoda.ttf',30).render(f"Name", True, "maroon")
		checku_text_rect = checku_text.get_rect(center=(600,250))
		checkp_text = pygame.font.Font('font/LycheeSoda.ttf', 30).render(f"Course and Year Level", True, "maroon")
		checkp_text_rect = checkp_text.get_rect(center=(620,350))
		checks_text = pygame.font.Font('font/LycheeSoda.ttf',30).render(f"Student Number", True, "maroon")
		checks_text_rect = checkp_text.get_rect(center=(640,450))
		check_user_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((390, 275), (450, 50)), manager=manager,
													object_id='#check_user_text_entry')
		check_pass_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((390, 375), (450, 50)), manager=manager,
													object_id='#check_pass_text_entry')
		check_sn_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((390, 475), (450, 50)), manager=manager,
													object_id='#check_stud_num_entry')
		approve_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 550), (250, 50)), text="Approve", manager=manager,
                                                object_id='#approvebutton')
		decline_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((650, 550), (250, 50)), text="Decline", manager=manager,
                                                object_id='#declinebutton')
		back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((980, 665), (250, 50)), text="Back", manager=manager,
                                                object_id='#backbutton')		
		while True:
			dt = clock.tick() / 1000
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if (event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == '#showbutton'):
					test=admin_window_student_approval.selected_option
					print(test)
					mycursor.execute(''' SELECT full_name, program, year_level,student_no from administrator_pending WHERE full_name=%s''',(test,))
					myresult = mycursor.fetchall()
					mydb.commit()
					check_user_input.selected_text_colour='white'
					check_user_input.set_text(myresult[0][0])
					check_pass_input.selected_text_colour='white'
					check_pass_input.set_text(myresult[0][1]+""+str(myresult[0][2]))
					check_sn_input.selected_text_colour='white'
					check_sn_input.set_text(myresult[0][3])	
				if (event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == '#approvebutton'):
					mycursor.execute(''' SELECT email, password, full_name, rights from administrator_pending WHERE full_name=%s''',(test,))
					myresult=mycursor.fetchall()
					mydb.commit()
					email=myresult[0][0]
					password=myresult[0][1]
					full_name=myresult[0][2]
					rights=myresult[0][3]
					mycursor.execute(''' INSERT INTO account VALUES (%s,%s,%s,%s)''',(email,password,full_name,rights))
					mycursor.execute(''' DELETE from administrator_pending WHERE full_name = %s''',(full_name,))
					mydb.commit()
					print("Approved")
					check_user_input.clear()
					check_pass_input.clear()
					check_sn_input.clear()
				if (event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == '#declinebutton'):
					mycursor.execute(''' SELECT email, password, full_name, rights from administrator_pending WHERE full_name=%s''',(test,))
					myresult=mycursor.fetchall()
					mydb.commit()
					email=myresult[0][0]
					password=myresult[0][1]
					full_name=myresult[0][2]
					rights=myresult[0][3]
					mycursor.execute(''' DELETE from administrator_pending WHERE full_name = %s''',(full_name,))
					mydb.commit()
					print("Deleted")
					check_user_input.clear()
					check_pass_input.clear()
					check_sn_input.clear()
				if (event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == '#backbutton'):
					main_menu()
				manager.process_events(event)	
			SCREEN.fill("white")
			half_screen_x = SCREEN.get_width() // 2
			bg = pygame.image.load("mainmenu/LOGIN FORM/teacher and admin page.png")
			bg_rect = bg.get_rect(midbottom = (half_screen_x, SCREEN.get_height()))
			SCREEN.blit(bg,bg_rect)
			SCREEN.blit(checku_text,checku_text_rect)
			SCREEN.blit(checkp_text,checkp_text_rect)
			SCREEN.blit(checks_text,checks_text_rect)
			manager.update(dt)
			manager.draw_ui(SCREEN)
			pygame.display.update()
	def teacher_window():
		WIDTH, HEIGHT = 1280,720
		SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
		pygame.display.set_caption("Adventures of Tom Teacher Page")
		mydb = mysql.connector.connect(
				host="localhost",
				username="root",
				password="",
				database="adventures_of_tom"
			)
		mycursor =  mydb.cursor()
		for_approval_queue = ['--']
		mycursor.execute(''' SELECT full_name from administrator_pending''')
		myresult = mycursor.fetchall()
		mydb.commit()
		for row in myresult:
			for x in row:
				for_approval_queue.append(x)
		manager = pygame_gui.UIManager((1600,900))
		add_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((505, 325), (250, 50)), text="Add Questions", manager=manager,
                                                object_id='#addbutton')
		update_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((505, 375), (250, 50)), text="Update Questions", manager=manager,
                                                object_id='#updatebutton')
		delete_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((505, 425), (250, 50)), text="Delete Questions", manager=manager,
                                                object_id='#deletebutton')
		back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((980, 665), (250, 50)), text="Back", manager=manager,
                                                object_id='#backbutton')
		while True:
			dt = clock.tick() / 1000
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if (event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == '#addbutton'):	
					add_questions()
				if (event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == '#updatebutton'):	
					update_questions()
				if (event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == '#deletebutton'):	
					delete_questions()
				if (event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == '#backbutton'):
					main_menu()
				manager.process_events(event)
			SCREEN.fill("white")
			half_screen_x = SCREEN.get_width() // 2
			bg = pygame.image.load("mainmenu/LOGIN FORM/teacher and admin page.png")
			bg_rect = bg.get_rect(midbottom = (half_screen_x, SCREEN.get_height()))
			SCREEN.blit(bg,bg_rect)
			manager.update(dt)
			manager.draw_ui(SCREEN)
			pygame.display.update()
	def add_questions():
		WIDTH, HEIGHT = 1280,720
		SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
		pygame.display.set_caption("Adventures of Tom Add Questions Page")
		grading_period_arr=['--']
		lesson_title_arr=['--']
		mydb = mysql.connector.connect(
				host="localhost",
				username="root",
				password="",
				database="adventures_of_tom"
			)
		mycursor =  mydb.cursor()
		mycursor.execute(''' SELECT DISTINCT(grading_period) from lesson_array''')
		gpresult = mycursor.fetchall()
		mydb.commit()
		for row in gpresult:
			for x in row:
				grading_period_arr.append(x)
		manager = pygame_gui.UIManager((1600,900))
		
		grading_period= pygame_gui.elements.UIDropDownMenu(options_list=grading_period_arr,starting_option=grading_period_arr[0],relative_rect=pygame.Rect((150, 105), (550, 50)), manager=manager,
                                                object_id='#gradingperiod')
		lesson_title= pygame_gui.elements.UIDropDownMenu(options_list=lesson_title_arr,starting_option=lesson_title_arr[0],relative_rect=pygame.Rect((150, 205), (550, 50)), manager=manager,
                                                object_id='#lessontitle')
		gp_text = pygame.font.Font('font/LycheeSoda.ttf',30).render(f"Grading Period", True, "maroon")
		gp_text_rect = gp_text.get_rect(center=(235,85))
		lt_text = pygame.font.Font('font/LycheeSoda.ttf',30).render(f"Lesson Title", True, "maroon")
		lt_text_rect = lt_text.get_rect(center=(225,185))
		question_text = pygame.font.Font('font/LycheeSoda.ttf',30).render(f"Question", True, "maroon")
		question_text_rect = question_text.get_rect(center=(200,275))
		choice1_text = pygame.font.Font('font/LycheeSoda.ttf', 30).render(f"Choice 1", True, "maroon")
		choice1_text_rect = choice1_text.get_rect(center=(200,375))
		choice2_text = pygame.font.Font('font/LycheeSoda.ttf', 30).render(f"Choice 2", True, "maroon")
		choice2_text_rect = choice1_text.get_rect(center=(500,375))
		choice3_text = pygame.font.Font('font/LycheeSoda.ttf', 30).render(f"Choice 3", True, "maroon")
		choice3_text_rect = choice1_text.get_rect(center=(200,475))
		choice4_text = pygame.font.Font('font/LycheeSoda.ttf', 30).render(f"Choice 4", True, "maroon")
		choice4_text_rect = choice1_text.get_rect(center=(500,475))
		answer_text = pygame.font.Font('font/LycheeSoda.ttf',30).render(f"Answer", True, "maroon")
		answer_text_rect = answer_text.get_rect(center=(200,575))
		question_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((150, 300), (550, 50)), manager=manager,
													object_id='#question_entry')
		choice1_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((150, 400), (250, 50)), manager=manager,
													object_id='#choice1_text_entry')
		choice2_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((450, 400), (250, 50)), manager=manager,
													object_id='#choice2_text_entry')
		choice3_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((150, 500), (250, 50)), manager=manager,
													object_id='#choice3_text_entry')
		choice4_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((450, 500), (250, 50)), manager=manager,
													object_id='#choice4_text_entry')
		answer_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((150, 600), (550, 50)), manager=manager,
													object_id='#answer_entry')
		add_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((850, 350), (250, 50)), text="Add", manager=manager,
                                                object_id='#addbutton')
		back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((980, 665), (250, 50)), text="Back", manager=manager,
                                                object_id='#backbutton')
		while True:
			dt = clock.tick() / 1000
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if (event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED and event.ui_object_id == '#gradingperiod'):
					gperiod= grading_period.selected_option
					mycursor =  mydb.cursor()
					mycursor.execute(''' SELECT lesson_title from lesson_array WHERE grading_period=%s''',(gperiod,))
					ltresult = mycursor.fetchall()
					mydb.commit()
					lesson_title_arr.clear()
					lesson_title_arr.append('--')
					for row in ltresult:
						for x in row:
							lesson_title_arr.append(x)
					lesson_title.options_list= lesson_title_arr
					lesson_title.selected_option = lesson_title_arr[0]
				if (event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED and event.ui_object_id == '#lessontitle'):
					manager.set_focus_set(question_input)
				if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#question_entry'):
					manager.set_focus_set(choice1_input)
				if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#choice1_text_entry'):
					manager.set_focus_set(choice2_input)
				if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#choice2_text_entry'):
					manager.set_focus_set(choice3_input)
				if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#choice3_text_entry'):
					manager.set_focus_set(choice4_input)
				if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#choice4_text_entry'):
					manager.set_focus_set(answer_input)
				if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#answer_entry'):
					manager.set_focus_set(back_button)
				if (event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == '#addbutton'):
					gp= grading_period.selected_option
					lt= lesson_title.selected_option
					question=question_input.get_text()
					choice1=choice1_input.get_text()
					choice2=choice2_input.get_text()
					choice3=choice3_input.get_text()
					choice4=choice4_input.get_text()
					answer=answer_input.get_text()
					mycursor =  mydb.cursor()
					mycursor.execute('''SELECT lesson_number FROM lesson_array WHERE lesson_title=%s''',(lt,))
					ltresult = mycursor.fetchall()
					mydb.commit()
					ln= ltresult[0][0]
					mycursor =  mydb.cursor()
					mycursor.execute(''' INSERT INTO question_bank_prog1 VALUES(%s,%s,%s,%s,%s,%s,%s,%s)''',(gp,ln,question,choice1,choice2,choice3,choice4,answer))
					mydb.commit()
					print("Success")
					question_input.clear()
					choice1_input.clear()
					choice2_input.clear()
					choice3_input.clear()
					choice4_input.clear()
					answer_input.clear()	
				manager.process_events(event)
				if (event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == '#backbutton'):
					teacher_window()
			SCREEN.fill("white")
			half_screen_x = SCREEN.get_width() // 2
			bg = pygame.image.load("mainmenu/LOGIN FORM/teacher and admin page.png")
			bg_rect = bg.get_rect(midbottom = (half_screen_x, SCREEN.get_height()))
			SCREEN.blit(bg,bg_rect)
			SCREEN.blit(gp_text,gp_text_rect)
			SCREEN.blit(lt_text,lt_text_rect)
			SCREEN.blit(question_text,question_text_rect)
			SCREEN.blit(choice1_text,choice1_text_rect)
			SCREEN.blit(choice2_text,choice2_text_rect)
			SCREEN.blit(choice3_text,choice3_text_rect)
			SCREEN.blit(choice4_text,choice4_text_rect)
			SCREEN.blit(answer_text,answer_text_rect)
			manager.update(dt)
			manager.draw_ui(SCREEN)
			pygame.display.update()
	def update_questions():
		WIDTH, HEIGHT = 1280,720
		SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
		pygame.display.set_caption("Adventures of Tom Update Questions Page")
		grading_period_arr=['--']
		lesson_title_arr=['--']
		mydb = mysql.connector.connect(
				host="localhost",
				username="root",
				password="",
				database="adventures_of_tom"
			)
		mycursor =  mydb.cursor()
		mycursor.execute(''' SELECT DISTINCT(grading_period) from lesson_array''')
		gpresult = mycursor.fetchall()
		mydb.commit()
		for row in gpresult:
			for x in row:
				grading_period_arr.append(x)
		manager = pygame_gui.UIManager((1600,900))
		grading_period= pygame_gui.elements.UIDropDownMenu(options_list=grading_period_arr,starting_option=grading_period_arr[0],relative_rect=pygame.Rect((150, 105), (550, 50)), manager=manager,
                                                object_id='#gradingperiod')
		lesson_title= pygame_gui.elements.UIDropDownMenu(options_list=lesson_title_arr,starting_option=lesson_title_arr[0],relative_rect=pygame.Rect((150, 205), (550, 50)), manager=manager,
                                                object_id='#lessontitle')
		gp_text = pygame.font.Font('font/LycheeSoda.ttf',30).render(f"Grading Period", True, "maroon")
		gp_text_rect = gp_text.get_rect(center=(235,85))
		lt_text = pygame.font.Font('font/LycheeSoda.ttf',30).render(f"Lesson Title", True, "maroon")
		lt_text_rect = lt_text.get_rect(center=(225,185))
		question_text = pygame.font.Font('font/LycheeSoda.ttf',30).render(f"Question", True, "maroon")
		question_text_rect = question_text.get_rect(center=(200,275))
		choice1_text = pygame.font.Font('font/LycheeSoda.ttf', 30).render(f"Choice 1", True, "maroon")
		choice1_text_rect = choice1_text.get_rect(center=(200,375))
		choice2_text = pygame.font.Font('font/LycheeSoda.ttf', 30).render(f"Choice 2", True, "maroon")
		choice2_text_rect = choice1_text.get_rect(center=(500,375))
		choice3_text = pygame.font.Font('font/LycheeSoda.ttf', 30).render(f"Choice 3", True, "maroon")
		choice3_text_rect = choice1_text.get_rect(center=(200,475))
		choice4_text = pygame.font.Font('font/LycheeSoda.ttf', 30).render(f"Choice 4", True, "maroon")
		choice4_text_rect = choice1_text.get_rect(center=(500,475))
		answer_text = pygame.font.Font('font/LycheeSoda.ttf',30).render(f"Answer", True, "maroon")
		answer_text_rect = answer_text.get_rect(center=(200,575))
		question_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((150, 300), (550, 50)), manager=manager,
													object_id='#question_entry')
		choice1_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((150, 400), (250, 50)), manager=manager,
													object_id='#choice1_text_entry')
		choice2_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((450, 400), (250, 50)), manager=manager,
													object_id='#choice2_text_entry')
		choice3_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((150, 500), (250, 50)), manager=manager,
													object_id='#choice3_text_entry')
		choice4_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((450, 500), (250, 50)), manager=manager,
													object_id='#choice4_text_entry')
		answer_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((150, 600), (550, 50)), manager=manager,
													object_id='#answer_entry')
		back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((980, 665), (250, 50)), text="Back", manager=manager,
                                                object_id='#backbutton')
		while True:
			dt = clock.tick() / 1000		
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if (event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED and event.ui_object_id == '#gradingperiod'):
					gperiod= grading_period.selected_option
					mycursor =  mydb.cursor()
					mycursor.execute(''' SELECT lesson_title from lesson_array WHERE grading_period=%s''',(gperiod,))
					ltresult = mycursor.fetchall()
					mydb.commit()
					lesson_title_arr.clear()
					lesson_title_arr.append('--')	
					for row in ltresult:
						for x in row:
							lesson_title_arr.append(x)			
					lesson_title.options_list= lesson_title_arr
					lesson_title.selected_option = lesson_title_arr[0]
				manager.process_events(event)
				if (event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == '#backbutton'):
					teacher_window()
			SCREEN.fill("white")
			half_screen_x = SCREEN.get_width() // 2
			bg = pygame.image.load("mainmenu/LOGIN FORM/teacher and admin page.png")
			bg_rect = bg.get_rect(midbottom = (half_screen_x, SCREEN.get_height()))
			SCREEN.blit(bg,bg_rect)
			SCREEN.blit(gp_text,gp_text_rect)
			SCREEN.blit(lt_text,lt_text_rect)
			SCREEN.blit(question_text,question_text_rect)
			SCREEN.blit(choice1_text,choice1_text_rect)
			SCREEN.blit(choice2_text,choice2_text_rect)
			SCREEN.blit(choice3_text,choice3_text_rect)
			SCREEN.blit(choice4_text,choice4_text_rect)
			SCREEN.blit(answer_text,answer_text_rect)
			manager.update(dt)
			manager.draw_ui(SCREEN)
			pygame.display.update()
	def delete_questions():
		WIDTH, HEIGHT = 1280,720
		SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
		pygame.display.set_caption("Adventures of Tom Delete Questions Page")
		grading_period_arr=['--']
		lesson_title_arr=['--']
		questions=['--']
		mydb = mysql.connector.connect(
				host="localhost",
				username="root",
				password="",
				database="adventures_of_tom"
			)
		mycursor =  mydb.cursor()
		mycursor.execute(''' SELECT DISTINCT(grading_period) from lesson_array''')
		gpresult = mycursor.fetchall()
		mydb.commit()
		for row in gpresult:
			for x in row:
				grading_period_arr.append(x)
		manager = pygame_gui.UIManager((1600,900))
		grading_period= pygame_gui.elements.UIDropDownMenu(options_list=grading_period_arr,starting_option=grading_period_arr[0],relative_rect=pygame.Rect((150, 105), (550, 50)), manager=manager,
                                                object_id='#gradingperiod')
		lesson_title= pygame_gui.elements.UIDropDownMenu(options_list=lesson_title_arr,starting_option=lesson_title_arr[0],relative_rect=pygame.Rect((150, 205), (550, 50)), manager=manager,
                                                object_id='#lessontitle')
		gp_text = pygame.font.Font('font/LycheeSoda.ttf',30).render(f"Grading Period", True, "maroon")
		gp_text_rect = gp_text.get_rect(center=(235,85))
		lt_text = pygame.font.Font('font/LycheeSoda.ttf',30).render(f"Lesson Title", True, "maroon")
		lt_text_rect = lt_text.get_rect(center=(225,185))
		question_text = pygame.font.Font('font/LycheeSoda.ttf',30).render(f"Question", True, "maroon")
		question_text_rect = question_text.get_rect(center=(200,275))
		question_dd = pygame_gui.elements.UIDropDownMenu(options_list=questions,starting_option=questions[0],relative_rect=pygame.Rect((150, 305), (550, 50)), manager=manager,
                                                object_id='#question_dd')
		back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((980, 665), (250, 50)), text="Back", manager=manager,
                                                object_id='#backbutton')
		while True:
			dt = clock.tick() / 1000
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if (event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED and event.ui_object_id == '#gradingperiod'):
								gperiod= grading_period.selected_option
								mycursor =  mydb.cursor()
								mycursor.execute(''' SELECT lesson_title from lesson_array WHERE grading_period=%s''',(gperiod,))
								ltresult = mycursor.fetchall()
								mydb.commit()
								lesson_title_arr.clear()
								lesson_title_arr.append('--')
								for row in ltresult:
									for x in row:
										lesson_title_arr.append(x)		
								lesson_title.options_list= lesson_title_arr
								lesson_title.selected_option = lesson_title_arr[0]
				if (event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED and event.ui_object_id == '#lessontitle'):
					gper=grading_period.selected_option
					less_title=lesson_title.selected_option
					mycursor =  mydb.cursor()
					mycursor.execute(''' SELECT lesson_number from lesson_array WHERE lesson_title=%s''',(less_title,))
					lnresult = mycursor.fetchall()
					mydb.commit()
					mycursor.execute(''' SELECT question from question_bank_prog1 WHERE lesson_number=%s and grading_period=%s''',(lnresult[0][0],gper,))
					qresult = mycursor.fetchall()
					mydb.commit()
					questions.clear()
					questions.append('--')
					for row in qresult:
						for x in row:
							questions.append(x)	
					question_dd.options_list=questions
					question_dd.selected_option=questions[0]
				if (event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED and event.ui_object_id == '#question_dd'):
					q= question_dd.selected_option
					mycursor.execute(''' DELETE from question_bank_prog1 WHERE question=%s''',(q,))
					qr = mycursor.fetchall()
					mydb.commit()
					print("Deleted")
				manager.process_events(event)
				if (event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == '#backbutton'):
					teacher_window()
			SCREEN.fill("white")
			half_screen_x = SCREEN.get_width() // 2
			bg = pygame.image.load("mainmenu/LOGIN FORM/teacher and admin page.png")
			bg_rect = bg.get_rect(midbottom = (half_screen_x, SCREEN.get_height()))
			SCREEN.blit(bg,bg_rect)
			SCREEN.blit(gp_text,gp_text_rect)
			SCREEN.blit(lt_text,lt_text_rect)
			SCREEN.blit(question_text,question_text_rect)
			manager.update(dt)
			manager.draw_ui(SCREEN)
			pygame.display.update()
	def enter_login_det():
		mydb = mysql.connector.connect(
				host="localhost",
				username="root",
				password="",
				database="adventures_of_tom"
			)
		mycursor =  mydb.cursor()
		actual_password_arr = []
		while True:
			dt = clock.tick() / 1000
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#user_text_entry'):
					manager.set_focus_set(pass_input)
				if (event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED and event.ui_object_id == '#pass_text_entry'):
					password = pass_input.get_text()
					masked_password, original_password = mask_character(password)
					password_text = original_password[-1]
					actual_password_arr.append(password_text)
					pass_input.set_text(masked_password)
					actual_password=''.join(actual_password_arr)
					print(actual_password)
				if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#pass_text_entry'):
					manager.set_focus_set(login_button)
				manager.process_events(event)
				if (event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == '#loginbutton'):
					mypassword_queue=[]
					email = user_input.get_text()
					passw = actual_password
					mycursor.execute(''' SELECT * from account where email = %s AND password = %s''',(email,passw))
					myresult = mycursor.fetchall()
					for row in myresult:
						for x in row:
							mypassword_queue.append(x)
							if (email and passw) in mypassword_queue:
								mycursor.execute('''SELECT rights from account where email = %s AND password = %s''',(email,passw))
								rightsresults = mycursor.fetchall()
								rights = [item[0] for item in rightsresults]
								mydb.commit()
								mycursor.close()
								if rights[0] == "Student":
									game = Game()
									game.run()
								if rights[0] == "Administrator":
									admin_window()
								if rights[0] == "Teacher":
									teacher_window()
				if (event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == '#registerbutton'):
					register()
				if (event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == '#backbutton'):
					main_menu()			
			SCREEN.fill("white")
			half_screen_x = SCREEN.get_width() // 2
			bg = pygame.image.load("mainmenu/LOGIN FORM/loginform.png")
			bg_rect = bg.get_rect(midbottom = (half_screen_x, SCREEN.get_height()))
			SCREEN.blit(bg,bg_rect)
			manager.update(dt)
			manager.draw_ui(SCREEN)
			SCREEN.blit(loginu_text, loginu_text_rect)
			SCREEN.blit(loginp_text,loginp_text_rect)
			pygame.display.update()
	enter_login_det()
def main_menu(): 
	while True:
			dt = clock.tick() / 1000
			screen.blit(bg, bg_rect)
			screen.blit(design,design_rect)
			pixels.update(dt)
			title.update(dt)
			tom.update(dt)
			MENU_MOUSE_POS = pygame.mouse.get_pos()
			LOGIN_BUTTON = Button(image=pygame.image.load("mainmenu/BUTTONS/LOGIN.png"), 
								pos=(160, SCREEN_HEIGHT - 80), 
								hover=pygame.image.load("mainmenu/BUTTONS/login_hover.png") )
			PLAY_BUTTON = Button(image=pygame.image.load("mainmenu/BUTTONS/PLAY.png"), 
								pos=((SCREEN_WIDTH//2) - 160, SCREEN_HEIGHT - 80), 
                            	hover=pygame.image.load("mainmenu/BUTTONS/play_hover.png") )
			OPTIONS_BUTTON = Button(image=pygame.image.load("mainmenu/BUTTONS/OPTIONS.png"), 
									pos=(SCREEN_WIDTH - 480 ,SCREEN_HEIGHT - 80), 
                            		hover=pygame.image.load("mainmenu/BUTTONS/options_hover.png") )
			QUIT_BUTTON = Button(image=pygame.image.load("mainmenu/BUTTONS/QUIT.png"), 
								pos=(SCREEN_WIDTH - 160, SCREEN_HEIGHT - 80), 
                            	hover=pygame.image.load("mainmenu/BUTTONS/quit_hover.png") )
			for button in [LOGIN_BUTTON, PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
				button.changeColor(MENU_MOUSE_POS)
				button.update(screen)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
						game = Game()
						game.run()
					if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
						pygame.quit()
						sys.exit()
					if LOGIN_BUTTON.checkForInput(MENU_MOUSE_POS):
						login()
			pygame.display.flip()
main_menu()
class bootup:
	def __init__(self) :
		pygame.init()
		self.display_surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
		pygame.display.set_caption('Adventures of Tom')
		self.clock = pygame.time.Clock()
		self.frames = []
		for i in range(0, 200):
			self.frames.append(pygame.image.load('mainmenu/BOOTUP/'+str(i)+'.png'))
		self.frame_index = 0
		self.image = self.frames[self.frame_index]
		self.rect = self.image.get_rect()
		self.rect.topleft = (0, 0)
	def animate(self, dt):
		self.frame_index += 5 * dt
		if self.frame_index >= len(self.frames):
			self.frame_index = 89
			self.image = None
			main_menu()
		else:
			self.image = self.frames[int(self.frame_index)]
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			dt = self.clock.tick() / 1000

			if self.image is not None:
				self.display_surface.blit(self.image, self.rect)
			self.animate(dt)	
			pygame.display.update()
# bootup_animation = bootup()
# bootup_animation.run()