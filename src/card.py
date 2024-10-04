import pygame
from values import *
from description import CardDescription

class Card:
    selected_card = None

    def __init__(self, index, attack_Value=0, defense_Value=0, state=0, behavior= 0):
        # Campos de la carta
        self.index = index
        self.attack_Value = attack_Value
        self.defense_Value = defense_Value
        self.state= state # state -1= No disponible, state 0= Disponible, state 1= No disponible temporalmente
        self.behavior= behavior #Determina si esta en ataque (0) o defensa (1)
        self.board_Position= None
        # Estado de seleccion inicializado en falso
        self.is_Selected = False
        self.isfieldCardClicked = False
        # Descripcion de la carta (IMG), probablemente se borre
        self.description = CardDescription()

    #Dibujado de las cartas
    def draw(self, screen, pos_X, pos_Y, behavior):
        if pos_Y==1: #posY indica que se dibujara en el campo
            draw_Y= positionY[pos_Y]
            match behavior:
                case 0:
                    screen.blit(red_Card_Image, (positionX[pos_X], draw_Y)) #Dibujado en la pantalla
                case 1:
                    screen.blit(blue_Card_Image, (positionX[pos_X], draw_Y)) #Dibujado en la pantalla
            self.drawStats(screen, positionX[pos_X], draw_Y) #Llamada al dibujado de estadisticas
        elif pos_Y==0: #posY indica que se dibujara en la mano
            draw_Y= positionY[pos_Y]-20 if self.is_Selected else positionY[pos_Y] #Ubicacion si es seleccionada o no
            screen.blit(red_Card_Image, (positionX[pos_X], draw_Y)) #Dibujado en la pantalla
            self.drawStats(screen, positionX[pos_X], draw_Y) #Llamada al dibujado de estadisticas
    
    # Dibujado de las estadisticas de las cartas
    def drawStats(self, screen, pos_X, pos_Y):
        # Definicion de la fuente
        font= pygame.font.SysFont(None, 24)
        # Dibujado de los textos de estadisticas y su color
        attack_text = font.render(str(self.attack_Value), True, (101, 101, 102))
        defense_text = font.render(str(self.defense_Value), True, (101, 101, 102))
        attack_text_x = pos_X + 30
        attack_text_y = pos_Y + 142
        screen.blit(attack_text, (attack_text_x, attack_text_y))
        
        defense_text_x = attack_text_x + 35
        defense_text_y = attack_text_y
        screen.blit(defense_text, (defense_text_x, defense_text_y))
        
    # Al hacer click
    def click(self, mouse_Position, i, pos_Y):
        # Verifica que el índice i sea válido
        if i < len(positionX):
            card_rect = pygame.Rect(positionX[i], positionY[pos_Y], card_Width, card_Height)
            if card_rect.collidepoint(mouse_Position):
                if not self.is_Selected:
                    if Card.selected_card:
                        Card.selected_card.deselect()
                    self.is_Selected = True
                    self.description.show()
                    Card.selected_card = self
                else:
                    self.deselect()

    def fieldClick(self, mouse_Position, i, pos_Y):
        # Verifica que el índice i sea válido
        if i < len(positionX):
            card_rect = pygame.Rect(positionX[i], positionY[pos_Y], card_Width, card_Height)
            self.isfieldCardClicked = card_rect.collidepoint(mouse_Position)
            return self.isfieldCardClicked
        
    def changeBehavior(self):
        Card.selected_card= self
        if(Card.selected_card.behavior==1):
            Card.selected_card.behavior=0
            print("Cambiado a ataque")
        elif(Card.selected_card.behavior==0):
            Card.selected_card.behavior=1
            print("Camdiado a defensa")
        Card.selected_card= None
    def deselect(self):
        self.is_Selected = False
        self.description.hide()
        if Card.selected_card == self:
            Card.selected_card = None
