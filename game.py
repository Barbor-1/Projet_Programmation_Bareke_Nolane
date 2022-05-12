import pygame
from unit.unit import Unit
from grid import Grid
from player import Player

# Est-ce que le jeu est une classe ou une serie de fonction
# On va partir sur une liste de fonction


def placeUnit(target, y, player, grid):
    #Place une unité dans la grille, dans le cas où on en creer une nouvelle
    if player.allegiance == 1:
        grid.setUnitAtGrid(1, y, target)
    if player.allegiance == -1:
        grid.setUnitAtGrid(grid.getGridSize() - 1, y, target)


def moveUnit(target, grid):
    #Ordonne l'unité d'avancer d'une case dans la grille si elle en est capable
    newPosX = target.getPosX() + target.getAllegiance
    if newPosX >= grid.getGridSize()-1 | newPosX <= 0:
        #TODO : Verifier aussi si on est dans la base ennemie
        nextTarget = grid.getUnitAtGrid(target.getPosX()+1, target.getPosY())
        if nextTarget == 0:
            target.move()
        else:
            target.attack(nextTarget)  #attack() vérifie déjà l'allegiance des 2 unités

# TODO : Plus de fonction, afficher les unité? avoir la grille sur l'écran. deplacé les unités sur la grille et qu'ils s'affichent
def showUnits(grid):
    size = grid.getGridSize()
    for i in range(0, size):
        for j in range(0, size):
            target = grid.getUnitAtGrid(i, j)
            if(target != 0):
                target.show()

def spawnUnit(screen, grid, joueur=1): # Pourquoi c'est pas en orange?
    target = Unit(screen) #TODO : inclure allegiance de joueur
    #Inclure un placeUnit ducoup
    return target # De cette manière l'instance serait créer dans game mais utilisable dans main? Peut bugger
