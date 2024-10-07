class AI:

    def __init__(self):
        self.maxAtkScore= 0
        self.maxDefScore= 0
        self.maxAtkValue= 0
        self.maxDefValue= 0
        self.maxAtkPosition= -1
        self.maxDefPosition= -1
        self.minAtkScore= 99
        self.minDefScore= 99
        self.minAtkValue= 99
        self.minDefValue= 99
        self.minAtkPosition= -1
        self.minDefPosition= -1
        self.score=0

    def restartScores(self):
        self.maxAtkScore= 0
        self.maxDefScore= 0
        self.maxAtkValue= 0
        self.maxDefValue= 0
        self.maxAtkPosition= -1
        self.maxDefPosition= -1
        self.minAtkScore= 99
        self.minDefScore= 99
        self.minAtkValue= 99
        self.minDefValue= 99
        self.minAtkPosition= -1
        self.minDefPosition= -1
        self.score=0

    def evaluateCardPosition(self):
        if(self.maxAtkScore>self.maxDefScore):
            return self.maxAtkPosition
        else:
            return self.maxDefPosition

    def evaluateCardPositionHard(self):
        if(self.maxDefScore>=self.maxAtkScore and self.maxAtkScore>=self.minDefScore):
            return self.maxDefPosition
        elif(self.maxDefScore>self.minDefScore and self.minDefScore>=self.maxAtkScore):
            return self.maxDefPosition
        elif(self.maxAtkScore>self.maxDefScore and self.maxDefScore>=self.minDefScore):
            return self.maxAtkPosition
        elif(self.maxAtkScore>self.minDefScore and self.minDefScore>=self.maxDefScore):
            return self.maxAtkPosition
        elif(self.minDefScore>=self.maxAtkScore and self.maxAtkScore>=self.maxDefScore):
            return self.minDefPosition
        elif(self.minDefScore>=self.maxDefScore and self.maxDefScore>=self.maxAtkScore):
            return self.minDefPosition            


    def evaluateCardColocation(self, card):
        if(card.attack_Value>=card.defense_Value):
            return 0
        else:
            return 1
        
    def evaluateCardColocationHard(self, card):
        if(card.attack_Value>=card.defense_Value):
            if(card.defense_Value==self.minDefValue and card.attack_Value== self.minAtkValue):
                return 1
            else:
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

    def evaluateCardStatsHard(self, card, position, decision):
        atk_Score= self.evaluateCardAttack(card.attack_Value)
        def_Score= self.evaluateCardDefense(card.defense_Value)
        match decision:
            case 0:
                atk_Score= atk_Score+2
            case 1:
                def_Score= def_Score+2
            case 2:
                atk_Score= atk_Score
                def_Score= def_Score
        if(atk_Score>def_Score):
            if(atk_Score>=self.maxAtkScore):
                self.maxAtkScore= atk_Score
                self.maxAtkPosition= position
                self.maxAtkValue= card.attack_Value
            elif(atk_Score<self.minAtkScore):
                self.minAtkScore= atk_Score
                self.minAtkPosition= position
                self.minAtkValue= card.attack_Value
        else:
            if(def_Score>=self.maxDefScore):
                self.maxDefScore= def_Score
                self.maxDefPosition= position
                self.maxDefValue= card.defense_Value
            elif(def_Score<self.minDefScore):
                self.minDefScore= def_Score
                self.minDefPosition= position
                self.minDefValue= card.defense_Value

    def comparePlayerCard(self, playerCard):
        if (playerCard.attack_Value>self.maxAtkValue):
            self.minDefScore= self.minDefScore+10
        elif(playerCard.defense_Value>self.maxAtkValue):
            self.maxAtkScore= self.maxAtkScore+1
            self.maxDefScore= self.maxDefScore+1
        elif(playerCard.attack_Value<self.maxAtkValue):
            self.maxAtkScore= self.maxAtkScore+10
        elif(playerCard.defense_Value<self.maxAtkValue):
            self.maxAtkScore= self.maxAtkScore+10


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

    def calculate_game_state(self, ia_LP, player_LP, ia_Field, player_Field):
        # Fórmula del estado del juego S
        S = (ia_LP - player_LP) + (len(ia_Field) - len(player_Field))
        for card in ia_Field: #Ataque de la IA
            #Cambiar por valores de ataques
            S += card.attack_Value
        for card in player_Field: #Defensa del jugador
            #Cambiar por valores de defensas
            #Agregar valores de ataques del jugador
            if(card.behavior==0):
                S -= card.attack_Value
            if(card.behavior==1):
                S -= card.defense_Value
        return S

    def select_attack_target(self):
        # Elegir la mejor carta para atacar del oponente
        best_target = None
        for opponent_card in self.opponent_field:
            if opponent_card.attack_Value < self.field[0].attack_Value: 
                best_target = opponent_card
                break
        return best_target
    
    def decideMove(self, ia_LP, player_LP, ia_Field, player_Field):
        S = self.calculate_game_state(ia_LP, player_LP, ia_Field, player_Field)
        decision=self.strategy_move(S)
        return decision

    def strategy_move(self, S):
        if S > 10:  
            #Utilizar ataque +2
            return 0
        elif S < -10:
            #Utilizar defensa +2
            return 1
        else:
            #Utilizar IA de medio mejorada
            return 2