import pygame, sys
import mysql.connector, random
from settings import *
from support import *
from sprites import *
from timer import Timer
from player import *


class review:
    def __init__(self, name , surf, player):
        self.font = pygame.font.Font('font/LycheeSoda.ttf', 30)
        self.display_surface = pygame.display.get_surface()
        self.name = name
        self.surf = surf
        self.active = False
        self.player = player
 
        self.image = pygame.image.load(surf).convert_alpha()
        self.rect = self.image.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

        mydb=mysql.connector.connect(
            host="localhost",
            username="root",
            password="",
            database="adventures_of_tom"
            )
        mycursor= mydb.cursor()

        mycursor.execute('SELECT question, choice1, choice2, choice3, choice4, answer_key FROM question_bank_prog1 WHERE grading_period="Prelim" AND lesson_number="L1" ')
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

        # shuffle the quiz data
        random.shuffle(self.quiz_data)

        # set up the game loop
        self.current_question = 0
        self.score = 0

        self.timer = Timer(200)

    def reset(self):
        mydb=mysql.connector.connect(
            host="localhost",
            username="root",
            password="",
            database="adventures_of_tom"
            )
        mycursor= mydb.cursor()

        mycursor.execute('SELECT question, choice1, choice2, choice3, choice4, answer_key FROM question_bank_prog1 WHERE grading_period="Prelim" AND lesson_number="L1" ')
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

        # shuffle the quiz data
        random.shuffle(self.quiz_data)

        # set up the game loop
        self.current_question = 0
        self.score = 0

        self.player.retry = False


    def input(self):
        # for event in pygame.event.get():
        #     if event.type==pygame.KEYDOWN:
        keys = pygame.key.get_pressed()
        self.timer.update()

        if not self.timer.active:
            if self.current_question < len(self.quiz_data):
                if keys[pygame.K_1]:
                    if self.quiz_data[self.current_question]["options"][0] == self.quiz_data[self.current_question]["answer"]:
                        self.score += 1
                    self.timer.activate()
                    self.current_question += 1
                elif keys[pygame.K_2]:
                        if self.quiz_data[self.current_question]["options"][1] == self.quiz_data[self.current_question]["answer"]:
                            self.score += 1
                        self.timer.activate()
                        self.current_question += 1
                elif keys[pygame.K_3]:
                    if self.quiz_data[self.current_question]["options"][2] == self.quiz_data[self.current_question]["answer"]:
                        self.score += 1
                    self.timer.activate()
                    self.current_question += 1
                elif keys[pygame.K_4]:
                    if self.quiz_data[self.current_question]["options"][3] == self.quiz_data[self.current_question]["answer"]:
                        self.score += 1
                    self.timer.activate()
                    self.current_question += 1
        if self.current_question >= len(self.quiz_data):
                pass
               
    def display(self):
        if self.active:
            self.input()
            self.display_surface.blit(self.image, self.rect)
            if self.current_question < len(self.quiz_data):
                question_text = self.font.render((self.quiz_data[self.current_question]["question"]), True, 'white',None)
                question_rect = question_text.get_rect()
                question_rect.center = (self.rect.centerx,150)
                self.display_surface.blit(question_text, question_rect)

                option1_text = self.font.render("1. " + self.quiz_data[self.current_question]["options"][0], True, 'gray')
                option1_rect = option1_text.get_rect()
                option1_rect.center = (self.rect.centerx,250)
                self.display_surface.blit(option1_text, option1_rect)

                option2_text = self.font.render("2. " + self.quiz_data[self.current_question]["options"][1], True, 'gray')
                option2_rect = option2_text.get_rect()
                option2_rect.center = (self.rect.centerx,300)
                self.display_surface.blit(option2_text, option2_rect)

                option3_text = self.font.render("3. " + self.quiz_data[self.current_question]["options"][2], True, 'gray')
                option3_rect = option3_text.get_rect()
                option3_rect.center = (self.rect.centerx,350)
                self.display_surface.blit(option3_text, option3_rect)

                option4_text = self.font.render("4. " + self.quiz_data[self.current_question]["options"][3], True, 'gray')
                option4_rect = option4_text.get_rect()
                option4_rect.center = (self.rect.centerx,400)
                self.display_surface.blit(option4_text, option4_rect)

            if self.current_question >= len(self.quiz_data):
                if (self.score)/(len(self.quiz_data))>=.75:
                    score_text= self.font.render("Your score was: " + str(self.score) +" out of "+ str(len(self.quiz_data))+". You passed!", True, 'white')
                    score_rect = score_text.get_rect()
                    score_rect.center=self.rect.center
                    self.display_surface.blit(score_text, score_rect)
                    exit_text = self.font.render('Back[x]', True, 'white')
                    exit_rect = exit_text.get_rect(bottomright = (SCREEN_WIDTH-120, SCREEN_HEIGHT-80))
                    self.display_surface.blit(exit_text, exit_rect)
                    if pygame.key.get_pressed()[pygame.K_x]:
                        self.player.chief_second_dialogue_complete=False
                        self.active=False
                        self.player.dialogue_order = 11
                else:
                    score_text= self.font.render("Your score was: " + str(self.score) +" out of "+ str(len(self.quiz_data))+". You didn't pass!", True, 'white')
                    score_rect = score_text.get_rect()
                    score_rect.center=self.rect.center
                    self.display_surface.blit(score_text, score_rect)
                    exit_text = self.font.render('Back[x]', True, 'white')
                    exit_rect = exit_text.get_rect(bottomright = (SCREEN_WIDTH-120, SCREEN_HEIGHT-80))
                    self.display_surface.blit(exit_text, exit_rect)
                    if pygame.key.get_pressed()[pygame.K_x]:
                        self.player.chief_second_dialogue_complete=False
                        self.active=False
                        self.player.dialogue_order = 12
                        self.player.retry = True
                        self.reset()

            tutorial = pygame.image.load('graphics/review_question_tutorial.png').convert_alpha()
            tutorial_rect = tutorial.get_rect(midbottom = ((SCREEN_WIDTH/2) + 30,SCREEN_HEIGHT-5))
            self.display_surface.blit(tutorial, tutorial_rect)

