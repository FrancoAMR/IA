class Combat:
    def __init__(self):
        self.damage = 0

    #Para el resolve, se tendran en cuenta numeros para decidir si las cartas se destruyen
    # Return: 0= No pasa nada, 1= Se destruye la carta atacada, 2= Se destruye la carta atacante, 3= Se destruyen ambas
    def resolve(self, attacker_Card, attacked_Card, lp_atacante, lp_atacado):
        if (attacker_Card.state==0):
            if attacked_Card == None:
                self.damage = attacker_Card.attack_Value
                lp_atacado.receiveDMG(self.damage)
                attacker_Card.state=1
                return 0
            if attacked_Card.behavior==0:
                if attacker_Card.attack_Value > attacked_Card.attack_Value:
                    self.damage = attacker_Card.attack_Value - attacked_Card.attack_Value
                    lp_atacado.receiveDMG(self.damage)
                    attacker_Card.state=1
                    print(f"¡Carta atacada destruida! Se restan {self.damage} puntos de vida al oponente.")
                    return 1
                elif attacker_Card.attack_Value < attacked_Card.attack_Value:
                    self.damage = attacked_Card.attack_Value - attacker_Card.attack_Value
                    lp_atacante.receiveDMG(self.damage)
                    attacker_Card.state=1
                    print(f"¡Carta atacante destruida! Se restan {self.damage} puntos de vida al atacante.")
                    return 2
                else:
                    attacker_Card.state=1
                    print(f"¡Ambas cartas son destruidas! Ambos jugadores pierden {attacker_Card.attack_Value} puntos de vida.")
                    return 3
                
            elif attacked_Card.behavior==1 :   
                if attacker_Card.attack_Value > attacked_Card.defense_Value:
                    attacker_Card.state=1
                    print(f"¡Carta atacada destruida!")
                    return 1
                elif attacker_Card.attack_Value < attacked_Card.defense_Value:
                    self.damage = attacked_Card.defense_Value - attacker_Card.attack_Value
                    lp_atacante.receiveDMG(self.damage)
                    attacker_Card.state=1
                    print(f"Se restan {self.damage} puntos de vida al atacante.")
                    return 0
                
    def removeCard(self, cardList, card):
            cardList.remove(card)