import pygame
import random
from values import *
from board import Board
from description import CardDescription

class Card:
    selected_card = None

    def __init__(self, index, is_opponent=False):
        self.index = index
        self.x = 0
        self.y = card_y

        self.is_selected = False
        self.is_on_board = False  
        self.is_opponent = is_opponent
        self.description = CardDescription()

        self.attack_value = random.randint(1, 8)
        self.defense_value = random.randint(1, 8)

    def draw(self, screen, num_cards):
        if self.is_on_board:
            screen.blit(card_image, (self.x, self.y))
            self.draw_stats(screen, self.x, self.y)  
        else:
            self.x = card_init_x - (card_width * num_cards) / 2 + card_width * self.index
            self.y = card_y - 20 if self.is_selected else card_y
            screen.blit(card_image, (self.x, self.y))
            self.draw_stats(screen, self.x, self.y)  

    def draw_stats(self, screen, x, y): 
        font = pygame.font.SysFont(None, 24)
        
        attack_text = font.render(str(self.attack_value), True, (101, 101, 102))
        defense_text = font.render(str(self.defense_value), True, (101, 101, 102))
        
        attack_text_x = x + 30
        attack_text_y = y + 142
        screen.blit(attack_text, (attack_text_x, attack_text_y))
        
        defense_text_x = attack_text_x + 35
        defense_text_y = attack_text_y
        screen.blit(defense_text, (defense_text_x, defense_text_y))

    def click(self, mouse_pos):
        card_rect = pygame.Rect(self.x, self.y, card_width, card_height)
        if card_rect.collidepoint(mouse_pos):
            if not self.is_selected:
                if Card.selected_card:
                    Card.selected_card.deselect()
                self.is_selected = True
                self.description.show()
                Card.selected_card = self
            else:
                self.deselect()

    def move_to_board(self, rect):
        self.x = rect.x
        self.y = rect.y
        self.is_on_board = True
        self.deselect()

        self.board_x = self.x
        self.board_y = self.y

    def deselect(self):
        self.is_selected = False
        self.description.hide()
        if Card.selected_card == self:
            Card.selected_card = None
