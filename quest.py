import pygame, sys
from settings import *
from support import *
from timer import Timer

class quest:
    def __init__(self, name, description, objectives):
        self.name = name
        self.description = description
        self.objectives = objectives
        self.completed = False
    def get_name(self):
        return self.name
    def get_description(self):
        return self.description
    def get_objectives(self):
        obj_list = []
        for text in self.objectives:
            obj_list.append(text.get_text())
        return obj_list
    def objectives_class(self):
        objctv_list = []
        for objctv in self.objectives:
            objctv_list.append(objctv)
        return objctv_list
    def check_objectives(self):
        for objective in self.objectives:
            if not objective.completed:
                return False
        self.completed = True
        return True
class objectives:
    def __init__(self, description):
        self.description = description
        self.completed = False
    def get_text(self):
        return self.description
    def complete(self):
        self.completed = True
class quest_log:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font('font/Almendra-Bold.ttf', 30)
        self.font_title = pygame.font.Font('font/Almendra-Bold.ttf', 40)
        self.font1 = pygame.font.Font('font/Almendra-Bold.ttf', 18)
        self.width = 400
        self.space = 10
        self.padding = 8
        self.quests = []
        self.primary_quest = []
        self.index = None
        self.index1 = 0
        self.timer = Timer(200)
        self.b_time = pygame.time.get_ticks()
        self.new_quest = False
        self.already_selected = []
        self.input_1 = True
        self.input_2 = False
        self.move = False
    def add_quest(self, quest):
        self.quests.append(quest)
        self.new_quest = True
    def add_primary_quest(self, quest):
        self.primary_quest.append(quest)
        self.new_quest = True
    def get_primary_description(self):
        self.quest_description = []
        for description in self.primary_quest:
            self.quest_description.append(description.get_description())
        return self.quest_description
    def get_description(self):
        self.quest_description = []
        for description in self.quests:
            self.quest_description.append(description.get_description())
        return self.quest_description
    def get_primary_objectives(self):
        texts = []
        for text in self.primary_quest:
            texts.append(text.get_objectives())
        return texts
    def get_objectives(self):
        texts = []
        for text in self.quests:
            texts.append(text.get_objectives())
        return texts
    def primary_objectives_check(self):
        class_obj = []
        for objctv in self.primary_quest:
            class_obj.append(objctv.objectives_class())
        return class_obj
    def objectives_check(self):
        class_obj = []
        for objctv in self.quests:
            class_obj.append(objctv.objectives_class())
        return class_obj
    def input(self):
        keys = pygame.key.get_pressed()
        self.timer.update()
        if not self.timer.active:
            if keys[pygame.K_UP]:
                self.index -= 1
                self.move = True
                self.timer.activate()
            if keys[pygame.K_DOWN]:
                self.index += 1
                self.move = True
                self.timer.activate()
        if self.index < 0:
            self.input_2 = False
            self.input_1 = True
            if self.input_1:
                 self.index1 = len(self.get_primary_quest_name()) - 1
        if self.index > len(self.get_quest_name()) - 1:
            self.input_2 = False
            self.input_1 = True
            if self.input_1:
                self.index1 = 0
    def input_primary(self):
        keys = pygame.key.get_pressed()
        self.timer.update()
        if not self.timer.active:
            if keys[pygame.K_UP]:
                self.index1 -= 1
                self.move = True
                self.timer.activate()
            if keys[pygame.K_DOWN]:
                self.index1 += 1
                self.move = True
                self.timer.activate()
        if self.index1 < 0:
            if len(self.quests) == 0:
                self.index1 = len(self.get_primary_quest_name()) - 1
            else:
                self.input_1 = False
                self.input_2 = True
                if self.input_2:
                    self.index = len(self.get_quest_name()) - 1
        if self.index1 > len(self.get_primary_quest_name()) - 1:
            if len(self.quests) == 0:
                self.index1 = 0
            else:
                self.input_1 = False
                self.input_2 = True
                if self.input_2:
                    self.index = 0
    def get_primary_quest_name(self):
        self.quest_title = []
        self.ptotal_height = 0
        for title in self.primary_quest:
            title_name = self.font.render(title.get_name(), True, 'black')
            self.quest_title.append(title_name)
            self.ptotal_height += title_name.get_height() + (self.padding * 2)
        self.ptotal_height += (len(self.quest_title) - 1) * self.space
        self.pmenu_top = ((SCREEN_HEIGHT / 2) - 180) - self.ptotal_height / 2
        self.pmain_rect = pygame.Rect(220 , self.pmenu_top,self.width,self.ptotal_height)
        return self.quest_title
    def get_quest_name(self):
        self.quest_title = []
        self.total_height = 0
        for title in self.quests:
            title_name = self.font.render(title.get_name(), True, 'black')
            self.quest_title.append(title_name)
            self.total_height += title_name.get_height() + (self.padding * 2)
        self.total_height += (len(self.quest_title) - 1) * self.space
        self.menu_top = ((SCREEN_HEIGHT / 2) + 100) - self.total_height / 2
        self.main_rect = pygame.Rect(220 , self.menu_top,self.width,self.total_height)
        return self.quest_title
    def show_entry_primary(self, text_surf, title_surf ,desc_surf,  objctv_text, objctv_check,top, selected, quest):
        bg_rect = pygame.Rect(self.pmain_rect.left,top,self.width,text_surf.get_height() + (self.padding * 2))
        pygame.draw.rect(self.display_surface, 'White',bg_rect, 0, 4)
        text_rect = text_surf.get_rect(midleft = (self.pmain_rect.left + 20,bg_rect.centery))
        self.display_surface.blit(text_surf, text_rect)
        if not selected and quest not in self.already_selected:
            img = pygame.image.load('graphics/questlog/question_mark.png').convert_alpha()
            img_rect = img.get_rect(midleft=(self.main_rect.left - 75, bg_rect.centery))   
            self.c_time = pygame.time.get_ticks()
            if ((self.c_time - self.b_time) % 1000) < 500:
                self.display_surface.blit(img, img_rect)
        if selected:
            pygame.draw.rect(self.display_surface,'#c79931',bg_rect, 4,4)
            if quest not in self.already_selected:
                self.already_selected.append(quest)
            title_rect = title_surf.get_rect(center=((SCREEN_WIDTH /2) + 290, 205))
            self.display_surface.blit(title_surf, title_rect)
            lines = desc_surf.splitlines()
            y= 255
            for line in lines:
                desc = self.font1.render(line, True, 'black')
                desc_rect = desc.get_rect(midleft=((SCREEN_WIDTH /2) + 115, y))
                self.display_surface.blit(desc, desc_rect)
                y += desc.get_height()
            for i, text in enumerate(objctv_text):
                objctv_lines = text.splitlines()
                y_objctv = 345
                for objctv_line in objctv_lines:
                    objctv_surf = self.font1.render(objctv_line, True, 'black')
                    objctv_rect = objctv_surf.get_rect(midleft = ((SCREEN_WIDTH /2) + 180, (y_objctv + i * 70)))
                    self.display_surface.blit(objctv_surf, objctv_rect)
                    y_objctv += objctv_surf.get_height()
            box = pygame.image.load('graphics/questlog/checkbox0.png').convert_alpha()
            checkbox = pygame.image.load('graphics/questlog/checkboc_wch.png').convert_alpha()
            for i, obj in enumerate(objctv_check):
                if obj.completed:
                    image = checkbox
                else:
                    image = box
                image_rect = image.get_rect(midleft=((SCREEN_WIDTH /2) + 120, 345 + i * 70 ))
                self.display_surface.blit(image, image_rect)
        if quest.check_objectives():
            comp_surf = pygame.image.load('graphics/questlog/completed.png').convert_alpha()
            comp_rect = comp_surf.get_rect(midleft=(self.main_rect.left + 300, bg_rect.centery))
            self.display_surface.blit(comp_surf,comp_rect)
    def show_entry(self, text_surf, title_surf ,desc_surf,  objctv_text, objctv_check,top, selected, quest):
        bg_rect = pygame.Rect(self.main_rect.left,top,self.width,text_surf.get_height() + (self.padding * 2))
        pygame.draw.rect(self.display_surface, 'White',bg_rect, 0, 4)
        text_rect = text_surf.get_rect(midleft = (self.main_rect.left + 20,bg_rect.centery))
        self.display_surface.blit(text_surf, text_rect)
        if not selected and quest not in self.already_selected:
            img = pygame.image.load('graphics/questlog/question_mark.png').convert_alpha()
            img_rect = img.get_rect(midleft=(self.main_rect.left - 75, bg_rect.centery))
            self.c_time = pygame.time.get_ticks()
            if ((self.c_time - self.b_time) % 1000) < 500:
                self.display_surface.blit(img, img_rect)
        if selected:
            pygame.draw.rect(self.display_surface,'#c79931',bg_rect, 4,4)
            if quest not in self.already_selected:
                self.already_selected.append(quest)
            title_rect = title_surf.get_rect(center=((SCREEN_WIDTH /2) + 290, 205))
            self.display_surface.blit(title_surf, title_rect)
            lines = desc_surf.splitlines()
            y= 255
            for line in lines:
                desc = self.font1.render(line, True, 'black')
                desc_rect = desc.get_rect(midleft=((SCREEN_WIDTH /2) + 115, y))
                self.display_surface.blit(desc, desc_rect)
                y += desc.get_height()
            for i, text in enumerate(objctv_text):
                objctv_lines = text.splitlines()
                y_objctv = 345
                for objctv_line in objctv_lines:
                    objctv_surf = self.font1.render(objctv_line, True, 'black')
                    objctv_rect = objctv_surf.get_rect(midleft = ((SCREEN_WIDTH /2) + 180, (y_objctv + i * 70)))
                    self.display_surface.blit(objctv_surf, objctv_rect)
                    y_objctv += objctv_surf.get_height()
            box = pygame.image.load('graphics/questlog/checkbox0.png').convert_alpha()
            checkbox = pygame.image.load('graphics/questlog/checkboc_wch.png').convert_alpha()
            for i, obj in enumerate(objctv_check):
                if obj.completed:
                    image = checkbox
                else:
                    image = box
                image_rect = image.get_rect(midleft=((SCREEN_WIDTH /2) + 120, 345 + i * 70 ))
                self.display_surface.blit(image, image_rect)
            img_arrow = pygame.image.load('graphics/lessonlog/arrow_indicator.png').convert_alpha()
            img_arrow_rect = img_arrow.get_rect(midleft=(self.main_rect.left - 75, bg_rect.centery))
            self.c_time = pygame.time.get_ticks()
            if ((self.c_time - self.b_time) % 1000) < 500:
                self.display_surface.blit(img_arrow, img_arrow_rect)
        if quest.check_objectives():
            comp_surf = pygame.image.load('graphics/questlog/completed.png').convert_alpha()
            comp_rect = comp_surf.get_rect(midleft=(self.main_rect.left + 300, bg_rect.centery))
            self.display_surface.blit(comp_surf,comp_rect)
    def display(self):
        self.new_quest = False
        if self.input_1 and not self.input_2:
            self.input_primary()
        if self.input_2 and not self.input_1:
            self.input()
        img_surf =  pygame.image.load('graphics/questlog/questlog2.png').convert_alpha()
        img_rect = img_surf.get_rect(center = (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2))
        self.display_surface.blit(img_surf, img_rect)
        img1_surf =  pygame.image.load('graphics/questlog/quest_log.png').convert_alpha()
        img1_rect = img1_surf.get_rect(center = (SCREEN_WIDTH // 2 + 300, SCREEN_HEIGHT // 2))
        self.display_surface.blit(img1_surf, img1_rect)
        title_surf = self.font_title.render('Quest Log', False, 'white')
        title_rect = title_surf.get_rect(midbottom = (SCREEN_WIDTH // 2 - 220, 90))
        self.display_surface.blit(title_surf, title_rect)
        quest_names = self.get_quest_name()
        quest_descs = self.get_description()
        quest_objctv = self.get_objectives()
        check_objctv = self.objectives_check()
        for i, quest_name in enumerate(quest_names):
            top = self.main_rect.top + i * (quest_name.get_height() + (self.padding * 2) + self.space)
            self.show_entry(quest_name, quest_names[i],quest_descs[i], quest_objctv[i], check_objctv[i],top, self.index == i, self.quests[i])
        quest_names1 = self.get_primary_quest_name()
        quest_descs1 = self.get_primary_description()
        quest_objctv1 = self.get_primary_objectives()
        check_objctv1 = self.primary_objectives_check()
        for j, quest_name1 in enumerate(quest_names1):
            top1 = self.pmain_rect.top + j * (quest_name1.get_height() + (self.padding * 2) + self.space)
            self.show_entry(quest_name1, quest_names1[j],quest_descs1[j], quest_objctv1[j], check_objctv1[j],top1, self.index1 == j, self.primary_quest[j])
        tutorial = pygame.image.load('graphics/questlog/QUESTLOG_TOGGLE.png').convert_alpha()
        tutorial_rect = tutorial.get_rect(center = (((SCREEN_WIDTH/2) / 2 ) + 30, SCREEN_HEIGHT - 60))
        if not self.move:
            self.c_time = pygame.time.get_ticks()
            if ((self.c_time - self.b_time) % 1000) < 500:
                self.display_surface.blit(tutorial, tutorial_rect)