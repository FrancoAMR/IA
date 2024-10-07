import pygame
from values import *

class Menu:
    def __init__(self):
        self.initial_difficult_y = window_Height/2 - 190
        self.difficult_x = (window_Width - difficulty_width)/2
        self.difficult_y = [self.initial_difficult_y+50, 
                            self.initial_difficult_y+50 + difficulty_height+40, 
                            self.initial_difficult_y+50 + difficulty_height*2+80] 
        self.button_rect_array = []
        self.selected_difficulty = -1

    def render(self, screen):
        font = pygame.font.SysFont('/assets/fonts/font1.ttf',80)
        self.button_rect_array = []
        screen.fill(background_Color)
        screen.blit(background_Image, (0,0))

        title_text = font.render("Seleccione dificultad", True, (255, 255, 255))
        title_text_width = title_text.get_width()
        title_text_x = (window_Width - title_text_width) / 2
        title_text_y = 140
        screen.blit(title_image,((window_Width-title_image_width)/2,10))
        screen.blit(title_text, (title_text_x, title_text_y))

        screen.blit(easy_image, (self.difficult_x, self.difficult_y[0]))
        screen.blit(medium_image, (self.difficult_x, self.difficult_y[1]))
        screen.blit(hard_image, (self.difficult_x, self.difficult_y[2]))

        for i in range(3):
            
            button_rect = pygame.Rect(self.difficult_x, self.difficult_y[i], difficulty_width, difficulty_height)
            self.button_rect_array.append(button_rect)

    def menu_events(self,events):
        mouse_Position= pygame.mouse.get_pos()
        #print("Posición del mouse", mouse_Position)
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button ==1:
                    print("Presionado botón click en: ", mouse_Position)
                    for i, button_rect in enumerate(self.button_rect_array):
                        if button_rect.collidepoint(mouse_Position):
                            if i == 0:
                                self.selected_difficulty = 0
                            elif i == 1:
                                self.selected_difficulty = 1
                            elif i == 2:
                                self.selected_difficulty = 2
                    
