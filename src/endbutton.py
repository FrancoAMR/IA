import pygame
from values import *

class Endbutton:
    def __init__(self):
        
        self.image = end_Button_Image
        self.width = end_Button_Width
        self.height = end_Button_Height
        self.click_flag = False

        self.x = end_Button_X
        self.y = end_Button_Y

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

    def isClicked(self, mouse_Position):
        button_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.click_flag = button_rect.collidepoint(mouse_Position)
        print("Botón presionado: ", self.click_flag)
        return self.click_flag
