import pygame
from values import *
from board import Board
from description import CardDescription

class Card:
    selected_card = None

    def __init__(self, index, attack_value=0, defense_value=0, state=0):
        self.index = index
        self.is_selected = False
        self.is_on_board = False  
        self.description = CardDescription()

        self.attack_value = attack_value
        self.defense_value = defense_value
        self.board_position = None  # Posición en el tablero
        self.state = state
        self.positions_x = []  # Posiciones X para cartas en mano
        self.initial_y = positionY[0]  # Almacena la posición Y inicial

    def draw(self, screen, num_cards):
        # Eleva la carta seleccionada solo una vez
        draw_y = self.initial_y - 20 if self.is_selected else self.initial_y
        
        if self.is_on_board:
            screen.blit(card_image, (positionX[num_cards], positionY[1]))
            self.draw_stats(screen, positionX[num_cards], positionY[1])  
        else:
            screen.blit(card_image, (positionX[num_cards], draw_y))
            self.draw_stats(screen, positionX[num_cards], draw_y)

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

    def click(self, mouse_pos, i):
        # Verifica que el índice i sea válido
        if i < len(positionX):
            card_rect = pygame.Rect(positionX[i], self.initial_y, card_width, card_height)
            print("Carta numero: ", i)
            if card_rect.collidepoint(mouse_pos):
                if not self.is_selected:
                    if Card.selected_card:
                        Card.selected_card.deselect()
                    self.is_selected = True
                    self.description.show()
                    Card.selected_card = self
                else:
                    self.deselect()

    def move_to_board(self, rect, board_position):
        self.is_on_board = True
        self.board_position = board_position  # Guardamos el índice de la posición en el tablero
        self.deselect()  # Deseleccionamos la carta después de moverla

    def deselect(self):
        self.is_selected = False
        self.description.hide()
        if Card.selected_card == self:
            Card.selected_card = None
