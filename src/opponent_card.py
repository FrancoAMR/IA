import pygame
from board import Board
from values import *

class OpponentCard:
    def __init__(self, index, attack_Value=0, defense_Value=0, state=0):
        self.image = pygame.transform.flip(card_Image, False, True) 
        self.width = card_Width
        self.height = card_Height
        self.index = index
        self.is_selected = False


        self.attack_Value = attack_Value
        self.defense_Value = defense_Value
        
        self.is_on_board = False  # Añadir esto para manejar las cartas que están en el tablero

    def draw(self, screen, num_cards):
        screen.blit(self.image, (positionX[num_cards],positionY[3]))
        self.draw_stats(screen, num_cards)

    def draw_stats(self, screen, num_cards):
        font = pygame.font.SysFont(None, 24)
        
        attack_text = font.render(str(self.attack_Value), True, stat_Color)
        defense_text = font.render(str(self.defense_Value), True, stat_Color)
        attack_text = pygame.transform.flip(attack_text, False, True)
        defense_text = pygame.transform.flip(defense_text, False, True)
        
        attack_text_x = positionX[num_cards]+ 30
        attack_text_y = positionY[3] + 10
        screen.blit(attack_text, (attack_text_x, attack_text_y))
        
        defense_text_x = attack_text_x + 35
        defense_text_y = attack_text_y
        screen.blit(defense_text, (defense_text_x, defense_text_y))
    
    def draw_deck(self, screen,deck):
        font = pygame.font.SysFont(None, 80)
        deck_text = font.render(str(deck), True, stat_Color)
        screen.blit(deck_text, (window_Width-lp_Width+60, 80))

    def move_to_board(self, rect):
        self.x = rect.x
        self.y = rect.y
        self.is_on_board = True  # Marcar como que está en el tablero
