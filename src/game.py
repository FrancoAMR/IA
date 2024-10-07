import pygame
from values import *
from lp import Lp
from opponent_lp import OpponentLp
from board import Board
from card import Card
from opponent_card import OpponentCard
from endbutton import Endbutton
from combat import Combat
from ia import AI
from input import handle_input
from menu import Menu
from restart import Restart
import random
import time

class Game:
    #Inicializacion
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Sombras del duelo")
        self.screen = pygame.display.set_mode((window_Width, window_Height))
        self.clock = pygame.time.Clock()
        self.lp= Lp()
        self.op_Lp = OpponentLp()
        self.board = Board()
        self.endbutton = Endbutton()
        self.combat = Combat()
        self.ia = AI()
        self.menu = Menu()
        self.restart = Restart()
        
        #Valores para las cartas y mazos de ambos jugadores
        self.attack_Values = [0, 4, 6, 6, 2, 1, 2, 6, 2, 5, 0, 4, 1, 3, 2, 1, 2, 6, 2, 5, 0, 4, 1, 3, 2, 1, 2, 6, 2, 5]
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
        self.first_turn = True

        #Selector de dificultad (0: Facil| 1: Medio| 2: Dificil)
        self.difficulty= -1

        #Indices para la busqueda al atacar
        self.temporaryIndex= -1
        self.temporaryOpponentIndex= -1
        #Correr
        self.initialize_flag = True
        self.running= True
        self.restart_Flag= False

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
        while self.initialize_flag:
            
            while self.difficulty == -1:
                events = pygame.event.get()
                self.menu.render(self.screen)
                self.menu.menu_events(events)
                self.difficulty = self.menu.selected_difficulty
                #print("Dificultad seleccionda: ", self.difficulty)
                pygame.display.flip()
                
                
            while self.running==True:
                events= pygame.event.get()
                self.events(events) #Manejo de eventos (clicks y movimientos)
                self.render() #Dibuja los elementos en la pantalla
                self.lp.loss()
                self.running = self.lp.loss_Flag
                if self.turn_State in [0,1,2,3,4,5]:
                    self.changeState()
                
            while not self.restart_Flag:
                events= pygame.event.get()
                self.restart.render(self.screen)
                self.restart.restart_events(events)
                
                self.restart_Flag = self.restart.select_restart
                pygame.display.flip()
                
                
            if(self.restart_Flag):
                
                self.reset_game()
                self.board.restart_board()
                self.lp.restart_lp()
                self.op_Lp.restart_op_lp()
            else:
                self.initialize_flag = False

    def reset_game(self):
        
        # Reiniciar el mazo y la mano de los jugadores
        self.difficulty = -1
        self.running= True
        self.restart.select_restart = False
        self.restart_Flag = False
        
        self.lp.loss_Flag = True
        self.menu.selected_difficulty = -1
        
        self.player_Deck = []
        self.opponent_Deck = []
        self.fillCards(0)
        self.fillCards(1)
        
        self.player_Hand = []
        self.opponent_Hand = []
        self.player_Field = []
        self.opponent_Field = []
        
        # Reiniciar los turnos y estados
        self.active_Turn = 0
        self.turn_State = 0
        self.first_turn = True
        
        # Reiniciar la dificultad y selección
        self.difficulty = -1
        self.temporaryIndex = -1
        self.temporaryOpponentIndex = -1
        
        # Reiniciar indicadores de fin de juego
        self.running = True
        self.restart_Flag = False
        self.lp.loss_Flag = True
        self.menu.selected_difficulty = -1

        

    #Funcion para el tratamiento de eventos
    def events(self, events):
        mouse_Position= pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button ==1:
                    if self.active_Turn==1:
                        match self.turn_State:
                            case 1:
                                if self.endbutton.isClicked(mouse_Position):
                                    self.returnState()
                                    self.changeState(True)
                                    Card.selected_card= None
                                    self.first_turn= False
                                else:
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
                                    #----
                                    for i in range(len(self.player_Field)):
                                        for j in range(len(self.board.cards_Board)):
                                            if (self.player_Field[i].index==self.board.cards_Board[j].index):
                                                fieldPosition= self.board.cards_Board[j].board_Position
                                    #---Algoritmo de búsqueda de carta (TODO: Hacerla función)
                                                if self.player_Field[i].fieldClick(mouse_Position, fieldPosition, 1):
                                                    self.player_Field[i].changeBehavior()
                                                    self.board.cards_Board[j].behavior=self.player_Field[i].behavior
                                                    break
                            case 3:
                                if self.endbutton.isClicked(mouse_Position):
                                    self.returnState()
                                    self.changeState(True)
                                    Card.selected_card= None
                                    self.first_turn= False
                                else:
                                    if Card.selected_card:
                                        result= -1
                                        if Card.selected_card.behavior==0:
                                            if len(self.opponent_Field) == 0:
                                                self.combat.resolve(Card.selected_card, None, self.lp, self.op_Lp)
                                                found = True
                                            else:
                                                found= False
                                                for k in range(len(self.opponent_Field)):
                                                    for l in range(len(self.board.opponent_Cards_Board)):
                                                        if (self.opponent_Field[k].index==self.board.opponent_Cards_Board[l].index):
                                                            attackedPosition= self.board.opponent_Cards_Board[l].board_Position
                                                            if self.opponent_Field[k].fieldClick(mouse_Position, (attackedPosition-5), 2):
                                                                result= self.combat.resolve(Card.selected_card, self.opponent_Field[k], self.lp, self.op_Lp)
                                                                self.temporaryOpponentIndex=self.opponent_Field[k].index
                                                                self.declareResult(result)
                                                                found= True
                                                                break
                                                    if(found==True):
                                                        break
                                            Card.selected_card=None
                                    else:
                                        found=False
                                        for i in range(len(self.player_Field)):
                                            for j in range(len(self.board.cards_Board)):
                                                if (self.player_Field[i].index==self.board.cards_Board[j].index):
                                                    fieldPosition= self.board.cards_Board[j].board_Position
                                        #---Algoritmo de búsqueda de carta (TODO: Hacerla función)
                                                    if self.player_Field[i].fieldClick(mouse_Position, fieldPosition, 1):
                                                        self.player_Field[i].click(mouse_Position, fieldPosition, 1)
                                                        self.temporaryIndex= self.player_Field[i].index
                                                        found=True
                                                        break
                                            if(found==True):
                                                break         
                    elif self.active_Turn==2:
                        self.aiTurn()


    #------------------------------Funcionamiento del jugador----------------------------------------



    #------------------------------Fin del funcionamiento del jugador--------------------------------
    
    #------------------------------Funcionamiento de la IA-------------------------------------------
    #Definicion del turno del oponente
    def aiTurn(self):
        if(len(self.opponent_Field)<5):
            self.opponentInvocation()
        self.changeState(True)
        self.opponentColocation()
        self.changeState(True)
        temporalCardsOnField= len(self.opponent_Field)
        for i in range(temporalCardsOnField):
            self.opponentAttack()
        self.returnAIState()
        self.changeState(True)
        
    def opponentInvocation(self):
        self.ia.restartScores()
        match self.difficulty:
            case 0:
                newPosition= random.randint(0,(len(self.opponent_Hand)-1))
                if self.board.opponentPlaceCard(self.opponent_Hand[newPosition]):
                    self.moveCard(self.opponent_Hand, self.opponent_Field, self.opponent_Hand[newPosition])
            case 1:
                for i in range(len(self.opponent_Hand)):
                    self.ia.evaluateCardStats(self.opponent_Hand[i], i)
                newPosition= self.ia.evaluateCardPosition()
                if self.board.opponentPlaceCard(self.opponent_Hand[newPosition]):
                    self.moveCard(self.opponent_Hand, self.opponent_Field, self.opponent_Hand[newPosition])
            case 2:
                TODO: ComplexInvocation

    def opponentColocation(self):
        match self.difficulty:
            case 0:
                print("Cartas siempre en ataque en facil.")
            case 1:
                for i in range(len(self.opponent_Field)):
                    self.opponent_Field[i].behavior= self.ia.evaluateCardColocation(self.opponent_Field[i])
                    self.board.opponent_Cards_Board[i].behavior= self.opponent_Field[i].behavior
            case 2:
                TODO: ComplexColocation

    def opponentAttack(self):
        match self.difficulty:
            case 0:
                self.attackDecisionEasy()
            case 1:
                self.determineAttacksMedium()
            case 2:
                TODO: attackDecisionHard()

    def attackDecisionEasy(self):
        attack_Succesful= False
        for i in range(len(self.opponent_Field)):
            if(self.opponent_Field[i].behavior==0):
                if (len(self.player_Field)==0):
                    self.combat.resolve(self.opponent_Field[i], None, self.op_Lp, self.lp)
                else:
                    for j in range(len(self.player_Field)):
                        match self.player_Field[j].behavior:
                            case 0:
                                if(self.opponent_Field[i].attack_Value>self.player_Field[j].attack_Value):
                                    self.temporaryOpponentIndex= self.opponent_Field[i].index
                                    self.temporaryIndex= self.player_Field[j].index
                                    result= self.combat.resolve(self.opponent_Field[i], self.player_Field[j], self.op_Lp, self.lp)
                                    self.declareResult(result)
                                    attack_Succesful= True
                            case 1:
                                if(self.opponent_Field[i].attack_Value>self.player_Field[j].defense_Value):
                                    self.temporaryOpponentIndex= self.opponent_Field[i].index
                                    self.temporaryIndex= self.player_Field[j].index
                                    result= self.combat.resolve(self.opponent_Field[i], self.player_Field[j], self.op_Lp, self.lp)
                                    self.declareResult(result)
                                    attack_Succesful= True
                        if(attack_Succesful==True):
                            attack_Succesful=False
                            break

    def determineAttacksMedium(self):
        sorted_Opponent_Cards= sorted(self.opponent_Field, key=lambda card: card.attack_Value)
        self.attackDecisionMedium(sorted_Opponent_Cards)

    def attackDecisionMedium(self, sorted_Cards):
        attack_Succesful= False
        for i in range(len(sorted_Cards)):
            if(sorted_Cards[i].behavior==0):
                if (len(self.player_Field)==0):
                    self.combat.resolve(sorted_Cards[i], None, self.op_Lp, self.lp)
                else:
                    temporary_Array_Index= -1
                    maximumAttacked= -1
                    for j in range(len(self.player_Field)):
                        match self.player_Field[j].behavior:
                            case 0:
                                if(sorted_Cards[i].attack_Value>self.player_Field[j].attack_Value):
                                    if(self.player_Field[j].attack_Value>maximumAttacked):
                                        maximumAttacked= self.player_Field[j].attack_Value
                                        temporary_Array_Index= j
                            case 1:
                                if(sorted_Cards[i].attack_Value>self.player_Field[j].defense_Value):
                                    if(self.player_Field[j].defense_Value>maximumAttacked):
                                        maximumAttacked= self.player_Field[j].defense_Value
                                        temporary_Array_Index= j
                    if(maximumAttacked!=-1):
                        self.temporaryOpponentIndex= sorted_Cards[i].index
                        self.temporaryIndex= self.player_Field[temporary_Array_Index].index
                        result= self.combat.resolve(sorted_Cards[i], self.player_Field[temporary_Array_Index], self.op_Lp, self.lp)
                        self.declareResult(result)
                        attack_Succesful= True
                    if(attack_Succesful):
                        attack_Succesful= False
                        break

    def returnAIState(self):
        for i in range(len(self.opponent_Field)):
            self.opponent_Field[i].state=0

    #-------------------------------Fin del funcionamiento de la IA-----------------------------------

    def declareResult(self, result):
        match result:
            case 1: #Destruccion del atacado
                if(self.active_Turn==1):
                    self.destroyOpponentCard()
                elif(self.active_Turn==2):
                    self.destroyPlayerCard()
            case 2: #Destruccion del atacante
                if(self.active_Turn==1):
                    self.destroyPlayerCard()
                elif(self.active_Turn==2):
                    self.destroyOpponentCard
            case 3:
                self.destroyOpponentCard()
                self.destroyPlayerCard()
        self.temporaryIndex=-1
        self.temporaryOpponentIndex=-1

    def destroyOpponentCard(self):
        for i in range(len(self.board.opponent_Cards_Board)):
            if self.temporaryOpponentIndex== self.board.opponent_Cards_Board[i].index:
                self.board.remove_card(self.board.opponent_Cards_Board[i])
                self.board.opponent_Cards_Board.pop(i)
                self.board.opponent_Card_On_Board= self.board.opponent_Card_On_Board-1
                break
        for j in range(len(self.opponent_Field)):
            if self.temporaryOpponentIndex== self.opponent_Field[j].index:
                self.opponent_Field.pop(j)
                break

    def destroyPlayerCard(self):
        for i in range(len(self.board.cards_Board)):
            print("Valor de i: ", i)
            if self.temporaryIndex== self.board.cards_Board[i].index:
                self.board.remove_card(self.board.cards_Board[i])
                self.board.cards_Board.pop(i)
                self.board.card_on_board= self.board.card_on_board-1
                break
        for j in range(len(self.player_Field)):
            if self.temporaryIndex== self.player_Field[j].index:
                self.player_Field.pop(j)
                break

    def returnState(self):
        for i in range(len(self.player_Field)):
            self.player_Field[i].state=0

    #Cambios de estado
    def changeState(self, isTrue= False):
        #Encendido del juego
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
                if(isTrue==True):
                    self.turn_State= 4
            case 4:
                self.changeActivePlayer()
                if self.active_Turn==1:
                    print("Turno cambiado al del jugador")
                elif self.active_Turn==2:
                    print("Turno cambiado al de la IA")
                self.turn_State= 0
        
                

    # Cambiar de jugador
    def changeActivePlayer(self):
        match self.active_Turn:
            case 1:
                self.active_Turn= 2
            case 2:
                self.active_Turn= 1
    
    # Robo del mazo a la mano
    def pickup(self):
        match self.active_Turn:
            case 0: #Llenado de la mano del jugador y la IA
                self.opponentPickup()
                self.playerPickup()
            case 1: # Llenado unicamente de la mano del jugador
                self.playerPickup()
            case 2: #Llenado unicamente de la mano de la IA
                self.opponentPickup()
    
    def playerPickup(self):
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

    def opponentPickup(self):
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

    # Pasar de la mano al campo
    def moveCard(self, sender, receiver, card):
        card.is_Selected= False
        receiver.append(card)
        sender.remove(card)
    
    # Funcion de renderizado
    def render(self):
        self.screen.fill(background_Color)
        self.screen.blit(background_Image, (0,0))
        mouse_pos = pygame.mouse.get_pos()
        self.board.draw(self.screen)
        self.board.mouse(self.screen, mouse_pos)
        self.endbutton.draw(self.screen, self.turn_State,self.active_Turn)
        self.lp.draw(self.screen)
        self.op_Lp.draw(self.screen)
        # Dibujado de las cartas de la mano
        for i in range(len(self.player_Hand)):
            self.player_Hand[i].draw(self.screen, i, 0, 0)
        for j in range(len(self.opponent_Hand)):
            self.opponent_Hand[j].draw(self.screen, j, 3, 0)
        #Dibujado de las cartas del campo
        for card in self.player_Field:
            if card.board_Position is not None:
                pos_x = self.board.rectangles[card.board_Position].x #Obtener la posicion de la hitbox en la que se coloca la carta
                new_X= self.defineX(pos_x) #Buscar la posicion en el array de ubicaciones de X
                card.draw(self.screen, new_X, 1, card.behavior)    # Dibujar la carta de acuerdo a la informacion obtenida
        for opponentCard in self.opponent_Field:
            if opponentCard.board_Position is not None:
                    pos_x = self.board.rectangles[opponentCard.board_Position].x #Obtener la posicion de la hitbox en la que se coloca la carta
                    new_X= self.defineX(pos_x) #Buscar la posicion en el array de ubicaciones de X
                    opponentCard.draw(self.screen, new_X, 2, opponentCard.behavior)    # Dibujar la carta de acuerdo a la informacion obtenida
        pygame.display.update()
        self.clock.tick(60)

    def defineX(self, pos_x):
        for i in range(5):
            if pos_x== positionX[i]:
                return i
        

        