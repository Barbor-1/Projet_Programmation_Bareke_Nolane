import pygame



class Unit():
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.allegiance = 0  # A qui appartient l'unité
        self.type = ""
        self.health = 10
        self.atk = 5  # Valeur de puissance d'attaque
        self.armor = 2  # Valeur de défense, pas sur qu'on va la garder
        self.speed = 1

    def move(self):
        self.pos_x += self.speed  # TO DO : vérifier si on est pas en dehors de la grid
        self.pos_y += self.speed

    def hurt(self, atk):
        self.health = atk - self.armor

    def attack(self, target):
        target.hurt(self.atk)  # Prendre en compte pour avoir un eventuel système de power-up en attaque
