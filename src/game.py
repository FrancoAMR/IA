import pygame
from values import *
from board import Board
from card import Card
from opponent_card import OpponentCard
from endbutton import Endbutton
#from lp import LP
from input import handle_input
import random
import json

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Window")
        self.screen = pygame.display.set_mode((window_width, window_height))
        self.clock = pygame.time.Clock()

        self.board = Board()
        self.endbutton = Endbutton()
        #self.lp = Lp()
        #self.opponent_lp = OpponentLp()
        self.attack_values=[0,4,1,3,2,1,2,6,2,5,0,4,1,3,2,1,2,6,2,5,0,4,1,3,2,1,2,6,2,5]
        self.defense_values=[3,2,4,3,4,1,3,1,4,5,3,2,4,3,4,1,3,1,4,5,3,2,4,3,4,1,3,1,4,5]
        self.cards={}
        self.fillCards("card")
        #cardData= json.dumps(self.cards[1])
        #print(cardData)
        #data= json.loads(cardData)
        #print(data['attack_value'])
        
        self.oponent_cards={}
        self.fillCards("opCard")
        
        #0= Robo de cartas, 1= Invocacion, 2= Colocacion, 3= Ataque, 4= Calculo de daño, 5= Fin de turno
        #6= ""            , 7= ""        , 8= ""        , 9= ""    , 10= ""            , 11= ""
        self.turnState= 0
        self.hand = {}
        self.num_cards = len(self.hand)
        self.opHand= {}
        self.num_opponent_cards = len(self.opHand)
        self.running = True
        
    
    def fillCards(self, typeCard):
        if(typeCard=="card"):
            for i in range(30):
                self.cards[i] = {
                    "index": i,
                    "attack_value": self.attack_values[i],
                    "defense_value": self.defense_values[i],
                    "state": 0
                }
        elif (typeCard=="opCard"):
            for i in range(30):
                self.oponent_cards[i] = {
                    "index": i,
                    "attack_value": self.attack_values[i],
                    "defense_value": self.defense_values[i],
                    "state": 0
                }

    def run(self):
        while self.running:
            events = pygame.event.get()
            self.events(events)  # Manejo de eventos (clics, movimientos)
            self.render()  # Dibujar los elementos en pantalla

            # Manejar el cambio de estado si es necesario
            if self.turnState in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                self.change_state()


    
    def events(self, events):
        mouse_pos = pygame.mouse.get_pos()
        #handle_input(self.cards, self.num_cards, self.board, events)
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    if self.endbutton.is_clicked(mouse_pos) and (self.turnState==3 or self.turnState==5):
                        self.change_state()



                    if Card.selected_card:
                        if self.board.place_card(mouse_pos, Card.selected_card, is_opponent=False):  
                            if Card.selected_card in self.cards:
                                self.cards.remove(Card.selected_card)
                            Card.selected_card = None
                            print(self.num_cards)
                    else:
                        for i in range(self.num_cards):
                            handData = json.dumps(self.hand[i])
                            newData = json.loads(handData)
                            card = Card(index=newData["index"], attack_value=newData["attack_value"], defense_value=newData["defense_value"], state=0)

                            print("Seleccionó")
                            card.click(mouse_pos, i)
                    
    
    def change_state(self):
        match self.turnState:
            case 0:
                print("Pickup0")
                self.pickup()                
                self.turnState = 1
            case 1:
                print("El juego entra en el segundo estado")
                self.turnState = 2
            case 2:
                self.turnState = 3
            case 3:
                if self.atk_decision():
                    self.turnState = 4
                else:
                    self.turnState = 5
            case 4:
                self.turnState = 3
            #-----
            case 5:
                print("Pickup1")
                self.opPickup()
                self.turnState = 6
            case 6:
                self.turnState = 7
            case 7:
                self.turnState = 8
            case 8:
                if self.atk_decision():
                    self.turnState = 9
                else:
                    self.turnState = 0
    
    def pickup(self):
        print("Pickup3")
        if self.turnState != 0:
            print("Pickup4")
            return 0
        else:
            print("Pickup5")
            while(len(self.hand) < 5):
                print("Pickup6")
                i = random.randint(0, 29)
                cardData = int(json.dumps(self.cards[i]["state"]))
                print(cardData)
                while(cardData == 1):
                    print("Pickup7")
                    i = random.randint(0, 29)
                    cardData = int(json.dumps(self.cards[i]["state"]))
                j = len(self.hand)
                print(j)
                self.hand[j] = {
                    "index": i,
                    "attack_value": self.attack_values[i],
                    "defense_value": self.defense_values[i],
                    "state": 0
                }
            self.num_cards = len(self.hand)  # Actualizamos el número de cartas en la mano

    def opPickup(self):
        if self.turnState!=0:
            return 0
        else:
            print("Dibujó")
            while(len(self.opHand) < 5):
                print("Pickup6")
                i = random.randint(0, 29)
                cardData = int(json.dumps(self.oponent_cards[i]["state"]))
                print(cardData)
                while(cardData == 1):
                    print("Pickup7")
                    i = random.randint(0, 29)
                    cardData = int(json.dumps(self.oponent_cards[i]["state"]))
                j = len(self.opHand)
                print(j)
                self.opHand[j] = {
                    "index": i,
                    "attack_value": self.attack_values[i],
                    "defense_value": self.defense_values[i],
                    "state": 0
                }
            self.num_opponent_cards = len(self.opHand)  # Actualizamos el número de cartas en la mano

    def atk_decision(self):
        return True

    #turn cpu

                
    def render(self):
        # Limpiar la pantalla
        self.screen.fill(background_color)

        # Dibujar el tablero y el botón de fin de turno
        self.board.draw(self.screen)
        self.endbutton.draw(self.screen, self.turnState)

        # Dibujar las cartas en la mano
        for i in range(self.num_cards):
            handData = json.dumps(self.hand[i])
            newData = json.loads(handData)
            newDraw = Card(index=newData["index"], attack_value=newData["attack_value"], defense_value=newData["defense_value"], state=0)
            newDraw.draw(self.screen, i)
        
        #self.cards = [Card(i) for i in range(5)]
        for j in range(self.num_opponent_cards):
            opHandData = json.dumps(self.opHand[j])
            newOpData = json.loads(opHandData)
            newOpDraw = OpponentCard(index=newOpData["index"], attack_value=newOpData["attack_value"], defense_value=newOpData["defense_value"], state=0)
            newOpDraw.draw(self.screen, j)

        pygame.display.update()
        self.clock.tick(60)
