import pygame
from values import *
from board import Board
from card import Card
from opponent_card import OpponentCard
from endbutton import Endbutton
from input import handle_input
import random

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Window")
        self.screen = pygame.display.set_mode((window_width, window_height))
        self.clock = pygame.time.Clock()

        self.board = Board()
        self.endbutton = Endbutton()
        self.attack_values = [0, 4, 1, 3, 2, 1, 2, 6, 2, 5, 0, 4, 1, 3, 2, 1, 2, 6, 2, 5, 0, 4, 1, 3, 2, 1, 2, 6, 2, 5]
        self.defense_values = [3, 2, 4, 3, 4, 1, 3, 1, 4, 5, 3, 2, 4, 3, 4, 1, 3, 1, 4, 5, 3, 2, 4, 3, 4, 1, 3, 1, 4, 5]
        self.cards = []
        self.fillCards("card")
        
        self.oponent_cards = []
        self.fillCards("opCard")
        
        self.turnState = 0
        self.hand = []
        self.num_cards = len(self.hand)
        self.opHand = []
        self.num_opponent_cards = len(self.opHand)
        self.running = True
        
    def fillCards(self, typeCard):
        if typeCard == "card":
            for i in range(30):
                self.cards.append({
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
                        self.change_state()

                    if Card.selected_card:
                        if self.board.place_card(mouse_pos, Card.selected_card, is_opponent=False):  
                            if Card.selected_card in self.cards:
                                self.cards.remove(Card.selected_card)
                            Card.selected_card = None
                    else:
                        for i in range(self.num_cards):
                            card = Card(
                                index=self.hand[i]["index"],
                                attack_value=self.hand[i]["attack_value"],
                                defense_value=self.hand[i]["defense_value"],
                                state=0
                            )
                            card.click(mouse_pos, i)
    
    def change_state(self):
        match self.turnState:
            case 0:
                self.pickup()
                self.opPickup()         
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
                if self.cards[i]["state"] == 1:
                    continue
                self.hand.append({
                    "index": i,
                    "attack_value": self.attack_values[i],
                    "defense_value": self.defense_values[i],
                    "state": 0
                })
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
            self.num_opponent_cards = len(self.opHand)

    def atk_decision(self):
        return True
                
    def render(self):
        self.screen.fill(background_color)
        mouse_pos = pygame.mouse.get_pos()
        self.board.draw(self.screen)
        self.board.mouse(self.screen, mouse_pos)
        self.endbutton.draw(self.screen, self.turnState)

        for i in range(self.num_cards):
            card = Card(
                index=self.hand[i]["index"],
                attack_value=self.hand[i]["attack_value"],
                defense_value=self.hand[i]["defense_value"],
                state=0
            )
            card.draw(self.screen, i)

        for j in range(self.num_opponent_cards):
            opCard = OpponentCard(
                index=self.opHand[j]["index"],
                attack_value=self.opHand[j]["attack_value"],
                defense_value=self.opHand[j]["defense_value"],
                state=0
            )
            opCard.draw(self.screen, j)

        pygame.display.update()
        self.clock.tick(60)
