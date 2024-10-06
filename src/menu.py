import pygame
from values import *

class Menu:
    def __init__(self):
        self.state = True
        self.initial_difficult_y = window_Height/2 - 190
        self.difficult_x = (window_Width - end_Button_Width)/2
        self.difficult_y = [self.initial_difficult_y+50, 
                            self.initial_difficult_y+50 + end_Button_Height+40, 
                            self.initial_difficult_y+50 + end_Button_Height*2+80] 
        self.click_flag = False
        self.button_rect_array = []
        self.selected_difficulty = -1

    def render(self, screen):
        font = pygame.font.SysFont('../assets/fonts/font1.ttf',80)
        self.button_rect_array = []
        screen.fill(background_Color)

        title_text = font.render("Seleccione dificultad", True, (255, 255, 255))
        title_text_width = title_text.get_width()
        title_text_x = (window_Width - title_text_width) / 2
        title_text_y = 20
        screen.blit(title_text, (title_text_x, title_text_y))
        
        for i in range(3):
            screen.blit(end_Button_Image, (self.difficult_x, self.difficult_y[i]))
            button_rect = pygame.Rect(self.difficult_x, self.difficult_y[i], end_Button_Width, end_Button_Height)
            
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
                    
    def set_difficulty(self):
        
        return self.selected_difficulty