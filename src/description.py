import pygame
from values import *

class CardDescription:
    def __init__(self):
        self.image = card_desc_image
        self.width = card_desc_width
        self.height = card_desc_height
        self.x = card_desc_x
        self.y = card_desc_y
        self.visible = False

    def show(self):
        self.visible = True

    def hide(self):
        self.visible = False

    def draw(self, screen):
        if self.visible:
            screen.blit(self.image, (self.x, self.y))
