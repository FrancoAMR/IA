import pygame
import random
from values import *

class OpponentCard:
    def __init__(self, index, attack_value=0, defense_value=0, state=0):
        self.image = pygame.transform.flip(card_image, False, True) 
        self.width = card_width
        self.height = card_height
        self.index = index
        self.is_selected = False
        self.state = state

        self.x = 0
        self.y = 0  

        self.attack_value = attack_value
        self.defense_value = defense_value
        
        self.is_on_board = False  # Añadir esto para manejar las cartas que están en el tablero

    def draw(self, screen, num_cards):
        card_x = card_init_x - (self.width * num_cards) / 2 + card_width * self.index
        self.x = card_x
        screen.blit(self.image, (card_x, self.y))
        self.draw_stats(screen)

    def draw_stats(self, screen):
        font = pygame.font.SysFont(None, 24)
        
        attack_text = font.render(str(self.attack_value), True, stat_color)
        defense_text = font.render(str(self.defense_value), True, stat_color)
        attack_text = pygame.transform.flip(attack_text, False, True)
        defense_text = pygame.transform.flip(defense_text, False, True)
        
        attack_text_x = self.x + 30
        attack_text_y = self.y + 10
        screen.blit(attack_text, (attack_text_x, attack_text_y))
        
        defense_text_x = attack_text_x + 35
        defense_text_y = attack_text_y
        screen.blit(defense_text, (defense_text_x, defense_text_y))

    def move_to_board(self, rect):
        self.x = rect.x
        self.y = rect.y
        self.is_on_board = True  # Marcar como que está en el tablero
