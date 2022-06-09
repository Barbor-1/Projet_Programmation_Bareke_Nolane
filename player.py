from textbox import  Textbox

class Player():
    def __init__(self, allegiance):
        self.health = 200
        self.allegiance = allegiance
        self.money = 80

    def getHealth(self): # Affiche la santé du joueur
        return self.health

    def getMoney(self): # Affiche les ressources du joueur
        return self.money

    def cost(self,valeur): # Réduit les ressources du joueur
        self.money -= valeur

    def gain(self,valeur): # Augmente les ressources du joueur
        self.money += valeur

    def getAllegiance(self): # Donne le camp du joueur
        return self.allegiance

    def hurt(self,atk): # Appeler quand le joueur subit des dégats
        self.health -= atk
