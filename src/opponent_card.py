import pygame
from values import *

class OpponentCard:
    def __init__(self, index):
        
        self.image = pygame.transform.flip(card_image, False, True) 
        self.width = card_width
        self.height = card_height
        self.index = index
        self.is_selected = False

        self.x = 0
        self.y = 0  

    def draw(self, screen, num_cards):
        
        card_x = card_init_x - (self.width * num_cards) / 2 + card_width * self.index
        self.x = card_x
        screen.blit(self.image, (card_x, self.y))
