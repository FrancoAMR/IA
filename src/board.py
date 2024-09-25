import pygame
from values import *

class Board:
    card_on_board = 0

    def __init__(self):
        self.rect_width = field_width // 5
        self.rect_height = field_height // 2
        self.rectangles = []
        self.occupied = [False] * 10
        self.occupied_cards = []  
        self.board_rect = [None] * 10
        
        # Crear los rectángulos del tablero
        for index in range(10):
            col = index % 5  # Columna (0 a 4)
            row = index // 5  # Fila (0 o 1)
            rect_x = positionX[col]
            rect_y = positionY[row + 1]  # Usar el segundo y tercer valor de positionY
            self.rectangles.append(pygame.Rect(rect_x, rect_y, card_width, card_height))
            self.board_rect[index] = pygame.Rect(rect_x, rect_y, card_width, card_height)

    def is_first_row(self, rect_index):
        return rect_index < 5  

    def is_second_row(self, rect_index):
        return rect_index >= 5

    def draw(self, screen):
        screen.blit(field_image, (field_x, field_y))

        for card in self.occupied_cards:
            card.draw(screen, Board.card_on_board)

    def mouse(self, screen, mouse_pos):
        for rect in self.rectangles:
            if rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, highlight_color, rect)

    # board.py
    def place_card(self, mouse_pos, selected_card, is_opponent=False):
        for i, rect in enumerate(self.rectangles):
            if rect.collidepoint(mouse_pos) and not self.occupied[i]:
                # Si la carta ya está en el tablero, liberamos su posición anterior
                if selected_card.board_position is not None:
                    self.remove_card(selected_card)

                # Posicionamos la carta en las coordenadas del rectángulo clicado
                card_x= rect.x
                card_y= rect.y
                selected_card.move_to_board((card_x, card_y), i)  # Pasamos las coordenadas y el índice

                # Marcamos el espacio como ocupado y agregamos la carta al tablero
                self.occupied[i] = True
                self.occupied_cards.append(selected_card)
                Board.card_on_board += 1
                return True
        return False


    # Función para que se pueda actualizar la liberación de la casilla de carta una vez movida 
    def remove_card(self, card):
        if card.board_position is not None:
            # Liberar la posición ocupada por la carta
            self.occupied[card.board_position] = False
            self.occupied_cards.remove(card)  # Remover la carta de las ocupadas
            Board.card_on_board -= 1
            print("Carta removida. Cartas en tablero:", Board.card_on_board)
            # Resetea la posición de la carta
            card.board_position = None
            return True
        return False
