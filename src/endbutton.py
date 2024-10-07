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

    def draw(self, screen, state,active_turn):
        screen.blit(self.image, (self.x, self.y))
        self.draw_state(screen, state,active_turn)

    def draw_state(self, screen, state,active_turn):
        txt1=""
        txt2=""
        font = pygame.font.SysFont(None,24)
        if active_turn == 1:
            if state == 1:
                txt1 = "Terminar"
                txt2 = "Invocación"
            if state == 2:
                txt1 = "Terminar"
                txt2 = "Colocación"
            if state == 3:
                txt1 = "Terminar"
                txt2 = "Turno"

        else:
            txt1="Empezar"
            txt2="IA"
        button_text1 = font.render(txt1, True, stat_Color)
        button_text2 = font.render(txt2, True, stat_Color)
        txt_1_width = button_text1.get_width()
        txt_2_width = button_text2.get_width()
        txt_height = button_text1.get_height()
        screen.blit(button_text1, (end_Button_X+(end_Button_Width-txt_1_width)/2,end_Button_Y+((end_Button_Height-txt_height)/2)))
        screen.blit(button_text2, (end_Button_X+(end_Button_Width-txt_2_width)/2,end_Button_Y+((end_Button_Height-txt_height)/2)+16))

    def isClicked(self, mouse_Position):
        button_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.click_flag = button_rect.collidepoint(mouse_Position)
        return self.click_flag
