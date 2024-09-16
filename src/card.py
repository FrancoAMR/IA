import pygame
from values import *
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

    def draw(self, screen, num_cards):
        if self.is_on_board:
            screen.blit(card_image, (self.x, self.y))
        else:
            self.x = card_init_x - (card_width * num_cards) / 2 + card_width * self.index
            self.y = card_y - 20 if self.is_selected else card_y
            screen.blit(card_image, (self.x, self.y))

    def click(self, mouse_pos):
        card_rect = pygame.Rect(self.x, self.y, card_width, card_height)
        if card_rect.collidepoint(mouse_pos):
            if not self.is_selected:
                self.is_selected = True
                self.description.show()
                if Card.selected_card and Card.selected_card != self:
                    Card.selected_card.deselect()
            else:
                self.deselect()
            Card.selected_card = self

    def move_to_board(self, rect):
        self.x = rect.x
        self.y = rect.y
        self.is_on_board = True
        self.deselect()

    def deselect(self):
        self.is_selected = False
        Card.selected_card = None
        self.description.hide()
