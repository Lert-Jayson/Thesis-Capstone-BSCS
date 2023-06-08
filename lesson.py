import pygame, json
from settings import *
from support import *
from sprites import *
from timer import Timer

class lesson_group:
    def __init__(self, name, lesson_log):
        self.name = name
        self.lesson_log = lesson_log
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font('font/Almendra-Bold.ttf', 30)
        self.font_title = pygame.font.Font('font/Almendra-Bold.ttf', 40)
        self.font1 = pygame.font.Font('font/Almendra-Bold.ttf', 18)
        self.width = 360
        self.space = 6
        self.padding = 4
        self.index = 0
        self.timer = Timer(200)
        self.b_time = pygame.time.get_ticks()
        self.lessons = []
        self.input_active = False
        self.lesson_active = False
    def add_lesson(self, lesson):
        self.lessons.append(lesson)
    def remove_lesson(self):
        for lesson in self.lessons[:]:
            if lesson != self.lessons[0]:
                self.lessons.remove(lesson)
    def get_lessons(self):
        lesson_list = []
        for lesson in self.lessons:
            lesson_list.append(lesson)
        return lesson_list   
    def input(self):
        keys = pygame.key.get_pressed()
        self.timer.update()
        if not self.timer.active:
            if keys[pygame.K_UP]:
                self.index -= 1
                self.timer.activate()
            if keys[pygame.K_DOWN]:
                self.index += 1
                self.timer.activate()
            if keys[pygame.K_LEFT]:
                self.timer.activate()
                self.input_active = False
                self.lesson_log.input_active = True
            if keys[pygame.K_RETURN]:
                selected_lesson = self.lessons[self.index]
                selected_lesson.log_active = True
                self.lesson_active = True
                self.lesson_log.lesson_active = True
                self.input_active = False
        if self.index < 0:
            self.index = len(self.get_lesson_name()) - 1
        if self.index > len(self.get_lesson_name()) - 1:
            self.index = 0
    def get_lesson_name(self):
        self.lesson_names = []
        self.total_height = 0
        for name in self.lessons:
            lesson_name = self.font.render(name.name, True, 'black')
            self.lesson_names.append(lesson_name)
            self.total_height += lesson_name.get_height() + (self.padding * 2)
        self.total_height += (len(self.lesson_names) - 1) * self.space
        self.menu_top = (SCREEN_HEIGHT / 2) + 85 - self.total_height / 2
        self.main_rect = pygame.Rect((SCREEN_WIDTH /2) + 110, self.menu_top,self.width,self.total_height)
        return self.lesson_names
    def show_entry(self, text_surf, top, selected, lesson):
        if not self.lesson_active:
            bg_rect = pygame.Rect(self.main_rect.left,top,self.width,text_surf.get_height() + (self.padding * 2))
            text_rect = text_surf.get_rect(midleft = (self.main_rect.left + 20,bg_rect.centery))
            self.display_surface.blit(text_surf, text_rect)
        if selected:
            if self.input_active:
                pygame.draw.rect(self.display_surface,'black',bg_rect, 4,4)
                img = pygame.image.load('graphics/lessonlog/arrow_indicator.png').convert_alpha()
                img_rect = img.get_rect(midleft=(self.main_rect.left - 75, bg_rect.centery))
                self.c_time = pygame.time.get_ticks()
                if ((self.c_time - self.b_time) % 1000) < 500:
                    self.display_surface.blit(img, img_rect)
            lesson.display_surf()
    def display(self):   
        if self.input_active:
            self.input()  
        lesson_names = self.get_lesson_name()
        for i, lesson_name in enumerate(lesson_names):
            top = self.main_rect.top + i * (lesson_name.get_height() + (self.padding * 2) + self.space)
            self.show_entry(lesson_name,top, self.index == i, self.lessons[i])
