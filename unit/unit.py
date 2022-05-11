import pygame



class Unit():
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.allegiance = 0  # A qui appartient l'unité. +1 pour un joueur -1 pour l'autre => ça peut passer
        self.type = ""
        self.health = 10
        self.atk = 5  # Valeur de puissance d'attaque
        self.armor = 2  # Valeur de défense, pas sur qu'on va la garder
        self.id = 0   #TODO : PUT UNIQUE ID

    def getPosX(self):
        return self.pos_x

    def getPosY(self):
        return self.pos_y

    def getAllegiance(self):
        return self.allegiance

    def move(self):
        self.pos_x += 1 * self.allegiance # TO DO : vérifier si on est pas en dehors de la grid

    def hurt(self, atk):
        self.health = atk - self.armor

    def attack(self, target):
        if target.getAllegiance() != self.allegiance:
            target.hurt(self.atk)  # Prendre en compte pour avoir un eventuel système de power-up en attaque

    def __str__(self):
        pass
