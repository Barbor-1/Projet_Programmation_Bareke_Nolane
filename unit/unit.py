import os
import pygame
from player import Player

class Unit():
    def __init__(self, screen=0, allegiance=0, id=0): # 0 pour éviter le chargement des images dans le démon TCP 
        self.pos_x = 0 #
        self.pos_y = 0
        self.allegiance = allegiance  # A qui appartient l'unité. +1 pour un joueur -1 pour l'autre => ça peut passer
        self.type = "a" # default type just for networking
        self.health = 10
        self.atk = 5  # Valeur de puissance d'attaque
        self.armor = 2  # Valeur de défense, pas sur qu'on va la garder
        self.id = id
        if allegiance == 1:
            pass
            self.image = pygame.image.load(os.path.join(os.getcwd(), "Soldat.png"))
        elif allegiance == -1:
            pass
            self.image = pygame.image.load(os.path.join(os.getcwd(), "SoldierB.png"))
        else:
            pass # do nothing
        self.screen = screen
        if(allegiance != 0):
            self.limits = pygame.display.get_surface().get_size()[0]
            pass
    

    def loadImage(self): # pour le chagement des unités a travers le réseau
        if self.allegiance == 1:
            self.image = pygame.image.load(os.path.join(os.getcwd(), "Soldat.png"))
        else :
            self.image = pygame.image.load(os.path.join(os.getcwd(), "SoldierB.png"))
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
        self.health = 0

    def __str__(self): # use __getstate__
        return str(self.pos_x) + " " +  str(self.pos_y) + " " + str(self.allegiance) + " " +  self.type + " "  + str(self.health)+ " " + str(self.atk)  + " " + str(self.armor) + " " + str(self.id)

    def show(self, offset):
        self.screen.blit(self.image, (self.pos_x * self.image.get_height(), self.pos_y * self.image.get_width() + offset))

    def __getstate__(self): # add screen later and update limits # dont use it maybe ? 
        return (self.pos_x, self.pos_y, self.allegiance,  self.type, self.health, self.atk,self.armor,self.id)
    def setstate(self, i):
        self.pos_x = i[0]
        self.pos_y = i[1]
        self.allegiance = i[2]pygame 2.1.2 (SDL 2.0.16, Python 3.6.8)
Hello from the pygame community. https://www.pygame.org/contribute.html
not a server !
connected
running
22 86
pos (61, 82)
collided 2
event
exception : timed out
received commands (or not) from network
first arg GET_UNIT
cycle ended
running
received commands (or not) from network
argument left ['0', '0', '-1', 'a', '10', '5', '2', '0']
queue empty
exception at queue reading
first arg
cycle ended
running
received commands (or not) from network
queue empty
exception at queue reading
first arg
cycle ended
running
event
Traceback (most recent call last):
  File "/home/local/AD/nd393594/PycharmProjects/Projet_Programmation_Bareke_Nolane/main.py", line 182, in <module>
    game.placeUnit(unit_to_create, unit_to_create.getPosY(), player_two, grid) # change player
  File "/home/local/AD/nd393594/PycharmProjects/Projet_Programmation_Bareke_Nolane/game.py", line 13, in placeUnit
    grid.setUnitAtGrid(grid.getGridSize() - 1, y, target)
  File "/home/local/AD/nd393594/PycharmProjects/Projet_Programmation_Bareke_Nolane/grid.py", line 15, in setUnitAtGrid
    self.grid[y][x] = target
TypeError: list indices must be integers or slices, not str
exception : timed out
received commands (or not) from network
first arg GET_UNIT
cycle ended
running
data treated : SET_UNIT 0 0 -1 a 10 5 2 0

Process finished with exit code 1

        self.type = i[3]
        self.health = i[4] 
        self.atk = i[5]
        self.armor = i[6]
        self.id = i[7]



