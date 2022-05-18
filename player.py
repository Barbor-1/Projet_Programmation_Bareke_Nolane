from textbox import  Textbox

class Player():
    def __init__(self, allegiance):
        self.health = 200
        self.allegiance = allegiance
        self.money = 80

    def getHealth(self):
        return self.health

    def getMoney(self):
        return self.money

    def cost(self,valeur):
        self.money -= valeur

    def gain(self,valeur):
        self.money += valeur

    def getAllegiance(self):
        return self.allegiance

    def hurt(self,atk):
        self.health -= atk
#TODO Afficher PV et argent du joueur, screen doit être dans game ou dans joueur?
