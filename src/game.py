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
<<<<<<< Updated upstream

    def createCards(self, typeCard):
        attack_values=[0,4,1,3,2,1,2,6,2,5,0,4,1,3,2,1,2,6,2,5,0,4,1,3,2,1,2,6,2,5]
        defense_values=[3,2,4,3,4,1,3,1,4,5,3,2,4,3,4,1,3,1,4,5,3,2,4,3,4,1,3,1,4,5]
        cards= []
        for i in range(30):
            if(typeCard=="card"):
                card= Card(index=i, attack_value=attack_values[i], defense_value=defense_values[i])
            else:
                card= OpponentCard(index=i, attack_value=attack_values[i], defense_value=defense_values[i])
            cards.append(card)
        return cards

=======
>>>>>>> Stashed changes
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Window")
        self.screen = pygame.display.set_mode((window_width, window_height))
        self.clock = pygame.time.Clock()

        self.board = Board()
        self.endbutton = Endbutton()
<<<<<<< Updated upstream
        self.lp = Lp()
        self.opponent_lp = OpponentLp()

        self.cards = self.createCards("card")
        self.opponent_cards = self.createCards("opcard")
        
        self.num_cards = 5
        print(self.num_cards)
        self.num_opponent_cards = 5
        self.running = True
=======
        #self.lp = Lp()
        #self.opponent_lp = OpponentLp()
        self.attack_values=[0,4,1,3,2,1,2,6,2,5,0,4,1,3,2,1,2,6,2,5,0,4,1,3,2,1,2,6,2,5]
        self.defense_values=[3,2,4,3,4,1,3,1,4,5,3,2,4,3,4,1,3,1,4,5,3,2,4,3,4,1,3,1,4,5]
        self.cards={}
        self.fillCards("card")
        cardData= json.dumps(self.cards[1])
        print(cardData)
        data= json.loads(cardData)
        print(data['attack_value'])
        #0= Robo de cartas, 1= Invocacion, 2= Colocacion, 3= Ataque, 4= Calculo de daño, 5= Fin de turno
        #6= ""            , 7= ""        , 8= ""        , 9= ""    , 10= ""            , 11= ""
        self.turnState= 0
        self.hand = {}
        self.num_cards = len(self.hand)
        self.num_opponent_cards = 5
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
            print("TODO")
>>>>>>> Stashed changes

    def run(self):
        while self.running:
            events = pygame.event.get()
            self.events(events)
            self.render()
<<<<<<< Updated upstream

=======
            if(self.turnState==0):
                self.change_state()
    
>>>>>>> Stashed changes
    def events(self, events):
        mouse_pos = pygame.mouse.get_pos()
        self.num_cards = handle_input(self.cards, self.num_cards, self.board, events)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
<<<<<<< Updated upstream
                    if self.endbutton.is_clicked(mouse_pos):
                        self.cpu_turn()
=======
                    if self.endbutton.is_clicked(mouse_pos) and (self.turnState==3 or self.turnState==5):
                        self.change_state()
    
    def change_state(self):
        match self.turnState:
            case 0:
                self.pickup()
                self.turnState = 1
            case 1:
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
        if self.turnState != 0:
            return 0
        else:
            while(len(self.hand)<5):
                i= random.randint(0,29)
                cardData= json.dumps(self.cards[i]["state"])
                while(cardData==1):
                    i= random.randint(0,29)
                    cardData= json.dumps(self.cards[i]["state"])
                j= len(self.hand)
                self.hand[j+1]={
                    "index": i,
                    "attack_value": self.attack_values[i],
                    "defense_value": self.defense_values[i],
                    "state": 0
                }
            for j in range(self.num_cards):
                handData= json.dumps(self.hand[j])
                handData.draw(self.screen, self.num_cards)

    def atk_decision():
        return True
>>>>>>> Stashed changes

    #turn cpu

                
    def render(self):
        self.screen.fill(background_color)
        self.board.draw(self.screen)
<<<<<<< Updated upstream
        self.endbutton.draw(self.screen)
        self.lp.draw(self.screen)
        self.opponent_lp.draw(self.screen)
=======
        self.endbutton.draw(self.screen, self.turnState)

>>>>>>> Stashed changes

        mouse_pos = pygame.mouse.get_pos()
        self.board.mouse(self.screen, mouse_pos)

        for i in range(self.num_cards):
<<<<<<< Updated upstream
            self.cards[i].draw(self.screen, self.num_cards)
=======
            handData= json.dumps(self.hand[i])
            newData= json.loads(handData)
            newDraw= Card(index= newData["index"], attack_value=newData["attack_value"], defense_value=["defense_value"], state=0)
            newDraw.draw(self.screen, self.num_cards)
>>>>>>> Stashed changes
        
#        for i in range(self.num_opponent_cards):
#            self.opponent_cards[i].draw(self.screen, self.num_opponent_cards)

 #       for card in self.cards:
 #           card.description.draw(self.screen)

        pygame.display.update()
        self.clock.tick(60)
