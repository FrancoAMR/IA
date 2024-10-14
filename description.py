import pygame
from values import *

class CardDescription:
    def __init__(self):
        self.image = card_Desc_Image
        self.width = card_Desc_Width
        self.height = card_Desc_Height
        self.x = card_Desc_X
        self.y = card_Desc_Y
        self.visible = False

    def show(self):
        self.visible = True

    def hide(self):
        self.visible = False

    def draw(self, screen):
        if self.visible:
            screen.blit(self.image, (self.x, self.y))
