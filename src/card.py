import pygame
from values import *
from description import CardDescription

class Card:
    selected_card = None

    def __init__(self, index, attack_Value=0, defense_Value=0, state=0):
        # Campos de la carta
        self.index = index
        self.attack_Value = attack_Value
        self.defense_Value = defense_Value
        self.state= state
        # Estado de seleccion inicializado en falso
        self.is_Selected = False
        # Descripcion de la carta (IMG), probablemente se borre
        self.description = CardDescription()

    #Dibujado de las cartas
    def draw(self, screen, num_Cards, pos_Y):
        if pos_Y==1: #posY indica que se dibujara en el campo
            draw_Y= positionY[pos_Y]
            screen.blit(card_Image, (positionX[num_Cards], draw_Y)) #Dibujado en la pantalla
            self.drawStats(screen, positionX[num_Cards], draw_Y) #Llamada al dibujado de estadisticas
        elif pos_Y==0: #posY indica que se dibujara en la mano
            draw_Y= positionY[pos_Y]-20 if self.is_Selected else positionY[pos_Y] #Ubicacion si es seleccionada o no
            screen.blit(card_Image, (positionX[num_Cards], draw_Y)) #Dibujado en la pantalla
            self.drawStats(screen, positionX[num_Cards], draw_Y) #Llamada al dibujado de estadisticas
    
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
    def click(self, mouse_Position, i):
        # Verifica que el índice i sea válido
        if i < len(positionX):
            card_rect = pygame.Rect(positionX[i], positionY[0], card_Width, card_Height)
            print("Carta numero: ", i)
            if card_rect.collidepoint(mouse_Position):
                if not self.is_Selected:
                    if Card.selected_card:
                        Card.selected_card.deselect()
                    self.is_Selected = True
                    self.description.show()
                    Card.selected_card = self
                else:
                    self.deselect()

    def deselect(self):
        self.is_Selected = False
        self.description.hide()
        if Card.selected_card == self:
            Card.selected_card = None