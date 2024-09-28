import pygame
from values import *

class Lp:
    def __init__(self):
        
        self.image = lp_Image
        self.width = lp_Width
        self.height = lp_Height

        self.x = lp_X
        self.y = lp_Y
        self.lp = 20
        #self.deck = 35

    def receiveDMG(self, damage): 
        self.lp -= damage
        if self.lp < 0:
            self.lp = 0  # Los life points no pueden ser negativos

    
    #def decrease_deck(self, num_decreased):
        #self.deck = self.deck - num_decreased

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        self.draw_stats(screen)

    def draw_stats(self, screen):
        font = pygame.font.SysFont(None, 80)
        
        lp_text = font.render(str(self.lp), True, stat_Color)
        #deck_text = font.render(str(self.deck), True, stat_color)

        text_x = self.x + 60
        text_y = self.y + 10
        screen.blit(lp_text, (text_x, text_y))
        #screen.blit(deck_text, (text_x, text_y+80))

