import pygame 
from settings import *
from support import *
from timer import Timer
from dialogue import *
from transition import *
import random, mysql.connector

class Boss1:
    def __init__(self, change_map, cave_level_reset):
        self.change_map = change_map
        self.cave_level_reset = cave_level_reset
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font('font/Almendra-Bold.ttf', 26)
        self.font1 = pygame.font.Font('font/Almendra-Bold.ttf', 24)
        self.font2 = pygame.font.Font('font/Almendra-Bold.ttf',20)
        self.timer = Timer(200)
        self.bg = pygame.image.load('graphics/TOM ATTACK/cave.png').convert_alpha()
        self.bg_rect = self.bg.get_rect(topleft = (0,0))
        self.filter = pygame.image.load('graphics/TOM ATTACK/Filter.png').convert_alpha()
        self.filter_rect = self.filter.get_rect(topleft = (0,0))
        self.gui = pygame.image.load('graphics/TOM ATTACK/gui_turnbased.png').convert_alpha()
        self.gui_rect = self.gui.get_rect(bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.dialogue = dialogue_manager(self.display_surface)
        self.transition = Transition_boss_failed(self.change_map, self.cave_level_reset, self, 'cave1')
        self.transition_passed = Transition_boss_passed(self.change_map, 'cutscene_gem')
        self.retry = False
        self.intro = intro()
        self.k_o_player = K_O_player()
        self.k_o_ogre = K_O_ogre()
        self.idle = pygame.image.load('graphics/TOM ATTACK/TOM ATTACK 1/0.png').convert_alpha()
        self.idle_rect = self.idle.get_rect(topleft = (0,0))
        self.tom_attack_1 = tom_attack_1()
        self.tom_attack_2 = tom_attack_2()
        self.tom_combo_attack_1 = tom_combo_attack_1()
        self.tom_combo_attack_2 = tom_combo_attack_2()
        self.ogre_attack_1 = ogre_attack_1()
        self.ogre_attack_2 = ogre_attack_2()
        self.ogre_attack_3 = ogre_attack_3()
        self.ogre_combo_attack_1 = ogre_combo_attack_1()
        self.ogre_combo_attack_2 = ogre_combo_attack_2()
        self.ogre_combo_attack_3 = ogre_combo_attack_3()
        self.tom_current_health = 1000
        self.tom_target_health = 1000
        self.tom_max_health = 1000
        self.tom_health_bar_length = 355
        self.tom_health_ratio = self.tom_max_health / self.tom_health_bar_length
        self.tom_health_change_speed = 1
        self.ogre_current_health = 1000
        self.ogre_target_health = 1000
        self.ogre_max_health = 1000
        self.ogre_health_bar_length = 355
        self.ogre_health_ratio = self.tom_max_health / self.tom_health_bar_length
        self.ogre_health_change_speed = 1
        self.status = None
        self.dialogue_finished = False
        mydb=mysql.connector.connect(
            host="localhost",
            username="root",
            password="",
            database="adventures_of_tom"
            )
        mycursor= mydb.cursor()
        mycursor.execute('SELECT question, choice1, choice2, choice3, choice4, answer_key FROM question_bank_prog1 WHERE grading_period="Prelim"')
        rows = mycursor.fetchall()
        self.quiz_data = []
        for row in rows:
            question = {
                'question': row[0],
                'options': [row[1], row[2], row[3], row[4]],
                'answer': row[5]
         }
            self.quiz_data.append(question)
        mydb.commit()
        mycursor.close()
        random.shuffle(self.quiz_data)
        self.current_question = 0
        self.score = 0
        self.music = pygame.mixer.Sound('audio/sound_effects/Turn Based_mode.mp3')
        self.music.set_volume(0.4)
        self.music.play(loops = -1)
        self.passed = False
    def reset(self):
        self.dialogue = dialogue_manager(self.display_surface)
        self.transition = Transition_boss_failed(self.change_map, self.cave_level_reset, self, 'cave1')
        self.retry = False
        self.intro = intro()
        self.k_o_player = K_O_player()
        self.k_o_ogre = K_O_ogre()
        self.idle = pygame.image.load('graphics/TOM ATTACK/TOM ATTACK 1/0.png').convert_alpha()
        self.idle_rect = self.idle.get_rect(topleft = (0,0))
        self.tom_attack_1 = tom_attack_1()
        self.tom_attack_2 = tom_attack_2()
        self.tom_combo_attack_1 = tom_combo_attack_1()
        self.tom_combo_attack_2 = tom_combo_attack_2()
        self.ogre_attack_1 = ogre_attack_1()
        self.ogre_attack_2 = ogre_attack_2()
        self.ogre_attack_3 = ogre_attack_3()
        self.ogre_combo_attack_1 = ogre_combo_attack_1()
        self.ogre_combo_attack_2 = ogre_combo_attack_2()
        self.ogre_combo_attack_3 = ogre_combo_attack_3()
        self.tom_current_health = 1000
        self.tom_target_health = 1000
        self.tom_max_health = 1000
        self.tom_health_bar_length = 355
        self.tom_health_ratio = self.tom_max_health / self.tom_health_bar_length
        self.tom_health_change_speed = 1
        self.ogre_current_health = 1000
        self.ogre_target_health = 1000
        self.ogre_max_health = 1000
        self.ogre_health_bar_length = 355
        self.ogre_health_ratio = self.tom_max_health / self.tom_health_bar_length
        self.ogre_health_change_speed = 1
        self.status = None
        self.dialogue_finished = False
        mydb=mysql.connector.connect(
            host="localhost",
            username="root",
            password="",
            database="adventures_of_tom"
            )
        mycursor= mydb.cursor()
        mycursor.execute('SELECT question, choice1, choice2, choice3, choice4, answer_key FROM question_bank_prog1 WHERE grading_period="Prelim"')
        rows = mycursor.fetchall()
        self.quiz_data = []
        for row in rows:
            question = {
                'question': row[0],
                'options': [row[1], row[2], row[3], row[4]],
                'answer': row[5]
         }
            self.quiz_data.append(question)
        mydb.commit()
        mycursor.close()
        random.shuffle(self.quiz_data)
        self.current_question = 0
        self.score = 0
        self.dialogue.dialogue_complete.remove('boss')
        self.music = pygame.mixer.Sound('audio/sound_effects/Turn Based_mode.mp3')
        self.music.set_volume(0.4)
        self.music.play(loops = -1)
    def get_damage_tom(self, amount):
        if self.tom_current_health > 0:
            self.tom_current_health -= amount
        if self.tom_current_health < 0:
            self.tom_current_health = 0
    def get_damage_ogre(self, amount):
        if self.ogre_current_health > 0:
            self.ogre_current_health -= amount
        if self.ogre_current_health < 0:
            self.ogre_current_health = 0
    def draw_health(self):
        title = pygame.image.load('graphics/TOM ATTACK/LIFE BAR/title.png').convert_alpha()
        title_rect = title.get_rect(topleft = (0,0))
        self.display_surface.blit(title, title_rect)
        bg_health  = pygame.image.load('graphics/TOM ATTACK/LIFE BAR/lifebar_bg.png').convert_alpha()
        bg_health = pygame.transform.flip(bg_health, True, False)
        bg_health_rect = bg_health.get_rect(midtop = ((SCREEN_WIDTH / 2) /2 - 60, 45)) 
        self.display_surface.blit(bg_health, bg_health_rect)
        bg_health1  = pygame.image.load('graphics/TOM ATTACK/LIFE BAR/lifebar_bg.png').convert_alpha()
        bg_health_rect1 = bg_health1.get_rect(midtop = ((SCREEN_WIDTH/2)+ 360, 45)) 
        self.display_surface.blit(bg_health1, bg_health_rect1)
        transition_width = 0
        transition_color = 'white'
        if self.tom_current_health < self.tom_target_health:
            self.tom_target_health -= self.tom_health_change_speed
            transition_width = int((self.tom_target_health - self.tom_current_health) / self.tom_health_ratio)
            transition_color = 'white'
        health_bar_width = int(self.tom_current_health / self.tom_health_ratio)
        health_bar = pygame.Rect(86,58,health_bar_width,25)
        transition_bar = pygame.Rect(health_bar.right,58,transition_width,25)
        pygame.draw.rect(self.display_surface,'#38e4e4',health_bar)
        pygame.draw.rect(self.display_surface,transition_color,transition_bar)	
        container = pygame.image.load('graphics/TOM ATTACK/LIFE BAR/lifebar_container.png').convert_alpha()
        container = pygame.transform.flip(container, True, False)
        container_rect = container.get_rect(midtop = ((SCREEN_WIDTH / 2) /2 - 60, 45))
        self.display_surface.blit(container, container_rect)
        transition_width1 = 0
        transition_color1 = 'white'
        if self.ogre_current_health < self.ogre_target_health:
            self.ogre_target_health -= self.ogre_health_change_speed
            transition_width1 = int((self.ogre_target_health - self.ogre_current_health) / self.ogre_health_ratio)
            transition_color1 = 'white'
        health_bar_width1 = int(self.ogre_current_health / self.ogre_health_ratio)
        health_bar1 = pygame.Rect(((SCREEN_WIDTH/2)+ 180)+ self.ogre_health_bar_length - health_bar_width1 ,58,health_bar_width1,25)
        transition_bar1 = pygame.Rect(health_bar1.left - transition_width1,58,transition_width1,25)
        pygame.draw.rect(self.display_surface,'#38e4e4',health_bar1)
        pygame.draw.rect(self.display_surface,transition_color1,transition_bar1)	
        container1 = pygame.image.load('graphics/TOM ATTACK/LIFE BAR/lifebar_container.png').convert_alpha()
        container_rect1 = container1.get_rect(midtop = ((SCREEN_WIDTH/2)+ 360, 45))
        self.display_surface.blit(container1, container_rect1)
    def input(self):
        keys = pygame.key.get_pressed()
        self.timer.update()
        if not self.timer.active:
            if self.current_question < len(self.quiz_data):
                if keys[pygame.K_1]:
                    if self.quiz_data[self.current_question]["options"][0] == self.quiz_data[self.current_question]["answer"]:
                        self.score += 1
                        self.get_damage_ogre((750*(1/len(self.quiz_data))))
                        self.status = random.choice(['tom_attack_1', 'tom_attack_2', 'tom_combo_attack_1', 'tom_combo_attack_2'])
                        self.timer.activate()
                        self.current_question += 1
                    else:
                        self.get_damage_tom((750*(1/len(self.quiz_data))))
                        self.status = random.choice(['ogre_attack_1', 'ogre_attack_2', 'ogre_attack_3', 'ogre_combo_attack_1', 'ogre_combo_attack_2', 'ogre_combo_attack_3'])
                        self.timer.activate()
                        self.current_question += 1
                if keys[pygame.K_2]:
                    if self.quiz_data[self.current_question]["options"][1] == self.quiz_data[self.current_question]["answer"]:
                        self.score += 1
                        self.get_damage_ogre((750*(1/len(self.quiz_data))))
                        self.status = random.choice(['tom_attack_1', 'tom_attack_2', 'tom_combo_attack_1', 'tom_combo_attack_2'])
                        self.timer.activate() 
                        self.current_question += 1 
                    else:
                        self.get_damage_tom((750*(1/len(self.quiz_data))))
                        self.status = random.choice(['ogre_attack_1', 'ogre_attack_2', 'ogre_attack_3', 'ogre_combo_attack_1', 'ogre_combo_attack_2', 'ogre_combo_attack_3'])
                        self.timer.activate()
                        self.current_question += 1
                if keys[pygame.K_3]:
                    if self.quiz_data[self.current_question]["options"][2] == self.quiz_data[self.current_question]["answer"]:
                        self.score += 1
                        self.get_damage_ogre((750*(1/len(self.quiz_data))))
                        self.status = random.choice(['tom_attack_1', 'tom_attack_2', 'tom_combo_attack_1', 'tom_combo_attack_2'])
                        self.timer.activate() 
                        self.current_question += 1 
                    else:
                        self.get_damage_tom((750*(1/len(self.quiz_data))))
                        self.status = random.choice(['ogre_attack_1', 'ogre_attack_2', 'ogre_attack_3', 'ogre_combo_attack_1', 'ogre_combo_attack_2', 'ogre_combo_attack_3'])
                        self.timer.activate()
                        self.current_question += 1
                if keys[pygame.K_4]:
                    if self.quiz_data[self.current_question]["options"][3] == self.quiz_data[self.current_question]["answer"]:
                        self.score += 1
                        self.get_damage_ogre((750*(1/len(self.quiz_data))))
                        self.status = random.choice(['tom_attack_1', 'tom_attack_2', 'tom_combo_attack_1', 'tom_combo_attack_2'])
                        self.timer.activate() 
                        self.current_question += 1
                    else:
                        self.get_damage_tom((750*(1/len(self.quiz_data))))
                        self.status = random.choice(['ogre_attack_1', 'ogre_attack_2', 'ogre_attack_3', 'ogre_combo_attack_1', 'ogre_combo_attack_2', 'ogre_combo_attack_3'])
                        self.timer.activate()
                        self.current_question += 1
            if self.current_question >= len(self.quiz_data):
                pass
    def display_animation(self):
        if self.status == 'idle':
            self.display_surface.blit(self.idle, self.idle_rect)
        if self.status == 'tom_attack_1':
            self.tom_attack_1.play()
        if self.status == 'tom_attack_2':
            self.tom_attack_2.play()
        if self.status == 'ogre_attack_1':
            self.ogre_attack_1.play()  
        if self.status == 'ogre_attack_2':
            self.ogre_attack_2.play()
        if self.status == 'ogre_attack_3':
            self.ogre_attack_3.play()
        if self.status == 'tom_combo_attack_1':
            self.tom_combo_attack_1.play()
        if self.status == 'tom_combo_attack_2':
            self.tom_combo_attack_2.play()
        if self.status == 'ogre_combo_attack_1':
            self.ogre_combo_attack_1.play()
        if self.status == 'ogre_combo_attack_2':
            self.ogre_combo_attack_2.play()    
        if self.status == 'ogre_combo_attack_3':
            self.ogre_combo_attack_3.play()
    def run(self,dt):
        self.display_surface.fill('black')
        self.dialogue.start_dialogue(dialogue_last(self))
        if  self.dialogue_finished:
            self.display_surface.blit(self.bg, self.bg_rect)
            self.display_surface.blit(self.filter, self.filter_rect)
            self.display_surface.blit(self.gui, self.gui_rect)
            self.input()
            self.display_animation()
            if self.status == 'intro':
                self.intro.update(dt)
            if self.intro.finished:
                self.status = 'idle'
                self.tom_attack_1.update(dt)
                self.tom_attack_2.update(dt)
                self.ogre_attack_1.update(dt)
                self.ogre_attack_2.update(dt)
                self.ogre_attack_3.update(dt)
                self.draw_health()
                self.tom_combo_attack_1.update(dt)
                self.tom_combo_attack_2.update(dt)
                self.ogre_combo_attack_1.update(dt)
                self.ogre_combo_attack_2.update(dt)
                self.ogre_combo_attack_3.update(dt)
                if self.current_question < len(self.quiz_data):
                    question_text = self.font.render((self.quiz_data[self.current_question]["question"]), True, 'black',None)
                    question_rect = question_text.get_rect()
                    question_rect.centerx = self.gui_rect.centerx
                    question_rect.centery = self.gui_rect.centery-45
                    self.display_surface.blit(question_text, question_rect)
                    option1_text = self.font1.render("1. " + self.quiz_data[self.current_question]["options"][0], True, 'black')
                    option1_rect = option1_text.get_rect()
                    option1_rect.centerx = self.gui_rect.centerx-200
                    option1_rect.centery = self.gui_rect.centery+10
                    self.display_surface.blit(option1_text, option1_rect)
                    option2_text = self.font1.render("2. " + self.quiz_data[self.current_question]["options"][1], True, 'black')
                    option2_rect = option2_text.get_rect()
                    option2_rect.centerx = self.gui_rect.centerx-200
                    option2_rect.centery = self.gui_rect.centery+35
                    self.display_surface.blit(option2_text, option2_rect)
                    option3_text = self.font1.render("3. " + self.quiz_data[self.current_question]["options"][2], True, 'black')
                    option3_rect = option3_text.get_rect()
                    option3_rect.centerx = self.gui_rect.centerx+200
                    option3_rect.centery = self.gui_rect.centery+10
                    self.display_surface.blit(option3_text, option3_rect)
                    option4_text = self.font1.render("4. " + self.quiz_data[self.current_question]["options"][3], True, 'black')
                    option4_rect = option4_text.get_rect()
                    option4_rect.centerx = self.gui_rect.centerx+200
                    option4_rect.centery = self.gui_rect.centery+35
                    self.display_surface.blit(option4_text, option4_rect)
                elif self.current_question >= len(self.quiz_data):
                    if (self.score/len(self.quiz_data))>= 0.75:
                        self.get_damage_ogre(self.ogre_current_health)
                        score_text = self.font.render("Your score is: " + str(self.score) + ". You passed", True, 'black')
                        score_rect = score_text.get_rect()
                        score_rect.center = (self.gui_rect.centerx, self.gui_rect.centery)
                        self.display_surface.blit(score_text, score_rect)
                        exit_text = self.font.render('Back[x]', True, 'black')
                        exit_rect = exit_text.get_rect(bottomright = (SCREEN_WIDTH-120, SCREEN_HEIGHT-80))
                        self.display_surface.blit(exit_text, exit_rect)
                        if  self.tom_attack_1.finished or self.tom_attack_2.finished or self.ogre_attack_1.finished or  self.ogre_attack_2.finished or self.ogre_attack_3.finished or self.tom_combo_attack_1.finished or self.tom_combo_attack_2.finished or self.ogre_combo_attack_1.finished or self.ogre_combo_attack_2.finished or self.ogre_combo_attack_3.finished:
                            self.k_o_ogre.update(dt)
                        if pygame.key.get_pressed()[pygame.K_x]:
                            self.passed = True
                            self.music.stop()
                    else:
                        self.get_damage_tom(self.tom_current_health)
                        score_text = self.font.render("Your score is: " + str(self.score) + ". You did not pass", True, 'black')
                        score_rect = score_text.get_rect()
                        score_rect.center = (self.gui_rect.centerx, self.gui_rect.centery)
                        self.display_surface.blit(score_text, score_rect)
                        exit_text = self.font.render('Back[x]', True, 'black')
                        exit_rect = exit_text.get_rect(bottomright = (SCREEN_WIDTH-120, SCREEN_HEIGHT-80))
                        self.display_surface.blit(exit_text, exit_rect)
                        if  self.tom_attack_1.finished or self.tom_attack_2.finished or self.ogre_attack_1.finished or  self.ogre_attack_2.finished or self.ogre_attack_3.finished or self.tom_combo_attack_1.finished or self.tom_combo_attack_2.finished or self.ogre_combo_attack_1.finished or self.ogre_combo_attack_2.finished or self.ogre_combo_attack_3.finished:
                            self.k_o_player.update(dt)
                        if pygame.key.get_pressed()[pygame.K_x]:
                            self.retry = True
                            self.music.stop()      
        self.dialogue.update()
        self.dialogue.draw()
        if self.retry:
            self.transition.play()
        if self.passed:
            self.transition_passed.play()
class K_O_ogre:
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.frames = []
        for i in range(0, 4):
            self.frames.append(pygame.image.load('graphics/TOM ATTACK/K.O/'+str(i)+'.png'))
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = (960, SCREEN_HEIGHT/2))
        self.finished = False
    def animate(self, dt):
        self.frame_index += 4 * dt
        if self.frame_index >= len(self.frames):
            self.frame_index = len(self.frames)
            self.finished = True
        else:
            self.image = self.frames[int(self.frame_index)]
    def update(self, dt):
        self.display_surface.blit(self.image, self.rect)
        self.animate(dt)
