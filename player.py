
class Player():
    def __init__(self, allegiance):
        self.health = 20
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
