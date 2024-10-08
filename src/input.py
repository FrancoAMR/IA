import pygame
from card import Card

def handle_input(cards, num_cards, board, events):
    mouse_pos = pygame.mouse.get_pos()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                if Card.selected_card:
                    if board.place_card(mouse_pos, Card.selected_card, is_opponent=False):  
                        if Card.selected_card in cards:
                            cards.remove(Card.selected_card)
                        Card.selected_card = None
                        print(num_cards)
                else:
                    for card in cards[:num_cards]:
                        card.click(mouse_pos)

    #return num_cards
