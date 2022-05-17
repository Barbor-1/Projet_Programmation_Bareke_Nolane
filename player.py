from textbox import  Textbox

class Player():
    def __init__(self, allegiance):
        self.health = 200
        self.allegiance = allegiance
        self.money = 40

    def getHealth(self):
        return self.health

    def getMoney(self):
        return self.money

    def getAllegiance(self):
        return self.allegiance

    def hurt(self,atk):
        self.health -= atk
#TODO Afficher PV et argent du joueur, screen doit être dans game ou dans joueur?
