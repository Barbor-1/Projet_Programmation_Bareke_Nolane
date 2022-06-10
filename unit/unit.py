import os
import pygame
import random

from unit.player import Player


class Unit():
    def __init__(self, screen=0, allegiance=0, id=0): # 0 pour éviter le chargement des images dans le démon TCP
        """
        :param screen: Ecran sur lequel on va mettre l'unité
        :param allegiance: Camp auquel l'unité appartient
        :param id: Identifiant unique à l'unité
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
        """
        :return: Donne la position en x
        """
        return self.pos_x

    def getPosY(self):
        """
        :return: Donne la position en y
        """
        return self.pos_y

    def getAllegiance(self):
        """
        :return: Donne à quel camp l'unité appartient
        """
        return self.allegiance

    def getId(self):
        """
        :return: Donne l'identifiant
        """
        return self.id

    def move(self, speed): # Fait déplacer l'unité d'une certaine quantité speed vers la base ennemie
        """
        :param speed: Distance en x dont on déplace l'unité
        :int: speed of unit
        """
        if( abs(self.pos_x) > self.limits):
            pass

        else:
            self.pos_x += 1 * self.allegiance*speed  # TO DO : vérifier si on est pas en dehors de la grid

    def hurt(self, atk): # Appeler quand l'unité prend des dégats
        """
        :param atk: Puissance de l'attaque blessant l'unit
        :rtype: int
        """
        self.health -= atk - random.randint(0, self.armor)  # Dégat infliger reduit par un nombre aléatoire inférieure ou égale à la valeur d'armure


    def attack(self, target): # Appeler quand l'unité inflige des dégats
        """
        :param target: Cible a attaquer
        :rtype: Unit object
        :return: Si l'unité est morte
        """
        if target.getAllegiance() != self.allegiance: # Verifie si la cible est ennemie
            target.hurt(self.atk)
            self.changeSprite(2*self.allegiance) # Equipe le sprite en position d'attaque
            if(target.health < 0): # Si la cible meurt
                return -1

    def hurtPlayer(self, joueur): # Attaque la base ennemie
        """
        :param joueur: Joueur ciblé par l'attaque
        :rtype: Player object
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

    def show(self, offset): # Affiche l'unité
        """
        :param offset: Décalage avec lequel on affiche l'unité
        :rtype: int
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
        """
        :return: Donne la valeur d'attaque
        """
        return  self.atk

    def changeSprite(self,valeur): # Change l'image de l'unité
        """
        :param valeur: valeur differenciant en quel image changer l'unité
        :rtype: int
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

