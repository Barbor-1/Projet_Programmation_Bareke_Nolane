from ui.textbox import  Textbox

class Player():
    """player class

    :parameter allegiance: Variable décrivant a quel camp le joueur appartient 1 : allié, -1: ennemie
    :type allegiance: int

    """
    def __init__(self, allegiance):
        """init function
        """
        self.health = 200
        self.allegiance = allegiance
        self.money = 80

    def getHealth(self):
        """getter for player health
        
        :return: Affiche la santé du joueur
        :rtype: int

        """
        return self.health

    def getMoney(self):
        """getter for the player money
        
        :return: the player money (for displaying it later)
        :rtype: int

        """

        return self.money

    def cost(self,valeur): # 
        """reduce the player money
       
        :param valeur: value which is going to be substracted to the player money
        :type valeur: int

        """
        self.money -= valeur

    def gain(self,valeur): # 
        """augment the player resources
        
        :param valeur:  value which is going to be added to the player money
        :type valeur: int

        """
        self.money += valeur

    def getAllegiance(self):
        """getter for the player side
        
        :return: -1 for an ally, -1 for an ennemy
        :rtype: int
        """
        return self.allegiance

    def hurt(self,atk): # 
        """called when the player takes damages
        
        :param atk:  value which is going to be substracted to the player health
        :type atk: int
        
        """
        self.health -= atk
