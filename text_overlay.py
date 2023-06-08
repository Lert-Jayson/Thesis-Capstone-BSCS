import pygame

class text_overlay:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font('font/LycheeSoda.ttf', 35)

        self.b_time = pygame.time.get_ticks()

    def draw(self, text, pos):

        self.text_surface = self.font.render(text, True, 'white')
        self.text_rect = self.text_surface.get_rect(midbottom = pos)

        self.c_time = pygame.time.get_ticks()
        if ((self.c_time - self.b_time) % 1000) < 500 :
            self.display_surface.blit(self.text_surface, self.text_rect)