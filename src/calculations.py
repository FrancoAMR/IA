import pygame
from values import *

class Calculation:
    def calculateInvocation(self, value, position):
        atkScore= 0
        defScore= 0
        if(position== "attack"):
            match value:
                case 0: atkScore+= 0
                case 1: atkScore+= 2
                case 2: atkScore+= 4
                case 3: atkScore+= 6
                case 4: atkScore+= 8
                case 5: atkScore+= 10
                case 6: atkScore+= 12
                case 7: atkScore+= 14
                case 8: atkScore+= 16
                case 9: atkScore+= 18
                case 10: atkScore+= 20
            return atkScore
        if (position== "defense"):
            match value:
                case 0: defScore+=1
                case 1: defScore+= 2
                case 2: defScore+= 3
                case 3: defScore+= 5
                case 4: defScore+= 7
                case 5: defScore+= 9
                case 6: defScore+= 11
                case 7: defScore+= 13
                case 8: defScore+= 15
                case 9: defScore+= 17
                case 10: defScore+= 19
            return defScore
    def calculatePosition(self):
        #TODO: check the board if the player has or not cards and create conditions after that
        return