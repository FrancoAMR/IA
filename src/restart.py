import pygame
from values import *

class Restart:
    def __init__(self):
        
        self.initial_difficult_y = window_Height/2 - 190
        self.difficult_x = (window_Width - difficulty_width)/2
        self.difficult_y = [self.initial_difficult_y+50, 
                            self.initial_difficult_y+50 + difficulty_height+40] 
        self.select_restart = False
        self.button_rect_array = []
        self.selected_difficulty = -1
        
    def render(self,screen):
        screen.fill(background_Color)
        screen.blit(restart_image, (self.difficult_x, self.difficult_y[0]))
        screen.blit(exit_image, (self.difficult_x, self.difficult_y[1]))
        for i in range(2):
            
            button_rect = pygame.Rect(self.difficult_x, self.difficult_y[i], difficulty_width, difficulty_height)
            self.button_rect_array.append(button_rect)

    def restart_events(self, events):
        mouse_Position= pygame.mouse.get_pos()
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
                                    self.select_restart = True
                                elif i == 1:
                                    pygame.quit()
                                    exit()
    