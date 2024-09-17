import pygame
import random
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

        self.attack_value = random.randint(1, 8)
        self.defense_value = random.randint(1, 8)

    def draw(self, screen, num_cards):
        card_x = card_init_x - (self.width * num_cards) / 2 + card_width * self.index
        self.x = card_x
        screen.blit(self.image, (card_x, self.y))
        self.draw_stats(screen)

    def draw_stats(self, screen):
        font = pygame.font.SysFont(None, 24)
        
        attack_text = font.render(str(self.attack_value), True, (101, 101, 102))
        defense_text = font.render(str(self.defense_value), True, (101, 101, 102))
        attack_text = pygame.transform.flip(attack_text, False, True)
        defense_text = pygame.transform.flip(defense_text, False, True)
        
        attack_text_x = self.x + 30
        attack_text_y = self.y + 10
        screen.blit(attack_text, (attack_text_x, attack_text_y))
        
        defense_text_x = attack_text_x + 35
        defense_text_y = attack_text_y
        screen.blit(defense_text, (defense_text_x, defense_text_y))
