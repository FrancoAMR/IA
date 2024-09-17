import pygame
from values import *

class Endbutton:
    def __init__(self):
        
        self.image = end_button_image
        self.width = end_button_width
        self.height = end_button_height

        self.x = end_button_x
        self.y = end_button_y

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def is_clicked(self, mouse_pos):
        button_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return button_rect.collidepoint(mouse_pos)
