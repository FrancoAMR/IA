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
        #cambios para saber la piosicion de la carta         
        self.board_position = None  # Nueva variable para la posición en el tablero
        self.is_selected = False
        self.is_on_board = False  
        self.state = state
        self.description = CardDescription()
        self.positions_x = []

    def draw(self, screen, num_cards):
        if self.is_on_board:
            screen.blit(card_image, (positionX[num_cards], positionY[1]))
            self.draw_stats(screen, positionX[num_cards], positionY[1])  
        else:
            positionY[0] = positionY-20 if self.is_selected else positionY[0]
            if num_cards >= len(self.positions_x):
                self.positions_x.append(self.x[num_cards])  # Agrega la nueva posición
            else:
                self.positions_x[num_cards] = positionX[num_cards]  # Actualiza la posición existente
            screen.blit(card_image, (positionX[num_cards], positionY[0]))
            self.draw_stats(screen, positionX[num_cards], positionY[0])

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
        if i < len(self.x):
            card_rect = pygame.Rect(positionX[i], positionY[0], card_width, card_height)
            print("Carta numero: ", i)
            print("supera al if")
            if card_rect.collidepoint(mouse_pos):
                print("supera al 2do if")
                if not self.is_selected:
                    print("supera al 3er if")
                    if Card.selected_card:
                        print("supera al 4to if")
                        Card.selected_card.deselect()
                    print("supera la cadena de ifs")
                    self.is_selected = True
                    self.description.show()
                    print("supera la muestra de descripcion")
                    Card.selected_card = self
                else:
                    print("Antes del deselect")
                    self.deselect()


    def move_to_board(self, rect, board_position):
        print("TODO")
        #positionX[0] = rect.x
        #self.y = rect.y
        #self.is_on_board = True
        #self.deselect()
        #self.board_position = board_position  # Guardamos el índice de la posición en el tablero

    def deselect(self):
        self.is_selected = False
        self.description.hide()
        if Card.selected_card == self:
            Card.selected_card = None
