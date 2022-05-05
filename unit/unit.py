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


