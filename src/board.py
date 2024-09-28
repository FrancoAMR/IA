import pygame
from values import *

class Board:
    card_on_board = 0

    def __init__(self):
        self.rect_Width = field_Width // 5
        self.rect_Height = field_Height // 2
        self.rectangles = []
        self.occupied = [False] * 10
        self.board_Rect = [None] * 10
        self.cards_Board= []
        
        # Crear los rectángulos del tablero
        for index in range(10):
            col = index % 5  # Columna (0 a 4)
            row = index // 5  # Fila (0 o 1)
            rect_x = positionX[col]
            rect_y = positionY[row + 1]  # Usar el segundo y tercer valor de positionY
            self.rectangles.append(pygame.Rect(rect_x, rect_y, card_Width, card_Height))
            self.board_Rect[index] = pygame.Rect(rect_x, rect_y, card_Width, card_Height)

    def isFirstRow(self, rect_index):
        return rect_index < 5  

    def isSecondRow(self, rect_index):
        return rect_index >= 5

    def draw(self, screen):
        screen.blit(field_Image, (field_X, field_Y))

    def mouse(self, screen, mouse_pos):
        for rect in self.rectangles:
            if rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, highlight_Color, rect)


    def placeCard(self, mouse_Position, selected_card, is_opponent=False):
        for i, rect in enumerate(self.rectangles):
            if rect.collidepoint(mouse_Position) and not self.occupied[self.rectangles.index(rect)]:
                self.occupied[self.rectangles.index(rect)] = True
                selected_card.board_Position = self.rectangles.index(rect)  # Guarda la posición de la carta
                self.cards_Board.append(selected_card)
                Board.card_on_board += 1
                return True
        return False
                

    # Función para que se pueda actualizar la liberación de la casilla de carta una vez movida 
    def remove_card(self, card):
        if card.board_Position is not None:
            # Liberar la posición ocupada por la carta
            self.occupied[card.board_Position] = False
            self.occupied_cards.remove(card)  # Remover la carta de las ocupadas
            Board.card_on_board -= 1
            print("Carta removida. Cartas en tablero:", Board.card_on_board)
            # Resetea la posición de la carta
            card.board_Position = None
            return True
        return False