class reviewc:
    def __init__(self, name , surf, player):
        self.font = pygame.font.Font('font/LycheeSoda.ttf', 30)
        self.display_surface = pygame.display.get_surface()
        self.name = name
        self.surf = surf
        self.active = False
        self.player = player
 
        self.image = pygame.image.load(surf).convert_alpha()
        self.rect = self.image.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

        mydb=mysql.connector.connect(
            host="localhost",
            username="root",
            password="",
            database="adventures_of_tom"
            )
        mycursor= mydb.cursor()

        mycursor.execute('SELECT question, choice1, choice2, choice3, choice4, answer_key FROM question_bank_prog1 WHERE grading_period="Prelim" AND lesson_number="L2" ')
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

        # shuffle the quiz data
        random.shuffle(self.quiz_data)

        # set up the game loop
        self.current_question = 0
        self.score = 0
        self.timer = Timer(200)

    def reset(self):
        mydb=mysql.connector.connect(
            host="localhost",
            username="root",
            password="",
            database="adventures_of_tom"
            )
        mycursor= mydb.cursor()

        mycursor.execute('SELECT question, choice1, choice2, choice3, choice4, answer_key FROM question_bank_prog1 WHERE grading_period="Prelim" AND lesson_number="L2" ')
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

        # shuffle the quiz data
        random.shuffle(self.quiz_data)

        # set up the game loop
        self.current_question = 0
        self.score = 0

        self.player.failed = False


    def input(self):
        # for event in pygame.event.get():
        #     if event.type==pygame.KEYDOWN:

        keys = pygame.key.get_pressed()
        self.timer.update()

        if not self.timer.active:
            if self.current_question < len(self.quiz_data):
                if keys[pygame.K_1]:
                    if self.quiz_data[self.current_question]["options"][0] == self.quiz_data[self.current_question]["answer"]:
                        self.score += 1
                    self.timer.activate()
                    self.current_question += 1
                elif keys[pygame.K_2]:
                    if self.quiz_data[self.current_question]["options"][1] == self.quiz_data[self.current_question]["answer"]:
                        self.score += 1
                    self.timer.activate()
                    self.current_question += 1
                elif keys[pygame.K_3]:
                    if self.quiz_data[self.current_question]["options"][2] == self.quiz_data[self.current_question]["answer"]:
                        self.score += 1
                    self.timer.activate()
                    self.current_question += 1
                elif keys[pygame.K_4]:
                    if self.quiz_data[self.current_question]["options"][3] == self.quiz_data[self.current_question]["answer"]:
                        self.score += 1
                    self.timer.activate()
                    self.current_question += 1
        if self.current_question >= len(self.quiz_data):
            pass
               
    def display(self):
        if self.active:
            self.input()
            self.display_surface.blit(self.image, self.rect)
            if self.current_question < len(self.quiz_data):
                question_text = self.font.render((self.quiz_data[self.current_question]["question"]), True, 'white',None)
                question_rect = question_text.get_rect()
                question_rect.center = (self.rect.centerx,150)
                self.display_surface.blit(question_text, question_rect)

                option1_text = self.font.render("1. " + self.quiz_data[self.current_question]["options"][0], True, 'gray')
                option1_rect = option1_text.get_rect()
                option1_rect.center = (self.rect.centerx,250)
                self.display_surface.blit(option1_text, option1_rect)

                option2_text = self.font.render("2. " + self.quiz_data[self.current_question]["options"][1], True, 'gray')
                option2_rect = option2_text.get_rect()
                option2_rect.center = (self.rect.centerx,300)
                self.display_surface.blit(option2_text, option2_rect)

                option3_text = self.font.render("3. " + self.quiz_data[self.current_question]["options"][2], True, 'gray')
                option3_rect = option3_text.get_rect()
                option3_rect.center = (self.rect.centerx,350)
                self.display_surface.blit(option3_text, option3_rect)

                option4_text = self.font.render("4. " + self.quiz_data[self.current_question]["options"][3], True, 'gray')
                option4_rect = option4_text.get_rect()
                option4_rect.center = (self.rect.centerx,400)
                self.display_surface.blit(option4_text, option4_rect)

            if self.current_question >= len(self.quiz_data):
                if (self.score)/(len(self.quiz_data))>=.75:
                    score_text= self.font.render("Your score was: " + str(self.score) +" out of "+ str(len(self.quiz_data))+". You passed!", True, 'white')
                    score_rect = score_text.get_rect()
                    score_rect.center=self.rect.center
                    self.display_surface.blit(score_text, score_rect)
                    exit_text = self.font.render('Back[x]', True, 'white')
                    exit_rect = exit_text.get_rect(bottomright = (SCREEN_WIDTH-120, SCREEN_HEIGHT-80))
                    self.display_surface.blit(exit_text, exit_rect)
                    if pygame.key.get_pressed()[pygame.K_x]:
                        self.player.test = False
                        self.active = False
                        self.player.continueanim=True

                else:
                    score_text= self.font.render("Your score was: " + str(self.score) +" out of "+ str(len(self.quiz_data))+". You didn't pass!", True, 'white')
                    score_rect = score_text.get_rect()
                    score_rect.center=self.rect.center
                    self.display_surface.blit(score_text, score_rect)
                    exit_text = self.font.render('Back[x]', True, 'white')
                    exit_rect = exit_text.get_rect(bottomright = (SCREEN_WIDTH-120, SCREEN_HEIGHT-80))
                    self.display_surface.blit(exit_text, exit_rect)
                    if pygame.key.get_pressed()[pygame.K_x]:
                        self.player.test = False
                        self.active = False
                        self.player.retry = True
                        self.reset()
            
            tutorial = pygame.image.load('graphics/review_question_tutorial.png').convert_alpha()
            tutorial_rect = tutorial.get_rect(midbottom = ((SCREEN_WIDTH/2) + 30,SCREEN_HEIGHT-5))
            self.display_surface.blit(tutorial, tutorial_rect)

               
                   

        

                   

        
