class combat:
    def __init__(self, attacker_Card, attacked_Card, lp_atacante, lp_atacado):
        self.attacker_Card = attacker_Card
        self.attacked_Card = attacked_Card
        self.lp_atacante = lp_atacante
        self.lp_atacado = lp_atacado

    def resolver(self):
        print(f"Atacante: {self.attacker_Card.attack_Value} ATK vs Defensor: {self.attacked_Card.attack_Value} ATK")
        if self.attacked_Card.behavior==0:
            if self.attacker_Card.attack_Value > self.attacked_Card.attack_Value:
                daño = self.attacker_Card.attack_Value - self.attacked_Card.attack_Value
                self.lp_atacado.receiveDMG(daño)
                print(f"¡Carta atacada destruida! Se restan {daño} puntos de vida al oponente.")
                return 'atacado_destruido'
            elif self.attacker_Card.attack_Value < self.attacked_Card.attack_Value:
                daño = self.attacked_Card.attack_Value - self.attacker_Card.attack_Value
                self.lp_atacante.receiveDMG(daño)
                print(f"¡Carta atacante destruida! Se restan {daño} puntos de vida al atacante.")
                return 'atacante_destruido'
            else:
                self.lp_atacante.receiveDMG(self.attacker_Card.attack_Value)
                self.lp_atacado.receiveDMG(self.attacked_Card.attack_Value)
                print(f"¡Ambas cartas son destruidas! Ambos jugadores pierden {self.attacker_Card.attack_Value} puntos de vida.")
                return 'ambas_destruidas'
            
        elif self.attacked_Card.behavior==1 :   
            if self.attacker_Card.attack_Value > self.attacked_Card.defense_Value:
                print(f"¡Carta atacada destruida!")
                return 'atacado_destruido'
            elif self.attacker_Card.attack_Value < self.attacked_Card.defense_Value:
                daño = self.attacked_Card.defense_Value - self.attacker_Card.attack_Value
                self.lp_atacante.receiveDMG(daño)
                print(f"Se restan {daño} puntos de vida al atacante.")
                return 'ataque_repelido'
            else:
                print(f"¡Ambas cartas se han repelido!")
                return 'ambas_repelidos'