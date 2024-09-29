class AI:
    def __init__(self, hand, field, opponent_field, lp):
        self.hand = hand
        self.field = field
        self.opponent_field = opponent_field
        self.lp = lp

    def evaluate_hand(self):
        # Evaluar las cartas en la mano para seleccionar la mejor jugada
        best_card = None
        best_score = 0
        for card in self.hand:
            score = self.evaluate_card(card)
            if score > best_score:
                best_card = card
                best_score = score
        return best_card

    def evaluate_card(self, card):
        # Evaluar una carta basándose en el sistema de puntaje
        score = 0
        if card.attack_Value >= 7:
            score += 7  # Ataque alto
        elif card.attack_Value >= 5:
            score += 5  # Ataque medio
        elif card.attack_Value >= 3:
            score += 3  # Ataque bajo
        else:
            score += 0  # Ataque mínimo
        
        if card.defense_Value >= 6:
            score += 6  # Defensa alta
        elif card.defense_Value >= 4:
            score += 4  # Defensa media
        elif card.defense_Value >= 2:
            score += 2  # Defensa baja
        else:
            score += 1  # Defensa mínima

        return score

    def make_move(self):
        # Tomar una decisión de juego basándose en la evaluación del tablero
        if not self.opponent_field:  # Si el oponente no tiene cartas en el campo
            card_to_play = self.evaluate_hand()
            if card_to_play:
                self.play_card(card_to_play)

    def play_card(self, card):
        # Lógica para jugar la carta seleccionada
        self.field.append(card)
        self.hand.remove(card)
        print(f"IA juega la carta con ataque {card.attack_Value} y defensa {card.defense_Value}")

    def attack(self):
        # Lógica de ataque basada en el estado del tablero
        if self.opponent_field:
            for card in self.field:
                best_target = self.select_attack_target()
                if best_target:
                    print(f"IA ataca la carta del oponente con ataque {best_target.attack_Value}")
                    # Lógica de ataque 

    def select_attack_target(self):
        # Elegir la mejor carta para atacar del oponente
        best_target = None
        for opponent_card in self.opponent_field:
            if opponent_card.attack_Value < self.field[0].attack_Value: 
                best_target = opponent_card
                break
        return best_target
