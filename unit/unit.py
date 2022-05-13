import os
import pygame
from player import Player


class Unit():
    def __init__(self, screen, allegiance, id):
        self.pos_x = 0
        self.pos_y = 0
        self.allegiance = allegiance  # A qui appartient l'unité. +1 pour un joueur -1 pour l'autre => ça peut passer
        self.type = ""
        self.health = 10
        self.atk = 5  # Valeur de puissance d'attaque
        self.armor = 2  # Valeur de défense, pas sur qu'on va la garder
        self.id = id
        if allegiance == 1:
            self.image = pygame.image.load(os.path.join(os.getcwd(), "Soldat.png"))
        else :
            self.image = pygame.image.load(os.path.join(os.getcwd(), "SoldierB.png"))
        self.screen = screen
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
            self.pos_x += 1 * self.allegiance*speed # TO DO : vérifier si on est pas en dehors de la grid

    def hurt(self, atk):
        self.health -= atk - self.armor


    def attack(self, target):
        if target.getAllegiance() != self.allegiance:
            target.hurt(self.atk)  # Prendre en compte pour avoir un eventuel système de power-up en attaque
            if(target.health < 0):
                return -1

    def hurtPlayer(self, joueur):
        joueur.hurt(self.atk)

    def __str__(self):
        pass

    def show(self, offset):
        self.screen.blit(self.image, (self.pos_x * self.image.get_height(), self.pos_y * self.image.get_width() + offset))
