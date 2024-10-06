class AI:

    def __init__(self):
        self.maxAtkScore= 0
        self.maxDefScore= 0
        self.maxAtkPosition= -1
        self.maxDefPosition= -1
        self.score=0

    def restartScores(self):
        self.maxAtkScore= 0
        self.maxDefScore= 0
        self.maxAtkPosition= -1
        self.maxDefPosition= -1
        self.score=0

    def evaluateCardPosition(self):
        if(self.maxAtkScore>self.maxDefScore):
            return self.maxAtkPosition
        else:
            return self.maxDefPosition

    def evaluateCardColocation(self, card):
        if(card.attack_Value>card.defense_Value):
            return 0
        else:
            return 1

    def evaluateCardStats(self, card, position):
        atk_Score= self.evaluateCardAttack(card.attack_Value)
        def_Score= self.evaluateCardDefense(card.defense_Value)
        if(atk_Score>def_Score):
            if(atk_Score>self.maxAtkScore):
                self.maxAtkScore= atk_Score
                self.maxAtkPosition= position
        else:
            if(def_Score>self.maxDefScore):
                self.maxDefScore= def_Score
                self.maxDefPosition= position

    def evaluateCardAttack(self, stat_Value):
        # Evaluar una carta basándose en el sistema de puntaje
        score= 0
        match stat_Value:
            case 0:
                score= score+0
            case 1:
                score= score+2
            case 2:
                score= score+4
            case 3:
                score= score+6
            case 4:
                score= score+8
            case 5:
                score= score+10
            case 6:
                score= score+12
            case 7:
                score= score+14
            case 8:
                score= score+16
            case 9:
                score= score+18
            case 10:
                score= score+20
        return score
    
    def evaluateCardDefense(self, stat_Value):
        # Evaluar una carta basándose en el sistema de puntaje
        score= 0
        match stat_Value:
            case 0:
                score= score+1
            case 1:
                score= score+2
            case 2:
                score= score+3
            case 3:
                score= score+5
            case 4:
                score= score+7
            case 5:
                score= score+9
            case 6:
                score= score+11
            case 7:
                score= score+13
            case 8:
                score= score+15
            case 9:
                score= score+17
        return score


# Busca la carta con menor puntaje del oponente, esta debe atacar a la carta del jugador con mayor puntaje
# posible

    def selectAttacker(self):
        TODO: selectAttacker



    def calculate_game_state(self, player_life, opponent_life, player_cards, opponent_cards):
        # Fórmula del estado del juego S
        S = (player_life - opponent_life) + (len(player_cards) - len(opponent_cards))
        for card in player_cards: #Ataque de la IA
            #Cambiar por valores de ataques
            S += self.evaluateCardAttack(card.attack_Value)
        for card in opponent_cards: #Defensa del jugador
            #Cambiar por valores de defensas
            #Agregar valores de ataques del jugador
            S -= self.evaluateCardDefense(card.defense_Value)
        return S

    def attack(self):
        # Lógica de ataque basada en el estado del tablero
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
    
    def make_move(self, player_life, opponent_life, player_cards, opponent_cards):
            # Selecciona el movimiento basado en el nivel de dificultad
            S = self.calculate_game_state(player_life, opponent_life, player_cards, opponent_cards)

            if self.difficulty_level == "fácil":
                self.random_move()
            elif self.difficulty_level == "intermedio":
                if S > 0:
                    self.aggressive_move()
                else:
                    self.defensive_move()
            elif self.difficulty_level == "difícil":
                self.strategy_move(S)

    def random_move(self):
        # Implementa una lógica de movimiento aleatorio
        print("IA realiza un movimiento aleatorio")

    def aggressive_move(self):
        # Implementa una lógica de movimiento agresivo
        print("IA realiza un movimiento agresivo")

    def defensive_move(self):
        # Implementa una lógica de movimiento defensivo
        print("IA realiza un movimiento defensivo")

    def strategy_move(self, S):
        # Implementa una lógica de movimiento estratégica basada en el estado S
        if S > 10:  
            print("IA realiza un ataque decisivo")
        elif S < -10:
            print("IA se defiende fuertemente")
        else:
            print("IA elige un movimiento equilibrado")