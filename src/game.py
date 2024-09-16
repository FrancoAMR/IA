import pygame
from values import *
from board import Board
from card import Card
from opponent_card import OpponentCard
from input import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Window")
        self.screen = pygame.display.set_mode((window_width, window_height))
        self.clock = pygame.time.Clock()


        self.board = Board()
        self.cards = [Card(i) for i in range(5)]
        self.opponent_cards = [OpponentCard(i) for i in range(5)]
        self.num_cards = 5
        print(self.num_cards)
        self.num_opponent_cards = 5
        self.running = True

    def run(self):
        while self.running:
            events = pygame.event.get()
            self.events(events)
            self.render()

    def events(self, events):
        self.num_cards = handle_input(self.cards, self.num_cards, self.board, events) 
        

    def render(self):
        self.screen.fill(background_color)
        self.board.draw(self.screen)


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