class Lessons:
    def __init__(self, name, surf, group):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font('font/LycheeSoda.ttf', 35)
        self.name = name
        self.group = group
        self.surf = surf
        self.active = True
        self.log_active = False
        self.image = pygame.image.load(surf).convert_alpha()
        self.rect = self.image.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    def input(self):
        keys = pygame.key.get_pressed()
        load={
			'lesson_done':[]
        }
        try:
            with open('lessonload_file.txt') as load_file:
                load = json.load(load_file)
        except:
            pass
        if keys[pygame.K_x]:
           self.active = False
           self.lesson_done=load['lesson_done']
           self.lesson_done.append(self.name)
           with open('lessonload_file.txt','w') as load_file:
               json.dump({'lesson_done':self.lesson_done},load_file)
    def display(self):
        self.input()
        if self.active:
            self.display_surface.blit(self.image, self.rect)
            exit_text = self.font.render('Back[x]', True, 'black')
            exit_rect = exit_text.get_rect(bottomright = (SCREEN_WIDTH-50, SCREEN_HEIGHT-50))
            self.display_surface.blit(exit_text, exit_rect)
    def display_surf(self):
        if self.log_active:
            self.display_surface.blit(self.image, self.rect)
            exit_text = self.font.render('Back[x]', True, 'black')
            exit_rect = exit_text.get_rect(bottomright = (SCREEN_WIDTH-50, SCREEN_HEIGHT-50))
            self.display_surface.blit(exit_text, exit_rect)
            pygame.display.flip()
            if pygame.key.get_pressed()[pygame.K_x]:
                self.log_active = False
                self.group.input_active = True
                self.group.lesson_active = False
                self.group.lesson_log.lesson_active = False
class lesson_log:
    def __init__(self) :
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font('font/Almendra-Bold.ttf', 30)
        self.font_title = pygame.font.Font('font/Almendra-Bold.ttf', 40)
        self.font1 = pygame.font.Font('font/Almendra-Bold.ttf', 18)
        self.width = 360
        self.space = 10
        self.padding = 8
        self.index = 0
        self.timer = Timer(200)
        self.b_time = pygame.time.get_ticks()
        self.lesson_groups = []
        self.input_active = True
        self.lesson_active = False
    def add_lesson_group(self, lesson_group):
        self.lesson_groups.append(lesson_group)
    def input(self):
        keys = pygame.key.get_pressed()
        self.timer.update()
        if not self.timer.active:
            if keys[pygame.K_UP]:
                self.index -= 1
                self.timer.activate()
            if keys[pygame.K_DOWN]:
                self.index += 1
                self.timer.activate()
            if keys[pygame.K_RIGHT]:
                self.timer.activate()
                self.input_active = False
                current_index = self.get_lesson_class()[self.index]
                current_index.input_active = True
        if self.index < 0:
            self.index = len(self.get_lesson_group()) - 1
        if self.index > len(self.get_lesson_group()) - 1:
            self.index = 0
    def get_lesson_class(self):
        class_list = []
        for lesson in self.lesson_groups:
            class_list.append(lesson)
        return class_list
    def get_lesson_group(self):
        self.group_names = []
        self.total_height = 0
        for name in self.lesson_groups:
            group_name = self.font.render(name.name, True, 'black')
            self.group_names.append(group_name)
            self.total_height += group_name.get_height() + (self.padding * 2)
        self.total_height += (len(self.group_names) - 1) * self.space
        self.menu_top = (SCREEN_HEIGHT / 2) + 50 - self.total_height / 2
        self.main_rect = pygame.Rect(280 , self.menu_top,self.width,self.total_height)
        return self.group_names
    def show_entry(self, text_surf, top, selected, lessons):
        if not self.lesson_active:
            bg_rect = pygame.Rect(self.main_rect.left,top,self.width,text_surf.get_height() + (self.padding * 2))
            text_rect = text_surf.get_rect(midleft = (self.main_rect.left + 20,bg_rect.centery))
            self.display_surface.blit(text_surf, text_rect)
        if selected:
            if self.input_active:
                pygame.draw.rect(self.display_surface,'black',bg_rect, 4,4)
                img = pygame.image.load('graphics/lessonlog/arrow_indicator.png').convert_alpha()
                img_rect = img.get_rect(midleft=(self.main_rect.left - 75, bg_rect.centery))
                self.c_time = pygame.time.get_ticks()
                if ((self.c_time - self.b_time) % 1000) < 500:
                    self.display_surface.blit(img, img_rect)
            lessons.display()
    def display(self):
        if self.input_active:
            self.input()
        img_surf = pygame.image.load('graphics/lessonlog/lesson_log_title.png').convert_alpha()
        img_rect = img_surf.get_rect(topleft = (50,0))
        self.display_surface.blit(img_surf, img_rect)
        tutorial = pygame.image.load('graphics/lessonlog/LESSON_LOG_TOGGLE.png').convert_alpha()
        tutorial_rect = tutorial.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT - 40))
        self.display_surface.blit(tutorial, tutorial_rect)
        lesson_class = self.get_lesson_class()
        lesson_group_names = self.get_lesson_group()
        for i, group_name in enumerate(lesson_group_names):
            top = self.main_rect.top + i * (group_name.get_height() + (self.padding * 2) + self.space)
            self.show_entry(group_name,top, self.index == i, lesson_class[i])