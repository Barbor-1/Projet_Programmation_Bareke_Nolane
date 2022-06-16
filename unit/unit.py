import os
import pygame
import random

from unit.player import Player


class Unit():
    """basic unit

    :param screen: screen where we put the unit
    :type screen: pygame.Surface
    :param allegiance: which side the unit belongs to 
    :type allegiance: int
    :param id: unique unit id
    :type id: int

    """
    def __init__(self, screen=0, allegiance=0, id=0): # 0 pour éviter le chargement des images dans le démon TCP
        """
        init unit
        

        """
        self.pos_x = 0.0 #
        self.pos_y = 0.0
        self.allegiance = allegiance  # A qui appartient l'unité. +1 pour un joueur -1 pour l'autre => ça peut passer
        self.type = "a" # default type just for networking
        self.health = 10
        self.atk =  10 # Valeur de puissance d'attaque TO CHANGE ONLY FOR TESTING
        self.armor = 2  # Valeur de défense, pas sur qu'on va la garder
        self.id = id
        self.is_remote = False # si True : unité de l'autre client
        self.half_walk = False # for unit slow down
        if allegiance == 1: #for different  unit design
            self.image = pygame.image.load(os.path.join(os.getcwd(), "Sprite/Soldat.png"))
        elif allegiance == -1:
            self.image = pygame.image.load(os.path.join(os.getcwd(), "Sprite/SoldierB.png"))
        else:
            pass # do nothing
        self.screen = screen
        if(allegiance != 0):
            self.limits = pygame.display.get_surface().get_size()[0]
            pass
    

    def loadImage(self): # pour le chagement des unités a travers le réseau
        """load image => for network stuff : because i cant pass an image through the network (not pickable), I used this
        """
        if self.allegiance == 1:
            self.image = pygame.image.load(os.path.join(os.getcwd(), "Sprite/Soldat.png"))
        else :
            self.image = pygame.image.load(os.path.join(os.getcwd(), "Sprite/SoldierB.png"))
        self.limits = pygame.display.get_surface().get_size()[0]

    def getPosX(self):
        """get the x coordinate

        :return: the x coordinate
        :rtype: int

        """
        return self.pos_x

    def getPosY(self):
        """get the y coordinate

        :return: the y coordinate
        :rtype: int

        """
        return self.pos_y

    def getAllegiance(self):
        """give which side the unit belong

        :return: the unit side ( 1 ou -1)
        :rtype: int

        """
        return self.allegiance

    def getId(self):
        """gives the unique unit id

        :return: the id 
        :rtype: int

        """
        return self.id

    def move(self, speed): #
        """move the unit to the enemy base by a defined quantity by speed

        :param speed: speed of the unit
        :type speed: int

        """
        if( abs(self.pos_x) > self.limits):
            pass

        else:
            self.pos_x += 1 * self.allegiance*speed  # TO DO : vérifier si on est pas en dehors de la grid

    def hurt(self, atk): # 
        """called when the unit takes damages

        :param atk: power of the unit which attacked this unit
        :type atk: int

        """
        self.health -= atk - random.randint(0, self.armor)  # Dégat infliger reduit par un nombre aléatoire inférieure ou égale à la valeur d'armure


    def attack(self, target): 
        """called when the unit makes damages

        :param target: target to attack
        :type target: Unit object
        :return: -1 if the targeted unit has died
        :rtype: int

        """
        if target.getAllegiance() != self.allegiance: # Verifie si la cible est ennemie
            target.hurt(self.atk)
            self.changeSprite(2*self.allegiance) # Equipe le sprite en position d'attaque
            if(target.health < 0): # Si la cible meurt
                return -1

    def hurtPlayer(self, joueur): 
        """attack the enemy base

        :param joueur: player targeted by the attack
        :type joueur: Player object

        """
        joueur.hurt(self.atk)
        self.changeSprite(2*self.allegiance) # Animation d'attaque
        self.health = 0 # L'unité s'autodétruit en infligeant des dégats

    def __str__(self): # use __getstate__
        """convert to string

        :return: state of the unit
        :rtype: string

        """
        return str(self.pos_x) + " " +  str(self.pos_y) + " " + str(self.allegiance) + " " +  self.type + " "  + str(self.health)+ " " + str(self.atk)  + " " + str(self.armor) + " " + str(self.id)

    def show(self, offset): #
        """display the unit

        :param offset: offset for displaying the unit (because of the top toolbar)
        :type offset: int

        """
        self.screen.blit(self.image, (self.pos_x * self.image.get_height(), self.pos_y * self.image.get_width() + offset))

    def __getstate__(self): # 
        """get unit state

        :return: unit state
        :rtype: string

        """
        return (self.pos_x, self.pos_y, self.allegiance,  self.type, self.health, self.atk,self.armor,self.id)

    def setstate(self, i): # for network unit update
        """set a unit state

        :param i: unit state
        :type i: string

        """
        self.pos_x = int(i[0])
        self.pos_y = int(i[1])
        #self.allegiance = int(i[2]) # fix : no override of unit allegiance => because unit allegiance of network unit is always -1
        self.type = i[3]
        self.health = int(i[4])
        self.atk = int(i[5])
        self.armor = int(i[6])
        self.id = int(i[7])

    def getAttack(self):
        """return the attack level

        :return: the attack level
        :rtype: int

        """
        return  self.atk

    def changeSprite(self,valeur): # 
        """change the unit image
     
        :param valeur: value which differenciate which image to put
        :type valeur: int

        """
        # Donne le sprite de base aux unités selon leur camps
        if valeur == 1:
            self.image = pygame.image.load(os.path.join(os.getcwd(), "Sprite/Soldat.png"))
        if valeur == -1:
            self.image = pygame.image.load(os.path.join(os.getcwd(), "Sprite/SoldierB.png"))
        # on peut differencier l'allegiance en appelant avec 2*allegiance
        # Donne le sprite en position d'attaque
        if valeur == 2:
            self.image = pygame.image.load(os.path.join(os.getcwd(), "Sprite/Soldat-slash.png"))
        if valeur == -2:
            self.image = pygame.image.load(os.path.join(os.getcwd(), "Sprite/SoldatB-slash.png"))
        if(valeur == 3):
            self.image = pygame.image.load(os.path.join(os.getcwd(), "Sprite/Soldat_water.png"))
        if(valeur == -3):
            self.image = pygame.image.load(os.path.join(os.getcwd(), "Sprite/SoldatB_water.png"))

