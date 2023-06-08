import pygame,json
from support import import_folder
from text_overlay import *
from settings import *


def draw_text( name,text, size, color, x, y, namex, namey, display_surface):
    font = pygame.font.Font('font/Almendra-Bold.ttf', size)

    name_surf = font.render(name, True, color)
    # text_surface = font.render(text, True, color)

    name_rect = name_surf.get_rect()
    name_rect.topleft = (namex, namey)
    # text_rect = text_surface.get_rect()
    # text_rect.topleft = (x, y)
    
    display_surface.blit(name_surf, name_rect)
    # display_surface.blit(text_surface, text_rect)

    lines = text.splitlines()
    for line in lines:
        text_surf = font.render(line, True, color)
        text_rect = text_surf.get_rect(topleft = (x, y))
        display_surface.blit(text_surf, text_rect)
        y += text_surf.get_height()

def draw_npc(character, x, y , display_surface):
    image = pygame.image.load(character).convert_alpha()
    img_rect = image.get_rect()
    img_rect.midbottom = (x, y )

    display_surface.blit(image, img_rect)

class dialogue_npcChief:
    def __init__(self, player):
        # Variables
        self.name = 'Chief'
        self.step = 0
        self.dialogue_running = True

        self.player = player
        self.text_overlay = text_overlay()

        #characters
        self.character = {
            'Tom' : 'graphics/caracters_w1/tom.png', 
            'chief' : 'graphics/caracters_w1/chief.png'
        }
        self.char_name = ['Tom', 'Chief']


        # Dialogue
        self.text = {
            '0': "Hello sir, I just wanna ask, are you the chief of this village?",
            '1': "Yes I am the chief of this village, why are you asking?",
            '2': "I'm Tom, it is so nice meeting you. I'm looking for something\nthat is crucially important for me",
            '3': "A powerful Gem that is essential to save my world.",
            '4': "Why do you need the Gem? ",
            '5': " I'm from the future and my world is in real danger right now.\nI need to save my people before it's too late.",
            '6': "Do you know that this Gem is too powerful? It is not easy to\nfind and challenging to discover.",
            '7': "Would you still go for it?",
            '8': "Definitely!!",
            '9': " Before I give you the information about the untold power of\nthe gem, first you need to help my villagers.",
            '10': "In your journey you will see the scrolls of knowledge that\ncontains vital information that you must remember ",
            '11': "because it will determine your fate..",
            '12': "First, you must go to the monkey and help him.",
        }
        self.text_counter = 0


    def update(self):

        pressed = pygame.key.get_pressed()
        skip = pressed[pygame.K_x]
        skip_all = pressed[pygame.K_SPACE]

        # First step (dialogue)
        if self.step == 0:
            if int(self.text_counter) < len(self.text['0']):
                if skip_all:
                    self.text_counter = len(self.text['0'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 1  
        if self.step == 1:
            if int(self.text_counter) < len(self.text['1']):
                if skip_all:
                    self.text_counter = len(self.text['1'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 2
        if self.step == 2:
            if int(self.text_counter) < len(self.text['2']):
                if skip_all:
                    self.text_counter = len(self.text['2'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 3

        if self.step == 3:
            if int(self.text_counter) < len(self.text['3']):
                if skip_all:
                    self.text_counter = len(self.text['3'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 4

        if self.step == 4:
            if int(self.text_counter) < len(self.text['4']):
                if skip_all:
                    self.text_counter = len(self.text['4'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 5  

        if self.step == 5:
            if int(self.text_counter) < len(self.text['5']):
                if skip_all:
                    self.text_counter = len(self.text['5'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 6
        
        if self.step == 6:
            if int(self.text_counter) < len(self.text['6']):
                if skip_all:
                    self.text_counter = len(self.text['6'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 7

        if self.step == 7:
            if int(self.text_counter) < len(self.text['7']):
                if skip_all:
                    self.text_counter = len(self.text['7'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 8

        if self.step == 8:
            if int(self.text_counter) < len(self.text['8']):
                if skip_all:
                    self.text_counter = len(self.text['8'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 9

        if self.step == 9:
            if int(self.text_counter) < len(self.text['9']):
                if skip_all:
                    self.text_counter = len(self.text['9'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 10

        if self.step == 10:
            if int(self.text_counter) < len(self.text['10']):
                if skip_all:
                    self.text_counter = len(self.text['10'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 11

        if self.step == 11:
            if int(self.text_counter) < len(self.text['11']):
                if skip_all:
                    self.text_counter = len(self.text['11'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 12                     

        if self.step == 12:
            if int(self.text_counter) < len(self.text['12']):
                if skip_all:
                    self.text_counter = len(self.text['12'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    # Finish the dialogue
                    self.player.chief_quest = True
                    self.dialogue_running = False
                    self.player.speaking = False

        return self.dialogue_running
    
    def draw(self, display_surface):

        if self.step == 0:
            draw_text(self.char_name[0],self.text['0'][0:int(self.text_counter)],30,'white', 210 , (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['0']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
    
        if self.step == 1:
            draw_text( self.char_name[1], self.text['1'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['chief'], display_surface.get_width() - 378, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['1']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 2:
            draw_text(self.char_name[0],self.text['2'][0:int(self.text_counter)],30,'white', 210 , (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['2']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
    
        if self.step == 3:
            draw_text(self.char_name[0],self.text['3'][0:int(self.text_counter)],30,'white', 210 , (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['3']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
    
        if self.step == 4:
            draw_text( self.char_name[1], self.text['4'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['chief'], display_surface.get_width() - 378, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['4']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 5:
            draw_text(self.char_name[0],self.text['5'][0:int(self.text_counter)],30,'white', 210 , (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['5']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
    
        if self.step == 6:
            draw_text( self.char_name[1], self.text['6'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['chief'], display_surface.get_width() - 378, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['6']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 7:
            draw_text( self.char_name[1], self.text['7'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['chief'], display_surface.get_width() - 378, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['7']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        if self.step == 8:
            draw_text(self.char_name[0],self.text['8'][0:int(self.text_counter)],30,'white', 210 , (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['8']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
    
        if self.step == 9:
            draw_text( self.char_name[1], self.text['9'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['chief'], display_surface.get_width() - 378, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['9']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 10:
            draw_text( self.char_name[1], self.text['10'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['chief'], display_surface.get_width() - 378, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['10']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 11:
            draw_text( self.char_name[1], self.text['11'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['chief'], display_surface.get_width() - 378, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['11']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 12:
            draw_text( self.char_name[1], self.text['12'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['chief'], display_surface.get_width() - 378, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['12']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

class dialogue_npcChief_:
    def __init__(self, player):
        # Variables
        self.name = 'Chief_'
        self.step = 0
        self.dialogue_running = True

        self.player = player
        self.text_overlay = text_overlay()

        #characters
        self.character = {
            'Tom' : 'graphics/caracters_w1/tom.png', 
            'chief' : 'graphics/caracters_w1/chief.png'
        }
        self.char_name = ['Tom', 'Chief']


        # Dialogue
        self.text = {
            '0': "Have you gone to Monkey yet?",
            '1': "No, where can I find him?",
            '2': "Just check your MAP and you can find him in the CLEARING WOODS",
            '3': "Okay, Thank you.",
            
        }
        self.text_counter = 0


    def update(self):

        pressed = pygame.key.get_pressed()
        skip = pressed[pygame.K_x]
        skip_all = pressed[pygame.K_SPACE]

        # First step (dialogue)
        if self.step == 0:
            if int(self.text_counter) < len(self.text['0']):
                if skip_all:
                    self.text_counter = len(self.text['0'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 1  
        if self.step == 1:
            if int(self.text_counter) < len(self.text['1']):
                if skip_all:
                    self.text_counter = len(self.text['1'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 2
        if self.step == 2:
            if int(self.text_counter) < len(self.text['2']):
                if skip_all:
                    self.text_counter = len(self.text['2'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 3

        if self.step == 3:
            if int(self.text_counter) < len(self.text['3']):
                if skip_all:
                    self.text_counter = len(self.text['3'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    # Finish the dialogue
                    self.dialogue_running = False
                 

        return self.dialogue_running
    
    def draw(self, display_surface):

        if self.step == 0:
            draw_text( self.char_name[1], self.text['0'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['chief'], display_surface.get_width() - 378, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['0']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 1:
            draw_text(self.char_name[0],self.text['1'][0:int(self.text_counter)],30,'white', 210 , (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['1']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 2:
            draw_text( self.char_name[1], self.text['2'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['chief'], display_surface.get_width() - 378, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['2']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 3:
            draw_text(self.char_name[0],self.text['3'][0:int(self.text_counter)],30,'white', 210 , (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['3']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
class dialogue_npcChief1:
    def __init__(self, player):
        # Variables
        self.name = 'Chief1'
        self.step = 0
        self.dialogue_running = True

        self.player = player
        self.text_overlay = text_overlay()
        
            # set up the game loop
            

        #characters
        self.character = {
            'Tom' : 'graphics/caracters_w1/tom.png', 
            'chief' : 'graphics/caracters_w1/chief.png'
        }
        self.char_name = ['Tom', 'Chief']


        # Dialogue
        self.text = {
            '0': "Are you done with helping my villagers?",
            '1': "Yes I've helped them all",
            '2': "Did you also pay attention to the scrolls of knowledge\n you encounter?",
            '3': "I sure did",
            '4': "Let me test you then",
        }
        self.text_counter = 0


    def update(self):
       
        pressed = pygame.key.get_pressed()
        skip = pressed[pygame.K_x]
        skip_all = pressed[pygame.K_SPACE]
     

        # First step (dialogue)
        if self.step == 0:
            if int(self.text_counter) < len(self.text['0']):
                if skip_all:
                    self.text_counter = len(self.text['0'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 1  
        if self.step == 1:
            if int(self.text_counter) < len(self.text['1']):
                if skip_all:
                    self.text_counter = len(self.text['1'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 2
        if self.step == 2:
            if int(self.text_counter) < len(self.text['2']):
                if skip_all:
                    self.text_counter = len(self.text['2'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 3

        if self.step == 3:
            if int(self.text_counter) < len(self.text['3']):
                if skip_all:
                    self.text_counter = len(self.text['3'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 4

        if self.step == 4:
            if int(self.text_counter) < len(self.text['4']):
                if skip_all:
                    self.text_counter = len(self.text['4'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                     # Finish the dialogue
                    self.dialogue_running = False
                    self.player.chief_second_dialogue_complete = True

       
        return self.dialogue_running
    
    def draw(self, display_surface):
    
        if self.step == 0:
            draw_text( self.char_name[1], self.text['0'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['chief'], display_surface.get_width() - 378, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['0']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 1:
            draw_text(self.char_name[0],self.text['1'][0:int(self.text_counter)],30,'white', 210 , (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['1']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
      
        if self.step == 2:
            draw_text( self.char_name[1], self.text['2'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['chief'], display_surface.get_width() - 378, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['2']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 3:
            draw_text(self.char_name[0],self.text['3'][0:int(self.text_counter)],30,'white', 210 , (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['3']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
    
        if self.step == 4:
            draw_text( self.char_name[1], self.text['4'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['chief'], display_surface.get_width() - 378, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['4']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 4:
            draw_text( self.char_name[1], self.text['4'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['chief'], display_surface.get_width() - 378, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['4']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

class dialogue_npcChief2:
    def __init__(self, player):
        # Variables
        self.name = 'Chief2'
        self.step = 0
        self.dialogue_running = True

        self.player = player
        self.text_overlay = text_overlay()
        
            # set up the game loop
            

        #characters
        self.character = {
            'Tom' : 'graphics/caracters_w1/tom.png', 
            'chief' : 'graphics/caracters_w1/chief.png'
        }
        self.char_name = ['Tom', 'Chief']


        # Dialogue
        self.text = {
            '0': "Congratulations, you've passed the test.",
            '1': "As promised, I'll give you information on the \nwhereabouts of the Gem of Lightning.",
            '2': "Open your map and I'm sure you'll find the CAVE.",
            '3': "The Gem of Lightning is said to be inside of it.",
            '4': "Good luck adventurer and I hope you find that Gem",
        }
        self.text_counter = 0


    def update(self):
       
        pressed = pygame.key.get_pressed()
        skip = pressed[pygame.K_x]
        skip_all = pressed[pygame.K_SPACE]
     

        # First step (dialogue)
        if self.step == 0:
            if int(self.text_counter) < len(self.text['0']):
                if skip_all:
                    self.text_counter = len(self.text['0'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 1  
        if self.step == 1:
            if int(self.text_counter) < len(self.text['1']):
                if skip_all:
                    self.text_counter = len(self.text['1'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 2
        if self.step == 2:
            if int(self.text_counter) < len(self.text['2']):
                if skip_all:
                    self.text_counter = len(self.text['2'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 3

        if self.step == 3:
            if int(self.text_counter) < len(self.text['3']):
                if skip_all:
                    self.text_counter = len(self.text['3'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 4

        if self.step == 4:
            if int(self.text_counter) < len(self.text['4']):
                if skip_all:
                    self.text_counter = len(self.text['4'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                     # Finish the dialogue
                    self.dialogue_running = False
                    self.player.chief_second_dialogue_complete = False

        return self.dialogue_running
    
    def draw(self, display_surface):
    
        if self.step == 0:
            draw_text( self.char_name[1], self.text['0'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['chief'], display_surface.get_width() - 378, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['0']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 1:
            draw_text(self.char_name[0],self.text['1'][0:int(self.text_counter)],30,'white', 210 , (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['chief'], display_surface.get_width() - 378, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['1']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
      
        if self.step == 2:
            draw_text( self.char_name[1], self.text['2'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['chief'], display_surface.get_width() - 378, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['2']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 3:
            draw_text(self.char_name[0],self.text['3'][0:int(self.text_counter)],30,'white', 210 , (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['chief'], display_surface.get_width() - 378, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['3']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
    
        if self.step == 4:
            draw_text( self.char_name[1], self.text['4'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['chief'], display_surface.get_width() - 378, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['4']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 4:
            draw_text( self.char_name[1], self.text['4'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['chief'], display_surface.get_width() - 378, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['4']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

class dialogue_npcChief3:
    def __init__(self, player):
        # Variables
        self.name = 'Chief3'
        self.step = 0
        self.dialogue_running = True

        self.player = player
        self.text_overlay = text_overlay()
        
            # set up the game loop
            

        #characters
        self.character = {
            'Tom' : 'graphics/caracters_w1/tom.png', 
            'chief' : 'graphics/caracters_w1/chief.png'
        }
        self.char_name = ['Tom', 'Chief']


        # Dialogue
        self.text = {
            '0': "You failed the test...",
            '1': "Seems like you did not pay attention to the Scrolls of Knowledge.",
            '2': "Talk to me again when you have learned to take them seriously.",
            '3': "I won't give you information when you haven't prove yourself yet.",
            '4': "I'll wait for you here when you're ready.",
        }
        self.text_counter = 0


    def update(self):
       
        pressed = pygame.key.get_pressed()
        skip = pressed[pygame.K_x]
        skip_all = pressed[pygame.K_SPACE]
     

        # First step (dialogue)
        if self.step == 0:
            if int(self.text_counter) < len(self.text['0']):
                if skip_all:
                    self.text_counter = len(self.text['0'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 1  
        if self.step == 1:
            if int(self.text_counter) < len(self.text['1']):
                if skip_all:
                    self.text_counter = len(self.text['1'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 2
        if self.step == 2:
            if int(self.text_counter) < len(self.text['2']):
                if skip_all:
                    self.text_counter = len(self.text['2'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 3

        if self.step == 3:
            if int(self.text_counter) < len(self.text['3']):
                if skip_all:
                    self.text_counter = len(self.text['3'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 4

        if self.step == 4:
            if int(self.text_counter) < len(self.text['4']):
                if skip_all:
                    self.text_counter = len(self.text['4'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                     # Finish the dialogue
                    self.dialogue_running = False
                    self.player.chief_second_dialogue_complete = False
                    self.player.retry = True
                    

        return self.dialogue_running
    
    def draw(self, display_surface):
    
        if self.step == 0:
            draw_text( self.char_name[1], self.text['0'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['chief'], display_surface.get_width() - 378, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['0']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 1:
            draw_text(self.char_name[0],self.text['1'][0:int(self.text_counter)],30,'white', 210 , (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['chief'], display_surface.get_width() - 378, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['1']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
      
        if self.step == 2:
            draw_text( self.char_name[1], self.text['2'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['chief'], display_surface.get_width() - 378, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['2']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 3:
            draw_text(self.char_name[0],self.text['3'][0:int(self.text_counter)],30,'white', 210 , (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['chief'], display_surface.get_width() - 378, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['3']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
    
        if self.step == 4:
            draw_text( self.char_name[1], self.text['4'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['chief'], display_surface.get_width() - 378, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['4']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 4:
            draw_text( self.char_name[1], self.text['4'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['chief'], display_surface.get_width() - 378, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['4']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
      
  
          

class dialogue_npcGuard:
    def __init__(self):
        # Variables
        self.name = 'Guard'
        self.step = 0
        self.dialogue_running = True

        self.text_overlay = text_overlay()

        #characters
        self.character = {
            'Tom' : 'graphics/caracters_w1/tom.png', 
            'koala' : 'graphics/caracters_w1/koala.png'
        }
        self.char_name = ['Tom', 'Koala']


        # Dialogue
        self.text = {
            '0': "OOOOPS!! Where are you going?!",
            '1': "It is strictly prhobited to pass through here especially if you're not\na resident in this village",
            '2': "Are you from here?",
            '3': "Uhhmmm yeaah hehe. My place is totally nearby from that big tree\nover there.",
            '4': "Really???",
            '5': "Yeaah, I'm not that type of suspicious cat who just randomly enters a\nplace and making up some stories about his residency knowing that\nhe's don't actually live here, right? or am I?? He he he.",
            '6': "Oh yeah, I might just overlooked you and seems you're a fine\ngentlecat.",
            '7': "Alright! Then,  what can I do for you?",
            '8': "Do you know where the chief of this village lives??",
            '9': "Yes. Going upwards might be the path you're looking for.",

        }
        self.text_counter = 0


    def update(self):

        pressed = pygame.key.get_pressed()
        skip = pressed[pygame.K_x]
        skip_all = pressed[pygame.K_SPACE]
        # First step (dialogue)
        if self.step == 0:
            if int(self.text_counter) < len(self.text['0']):
                if skip_all:
                    self.text_counter = len(self.text['0'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 1    

        if self.step == 1:
            if int(self.text_counter) < len(self.text['1']):
                if skip_all:
                    self.text_counter = len(self.text['1'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 2

        if self.step == 2:
            if int(self.text_counter) < len(self.text['2']):
                if skip_all:
                    self.text_counter = len(self.text['2'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 3

        if self.step == 3:
            if int(self.text_counter) < len(self.text['3']):
                if skip_all:
                    self.text_counter = len(self.text['3'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 4

        if self.step == 4:
            if int(self.text_counter) < len(self.text['4']):
                if skip_all:
                    self.text_counter = len(self.text['4'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 5

        if self.step == 5:
            if int(self.text_counter) < len(self.text['5']):
                if skip_all:
                    self.text_counter = len(self.text['5'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 6

        if self.step == 6:
            if int(self.text_counter) < len(self.text['6']):
                if skip_all:
                    self.text_counter = len(self.text['6'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 7

        if self.step == 7:
            if int(self.text_counter) < len(self.text['7']):
                if skip_all:
                    self.text_counter = len(self.text['7'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 8
        if self.step == 8:
            if int(self.text_counter) < len(self.text['8']):
                if skip_all:
                    self.text_counter = len(self.text['8'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 9

        if self.step == 9:
            if int(self.text_counter) < len(self.text['9']):
                if skip_all:
                    self.text_counter = len(self.text['9'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    # Finish the dialogue
                    self.dialogue_running = False

        return self.dialogue_running
    
    def draw(self, display_surface):
        if self.step == 0:
            draw_text(self.char_name[1],self.text['0'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272),display_surface )
            draw_npc(self.character['koala'], display_surface.get_width() - 348, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['0']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 1:
            draw_text(self.char_name[1],self.text['1'][0:int(self.text_counter)],30,'white', 210 ,  (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['koala'], display_surface.get_width() - 348, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['1']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 2:
            draw_text(self.char_name[1],self.text['2'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272),display_surface )
            draw_npc(self.character['koala'], display_surface.get_width() - 348, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['2']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        

        if self.step == 3:
            draw_text(self.char_name[0],self.text['3'][0:int(self.text_counter)],30,'white', 210 ,  (SCREEN_HEIGHT - 200) ,  200,(SCREEN_HEIGHT - 272),display_surface )
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['3']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 4:
            draw_text(self.char_name[1],self.text['4'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272),display_surface )
            draw_npc(self.character['koala'], display_surface.get_width() - 348, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['4']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 5:
            draw_text(self.char_name[0],self.text['5'][0:int(self.text_counter)],30,'white', 210 ,  (SCREEN_HEIGHT - 200) ,  200,(SCREEN_HEIGHT - 272),display_surface )
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['5']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 295, SCREEN_HEIGHT - 80))
        
        if self.step == 6:
            draw_text(self.char_name[1],self.text['6'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272),display_surface )
            draw_npc(self.character['koala'], display_surface.get_width() - 348, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['6']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 7:
            draw_text(self.char_name[1],self.text['7'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272),display_surface )
            draw_npc(self.character['koala'], display_surface.get_width() - 348, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['7']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 8:
            draw_text(self.char_name[0],self.text['8'][0:int(self.text_counter)],30,'white', 210 ,  (SCREEN_HEIGHT - 200) ,  200,(SCREEN_HEIGHT - 272),display_surface )
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['8']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 9:
            draw_text(self.char_name[1],self.text['9'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272),display_surface )
            draw_npc(self.character['koala'], display_surface.get_width() - 348, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['9']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

class dialogue_npcGuard_1:
    def __init__(self, player):
        # Variables
        self.name = 'Guard1'
        self.step = 0
        self.dialogue_running = True
        self.player = player

        self.text_overlay = text_overlay()

        #characters
        self.character = {
            'Tom' : 'graphics/caracters_w1/tom.png', 
            'koala' : 'graphics/caracters_w1/koala.png'
        }
        self.char_name = ['Tom', 'Koala']


        # Dialogue
        self.text = {
            '0': "Have you seen the chief?",
            '1': "Yes, now I must go to monkey and help him with his task",
            '2': "Okay take care, you can find monkey in the CLEARING WOODS\nI assume you've met already",
            '3': "Yes Thank you very much.",
        }
        self.text_counter = 0


    def update(self):

        pressed = pygame.key.get_pressed()
        skip = pressed[pygame.K_x]
        skip_all = pressed[pygame.K_SPACE]
        # First step (dialogue)
        if self.step == 0:
            if int(self.text_counter) < len(self.text['0']):
                if skip_all:
                    self.text_counter = len(self.text['0'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 1    

        if self.step == 1:
            if int(self.text_counter) < len(self.text['1']):
                if skip_all:
                    self.text_counter = len(self.text['1'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 2

        if self.step == 2:
            if int(self.text_counter) < len(self.text['2']):
                if skip_all:
                    self.text_counter = len(self.text['2'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 3

        if self.step == 3:
            if int(self.text_counter) < len(self.text['3']):
                if skip_all:
                    self.text_counter = len(self.text['3'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    # Finish the dialogue
                    self.dialogue_running = False
                    self.player.speaking = False

        return self.dialogue_running
    
    def draw(self, display_surface):
        if self.step == 0:
            draw_text(self.char_name[1],self.text['0'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272),display_surface )
            draw_npc(self.character['koala'], display_surface.get_width() - 348, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['0']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 1:
            draw_text(self.char_name[0],self.text['1'][0:int(self.text_counter)],30,'white', 210 ,  (SCREEN_HEIGHT - 200) ,  200,(SCREEN_HEIGHT - 272),display_surface )
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['1']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 2:
            draw_text(self.char_name[1],self.text['2'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272),display_surface )
            draw_npc(self.character['koala'], display_surface.get_width() - 348, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['2']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 3:
            draw_text(self.char_name[0],self.text['3'][0:int(self.text_counter)],30,'white', 210 ,  (SCREEN_HEIGHT - 200) ,  200,(SCREEN_HEIGHT - 272),display_surface )
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['3']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
class dialogue_npcGuard_2:
    def __init__(self, player):
        # Variables
        self.name = 'Guard2'
        self.step = 0
        self.dialogue_running = True
        self.player = player

        self.text_overlay = text_overlay()

        #characters
        self.character = {
            'Tom' : 'graphics/caracters_w1/tom.png', 
            'koala' : 'graphics/caracters_w1/koala.png'
        }
        self.char_name = ['Tom', 'Koala']


        # Dialogue
        self.text = {
            '0':"Now where are you going ?",
            '1':"I just finished helping monkey with his task, and now\nI must find Andoks, monkey said he needs help",
            '2':"I see you can find Andoks in the FARM AREA just check your map",
            '3':"Okay, thank you very much."
        }
        self.text_counter = 0


    def update(self):

        pressed = pygame.key.get_pressed()
        skip = pressed[pygame.K_x]
        skip_all = pressed[pygame.K_SPACE]
        # First step (dialogue)
        if self.step == 0:
            if int(self.text_counter) < len(self.text['0']):
                if skip_all:
                    self.text_counter = len(self.text['0'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 1    

        if self.step == 1:
            if int(self.text_counter) < len(self.text['1']):
                if skip_all:
                    self.text_counter = len(self.text['1'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 2

        if self.step == 2:
            if int(self.text_counter) < len(self.text['2']):
                if skip_all:
                    self.text_counter = len(self.text['2'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 3

        if self.step == 3:
            if int(self.text_counter) < len(self.text['3']):
                if skip_all:
                    self.text_counter = len(self.text['3'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    # Finish the dialogue
                    self.dialogue_running = False
                    self.player.speaking = False

        return self.dialogue_running
    
    def draw(self, display_surface):
        if self.step == 0:
            draw_text(self.char_name[1],self.text['0'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272),display_surface )
            draw_npc(self.character['koala'], display_surface.get_width() - 348, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['0']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 1:
            draw_text(self.char_name[0],self.text['1'][0:int(self.text_counter)],30,'white', 210 ,  (SCREEN_HEIGHT - 200) ,  200,(SCREEN_HEIGHT - 272),display_surface )
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['1']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 2:
            draw_text(self.char_name[1],self.text['2'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272),display_surface )
            draw_npc(self.character['koala'], display_surface.get_width() - 348, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['2']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 3:
            draw_text(self.char_name[0],self.text['3'][0:int(self.text_counter)],30,'white', 210 ,  (SCREEN_HEIGHT - 200) ,  200,(SCREEN_HEIGHT - 272),display_surface )
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['3']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

class dialogue_npcGuard_3:
    def __init__(self, player):
        # Variables
        self.name = 'Guard3'
        self.step = 0
        self.dialogue_running = True
        self.player = player

        self.text_overlay = text_overlay()

        #characters
        self.character = {
            'Tom' : 'graphics/caracters_w1/tom.png', 
            'koala' : 'graphics/caracters_w1/koala.png'
        }
        self.char_name = ['Tom', 'Koala']


        # Dialogue
        self.text = {
            '0':"Hey, are you done with all the tasks ?",
            '1':"No, but I must find Chicken Hunter, Rabbit said he also needs my help",
            '2':"I see, in that case you can find him over there at that path near\nthe statues, he is scouting wildboar for us to eat",
            '3':"Okay, thank you very much."
        }
        self.text_counter = 0


    def update(self):

        pressed = pygame.key.get_pressed()
        skip = pressed[pygame.K_x]
        skip_all = pressed[pygame.K_SPACE]
        # First step (dialogue)
        if self.step == 0:
            if int(self.text_counter) < len(self.text['0']):
                if skip_all:
                    self.text_counter = len(self.text['0'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 1    

        if self.step == 1:
            if int(self.text_counter) < len(self.text['1']):
                if skip_all:
                    self.text_counter = len(self.text['1'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 2

        if self.step == 2:
            if int(self.text_counter) < len(self.text['2']):
                if skip_all:
                    self.text_counter = len(self.text['2'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 3

        if self.step == 3:
            if int(self.text_counter) < len(self.text['3']):
                if skip_all:
                    self.text_counter = len(self.text['3'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    # Finish the dialogue
                    self.dialogue_running = False
                    self.player.speaking = False

        return self.dialogue_running
    
    def draw(self, display_surface):
        if self.step == 0:
            draw_text(self.char_name[1],self.text['0'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272),display_surface )
            draw_npc(self.character['koala'], display_surface.get_width() - 348, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['0']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 1:
            draw_text(self.char_name[0],self.text['1'][0:int(self.text_counter)],30,'white', 210 ,  (SCREEN_HEIGHT - 200) ,  200,(SCREEN_HEIGHT - 272),display_surface )
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['1']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 2:
            draw_text(self.char_name[1],self.text['2'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272),display_surface )
            draw_npc(self.character['koala'], display_surface.get_width() - 348, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['2']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 3:
            draw_text(self.char_name[0],self.text['3'][0:int(self.text_counter)],30,'white', 210 ,  (SCREEN_HEIGHT - 200) ,  200,(SCREEN_HEIGHT - 272),display_surface )
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['3']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
  
class dialogue_npcGuard_4:
    def __init__(self, player):
        # Variables
        self.name = 'Guard4'
        self.step = 0
        self.dialogue_running = True
        self.player = player

        self.text_overlay = text_overlay()

        #characters
        self.character = {
            'Tom' : 'graphics/caracters_w1/tom.png', 
            'koala' : 'graphics/caracters_w1/koala.png'
        }
        self.char_name = ['Tom', 'Koala']


        # Dialogue
        self.text = {
            '0':"Hey, are you done with all the tasks?",
            '1':"Yes finally, do you know where the cave is?",
            '2':"Yes of course, it is the other path on the forest,\njust follow the path UPWARDS and check your map",
            '3':"Okay, thank you very much."
        }
        self.text_counter = 0


    def update(self):

        pressed = pygame.key.get_pressed()
        skip = pressed[pygame.K_x]
        skip_all = pressed[pygame.K_SPACE]
        # First step (dialogue)
        if self.step == 0:
            if int(self.text_counter) < len(self.text['0']):
                if skip_all:
                    self.text_counter = len(self.text['0'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 1    

        if self.step == 1:
            if int(self.text_counter) < len(self.text['1']):
                if skip_all:
                    self.text_counter = len(self.text['1'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 2

        if self.step == 2:
            if int(self.text_counter) < len(self.text['2']):
                if skip_all:
                    self.text_counter = len(self.text['2'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 3

        if self.step == 3:
            if int(self.text_counter) < len(self.text['3']):
                if skip_all:
                    self.text_counter = len(self.text['3'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    # Finish the dialogue
                    self.dialogue_running = False
                    self.player.speaking = False

        return self.dialogue_running
    
    def draw(self, display_surface):
        if self.step == 0:
            draw_text(self.char_name[1],self.text['0'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272),display_surface )
            draw_npc(self.character['koala'], display_surface.get_width() - 348, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['0']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 1:
            draw_text(self.char_name[0],self.text['1'][0:int(self.text_counter)],30,'white', 210 ,  (SCREEN_HEIGHT - 200) ,  200,(SCREEN_HEIGHT - 272),display_surface )
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['1']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 2:
            draw_text(self.char_name[1],self.text['2'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272),display_surface )
            draw_npc(self.character['koala'], display_surface.get_width() - 348, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['2']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 3:
            draw_text(self.char_name[0],self.text['3'][0:int(self.text_counter)],30,'white', 210 ,  (SCREEN_HEIGHT - 200) ,  200,(SCREEN_HEIGHT - 272),display_surface )
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['3']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
  

class dialogue_npcRabbit:
    def __init__(self, player):
        # Variables
        self.name = 'Rabbit'
        self.step = 0
        self.dialogue_running = True

        self.text_overlay = text_overlay()

        self.player = player

        #characters
        self.character = {
            'Tom' : 'graphics/caracters_w1/tom.png', 
            'rabbit' : 'graphics/caracters_w1/rabbit.png'
        }
        self.char_name = ['Tom', 'Rabbit']


        # Dialogue
        self.text = {
            '0': "Are you new here? because your face is not familiar.",
            '1': "No. I've been here for a long ti---...\nYes I'm new here. I am tom and I'm an adventurer.\nI'm here to help the villagers.",
            '2': "Then maybe you can help me in getting water from the river.",
            '3': "Sure."

        }
        self.text_counter = 0


    def update(self):

        pressed = pygame.key.get_pressed()
        skip = pressed[pygame.K_x]
        skip_all = pressed[pygame.K_SPACE]

        # First step (dialogue)
        if self.step == 0:
            if int(self.text_counter) < len(self.text['0']):
                if skip_all:
                    self.text_counter = len(self.text['0'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 1    

        if self.step == 1:
            if int(self.text_counter) < len(self.text['1']):
                if skip_all:
                    self.text_counter = len(self.text['1'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 2

        if self.step == 2:
            if int(self.text_counter) < len(self.text['2']):
                if skip_all:
                    self.text_counter = len(self.text['2'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 3

        if self.step == 3:
            if int(self.text_counter) < len(self.text['3']):
                if skip_all:
                    self.text_counter = len(self.text['3'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    # Finish the dialogue
                    self.player.quest_waterjar = True
                    self.player.water_active = True
                    self.dialogue_running = False
                    self.player.speaking = False

        return self.dialogue_running
    
    def draw(self, display_surface):

        if self.step == 0:
            draw_text( self.char_name[1],self.text['0'][0:int(self.text_counter)],30, 'white',210 , (display_surface.get_height() - 200) , 200,(display_surface.get_height() - 272), display_surface )
            draw_npc(self.character['rabbit'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['0']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 1:
            draw_text(self.char_name[0],self.text['1'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200, (display_surface.get_height() - 272),display_surface )
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['1']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 2:
            draw_text( self.char_name[1],self.text['2'][0:int(self.text_counter)],30, 'white',210 , (display_surface.get_height() - 200) , 200,(display_surface.get_height() - 272), display_surface )
            draw_npc(self.character['rabbit'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['2']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 3:
            draw_text(self.char_name[0],self.text['3'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200, (display_surface.get_height() - 272),display_surface )
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['3']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))


class dialogue_npcRabbit_1:
    def __init__(self, player):
        # Variables
        self.name = 'Rabbit1'
        self.step = 0
        self.dialogue_running = True

        self.text_overlay = text_overlay()

        self.player = player

        #characters
        self.character = {
            'Tom' : 'graphics/caracters_w1/tom.png', 
            'rabbit' : 'graphics/caracters_w1/rabbit.png'
        }
        self.char_name = ['Tom', 'Rabbit']


        # Dialogue
        self.text = {
            '0': "Thanks, it would be really helpful to me.",
            '1': "Do you still have anything you want me to do? ",
            '2': "None, but you can try to visit chicken warrior",
            '3': "You can find him in the RIGHT part of the village,\nwhere you can also find the HUNTING GROUNDS in the woods."

        }
        self.text_counter = 0


    def update(self):

        pressed = pygame.key.get_pressed()
        skip = pressed[pygame.K_x]
        skip_all= pressed[pygame.K_SPACE]

        # First step (dialogue)
        if self.step == 0:
            if int(self.text_counter) < len(self.text['0']):
                if skip_all:
                    self.text_counter = len(self.text['0'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 1    

        if self.step == 1:
            if int(self.text_counter) < len(self.text['1']):
                if skip_all:
                    self.text_counter = len(self.text['1'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 2

        if self.step == 2:
            if int(self.text_counter) < len(self.text['2']):
                if skip_all:
                    self.text_counter = len(self.text['2'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 3

        if self.step == 3:
            if int(self.text_counter) < len(self.text['3']):
                if skip_all:
                    self.text_counter = len(self.text['3'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    # Finish the dialogue
                    self.player.questwaterjar_complete = True
                    self.dialogue_running = False
                    self.player.speaking = False

        return self.dialogue_running
    
    def draw(self, display_surface):
        
        if self.step == 0:
            draw_text(self.char_name[1],self.text['0'][0:int(self.text_counter)], 30,'white',210 ,  (display_surface.get_height() - 200) , 200,(display_surface.get_height() - 272),display_surface)
            draw_npc(self.character['rabbit'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['0']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 1:
            draw_text(self.char_name[0],self.text['1'][0:int(self.text_counter)], 30,'white',210 , (display_surface.get_height() - 200) , 200,(display_surface.get_height() - 272),display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['1']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))


        if self.step == 2:
            draw_text(self.char_name[1],self.text['2'][0:int(self.text_counter)], 30,'white',210 ,  (display_surface.get_height() - 200) , 200,(display_surface.get_height() - 272),display_surface)
            draw_npc(self.character['rabbit'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['2']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 3:
            draw_text(self.char_name[1],self.text['3'][0:int(self.text_counter)], 30,'white',210 ,  (display_surface.get_height() - 200) , 200,(display_surface.get_height() - 272),display_surface)
            draw_npc(self.character['rabbit'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['3']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        

        
class dialogue_npcChicken1:
    def __init__(self, player):
        # Variables
        self.name = 'Chicken1'
        self.step = 0
        self.dialogue_running = True
        self.text_overlay = text_overlay()

        self.player = player

        #characters
        self.character = {
            'Tom' : 'graphics/caracters_w1/tom.png', 
            'chicken1' : 'graphics/caracters_w1/ckicken_1.png'
        }
        self.char_name = ['Tom', 'Andoks']


        # Dialogue
        self.text = {
            '0': " Hey! Are you the adventurer that they've been talking about?",
            '1': "Yes I am! Monkey  mentioned you needed help.",
            '2': "Monkey was right. Could you kindly help me clear the grass and plow\nthe soil, so that I can cultivate it and plant my precious crops?",
            '3': "Sure thing."

        }
        self.text_counter = 0


    def update(self):

        pressed = pygame.key.get_pressed()
        skip = pressed[pygame.K_x]
        skip_all = pressed[pygame.K_SPACE]

        # First step (dialogue)
        if self.step == 0:
            if int(self.text_counter) < len(self.text['0']):
                if skip_all:
                    self.text_counter = len(self.text['0'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 1    

        if self.step == 1:
            if int(self.text_counter) < len(self.text['1']):
                if skip_all:
                    self.text_counter = len(self.text['1'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 2

        if self.step == 2:
            if int(self.text_counter) < len(self.text['2']):
                if skip_all:
                    self.text_counter = len(self.text['2'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 3

        if self.step == 3:
            if int(self.text_counter) < len(self.text['3']):
                if skip_all:
                    self.text_counter = len(self.text['3'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    # Finish the dialogue
                    self.player.quest_farm = True
                    self.dialogue_running = False
                    self.player.speaking = False

        return self.dialogue_running
    
    def draw(self, display_surface):
      
        if self.step == 0:
            draw_text(self.char_name[1],self.text['0'][0:int(self.text_counter)],30,'white',210 ,  (display_surface.get_height() - 200) , 200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['chicken1'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['0']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 1:
            draw_text( self.char_name[0],self.text['1'][0:int(self.text_counter)],30, 'white',210 , (display_surface.get_height() - 200) , 200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['1']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 2:
            draw_text(self.char_name[1],self.text['2'][0:int(self.text_counter)],30,'white',210 ,  (display_surface.get_height() - 200) , 200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['chicken1'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['2']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 3:
            draw_text( self.char_name[0],self.text['3'][0:int(self.text_counter)],30, 'white',210 , (display_surface.get_height() - 200) , 200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['3']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

class dialogue_npcChicken1_1:
    def __init__(self, player):
        # Variables
        self.name = 'Chicken1_1'
        self.step = 0
        self.dialogue_running = True
        self.text_overlay = text_overlay()

        self.player = player

        #characters
        self.character = {
            'Tom' : 'graphics/caracters_w1/tom.png', 
            'chicken1' : 'graphics/caracters_w1/ckicken_1.png'
        }
        self.char_name = ['Tom', 'Andoks']


        # Dialogue
        self.text = {
            '0': "Find Rabbit",
            '1': "He can be found at the UPPER LEFT part of the village.",
            '2': "just look for the WATER JAR",
            '3': "You can also see mammoths there. They are nice to be with."

        }
        self.text_counter = 0


    def update(self):

        pressed = pygame.key.get_pressed()
        skip = pressed[pygame.K_x]
        skip_all= pressed[pygame.K_SPACE]

        # First step (dialogue)
        if self.step == 0:
            if int(self.text_counter) < len(self.text['0']):
                if skip_all:
                    self.text_counter = len(self.text['0'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 1    

        if self.step == 1:
            if int(self.text_counter) < len(self.text['1']):
                if skip_all:
                    self.text_counter = len(self.text['1'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 2

        if self.step == 2:
            if int(self.text_counter) < len(self.text['2']):
                if skip_all:
                    self.text_counter = len(self.text['2'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 3

        if self.step == 3:
            if int(self.text_counter) < len(self.text['3']):
                if skip_all:
                    self.text_counter = len(self.text['3'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    # Finish the dialogue
                    self.player.questfarm_complete = True
                    self.dialogue_running = False
                    self.player.speaking = False

        return self.dialogue_running
    
    def draw(self, display_surface):
        if self.step == 0:
            draw_text(self.char_name[1], self.text['0'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) , 200,(display_surface.get_height() - 272),display_surface)
            draw_npc(self.character['chicken1'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['0']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 1:
            draw_text(self.char_name[1], self.text['1'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) , 200,(display_surface.get_height() - 272),display_surface)
            draw_npc(self.character['chicken1'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['1']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
      
        if self.step == 2:
            draw_text(self.char_name[1], self.text['2'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) , 200,(display_surface.get_height() - 272),display_surface)
            draw_npc(self.character['chicken1'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['2']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
      
        if self.step == 3:
            draw_text(self.char_name[1], self.text['3'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) , 200,(display_surface.get_height() - 272),display_surface)
            draw_npc(self.character['chicken1'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['3']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
      
        
class dialogue_npcChicken:
    def __init__(self, player):
        # Variables
        self.name = 'Chicken'
        self.step = 0
        self.dialogue_running = True

        self.text_overlay = text_overlay()

        self.player = player

        #characters
        self.character = {
            'Tom' : 'graphics/caracters_w1/tom.png', 
            'chicken' : 'graphics/caracters_w1/chicken.png'
        }
        self.char_name = ['Tom', 'Chicken']


        # Dialogue
        self.text = {
            '0': "Mr. Rabbit told me to go here, and I'm here to help and assist you.",
            '1': "Are you strong enough to help me hunt those wild boars?",
            '2': "Hell yeah!",
            '3': "Alright! Let's go hunt 8 wild boars meat"

        }
        self.text_counter = 0


    def update(self):

        pressed = pygame.key.get_pressed()
        skip = pressed[pygame.K_x]
        skip_all = pressed[pygame.K_SPACE]

        # First step (dialogue)
        if self.step == 0:
            if int(self.text_counter) < len(self.text['0']):
                if skip_all:
                    self.text_counter = len(self.text['0'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 1    

        if self.step == 1:
            if int(self.text_counter) < len(self.text['1']):
                if skip_all:
                    self.text_counter = len(self.text['1'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 2

        if self.step == 2:
            if int(self.text_counter) < len(self.text['2']):
                if skip_all:
                    self.text_counter = len(self.text['2'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 3

        if self.step == 3:
            if int(self.text_counter) < len(self.text['3']):
                if skip_all:
                    self.text_counter = len(self.text['3'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    # Finish the dialogue
                    self.player.quest_hunt = True
                    self.dialogue_running = False
                    self.player.speaking = False

        return self.dialogue_running
    
    def draw(self, display_surface):
        if self.step == 0:
            draw_text(self.char_name[0],self.text['0'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272),display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['0']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 1:
            draw_text(self.char_name[1],self.text['1'][0:int(self.text_counter)],30, 'white',210 ,  (display_surface.get_height() - 200) ,200, (display_surface.get_height() - 272),display_surface )
            draw_npc(self.character['chicken'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['1']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 2:
            draw_text(self.char_name[0],self.text['2'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272),display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['2']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 3:
            draw_text(self.char_name[1],self.text['3'][0:int(self.text_counter)],30, 'white',210 ,  (display_surface.get_height() - 200) ,200, (display_surface.get_height() - 272),display_surface )
            draw_npc(self.character['chicken'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['3']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        


      
class dialogue_npcChicken_1:
    def __init__(self, player):
        # Variables
        self.name = '1Chicken'
        self.step = 0
        self.dialogue_running = True

        self.text_overlay = text_overlay()

        self.player = player

        #characters
        self.character = {
            'Tom' : 'graphics/caracters_w1/tom.png', 
            'chicken' : 'graphics/caracters_w1/chicken.png'
        }
        self.char_name = ['Tom', 'Chicken']


        # Dialogue
        self.text = {
            '0': " You're a lifesaver!! Now the whole village\ncan now eat something real good!!!",
            '1': "I suppose you have completed all of the required task.\nYou're mission ends here.",
            '2': "Our beloved chief is now waiting for you,\nmighty adventurer!"

        }
        self.text_counter = 0


    def update(self):

        pressed = pygame.key.get_pressed()
        skip = pressed[pygame.K_x]
        skip_all= pressed[pygame.K_SPACE]

        # First step (dialogue)
        if self.step == 0:
            if int(self.text_counter) < len(self.text['0']):
                if skip_all:
                    self.text_counter = len(self.text['0'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 1    

        if self.step == 1:
            if int(self.text_counter) < len(self.text['1']):
                if skip_all:
                    self.text_counter = len(self.text['1'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 2

        if self.step == 2:
            if int(self.text_counter) < len(self.text['2']):
                if skip_all:
                    self.text_counter = len(self.text['2'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    # Finish the dialogue
                    self.player.questhunt_complete = True
                    self.dialogue_running = False
                    self.player.speaking = False

        return self.dialogue_running
    
    def draw(self, display_surface):
     
        if self.step == 0:
            draw_text(self.char_name[1],self.text['0'][0:int(self.text_counter)], 30,'white',210 , (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272),display_surface )
            draw_npc(self.character['chicken'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['0']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        if self.step == 1:
            draw_text(self.char_name[1],self.text['1'][0:int(self.text_counter)], 30,'white',210 , (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272),display_surface )
            draw_npc(self.character['chicken'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['1']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        if self.step == 2:
            draw_text(self.char_name[1],self.text['2'][0:int(self.text_counter)], 30,'white',210 , (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272),display_surface )
            draw_npc(self.character['chicken'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['2']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        
class dialogue_npc1:
    def __init__(self, player):
        # Variables
        self.name = 'test'
        self.step = 0
        self.dialogue_running = True

        self.player = player

        self.text_overlay = text_overlay()

        #characters
        self.character = {
            'Tom' : 'graphics/caracters_w1/tom.png', 
            'monkey' : 'graphics/caracters_w1/monkey.png'
        }
        self.char_name = ['Tom', 'Monkey']


        # Dialogue
        self.text = {
            'one': "Hola, Bonjour, Ciao, Konnichiwa, Namaste, HELLO!?",
            'two': "Hello is already enough, but it is so nice of you.\nAnyway, HI!!",
            'three': "What is it that you want?",
            'four': "Do you know something about a powerful GEM around here? ",
            'five': " I dont know what are you talking about, you should go to the\nvillage and ask the chief. You just need to follow the road path\nto get to our village."

        }
        self.text_counter = 0

    


    def update(self):

        pressed = pygame.key.get_pressed()
        skip = pressed[pygame.K_x]
        skip_all = pressed[pygame.K_SPACE]

        # First step (dialogue)
        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                if skip_all:
                    self.text_counter = len(self.text['one'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 1    

        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                if skip_all:
                    self.text_counter = len(self.text['two'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 2

        if self.step == 2:
            if int(self.text_counter) < len(self.text['three']):
                if skip_all:
                    self.text_counter = len(self.text['three'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 3

        if self.step == 3:
            if int(self.text_counter) < len(self.text['four']):
                if skip_all:
                    self.text_counter = len(self.text['four'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 4

        if self.step == 4:
            if int(self.text_counter) < len(self.text['five']):
                if skip_all:
                    self.text_counter = len(self.text['five'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    # Finish the dialogue
                    self.dialogue_running = False
                    self.player.speaking = False

        return self.dialogue_running
    
    def draw(self, display_surface):
        if self.step == 0:
            draw_text(
                name = self.char_name[0],
                text = self.text['one'][0:int(self.text_counter)],
                size = 30,
                color = 'white',
                x = 210 , 
                y = (display_surface.get_height() - 200) ,  
                namex = 200,
                namey = (display_surface.get_height() - 272),
                display_surface = display_surface
            )
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            
            if int(self.text_counter) == len(self.text['one']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
    
        if self.step == 1:
            draw_text(
                name = self.char_name[1],
                text = self.text['two'][0:int(self.text_counter)],
                size = 30,
                color = 'white',
                x = 210 , 
                y = (display_surface.get_height() - 200) ,  
                namex = 200,
                namey = (display_surface.get_height() - 272),
                display_surface = display_surface
            )
            draw_npc(self.character['monkey'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
        
            if int(self.text_counter) == len(self.text['two']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 2:
            draw_text(
                name = self.char_name[1],
                text = self.text['three'][0:int(self.text_counter)],
                size = 30,
                color = 'white',
                x = 210 , 
                y = (display_surface.get_height() - 200) ,  
                namex = 200,
                namey = (display_surface.get_height() - 272),
                display_surface = display_surface
            )
            draw_npc(self.character['monkey'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
        
            if int(self.text_counter) == len(self.text['three']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        

        if self.step == 3:
            draw_text(
                name = self.char_name[0],
                text = self.text['four'][0:int(self.text_counter)],
                size = 30,
                color = 'white',
                x = 210 , 
                y = (display_surface.get_height() - 200) ,  
                namex = 200,
                namey = (display_surface.get_height() - 272),
                display_surface = display_surface
            )
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )

            if int(self.text_counter) == len(self.text['four']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 4:
            draw_text(
                name = self.char_name[1],
                text = self.text['five'][0:int(self.text_counter)],
                size = 30,
                color = 'white',
                x = 210 , 
                y = (display_surface.get_height() - 200) ,  
                namex = 200,
                namey = (display_surface.get_height() - 272),
                display_surface = display_surface
            )
            draw_npc(self.character['monkey'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )

            if int(self.text_counter) == len(self.text['five']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

class dialogue_npc1_2:
    def __init__(self, player):
        # Variables
        self.name = 'second encounter'
        self.step = 0
        self.dialogue_running = True

        self.player = player
        self.text_overlay = text_overlay()

        #characters
        self.character = {
            'Tom' : 'graphics/caracters_w1/tom.png', 
            'monkey' : 'graphics/caracters_w1/monkey.png'
        }
        self.char_name = ['Tom', 'Monkey']


        # Dialogue
        self.text = {
            'one': "Hey, The Chief said you need Help?",
            'two': "Yes, Thank you !",
            'three': "okay, so what do you want me to do?",
            'four': "Help me cut some trees",
            'five': "collect ten woods and deliver it to me."

        }
        self.text_counter = 0


    def update(self):

        pressed = pygame.key.get_pressed()
        skip = pressed[pygame.K_x]
        skip_all = pressed[pygame.K_SPACE]

        # First step (dialogue)
        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                if skip_all:
                    self.text_counter = len(self.text['one'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 1    

        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                if skip_all:
                    self.text_counter = len(self.text['two'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 2

        if self.step == 2:
            if int(self.text_counter) < len(self.text['three']):
                if skip_all:
                    self.text_counter = len(self.text['three'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 3
        if self.step == 3:
            if int(self.text_counter) < len(self.text['four']):
                if skip_all:
                    self.text_counter = len(self.text['four'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 4

        if self.step == 4:
            if int(self.text_counter) < len(self.text['five']):
                if skip_all:
                    self.text_counter = len(self.text['five'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    # Finish the dialogue
                    self.player.quest_trees = True
                    self.dialogue_running = False
                    self.player.speaking = False

        return self.dialogue_running
    
    def draw(self, display_surface):
        if self.step == 0:
            draw_text(self.char_name[0],self.text['one'][0:int(self.text_counter)],30, 'white',210 , (display_surface.get_height() - 200) , 200, (display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['one']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        if self.step == 1:
            draw_text(self.char_name[1], self.text['two'][0:int(self.text_counter)],30,'white',210 , (display_surface.get_height() - 200) ,   200,(display_surface.get_height() - 272),display_surface)
            draw_npc(self.character['monkey'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['two']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        if self.step == 2:
            draw_text(self.char_name[0], self.text['three'][0:int(self.text_counter)], 30, 'white', 210 , (display_surface.get_height() - 200) ,200, (display_surface.get_height() - 272), display_surface )
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['three']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 3:
            draw_text(self.char_name[1], self.text['four'][0:int(self.text_counter)], 30, 'white',210 , (display_surface.get_height() - 200) ,  200,(display_surface.get_height() - 272), display_surface )
            draw_npc(self.character['monkey'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['four']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 4:
            draw_text(self.char_name[1],self.text['five'][0:int(self.text_counter)], 30,'white',210 , (display_surface.get_height() - 200) ,200, (display_surface.get_height() - 272),display_surface )
            draw_npc(self.character['monkey'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['five']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

class dialogue_npc1_3:
    def __init__(self, player):
        # Variables
        self.name = 'last encounter'
        self.step = 0
        self.dialogue_running = True

        self.text_overlay = text_overlay()

        self.player = player

        #characters
        self.character = {
            'Tom' : 'graphics/caracters_w1/tom.png', 
            'monkey' : 'graphics/caracters_w1/monkey.png'
        }
        self.char_name = ['Tom', 'Monkey']


        # Dialogue
        self.text = {
            'one': "You're too kind! Thank you for being there for me..",
            'two': "Find  the Chicken Farmer. I know he's in need for your rescue",
            'three': "He can be found near the FARM AREA of the village.",
        }
        self.text_counter = 0


    def update(self):

        pressed = pygame.key.get_pressed()
        skip = pressed[pygame.K_x]
        skip_all= pressed[pygame.K_SPACE]

        # First step (dialogue)
        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                if skip_all:
                    self.text_counter = len(self.text['one'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 1 

        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                if skip_all:
                    self.text_counter = len(self.text['two'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step += 1   

        if self.step == 2:
            if int(self.text_counter) < len(self.text['three']):
                if skip_all:
                    self.text_counter = len(self.text['three'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    # Finish the dialogue
                    self.dialogue_running = False
                    self.player.questtrees_complete = True
                    self.player.speaking = False

        return self.dialogue_running
    
    def draw(self, display_surface):
        if self.step == 0:
            draw_text(self.char_name[1], self.text['one'][0:int(self.text_counter)], 30,'white',210 , (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['monkey'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['one']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 1:
            draw_text(self.char_name[1], self.text['two'][0:int(self.text_counter)], 30,'white',210 , (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['monkey'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['two']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 2:
            draw_text(self.char_name[1], self.text['three'][0:int(self.text_counter)], 30,'white',210 , (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['monkey'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['three']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))


class dialogue_self:
    def __init__(self, player):
        # Variables
        self.name = 'start'
        self.step = 0
        self.dialogue_running = True

        self.player = player
        self.text_overlay = text_overlay()

        #characters
        self.character = {
            'Tom' : 'graphics/caracters_w1/tom.png'
        }
        self.char_name = ['Tom']

        # Dialogue
        self.text = {
            'one': "woah! the portal works",
            'two': "Now I must fulfill my mission",
            'three': "Find and gather all the parts of the sword",
            'four': "Starting with the source of the power of the sword.\nthe Lightning Gem",
        }
        self.text_counter = 0


    def update(self):

        pressed = pygame.key.get_pressed()
        skip = pressed[pygame.K_x]
        skip_all = pressed[pygame.K_SPACE]

        # First step (dialogue)
        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                if skip_all:
                    self.text_counter = len(self.text['one'])
                else:
                    self.text_counter += 1
                
            else:
                if skip :
                    self.text_counter=0
                    self.step = 1    

        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                if skip_all:
                    self.text_counter = len(self.text['two'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 2

        if self.step == 2:
            if int(self.text_counter) < len(self.text['three']):
                if skip_all:
                    self.text_counter = len(self.text['three'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 3
        if self.step == 3:
            if int(self.text_counter) < len(self.text['four']):
                if skip_all:
                    self.text_counter = len(self.text['four'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    # Finish the dialogue
                    self.player.main_quest = True
                    self.dialogue_running = False

        return self.dialogue_running

    
    def draw(self, display_surface):
        if self.step == 0:
            draw_text(
                name = self.char_name[0],
                text = self.text['one'][0:int(self.text_counter)],
                size = 30,
                color = 'white',
                x = 210 , 
                y = (display_surface.get_height() - 200) ,  
                namex = 200,
                namey = (display_surface.get_height() - 272),
                display_surface = display_surface
            )
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            
            if int(self.text_counter) == len(self.text['one']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
    
        if self.step == 1:
            draw_text(
                name = self.char_name[0],
                text = self.text['two'][0:int(self.text_counter)],
                size = 30,
                color = 'white',
                x = 210 , 
                y = (display_surface.get_height() - 200) ,  
                namex = 200,
                namey = (display_surface.get_height() - 272),
                display_surface = display_surface
            )
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
        
            if int(self.text_counter) == len(self.text['two']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        
        if self.step == 2:
            draw_text(
                name = self.char_name[0],
                text = self.text['three'][0:int(self.text_counter)],
                size = 30,
                color = 'white',
                x = 210 , 
                y = (display_surface.get_height() - 200) ,  
                namex = 200,
                namey = (display_surface.get_height() - 272),
                display_surface = display_surface
            )
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )

            if int(self.text_counter) == len(self.text['three']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 3:
            draw_text(
                name = self.char_name[0],
                text = self.text['four'][0:int(self.text_counter)],
                size = 30,
                color = 'white',
                x = 210 , 
                y = (display_surface.get_height() - 200) ,  
                namex = 200,
                namey = (display_surface.get_height() - 272),
                display_surface = display_surface
            )
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['four']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

#Cave dialogue
##############may pagbabago####################
class dialogue_cave_tower:
    def __init__(self, player):
        # Variables
        self.name = 'cave_tower'
        self.step = 0
        self.dialogue_running = True


        self.player = player
        self.text_overlay = text_overlay()

        #characters
        self.character = {
            'Tom' : 'graphics/caracters_w1/tom.png'
        }

        self.stone_surf = pygame.image.load('graphics/rock_tablet.png').convert_alpha()
        self.stone_rect = self.stone_surf.get_rect(topleft = (0,0))

        self.char_name = ['Tom']

        # Dialogue
        self.text = {
            '0': "woah! what is this?",
            '1': "I can see some scripture writings on it.\nI can read it that's odd.",
            '2': "'Anyone who can read this is worthy of\nthe Gem of Lightning.'",
            '3': "It is located at the deepest part of the cave.",
            '4': "I am the great wizard who cast a spell on this\ncave to keep the monsters from wreaking havoc\non the outside world.", 
            '5': "And to keep the Gem of Lightning that is\nGuarded by many monsters",
            '6': "To go the Deepest part of the cave,\nYou must COLLECT 2 GEMS and put it on\nhere and this tower will activate",
            '7': "To collect the Gems, you must activate the\nfires on the braziers on both sides of the cave",
        }
        self.text_counter = 0


    def update(self):

        pressed = pygame.key.get_pressed()
        skip = pressed[pygame.K_x]
        skip_all = pressed[pygame.K_SPACE]

        # First step (dialogue)
        if self.step == 0:
            if int(self.text_counter) < len(self.text['0']):
                if skip_all:
                    self.text_counter = len(self.text['0'])
                else:
                    self.text_counter += 1
                
            else:
                if skip :
                    self.text_counter=0
                    self.step = 1    

        if self.step == 1:
            if int(self.text_counter) < len(self.text['1']):
                if skip_all:
                    self.text_counter = len(self.text['1'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 2

        if self.step == 2:
            if int(self.text_counter) < len(self.text['2']):
                if skip_all:
                    self.text_counter = len(self.text['2'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 3
        
        if self.step == 3:
            if int(self.text_counter) < len(self.text['3']):
                if skip_all:
                    self.text_counter = len(self.text['3'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 4

        if self.step == 4:
            if int(self.text_counter) < len(self.text['4']):
                if skip_all:
                    self.text_counter = len(self.text['4'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 5

        if self.step == 5:
            if int(self.text_counter) < len(self.text['5']):
                if skip_all:
                    self.text_counter = len(self.text['5'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 6

        if self.step == 6:
            if int(self.text_counter) < len(self.text['6']):
                if skip_all:
                    self.text_counter = len(self.text['6'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 7

        if self.step == 7:
            if int(self.text_counter) < len(self.text['7']):
                if skip_all:
                    self.text_counter = len(self.text['7'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    # Finish the dialogue
                   
                    self.dialogue_running = False
                    self.player.quest_tower = True
                    # self.player.tower_writing1 = True

        return self.dialogue_running

    
    def draw(self, display_surface):
        if self.step == 0:
            draw_text(self.char_name[0],self.text['0'][0:int(self.text_counter)],30,'white', 210 , (display_surface.get_height() - 200) ,  200, (display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['0']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        if self.step == 1:
            draw_text(self.char_name[0],self.text['1'][0:int(self.text_counter)],30,'white', 210 , (display_surface.get_height() - 200) ,  200, (display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['1']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        if self.step == 2:
            display_surface.blit(self.stone_surf, self.stone_rect)
            draw_text('',self.text['2'][0:int(self.text_counter)],30,'white', 330 , 180 ,  200, (display_surface.get_height() - 272), display_surface)
            if int(self.text_counter) == len(self.text['2']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 435, SCREEN_HEIGHT - 220))
        if self.step == 3:
            display_surface.blit(self.stone_surf, self.stone_rect)
            draw_text('',self.text['3'][0:int(self.text_counter)],30,'white', 330 , 180 ,  200, (display_surface.get_height() - 272), display_surface)
            if int(self.text_counter) == len(self.text['3']):
                self.text_overlay.draw('Press X to skip',(SCREEN_WIDTH - 435, SCREEN_HEIGHT - 220))
        if self.step == 4:
            display_surface.blit(self.stone_surf, self.stone_rect)
            draw_text('',self.text['4'][0:int(self.text_counter)],30,'white', 330 , 180 ,  200, (display_surface.get_height() - 272), display_surface)
            if int(self.text_counter) == len(self.text['4']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 435, SCREEN_HEIGHT - 220))
        if self.step == 5:
            display_surface.blit(self.stone_surf, self.stone_rect)
            draw_text('',self.text['5'][0:int(self.text_counter)],30,'white', 330 , 180 ,  200, (display_surface.get_height() - 272), display_surface)
            if int(self.text_counter) == len(self.text['5']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 435, SCREEN_HEIGHT - 220))
        if self.step == 6:
            display_surface.blit(self.stone_surf, self.stone_rect)
            draw_text('',self.text['6'][0:int(self.text_counter)],30,'white', 330 , 180 ,  200, (display_surface.get_height() - 272), display_surface)
            if int(self.text_counter) == len(self.text['6']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 435, SCREEN_HEIGHT - 220))
        if self.step == 7:
            display_surface.blit(self.stone_surf, self.stone_rect)
            draw_text('',self.text['7'][0:int(self.text_counter)],30,'white', 330 , 180 ,  200, (display_surface.get_height() - 272), display_surface)
            if int(self.text_counter) == len(self.text['7']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 435, SCREEN_HEIGHT - 220))
    
class dialogue_brazier:
    def __init__(self, player):
        # Variables
        self.name = 'brazier'
        self.step = 0
        self.dialogue_running = True

        self.player = player
        self.text_overlay = text_overlay()

        #characters
        self.character = {
            'Tom' : 'graphics/caracters_w1/tom.png'
        }

        self.stone_surf = pygame.image.load('graphics/rock_tablet.png').convert_alpha()
        self.stone_rect = self.stone_surf.get_rect(topleft = (0,0))

        self.char_name = ['Tom']

        # Dialogue
        self.text = {
            '0': "So this is the ancient brazier",
            '1': "There is another scriptures",
            '2': "'To get the gem for activating the tower,\nyou need to ignite the brazier '",
            '3': "But you need 3 FIRE ESSENCE to ignite\nthis brazier",
            '4': "You can only get fire essence by hunting\nthe fire spirits that you find in the cave"
        }
        self.text_counter = 0


    def update(self):

        pressed = pygame.key.get_pressed()
        skip = pressed[pygame.K_x]
        skip_all = pressed[pygame.K_SPACE]

        # First step (dialogue)
        if self.step == 0:
            if int(self.text_counter) < len(self.text['0']):
                if skip_all:
                    self.text_counter = len(self.text['0'])
                else:
                    self.text_counter += 1
                
            else:
                if skip :
                    self.text_counter=0
                    self.step = 1    

        if self.step == 1:
            if int(self.text_counter) < len(self.text['1']):
                if skip_all:
                    self.text_counter = len(self.text['1'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 2

        if self.step == 2:
            if int(self.text_counter) < len(self.text['2']):
                if skip_all:
                    self.text_counter = len(self.text['2'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 3
        
        if self.step == 3:
            if int(self.text_counter) < len(self.text['3']):
                if skip_all:
                    self.text_counter = len(self.text['3'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 4

        if self.step == 4:
            if int(self.text_counter) < len(self.text['4']):
                if skip_all:
                    self.text_counter = len(self.text['4'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    # Finish the dialogue
                   
                    self.dialogue_running = False
                    self.player.quest_fire = True
                    

        return self.dialogue_running

    
    def draw(self, display_surface):
        if self.step == 0:
            draw_text(self.char_name[0],self.text['0'][0:int(self.text_counter)],30,'white', 210 , (display_surface.get_height() - 200) ,  200, (display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['0']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        if self.step == 1:
            draw_text(self.char_name[0],self.text['1'][0:int(self.text_counter)],30,'white', 210 , (display_surface.get_height() - 200) ,  200, (display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['1']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 2:
            display_surface.blit(self.stone_surf, self.stone_rect)
            draw_text('',self.text['2'][0:int(self.text_counter)],30,'white', 330 , 180 ,  200, (display_surface.get_height() - 272), display_surface)
            if int(self.text_counter) == len(self.text['2']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 435, SCREEN_HEIGHT - 220))
        if self.step == 3:
            display_surface.blit(self.stone_surf, self.stone_rect)
            draw_text('',self.text['3'][0:int(self.text_counter)],30,'white', 330 , 180 ,  200, (display_surface.get_height() - 272), display_surface)
            if int(self.text_counter) == len(self.text['3']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 435, SCREEN_HEIGHT - 220))
        if self.step == 4:
            display_surface.blit(self.stone_surf, self.stone_rect)
            draw_text('',self.text['4'][0:int(self.text_counter)],30,'white', 330 , 180 ,  200, (display_surface.get_height() - 272), display_surface)
            if int(self.text_counter) == len(self.text['4']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 435, SCREEN_HEIGHT - 220))


class dialogue_wizard_tower:
    def __init__(self, player):
        # Variables
        self.name = 'Wizard tower'
        self.step = 0
        self.dialogue_running = True

        self.text_overlay = text_overlay()

        self.player = player

        #characters
        self.character = {
            'Tom' : 'graphics/caracters_w1/tom.png', 
            'wizard' : 'graphics/caracters_w1/wizard_tower.png'
        }
        self.char_name = ['Tom', 'Wizard']


        # Dialogue
        self.text = {
            '0': "Who dares seek my Gem of Lightning?",
            '1': "I am Tom, and I seek to prove my worthiness to wield the power\nof the Gem.",
            '2': "You, a little gentle cat? Don't make me laugh.",
            '3': "But you wrote the scripture that says 'whoever reads it is worthy',\ndid you not?",
            '4': "Perhaps I did. But before you can claim the Gem, you must first\nprove your worthiness through a test.",
        }
        self.text_counter = 0


    def update(self):

        pressed = pygame.key.get_pressed()
        skip = pressed[pygame.K_x]
        skip_all= pressed[pygame.K_SPACE]

        # First step (dialogue)
        if self.step == 0:
            if int(self.text_counter) < len(self.text['0']):
                if skip_all:
                    self.text_counter = len(self.text['0'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 1 

        if self.step == 1:
            if int(self.text_counter) < len(self.text['1']):
                if skip_all:
                    self.text_counter = len(self.text['1'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step += 1 
        if self.step == 2:
            if int(self.text_counter) < len(self.text['2']):
                if skip_all:
                    self.text_counter = len(self.text['2'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step += 1    

        if self.step == 3:
            if int(self.text_counter) < len(self.text['3']):
                if skip_all:
                    self.text_counter = len(self.text['3'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step += 1    

        if self.step == 4:
            if int(self.text_counter) < len(self.text['4']):
                if skip_all:
                    self.text_counter = len(self.text['4'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    # Finish the dialogue
                    self.dialogue_running = False
                    self.player.test = True
                   

        return self.dialogue_running
    
    def draw(self, display_surface):
        if self.step == 0:
            draw_text(self.char_name[1], self.text['0'][0:int(self.text_counter)], 30,'white',210 , (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['wizard'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['0']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 1:
            draw_text(self.char_name[0], self.text['1'][0:int(self.text_counter)], 30,'white',210 , (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['1']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 2:
            draw_text(self.char_name[1], self.text['2'][0:int(self.text_counter)], 30,'white',210 , (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['wizard'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['2']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 3:
            draw_text(self.char_name[0], self.text['3'][0:int(self.text_counter)], 30,'white',210 , (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['3']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 4:
            draw_text(self.char_name[1], self.text['4'][0:int(self.text_counter)], 30,'white',210 , (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['wizard'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['4']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

class dialogue_wizard_tower_passed:
    def __init__(self, player):
        # Variables
        self.name = 'Wizard tower_passed'
        self.step = 0
        self.dialogue_running = True

        self.text_overlay = text_overlay()

        self.player = player

        #characters
        self.character = {
            'Tom' : 'graphics/caracters_w1/tom.png', 
            'wizard' : 'graphics/caracters_w1/wizard_tower.png'
        }
        self.char_name = ['Tom', 'Wizard']


        # Dialogue
        self.text = {
            '0': "Well, well, well... I'm impressed. Looks like you might\nactually be worthy of this challenge.",
            '1': "Now, let's get rid of these pesky rocks so you\ncan move on to the next level of the cave.",
            '2': "I've got a surprise waiting for you there that\nyou won't want to miss.",
            '3': "But be warned: there are plenty of monsters\nlurking around every corner.",
            '4': "Don't let your guard down, or you'll be sorry.",
        }
        self.text_counter = 0


    def update(self):

        pressed = pygame.key.get_pressed()
        skip = pressed[pygame.K_x]
        skip_all= pressed[pygame.K_SPACE]

        # First step (dialogue)
        if self.step == 0:
            if int(self.text_counter) < len(self.text['0']):
                if skip_all:
                    self.text_counter = len(self.text['0'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 1 

        if self.step == 1:
            if int(self.text_counter) < len(self.text['1']):
                if skip_all:
                    self.text_counter = len(self.text['1'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step += 1 
        if self.step == 2:
            if int(self.text_counter) < len(self.text['2']):
                if skip_all:
                    self.text_counter = len(self.text['2'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step += 1    

        if self.step == 3:
            if int(self.text_counter) < len(self.text['3']):
                if skip_all:
                    self.text_counter = len(self.text['3'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step += 1    

        if self.step == 4:
            if int(self.text_counter) < len(self.text['4']):
                if skip_all:
                    self.text_counter = len(self.text['4'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    # Finish the dialogue
                    self.dialogue_running = False
                    self.player.passed = True
                   

        return self.dialogue_running
    
    def draw(self, display_surface):
        if self.step == 0:
            draw_text(self.char_name[1], self.text['0'][0:int(self.text_counter)], 30,'white',210 , (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['wizard'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['0']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 1:
            draw_text(self.char_name[1], self.text['1'][0:int(self.text_counter)], 30,'white',210 , (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['wizard'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['1']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 2:
            draw_text(self.char_name[1], self.text['2'][0:int(self.text_counter)], 30,'white',210 , (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['wizard'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['2']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 3:
            draw_text(self.char_name[1], self.text['3'][0:int(self.text_counter)], 30,'white',210 , (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['wizard'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['3']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
    
        if self.step == 4:
            draw_text(self.char_name[1], self.text['4'][0:int(self.text_counter)], 30,'white',210 , (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['wizard'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['4']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

class dialogue_wizard_tower_failed:
    def __init__(self, player):
        # Variables
        self.name = 'Wizard tower_failed'
        self.step = 0
        self.dialogue_running = True

        self.text_overlay = text_overlay()

        self.player = player

        #characters
        self.character = {
            'Tom' : 'graphics/caracters_w1/tom.png', 
            'wizard' : 'graphics/caracters_w1/wizard_tower.png'
        }
        self.char_name = ['Tom', 'Wizard']


        # Dialogue
        self.text = {
            '0': "Wow, what a surprise.\nThe gentle little kitty failed the challenge.",
            '1': "Who would have thought? Maybe you should\nstick to the easy challenges from now on.",
            '2': "But hey, don't give up. You never know when you\nmight surprise us all and actually succeed."
        }
        self.text_counter = 0


    def update(self):

        pressed = pygame.key.get_pressed()
        skip = pressed[pygame.K_x]
        skip_all= pressed[pygame.K_SPACE]

        # First step (dialogue)
        if self.step == 0:
            if int(self.text_counter) < len(self.text['0']):
                if skip_all:
                    self.text_counter = len(self.text['0'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step = 1 

        if self.step == 1:
            if int(self.text_counter) < len(self.text['1']):
                if skip_all:
                    self.text_counter = len(self.text['1'])
                else:
                    self.text_counter += 1
            else:
                if skip :
                    self.text_counter=0
                    self.step += 1 
        
        if self.step == 2:
            if int(self.text_counter) < len(self.text['2']):
                if skip_all:
                    self.text_counter = len(self.text['2'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    # Finish the dialogue
                    self.dialogue_running = False
                    self.player.failed = True
                   

        return self.dialogue_running
    
    def draw(self, display_surface):
        if self.step == 0:
            draw_text(self.char_name[1], self.text['0'][0:int(self.text_counter)], 30,'white',210 , (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['wizard'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['0']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 1:
            draw_text(self.char_name[1], self.text['1'][0:int(self.text_counter)], 30,'white',210 , (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['wizard'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['1']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

        if self.step == 2:
            draw_text(self.char_name[1], self.text['2'][0:int(self.text_counter)], 30,'white',210 , (display_surface.get_height() - 200) ,200,(display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['wizard'], display_surface.get_width() - 335, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['2']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
#####################################################################################            

class dialogue_chest:
    def __init__(self, player):
        # Variables
        self.name = 'chest'
        self.step = 0
        self.dialogue_running = True

        self.player = player
        self.text_overlay = text_overlay()

        #characters
        self.character = {
            'Tom' : 'graphics/caracters_w1/tom.png'
        }
        self.char_name = ['Tom']

        # Dialogue
        self.text = {
            '0': "A chest in a cave? A little cliché, isn't it?",
            '1': "I wonder if it's filled with treasure or something.",
            '2': "Okay, I see it's locked.",
            '3': "Wait a minute, I have a key in here.",
            '4': "Really? I wonder if it can unlock it"
        }
        self.text_counter = 0


    def update(self):

        pressed = pygame.key.get_pressed()
        skip = pressed[pygame.K_x]
        skip_all = pressed[pygame.K_SPACE]

        # First step (dialogue)
        if self.step == 0:
            if int(self.text_counter) < len(self.text['0']):
                if skip_all:
                    self.text_counter = len(self.text['0'])
                else:
                    self.text_counter += 1
                
            else:
                if skip :
                    self.text_counter=0
                    self.step = 1    

        if self.step == 1:
            if int(self.text_counter) < len(self.text['1']):
                if skip_all:
                    self.text_counter = len(self.text['1'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 2

        if self.step == 2:
            if int(self.text_counter) < len(self.text['2']):
                if skip_all:
                    self.text_counter = len(self.text['2'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 3
        
        if self.step == 3:
            if int(self.text_counter) < len(self.text['3']):
                if skip_all:
                    self.text_counter = len(self.text['3'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 4

        if self.step == 4:
            if int(self.text_counter) < len(self.text['4']):
                if skip_all:
                    self.text_counter = len(self.text['4'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    # Finish the dialogue
                   
                    self.dialogue_running = False

        return self.dialogue_running

    
    def draw(self, display_surface):
        if self.step == 0:
            draw_text(self.char_name[0],self.text['0'][0:int(self.text_counter)],30,'white', 210 , (display_surface.get_height() - 200) ,  200, (display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['0']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        if self.step == 1:
            draw_text(self.char_name[0],self.text['1'][0:int(self.text_counter)],30,'white', 210 , (display_surface.get_height() - 200) ,  200, (display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['1']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        if self.step == 2:
            draw_text(self.char_name[0],self.text['2'][0:int(self.text_counter)],30,'white', 210 , (display_surface.get_height() - 200) ,  200, (display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['2']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        if self.step == 3:
            draw_text(self.char_name[0],self.text['3'][0:int(self.text_counter)],30,'white', 210 , (display_surface.get_height() - 200) ,  200, (display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['3']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        if self.step == 4:
            draw_text(self.char_name[0],self.text['4'][0:int(self.text_counter)],30,'white', 210 , (display_surface.get_height() - 200) ,  200, (display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['4']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))

class dialogue_chest1:
    def __init__(self, player):
        # Variables
        self.name = 'new'
        self.step = 0
        self.dialogue_running = True

        self.player = player
        self.text_overlay = text_overlay()

        #characters
        self.character = {
            'Tom' : 'graphics/caracters_w1/tom.png'
        }
        self.char_name = ['Tom']

        # Dialogue
        self.text = {
            '0': "Okay, great! More monsters!",
            '1': "I wonder if I can find more treasure chests in this cave.",
            '2': "Alright, if I can defeat these giant monsters, I might find a key.",
            '3': "It's hunting time!",
            '4': "Get ready, monsters, because I'm after those treasures!"
        }
        self.text_counter = 0


    def update(self):

        pressed = pygame.key.get_pressed()
        skip = pressed[pygame.K_x]
        skip_all = pressed[pygame.K_SPACE]

        # First step (dialogue)
        if self.step == 0:
            if int(self.text_counter) < len(self.text['0']):
                if skip_all:
                    self.text_counter = len(self.text['0'])
                else:
                    self.text_counter += 1
                
            else:
                if skip :
                    self.text_counter=0
                    self.step = 1    

        if self.step == 1:
            if int(self.text_counter) < len(self.text['1']):
                if skip_all:
                    self.text_counter = len(self.text['1'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 2

        if self.step == 2:
            if int(self.text_counter) < len(self.text['2']):
                if skip_all:
                    self.text_counter = len(self.text['2'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 3
        
        if self.step == 3:
            if int(self.text_counter) < len(self.text['3']):
                if skip_all:
                    self.text_counter = len(self.text['3'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 4

        if self.step == 4:
            if int(self.text_counter) < len(self.text['4']):
                if skip_all:
                    self.text_counter = len(self.text['4'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    # Finish the dialogue
                   
                    self.dialogue_running = False
                    self.player.quest_chest = True

        return self.dialogue_running

    
    def draw(self, display_surface):
        if self.step == 0:
            draw_text(self.char_name[0],self.text['0'][0:int(self.text_counter)],30,'white', 210 , (display_surface.get_height() - 200) ,  200, (display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['0']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        if self.step == 1:
            draw_text(self.char_name[0],self.text['1'][0:int(self.text_counter)],30,'white', 210 , (display_surface.get_height() - 200) ,  200, (display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['1']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        if self.step == 2:
            draw_text(self.char_name[0],self.text['2'][0:int(self.text_counter)],30,'white', 210 , (display_surface.get_height() - 200) ,  200, (display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['2']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        if self.step == 3:
            draw_text(self.char_name[0],self.text['3'][0:int(self.text_counter)],30,'white', 210 , (display_surface.get_height() - 200) ,  200, (display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['3']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        if self.step == 4:
            draw_text(self.char_name[0],self.text['4'][0:int(self.text_counter)],30,'white', 210 , (display_surface.get_height() - 200) ,  200, (display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['4']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
      
class dialogue_last:
    def __init__(self, player):
        # Variables
        self.name = 'boss'
        self.step = 0
        self.dialogue_running = True

        self.player = player
        self.text_overlay = text_overlay()

        #characters
        self.character = {
            'Tom' : 'graphics/caracters_w1/tom.png'
        }
        self.char_name = ['Tom']

        # Dialogue
        self.text = {
            '0': "I can feel the power of the gem coursing through my veins.",
            '1': "It's so close now, I can almost taste it.",
            '2': "But first, I must defeat this monstrous ogre standing in my way.",
            '3': "Get ready for me, you foul creature!",
            '4': "I will stop at nothing to obtain that precious gem."
        }
        self.text_counter = 0


    def update(self):

        pressed = pygame.key.get_pressed()
        skip = pressed[pygame.K_x]
        skip_all = pressed[pygame.K_SPACE]

        # First step (dialogue)
        if self.step == 0:
            if int(self.text_counter) < len(self.text['0']):
                if skip_all:
                    self.text_counter = len(self.text['0'])
                else:
                    self.text_counter += 1
                
            else:
                if skip :
                    self.text_counter=0
                    self.step = 1    

        if self.step == 1:
            if int(self.text_counter) < len(self.text['1']):
                if skip_all:
                    self.text_counter = len(self.text['1'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 2

        if self.step == 2:
            if int(self.text_counter) < len(self.text['2']):
                if skip_all:
                    self.text_counter = len(self.text['2'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 3
        
        if self.step == 3:
            if int(self.text_counter) < len(self.text['3']):
                if skip_all:
                    self.text_counter = len(self.text['3'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    self.text_counter=0
                    self.step = 4

        if self.step == 4:
            if int(self.text_counter) < len(self.text['4']):
                if skip_all:
                    self.text_counter = len(self.text['4'])
                else:
                    self.text_counter += 1
            else:
                if skip:
                    # Finish the dialogue
                   
                    self.dialogue_running = False
                    self.player.status = 'intro'
                    self.player.dialogue_finished = True

        return self.dialogue_running

    
    def draw(self, display_surface):
        if self.step == 0:
            draw_text(self.char_name[0],self.text['0'][0:int(self.text_counter)],30,'white', 210 , (display_surface.get_height() - 200) ,  200, (display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['0']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        if self.step == 1:
            draw_text(self.char_name[0],self.text['1'][0:int(self.text_counter)],30,'white', 210 , (display_surface.get_height() - 200) ,  200, (display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['1']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        if self.step == 2:
            draw_text(self.char_name[0],self.text['2'][0:int(self.text_counter)],30,'white', 210 , (display_surface.get_height() - 200) ,  200, (display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['2']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        if self.step == 3:
            draw_text(self.char_name[0],self.text['3'][0:int(self.text_counter)],30,'white', 210 , (display_surface.get_height() - 200) ,  200, (display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['3']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
        if self.step == 4:
            draw_text(self.char_name[0],self.text['4'][0:int(self.text_counter)],30,'white', 210 , (display_surface.get_height() - 200) ,  200, (display_surface.get_height() - 272), display_surface)
            draw_npc(self.character['Tom'], display_surface.get_width() - 313, display_surface.get_height() - 228 , display_surface )
            if int(self.text_counter) == len(self.text['4']):
                self.text_overlay.draw('Press X to skip', (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 80))
      

class dialogue_manager:
    def __init__(self, display_surface):
        self.display_surface = display_surface

        try:
            with open ('prehistoric_dialogue_done.txt') as load_file:
                load= json.load(load_file)
        except:
            load={
			'self.dialogue_complete':[]
		}
        
        self.dialogue_complete = load['self.dialogue_complete']
        self.dialogue = None
        self.dialogue_running = False
        

        self.image = pygame.image.load('graphics/dialogbox.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = (self.display_surface.get_width()// 2, self.display_surface.get_height() - 50))
    
    def start_dialogue(self, dialogue):
        if dialogue.name not in self.dialogue_complete:
            self.dialogue_complete.append(dialogue.name)
            self.dialogue = dialogue
            self.dialogue_running = True

    def end_dialogue(self):
        self.dialogue = None
        self.dialogue_running = False   

    def update(self):
        with open('prehistoric_dialogue_done.txt','w') as load_file:
            json.dump({'self.dialogue_complete':self.dialogue_complete},load_file)
        if self.dialogue_running:
            self.dialogue_running = self.dialogue.update()
        else:
            self.end_dialogue()

    def draw(self):
        if self.dialogue_running:
            if self.dialogue.name == "brazier" and self.dialogue.step >= 2:
                pass
            elif self.dialogue.name == "cave_tower" and self.dialogue.step >= 2:
                pass
            else:
                self.display_surface.blit(self.image, self.rect)
            self.dialogue.draw(self.display_surface)

