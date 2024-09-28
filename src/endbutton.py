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

    def isClicked(self, mouse_Position):
        button_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.click_flag = button_rect.collidepoint(mouse_Position)
        print("Botón presionado: ", self.click_flag)
        return self.click_flag
