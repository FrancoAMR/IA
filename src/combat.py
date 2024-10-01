class Combat:
    def __init__(self):
        self.damage = 0

    def resolve(self, attacker_Card, attacked_Card, lp_atacante, lp_atacado):
        print(f"Atacante: {attacker_Card.attack_Value} ATK vs Sin carta defensora")
        if (attacker_Card.state==0):
            if attacked_Card == None:
                self.damage = attacker_Card.attack_Value
                lp_atacado.receiveDMG(self.damage)
                attacker_Card.state=1
                return 
            if attacked_Card.behavior==0:
                if attacker_Card.attack_Value > attacked_Card.attack_Value:
                    self.damage = attacker_Card.attack_Value - attacked_Card.attack_Value
                    lp_atacado.receiveDMG(self.damage)
                    attacker_Card.state=1
                    print(f"¡Carta atacada destruida! Se restan {self.damage} puntos de vida al oponente.")
                    return 'atacado_destruido'
                elif attacker_Card.attack_Value < attacked_Card.attack_Value:
                    self.damage = attacked_Card.attack_Value - attacker_Card.attack_Value
                    lp_atacante.receiveDMG(self.damage)
                    attacker_Card.state=1
                    print(f"¡Carta atacante destruida! Se restan {self.damage} puntos de vida al atacante.")
                    return 'atacante_destruido'
                else:
                    lp_atacante.receiveDMG(attacker_Card.attack_Value)
                    lp_atacado.receiveDMG(attacked_Card.attack_Value)
                    attacker_Card.state=1
                    print(f"¡Ambas cartas son destruidas! Ambos jugadores pierden {attacker_Card.attack_Value} puntos de vida.")
                    return 'ambas_destruidas'
                
            elif attacked_Card.behavior==1 :   
                if attacker_Card.attack_Value > attacked_Card.defense_Value:
                    attacker_Card.state=1
                    print(f"¡Carta atacada destruida!")
                    return 'atacado_destruido'
                elif attacker_Card.attack_Value < attacked_Card.defense_Value:
                    self.damage = attacked_Card.defense_Value - attacker_Card.attack_Value
                    lp_atacante.receiveDMG(self.damage)
                    attacker_Card.state=1
                    print(f"Se restan {self.damage} puntos de vida al atacante.")
                    return 'ataque_repelido'
                else:
                    attacker_Card.state=1
                    print(f"¡Ambas cartas se han repelido!")
                    return 'ambas_repelidos'
                
    def removeCard(self, cardList, card):
            cardList.remove(card)