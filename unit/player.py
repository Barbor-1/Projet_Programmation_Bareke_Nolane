from ui.textbox import  Textbox

class Player():
    def __init__(self, allegiance):
        """
        :param allegiance: Variable décrivant a quel camp le joueur appartient 1 : allié, -1: ennemie
        """
        self.health = 200
        self.allegiance = allegiance
        self.money = 80

    def getHealth(self):
        """
        :return: Affiche la santé du joueur
        """
        return self.health

    def getMoney(self):
        """
        :return: Affiche les ressources du joueur
        """
        return self.money

    def cost(self,valeur): # Réduit les ressources du joueur
        """
        :param valeur: Nombre que l'on va soustraire à l'argent du joueur
        :rtype: int
        """
        self.money -= valeur

    def gain(self,valeur): # Augmente les ressources du joueur
        """
        :param valeur: Nombre que l'on va additionner à l'argent du joueur
        :rtype: int
        """
        self.money += valeur

    def getAllegiance(self):
        """
        :return: Donne le camp du joueur 1 pour allié -1 pour l'ennemie
        """
        return self.allegiance

    def hurt(self,atk): # Appeler quand le joueur subit des dégats
        """
        :param atk: Nombre dont on va soustraire la santé du joueur
        :rtype: int
        """
        self.health -= atk
