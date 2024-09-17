import pygame
from values import *

class Board:
    card_on_board = 0

    def __init__(self):
        self.rect_width = field_width // 5
        self.rect_height = field_height // 2
        self.rectangles = []
        self.occupied = [False] * 10
        self.occupied_cards = []  # Lista para almacenar las cartas en el tablero
        
        for row in range(2):
            for col in range(5):
                rect_x = field_x + col * self.rect_width
                rect_y = field_y + row * self.rect_height
                self.rectangles.append(pygame.Rect(rect_x, rect_y, self.rect_width, self.rect_height))

    def draw(self, screen):
        screen.blit(field_image, (field_x, field_y))
        # Dibujar las cartas en el tablero
        for card in self.occupied_cards:
            card.draw(screen, Board.card_on_board)

    def mouse(self, screen, mouse_pos):
        for rect in self.rectangles:
            if rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, highlight_color, rect)
    
    def place_card(self, mouse_pos, selected_card):
        for i, rect in enumerate(self.rectangles):
            if rect.collidepoint(mouse_pos) and not self.occupied[i]:
                selected_card.move_to_board(rect)
                self.occupied[i] = True
                self.occupied_cards.append(selected_card)
                Board.card_on_board += 1
                print("Cartas en tablero:", Board.card_on_board)
                return True
        return False
