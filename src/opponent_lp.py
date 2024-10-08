import pygame
from values import *

class OpponentLp:
    def __init__(self):
        
        self.image = lp_Image  # Puedes usar la misma imagen o una diferente si prefieres
        self.width = lp_Width
        self.height = lp_Height

        self.x = window_Width - self.width
        self.y = 0     
        self.lp = 20
        self.win_Flag = False   
        self.deck = 30

    def receiveDMG(self, damage): 
        self.lp -= damage
        if self.lp < 0:
            self.lp = 0  # Los life points no pueden ser negativos
    
    def restart_op_lp(self):
        self.image = lp_Image  # Puedes usar la misma imagen o una diferente si prefieres
        self.width = lp_Width
        self.height = lp_Height

        self.x = window_Width - self.width
        self.y = 0     
        self.lp = 20   
        self.win_Flag = False  

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        self.draw_stats(screen)

    def draw_stats(self, screen):
        font = pygame.font.SysFont(None, 80)
        
        lp_text = font.render(str(self.lp), True, stat_Color)
        deck_text = font.render(str(self.deck), True, stat_Color)

        text_x = self.x + 60
        text_y = self.y + 10
        screen.blit(lp_text, (text_x, text_y))
        screen.blit(deck_text, (text_x, text_y+80))
    def win(self):
        if self.lp == 0 or self.deck == 0:
            self.win_Flag = True
        else:
            self.win_Flag = False
