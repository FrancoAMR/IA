import pygame
from values import *
from lp import Lp
from board import Board
from card import Card
from opponent_card import OpponentCard
from endbutton import Endbutton
from input import handle_input
import random

class Game:
    #Inicializacion
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Window")
        self.screen = pygame.display.set_mode((window_Width, window_Height))
        self.clock = pygame.time.Clock()
        self.lp= Lp()
        self.board = Board()
        self.endbutton = Endbutton()
        
        #Valores para las cartas y mazos de ambos jugadores
        self.attack_Values = [0, 4, 1, 3, 2, 1, 2, 6, 2, 5, 0, 4, 1, 3, 2, 1, 2, 6, 2, 5, 0, 4, 1, 3, 2, 1, 2, 6, 2, 5]
        self.defense_Values = [3, 2, 4, 3, 4, 1, 3, 1, 4, 5, 3, 2, 4, 3, 4, 1, 3, 1, 4, 5, 3, 2, 4, 3, 4, 1, 3, 1, 4, 5]
        self.player_Deck= []
        self.opponent_Deck= []

        #Llenado de los mazos con los valores designados
        self.fillCards(0)
        self.fillCards(1)

        #Manos y campos de ambos jugadores
        self.player_Hand= []
        self.opponent_Hand= []
        self.player_Field= []
        self.opponent_Field= []

        #Manejo de turnos (0: Inicio| 1: Jugador| 2: IA)
        self.active_Turn= 0

        #Manejo de estados del turno (0: Robo de cartas| 1: Invocacion| 2: Posicionamiento| 3: Ataque
        #                             4: Calculo de daño| 5: Fin de turno)
        self.turn_State= 0

        #Correr
        self.running= True

    # Llenado del mazo
    def fillCards(self, typeCard):
        match typeCard:
            case 0: #Las cartas del jugador
                for i in range(len(self.attack_Values)):
                    deck_Card= Card(
                        index=i,
                        attack_Value=self.attack_Values[i],
                        defense_Value=self.defense_Values[i],
                        state=0,
                        behavior= 0
                    )
                    self.player_Deck.append(deck_Card)
            case 1: #Las cartas de la IA
                for i in range(len(self.attack_Values)):
                    op_deck_Card= OpponentCard(
                        index=i,
                        attack_Value=self.attack_Values[i],
                        defense_Value=self.defense_Values[i],
                        state=0,
                        behavior= 0
                    )
                    self.opponent_Deck.append(op_deck_Card)

    #Funcion para correr el juego
    def run(self):
        while self.running:
            events= pygame.event.get()
            self.events(events) #Manejo de eventos (clicks y movimientos)
            self.render() #Dibuja los elementos en la pantalla
            if self.turn_State in [0,1,2,3,4,5]:
                self.changeState()

    #Funcion para el tratamiento de eventos
    def events(self, events):
        mouse_Position= pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button ==1:
                    match self.turn_State:
                        case 1:
                            # La carta ha sido seleccionada
                            if Card.selected_card:
                                # Se detecta que se intenta colocar en el campo
                                if self.board.placeCard(mouse_Position, Card.selected_card, is_Opponent=False):  
                                    if Card.selected_card in self.player_Hand:
                                        self.moveCard(self.player_Hand, self.player_Field, Card.selected_card)
                                    Card.selected_card = None
                                    self.changeState(True)
                                # Se reinicia la busqueda al darle a otra carta
                                else:
                                    for i in range(len(self.player_Hand)):
                                        self.player_Hand[i].click(mouse_Position, i, 0)
                            # Se espera a que se seleccione
                            else:
                                #Se crea una instancia para todas las cartas y asi decidir cual se utiliza
                                for i in range(len(self.player_Hand)):
                                    self.player_Hand[i].click(mouse_Position, i, 0)
                                     
                        case 2:
                            if self.endbutton.isClicked(mouse_Position):
                                self.changeState(True)
                            else:
                                for i in range(len(self.player_Field)):
                                    for j in range(len(self.board.cards_Board)):
                                        if (self.player_Field[i].index==self.board.cards_Board[j].index):
                                            fieldPosition= self.board.cards_Board[j].board_Position
                                            self.player_Field[i].fieldClick(mouse_Position, fieldPosition, 1)
                                            self.board.cards_Board[j].behavior=self.player_Field[i].behavior
                                            break
                        case 3:
                            TODO: cardBattle
                            if self.endbutton.isClicked(mouse_Position):
                                self.changeState(True)
                        case 4:
                            TODO: damageStep
                        case 5:
                            if self.endbutton.isClicked(mouse_Position):
                                self.changeState(True)
                    
                    
    
    #Cambios de estado
    def changeState(self, isTrue= False):
        if self.active_Turn==0:
            self.pickup()
            self.active_Turn=1
        match self.turn_State:
            case 0:
                self.pickup()
                self.turn_State= 1
                print("Cambio a fase de invocacion")
            case 1:
                if(isTrue==True):
                    self.turn_State= 2
                    print("Cambio a fase de posicion")
                    Card.selected_card=None
            case 2:
                if(isTrue==True):
                        self.turn_State= 3
                        print("Cambio a fase de ataque")
            case 3:
                TODO: ChangePosition
                TODO: Attack
                if(isTrue==True):
                    self.turn_State= 3
            case 4:
                TODO: DamageStep
                if(isTrue==True):
                    self.turn_State= 4
            case 5:
                self.changeActivePlayer()
                self.turn_State= 0
                

    # Cambiar de jugador
    def changeActivePlayer(self):
        match self.active_Turn:
            case 1:
                print("Cambiando de jugador a IA")
                self.active_Turn= 2
                print("Jugador activo: IA: ", self.active_Turn)
            case 2:
                print("Cambiando de IA a jugador")
                self.active_Turn= 1
                print("Jugador activo: Jugador: ", self.active_Turn)
    
    # Robo del mazo a la mano
    def pickup(self):
        match self.active_Turn:
            case 0: #Llenado de la mano del jugador y la IA
                while len(self.player_Hand)<5:
                    i= random.randint(0,len(self.player_Deck)-1)
                    if(self.player_Deck[i].state== 0):
                        new_Hand_Card= Card(
                            index= i,
                            attack_Value= self.attack_Values[i],
                            defense_Value= self.defense_Values[i],
                            state= 0,
                            behavior=0
                        )
                        self.player_Hand.append(new_Hand_Card)
                        self.player_Deck[i].state= -1
                        
                while len(self.opponent_Hand)<5:
                    i= random.randint(0,len(self.player_Deck)-1)
                    if(self.opponent_Deck[i].state== 0):
                        new_Hand_Card= OpponentCard(
                            index= i,
                            attack_Value= self.attack_Values[i],
                            defense_Value= self.defense_Values[i],
                            state= 0,
                            behavior= 0
                        )
                        self.opponent_Hand.append(new_Hand_Card)
                        self.opponent_Deck[i].state= -1
            case 1: # Llenado unicamente de la mano del jugador
                while len(self.player_Hand)<5:
                    i= random.randint(0,len(self.player_Deck)-1)
                    if(self.player_Deck[i].state== 0):
                        new_Hand_Card= Card(
                            index= i,
                            attack_Value= self.attack_Values[i],
                            defense_Value= self.defense_Values[i],
                            state= 0,
                            behavior= 0
                        )
                        self.player_Hand.append(new_Hand_Card)
                        self.player_Deck[i].state= -1
            case 2: #Llenado unicamente de la mano de la IA
                while len(self.opponent_Hand)<5:
                    i= random.randint(0,len(self.player_Deck)-1)
                    if(self.opponent_Deck[i].state== 0):
                        new_Hand_Card= OpponentCard(
                            index= i,
                            attack_Value= self.attack_Values[i],
                            defense_Value= self.defense_Values[i],
                            state= 0,
                            behavior= 0
                        )
                        self.opponent_Hand.append(new_Hand_Card)
                        self.opponent_Deck[i].state= -1
    
    # Pasar de hand a board
    def moveCard(self, sender, receiver, card):
        card.is_Selected= False
        receiver.append(card)
        sender.remove(card)

    # Attack decision(?)
    def atkDecision(self):
        return True
    
    # Funcion de renderizado
    def render(self):
        self.screen.fill(background_Color)
        mouse_pos = pygame.mouse.get_pos()
        self.board.draw(self.screen)
        self.board.mouse(self.screen, mouse_pos)
        self.endbutton.draw(self.screen, self.turn_State)
        self.lp.draw(self.screen)
        # Dibujado de las cartas de la mano
        for i in range(len(self.player_Hand)):
            self.player_Hand[i].draw(self.screen, i, 0)
        for j in range(len(self.opponent_Hand)):
            self.opponent_Hand[j].draw(self.screen, j, 3)
        #Dibujado de las cartas del campo
        for card in self.player_Field:
            if card.board_Position is not None:
                pos_x = self.board.rectangles[card.board_Position].x #Obtener la posicion de la hitbox en la que se coloca la carta
                new_X= self.defineX(pos_x) #Buscar la posicion en el array de ubicaciones de X
                card.draw(self.screen, new_X, 1)    # Dibujar la carta de acuerdo a la informacion obtenida
        for l in range(len(self.opponent_Field)):
            self.opponent_Field[l].draw(self.screen, l)
        pygame.display.update()
        self.clock.tick(60)

    def defineX(self, pos_x):
        for i in range(5):
            if pos_x== positionX[i]:
                return i