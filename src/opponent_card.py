import pygame
from board import Board
from values import *

class OpponentCard:
    selected_Card= None
    def __init__(self, index, attack_Value=0, defense_Value=0, state=0, behavior= 0):
        #self.image = pygame.transform.flip(card_Image, False, True) 

        #Valores de las cartas
        self.index = index
        self.attack_Value = attack_Value
        self.defense_Value = defense_Value
        self.state= state
        self.behavior= behavior
        self.board_Position= None
        self.is_Selected = False

    #Dibujado de las cartas del oponente
    def draw(self, screen, pos_X, pos_Y, behavior):
        if pos_Y==2: #posY indica que se dibujara en el campo
            draw_Y= positionY[pos_Y]
            match behavior:
                case 0:
                    screen.blit(red_Card_Image, (positionX[pos_X], draw_Y)) #Dibujado en la pantalla
                case 1:
                    screen.blit(blue_Card_Image, (positionX[pos_X], draw_Y)) #Dibujado en la pantalla
            self.drawStats(screen, positionX[pos_X], draw_Y) #Llamada al dibujado de estadisticas
            self.drawMonster(screen, positionX[pos_X], draw_Y)
        elif pos_Y==3: #posY indica que se dibujara en la mano
            draw_Y= positionY[pos_Y]-20 if self.is_Selected else positionY[pos_Y] #Ubicacion si es seleccionada o no
            screen.blit(dark_card_image, (positionX[pos_X], draw_Y)) #Dibujado en la pantalla
            #self.drawStats(screen, positionX[pos_X], draw_Y) #Llamada al dibujado de estadisticas
            #self.drawMonster(screen, positionX[pos_X], draw_Y)
    def drawMonster(self, screen,pos_X, pos_Y):
        monster_x = (pos_X + (card_Width-monster_image_width)/2) + 1 
        monster_y = pos_Y + 9
        screen.blit(monster_image[self.index], (monster_x, monster_y))

    def drawStats(self, screen, pos_X, pos_Y):
        # Definicion de la fuente
        font= pygame.font.SysFont(None, 24)
        # Dibujado de los textos de estadisticas y su color
        card_text_tuple = (0,0,0)
        if self.behavior == 0:
            card_text_tuple = (255,255,255)
        else:
            card_text_tuple = (stat_Color)

        attack_text = font.render(str(self.attack_Value), True, (card_text_tuple))
        defense_text = font.render(str(self.defense_Value), True, (card_text_tuple))
        attack_text_x = pos_X + 30
        attack_text_y = pos_Y + 142
        screen.blit(attack_text, (attack_text_x, attack_text_y))
        
        defense_text_x = attack_text_x + 35
        defense_text_y = attack_text_y
        screen.blit(defense_text, (defense_text_x, defense_text_y))
    
    def draw_deck(self, screen,deck):
        font = pygame.font.SysFont(None, 80)
        deck_text = font.render(str(deck), True, stat_Color)
        screen.blit(deck_text, (window_Width-lp_Width+60, 80))

    def move_to_board(self, rect):
        self.x = rect.x
        self.y = rect.y
        self.is_on_board = True  # Marcar como que está en el tablero


    def fieldClick(self, mouse_Position, i, pos_Y):
        # Verifica que el índice i sea válido
        if i < len(positionX):
            card_rect = pygame.Rect(positionX[i], positionY[pos_Y], card_Width, card_Height)
            self.isfieldCardClicked = card_rect.collidepoint(mouse_Position)
            return self.isfieldCardClicked