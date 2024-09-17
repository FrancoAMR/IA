import pygame
from values import *

class OpponentLp:
    def __init__(self):
        
        self.image = lp_image  # Puedes usar la misma imagen o una diferente si prefieres
        self.width = lp_width
        self.height = lp_height

        self.x = window_width - self.width
        self.y = 0     
        self.lp = 20   
        self.deck = 35

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        self.draw_stats(screen)

    def draw_stats(self, screen):
        font = pygame.font.SysFont(None, 80)
        
        lp_text = font.render(str(self.lp), True, (101, 101, 102))
        deck_text = font.render(str(self.deck), True, (101, 101, 102))

        text_x = self.x + 60
        text_y = self.y + 10
        screen.blit(lp_text, (text_x, text_y))
        screen.blit(deck_text, (text_x, text_y+80))
