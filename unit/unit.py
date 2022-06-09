import os
import pygame
import random

from player import Player


class Unit():
    def __init__(self, screen=0, allegiance=0, id=0): # 0 pour éviter le chargement des images dans le démon TCP 
        self.pos_x = 0 #
        self.pos_y = 0
        self.allegiance = allegiance  # A qui appartient l'unité. +1 pour un joueur -1 pour l'autre => ça peut passer
        self.type = "a" # default type just for networking
        self.health = 10
        self.atk =  10 # Valeur de puissance d'attaque TO CHANGE ONLY FOR TESTING
        self.armor = 2  # Valeur de défense, pas sur qu'on va la garder
        self.id = id
        self.is_remote = False # si True : unité de l'autre client
        if allegiance == 1: #for different  unit design
            pass
            self.image = pygame.image.load(os.path.join(os.getcwd(), "Sprite/Soldat.png"))
        elif allegiance == -1:
            pass
            self.image = pygame.image.load(os.path.join(os.getcwd(), "Sprite/SoldierB.png"))
        else:
            pass # do nothing
        self.screen = screen
        if(allegiance != 0):
            self.limits = pygame.display.get_surface().get_size()[0]
            pass
    

    def loadImage(self): # pour le chagement des unités a travers le réseau
        if self.allegiance == 1:
            self.image = pygame.image.load(os.path.join(os.getcwd(), "Sprite/Soldat.png"))
        else :
            self.image = pygame.image.load(os.path.join(os.getcwd(), "Sprite/SoldierB.png"))
        self.limits = pygame.display.get_surface().get_size()[0]

    def getPosX(self):
        return self.pos_x

    def getPosY(self):
        return self.pos_y

    def getAllegiance(self):
        return self.allegiance

    def getId(self):
        return self.id

    def move(self, speed):
        if( abs(self.pos_x) > self.limits):
            pass

        else:
            self.pos_x += 1 * self.allegiance*speed  # TO DO : vérifier si on est pas en dehors de la grid

    def hurt(self, atk):
        self.health -= atk - random.randint(0, self.armor)  # Dégat infliger reduit par un nombre aléatoire inférieure ou égale à la valeur d'armure


    def attack(self, target):
        if target.getAllegiance() != self.allegiance:
            target.hurt(self.atk)  # Prendre en compte pour avoir un eventuel système de power-up en attaque
            self.changeSprite(2*self.allegiance) # Equipe le sprite en position d'attaque
            if(target.health < 0):
                return -1

    def hurtPlayer(self, joueur): # attack player base
        joueur.hurt(self.atk)
        self.changeSprite(2*self.allegiance)
        self.health = 0

    def __str__(self): # use __getstate__
        return str(self.pos_x) + " " +  str(self.pos_y) + " " + str(self.allegiance) + " " +  self.type + " "  + str(self.health)+ " " + str(self.atk)  + " " + str(self.armor) + " " + str(self.id)

    def show(self, offset):
        self.screen.blit(self.image, (self.pos_x * self.image.get_height(), self.pos_y * self.image.get_width() + offset))

    def __getstate__(self): # get unit state
        return (self.pos_x, self.pos_y, self.allegiance,  self.type, self.health, self.atk,self.armor,self.id)

    def setstate(self, i): # for network unit update
        self.pos_x = int(i[0])
        self.pos_y = int(i[1])
        #self.allegiance = int(i[2]) # fix : no override of unit allegiance => because unit allegiance of network unit is always -1
        self.type = i[3]
        self.health = int(i[4])
        self.atk = int(i[5])
        self.armor = int(i[6])
        self.id = int(i[7])

    def getAttack(self):
        return  self.atk

    def changeSprite(self,valeur):
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