class K_O_player:
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.frames = []
        for i in range(0, 4):
            self.frames.append(pygame.image.load('graphics/TOM ATTACK/K.O/'+str(i)+'.png'))
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = ((SCREEN_WIDTH/2) /2, SCREEN_HEIGHT/2))
        self.finished = False
    def animate(self, dt):
        self.frame_index += 4 * dt
        if self.frame_index >= len(self.frames):
            self.frame_index = len(self.frames)
            self.finished = True
        else:
            self.image = self.frames[int(self.frame_index)]
    def update(self, dt):
        self.display_surface.blit(self.image, self.rect)
        self.animate(dt)
class intro(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.frames = []
        for i in range(0, 72):
            self.frames.append(pygame.image.load('graphics/TOM ATTACK/COMBO_ANIMATION/INTRO/'+str(i)+'.png'))
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(topleft = (0, 0))
        self.finished = False
    def animate(self, dt):
        self.frame_index += 6 * dt
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
class tom_combo_attack_1:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.frames = []
        for i in range(0, 22):
            self.frames.append(pygame.image.load('graphics/TOM ATTACK/COMBO_ANIMATION/TOM ATTACK/ATTACK 1/'+str(i)+'.png'))
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(topleft = (0, 0))
        self.active = False
        self.finished = False
        self.attack_sound = pygame.mixer.Sound('audio/sound_effects/Tom Attack 1/swoosh-2-99245.mp3')
    def play(self):
        self.active = True
        self.finished = False
        self.frame_index = 0
        self.attack_sound.play()
    def animate(self, dt):
        self.frame_index += 10 * dt
        if self.frame_index >= len(self.frames):
            self.active = False
            self.image = None
            self.finished = True
        else:
            self.image = self.frames[int(self.frame_index)]
    def update(self, dt):
        if self.active:
            if self.image is not None:
                self.display_surface.blit(self.image, self.rect)
            self.animate(dt)
class tom_combo_attack_2:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.frames = []
        for i in range(0, 24):
            self.frames.append(pygame.image.load('graphics/TOM ATTACK/COMBO_ANIMATION/TOM ATTACK/ATTACK 2/'+str(i)+'.png'))
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(topleft = (0, 0))
        self.active = False
        self.finished = False
        self.attack_sound = pygame.mixer.Sound('audio/sound_effects/Tom Attack 1/Pow.mp3')
    def play(self):
        self.active = True
        self.finished = False
        self.frame_index = 0
        self.attack_sound.play()
    def animate(self, dt):
        self.frame_index += 10 * dt
        if self.frame_index >= len(self.frames):
            self.active = False
            self.image = None
            self.finished = True        
        else:
            self.image = self.frames[int(self.frame_index)]
    def update(self, dt):
        if self.active:
            if self.image is not None:
                self.display_surface.blit(self.image, self.rect)
            self.animate(dt)
class ogre_combo_attack_1:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.frames = []
        for i in range(0, 23):
            self.frames.append(pygame.image.load('graphics/TOM ATTACK/COMBO_ANIMATION/OGRE ATTACK/ATTACK 1/'+str(i)+'.png'))
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(topleft = (0, 0))
        self.active = False
        self.finished = False
        self.attack_sound = pygame.mixer.Sound('audio/sound_effects/Ogre Attack 3/swoosh-2-99245.mp3')
    def play(self):
        self.active = True
        self.finished = False
        self.frame_index = 0 
        self.attack_sound.play()
    def animate(self, dt):
        self.frame_index += 10 * dt
        if self.frame_index >= len(self.frames):
            self.active = False
            self.image = None
            self.finished = True     
        else:
            self.image = self.frames[int(self.frame_index)]
    def update(self, dt):
        if self.active:
            if self.image is not None:
                self.display_surface.blit(self.image, self.rect)
            self.animate(dt)
class ogre_combo_attack_2:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.frames = []
        for i in range(0, 15):
            self.frames.append(pygame.image.load('graphics/TOM ATTACK/COMBO_ANIMATION/OGRE ATTACK/ATTACK 2/'+str(i)+'.png'))
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(topleft = (0, 0))
        self.active = False
        self.finished = False
        self.attack_sound = pygame.mixer.Sound('audio/sound_effects/Ogre Attack 3/swoosh-2-99245.mp3')
    def play(self):
        self.active = True
        self.finished = False
        self.frame_index = 0
        self.attack_sound.play()
    def animate(self, dt):
        self.frame_index += 10 * dt
        if self.frame_index >= len(self.frames):
            self.active = False
            self.image = None
            self.finished = True       
        else:
            self.image = self.frames[int(self.frame_index)]
    def update(self, dt):
        if self.active:
            if self.image is not None:
                self.display_surface.blit(self.image, self.rect)
            self.animate(dt)
class ogre_combo_attack_3:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.frames = []
        for i in range(0, 24):
            self.frames.append(pygame.image.load('graphics/TOM ATTACK/COMBO_ANIMATION/OGRE ATTACK/ATTACK 3/'+str(i)+'.png'))
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(topleft = (0, 0))
        self.active = False
        self.finished = False
        self.attack_sound = pygame.mixer.Sound('audio/sound_effects/Ogre Attack 3/swoosh-2-99245.mp3')
    def play(self):
        self.active = True
        self.finished = False
        self.frame_index = 0
        self.attack_sound.play()
    def animate(self, dt):
        self.frame_index += 10 * dt
        if self.frame_index >= len(self.frames):
            self.active = False
            self.image = None
            self.finished = True
        else:
            self.image = self.frames[int(self.frame_index)]
    def update(self, dt):
        if self.active:
            if self.image is not None:
                self.display_surface.blit(self.image, self.rect)
            self.animate(dt)
class tom_attack_1:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.frames = []
        for i in range(0, 24):
            self.frames.append(pygame.image.load('graphics/TOM ATTACK/TOM ATTACK 1/' + str(i) + '.png'))
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.active = False
        self.finished = False
        self.attack_sound = pygame.mixer.Sound('audio/sound_effects/Tom Attack 1/swoosh-18-46746.mp3')
    def play(self):
        self.active = True
        self.finished = False
        self.frame_index = 0
        self.attack_sound.play()
    def animate(self, dt):
        self.frame_index += 10 * dt
        if self.frame_index >= len(self.frames):
            self.active = False
            self.image = None
            self.finished = True
        else:
            self.image = self.frames[int(self.frame_index)]
    def update(self, dt):
        if self.active:
            if self.image is not None:
                self.display_surface.blit(self.image, self.rect)
            self.animate(dt)
class tom_attack_2:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.frames = []
        for i in range(0, 28):
            self.frames.append(pygame.image.load('graphics/TOM ATTACK/TOM ATTACK 2/'+str(i)+'.png'))
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(topleft = (0, 0))
        self.active = False
        self.finished = False
        self.attack_sound = pygame.mixer.Sound('audio/sound_effects/Tom Attack 2/8 combo punch.mp3')
    def play(self):
        self.active = True
        self.finished = False
        self.frame_index = 0
        self.attack_sound.play()
    def animate(self, dt):
        self.frame_index += 10 * dt
        if self.frame_index >= len(self.frames):
            self.active = False
            self.image = None
            self.finished = True
        else:
            self.image = self.frames[int(self.frame_index)]
    def update(self, dt):
        if self.active:
            if self.image is not None:
                self.display_surface.blit(self.image, self.rect)
            self.animate(dt)
class ogre_attack_1:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.frames = []
        for i in range(0, 18):
            self.frames.append(pygame.image.load('graphics/TOM ATTACK/OGRE ATTACK 1/'+str(i)+'.png'))
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(topleft = (0, 0))
        self.active = False
        self.finished = False
        self.attack_sound = pygame.mixer.Sound('audio/sound_effects/Ogre Attack 1/Hit.mp3')
    def play(self):
        self.active = True
        self.finished = False
        self.frame_index = 0
        self.attack_sound.play()
    def animate(self, dt):
        self.frame_index += 10 * dt
        if self.frame_index >= len(self.frames):
            self.active = False
            self.image = None
            self.finished = True       
        else:
            self.image = self.frames[int(self.frame_index)]
    def update(self, dt):
        if self.active:
            if self.image is not None:
                self.display_surface.blit(self.image, self.rect)
            self.animate(dt)
class ogre_attack_2:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.frames = []
        for i in range(0, 18):
            self.frames.append(pygame.image.load('graphics/TOM ATTACK/OGRE ATTACK 2/'+str(i)+'.png'))
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(topleft = (0, 0))
        self.active = False
        self.finished = False
        self.attack_sound = pygame.mixer.Sound('audio/sound_effects/Ogre Attack 2/kick.mp3')
    def play(self):
        self.active = True
        self.finished = False
        self.frame_index = 0
        self.attack_sound.play()
    def animate(self, dt):
        self.frame_index += 10 * dt
        if self.frame_index >= len(self.frames):
            self.active = False
            self.image = None
            self.finished = True      
        else:
            self.image = self.frames[int(self.frame_index)]
    def update(self, dt):
        if self.active:
            if self.image is not None:
                self.display_surface.blit(self.image, self.rect)
            self.animate(dt)
class ogre_attack_3:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.frames = []
        for i in range(0, 18):
            self.frames.append(pygame.image.load('graphics/TOM ATTACK/OGRE ATTACK 3/'+str(i)+'.png'))
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(topleft = (0, 0))
        self.active = False
        self.finished = False
        self.attack_sound = pygame.mixer.Sound('audio/sound_effects/Ogre Attack 3/Fight - Sound Effect.mp3')
    def play(self):
        self.active = True
        self.finished = False
        self.frame_index = 0
        self.attack_sound.play()
    def animate(self, dt):
        self.frame_index += 10 * dt
        if self.frame_index >= len(self.frames):
            self.active = False
            self.image = None
            self.finished = True     
        else:
            self.image = self.frames[int(self.frame_index)]
    def update(self, dt):
        if self.active:
            if self.image is not None:
                self.display_surface.blit(self.image, self.rect)
            self.animate(dt)