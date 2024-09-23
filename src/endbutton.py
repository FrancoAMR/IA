import pygame
from values import *

class Endbutton:
    def __init__(self):
        
        self.image = end_button_image
        self.width = end_button_width
        self.height = end_button_height

        self.x = end_button_x
        self.y = end_button_y

    def draw(self, screen, state):
        screen.blit(self.image, (self.x, self.y))
        self.draw_state(screen, state)

    def draw_state(self, screen, state):
        font = pygame.font.SysFont(None,24)
        state_text_x = self.x 
        state_text_y = self.y + self.height/2
        if state == 3:
            txt_1 = "Terminar"
            txt_2 = "turno"
            button_text1 = font.render(txt_1, True, stat_color)
            button_text2 = font.render(txt_2, True, stat_color)
            screen.blit(button_text1, (state_text_x,state_text_y))
            screen.blit(button_text2, (state_text_x,state_text_y+15))

    def is_clicked(self, mouse_pos):
        button_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return button_rect.collidepoint(mouse_pos)
