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
        pygame.init()
        pygame.display.set_caption("Window")
        self.screen = pygame.display.set_mode((window_width, window_height))
        self.clock = pygame.time.Clock()

        self.board = Board()
        self.endbutton = Endbutton()
        self.lp = Lp()
        self.opponent_lp = OpponentLp()

        self.cards = self.createCards("card")
        self.opponent_cards = self.createCards("opcard")

        #0= Robo de cartas, 1= Invocacion, 2= Colocacion, 3= Ataque, 4= Calculo de daño, 5= Fin de turno
        self.turnState= 0

        
        self.num_cards = 5
        print(self.num_cards)
        self.num_opponent_cards = 5
        self.running = True

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

    def run(self):
        while self.running:
            events = pygame.event.get()
            self.events(events)
            self.render()

    def events(self, events):
        mouse_pos = pygame.mouse.get_pos()
        self.num_cards = handle_input(self.cards, self.num_cards, self.board, events)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    if self.endbutton.is_clicked(mouse_pos):
                        self.cpu_turn()

    def cpu_turn(self):
        available_cards = [card for card in self.opponent_cards if not card.is_on_board]
        if available_cards:
            card_to_place = random.choice(available_cards)
            empty_rects = [rect for i, rect in enumerate(self.board.rectangles) if not self.board.occupied[i] and self.board.is_first_row(i)]
            if empty_rects:
                rect = random.choice(empty_rects)
                card_to_place.move_to_board(rect)
                self.board.occupied[self.board.rectangles.index(rect)] = True
                Board.card_on_board += 1
                print("Cartas en tablero:", Board.card_on_board)

                
    def render(self):
        self.screen.fill(background_color)
        self.board.draw(self.screen)
        self.endbutton.draw(self.screen)
        self.lp.draw(self.screen)
        self.opponent_lp.draw(self.screen)

        mouse_pos = pygame.mouse.get_pos()
        self.board.mouse(self.screen, mouse_pos)

        for i in range(self.num_cards):
            self.cards[i].draw(self.screen, self.num_cards)
        
        for i in range(self.num_opponent_cards):
            self.opponent_cards[i].draw(self.screen, self.num_opponent_cards)

        for card in self.cards:
            card.description.draw(self.screen)

        pygame.display.update()
        self.clock.tick(60)
