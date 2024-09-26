import pygame
from values import *
from board import Board
from card import Card
from opponent_card import OpponentCard
from endbutton import Endbutton
from lp import Lp
from opponent_lp import OpponentLp
from input import handle_input
import random

class Game:
    def __init__(self):
        #Inicialización de pygame
        pygame.init()
        pygame.display.set_caption("Window")
        self.screen = pygame.display.set_mode((window_width, window_height))
        self.clock = pygame.time.Clock()

        #Variables de objetos
        self.board = Board()
        self.endbutton = Endbutton()
        self.lp = Lp()
        self.op_lp = OpponentLp()

        #Valores de cartas
        self.attack_values = [0, 4, 1, 3, 2, 1, 2, 6, 2, 5, 0, 4, 1, 3, 2, 1, 2, 6, 2, 5, 0, 4, 1, 3, 2, 1, 2, 6, 2, 5]
        self.defense_values = [3, 2, 4, 3, 4, 1, 3, 1, 4, 5, 3, 2, 4, 3, 4, 1, 3, 1, 4, 5, 3, 2, 4, 3, 4, 1, 3, 1, 4, 5]

        # Arrays para las cartas
        self.field_cards = []
        self.deck = []
        self.hand = []
        self.oponent_cards = []

        #Llamado para llenar los mazos
        self.fillCards("card")
        self.fillCards("opCard")

        # Crear la lista caddo, para la mano del usuario (debe eliminarse)
        self.caddo = []
        for i in range(5):
            card = Card(
                index=i,
                attack_value=self.attack_values[i],
                defense_value=self.defense_values[i],
                state=0
            )
            self.caddo.append(card)

        #0= Robo de cartas, 1= Invocacion, 2= Colocacion, 3= Ataque, 4= Calculo de daño, 5= Fin de turno
        #6= ""            , 7= ""        , 8= ""        , 9= ""    , 10= ""            , 11= ""
        self.turnState = 0
        
        self.num_cards = len(self.hand)
        self.opHand = []
        self.num_opponent_cards = len(self.opHand)
        self.size_deck = 30
        self.size_op_deck = 30
        self.running = True

    # Función para llenar los mazos, del usuario y contrincante
    def fillCards(self, typeCard):
        if typeCard == "card":
            for i in range(30):
                self.deck.append({
                    "index": i,
                    "attack_value": self.attack_values[i],
                    "defense_value": self.defense_values[i],
                    "state": 0
                })
        elif typeCard == "opCard":
            for i in range(30):
                self.oponent_cards.append({
                    "index": i,
                    "attack_value": self.attack_values[i],
                    "defense_value": self.defense_values[i],
                    "state": 0
                })

    def run(self):
        while self.running:
            events = pygame.event.get()
            self.events(events)  # Manejo de eventos (clics, movimientos)
            self.render()  # Dibujar los elementos en pantalla
            print("Turno: ",self.turnState)
            if self.turnState in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                self.change_state()

    def events(self, events):
        mouse_pos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    if self.endbutton.is_clicked(mouse_pos) and (self.turnState == 3 or self.turnState == 5):
                        self.turnState = 0

                    if Card.selected_card:
                        if self.board.place_card(mouse_pos, Card.selected_card, is_opponent=False):  
                            if Card.selected_card in self.deck:
                                self.deck.remove(Card.selected_card)
                            Card.selected_card = None
                    else:
                        for i in range(len(self.caddo)):
                            card = self.caddo[i]
                            card.click(mouse_pos, i)
                
    
    def change_state(self):
        match self.turnState:
            case 0:
                self.pickup()
                #self.opPickup()         
                self.turnState = 1
            case 1:
                self.turnState = 2
            case 2:
                self.turnState = 3
            case 4:
                self.turnState = 3
            case 5:
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
        if self.turnState != 0:
            return 0
        else:
            while len(self.hand) < 5:
                i = random.randint(0, 29)
                if self.deck[i]["state"] == 1:
                    continue
                self.hand.append({
                    "index": i,
                    "attack_value": self.attack_values[i],
                    "defense_value": self.defense_values[i],
                    "state": 0
                })
                self.size_deck = self.size_deck-1
            self.num_cards = len(self.hand)

    def opPickup(self):
        if self.turnState != 0:
            return 0
        else:
            while len(self.opHand) < 5:
                i = random.randint(0, 29)
                if self.oponent_cards[i]["state"] == 1:
                    continue
                self.opHand.append({
                    "index": i,
                    "attack_value": self.attack_values[i],
                    "defense_value": self.defense_values[i],
                    "state": 0
                })
                self.size_op_deck = self.size_op_deck-1
            self.num_opponent_cards = len(self.opHand)

    def atk_decision(self):
        return False
                
    def render(self):
        self.screen.fill(background_color)
        mouse_pos = pygame.mouse.get_pos()
        self.board.draw(self.screen)
        self.lp.draw(self.screen)
        self.op_lp.draw(self.screen)
        self.board.mouse(self.screen, mouse_pos)
        self.endbutton.draw(self.screen, self.turnState)

        for i in range(len(self.caddo)):
            card = self.caddo[i]
            card.draw(self.screen, i)
            card.draw_deck(self.screen, self.size_deck)

        for j in range(self.num_opponent_cards):
            opCard = OpponentCard(
                index=self.opHand[j]["index"],
                attack_value=self.opHand[j]["attack_value"],
                defense_value=self.opHand[j]["defense_value"],
                state=0
            )
            opCard.draw(self.screen, j)
            opCard.draw_deck(self.screen, self.size_deck)

        pygame.display.update()
        self.clock.tick(60)
