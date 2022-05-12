import pygame
from unit import unit
from grid import Grid

# Est-ce que le jeu est une classe ou une serie de fonction
# On va partir sur une liste de fonction


def placeUnit(target, y, player, grid):
    if player == 1:
        grid.setUnitAtGrid(1, y, target)
    if player == -1:
        grid.setUnitAtGrid(grid.getGridSize() - 1, y, target)


def moveUnit(target, grid):
    newPosX = target.getPosX() + target.getAllegiance
    if newPosX >= grid.getGridSize() | newPosX <= 0:
        #TODO : Verifier aussi si on est dans la base ennemie
        nextTarget = grid.getUnitAtGrid(target.getPosX()+1, target.getPosY())
        if nextTarget == 0:
            target.move()
        else:
            target.attack(nextTarget)  #attack() vérifie déjà l'allegiance des 2 unités

# TODO : Plus de fonction, afficher les unité? avoir la grille sur l'écran. deplacé les unités sur la grille et qu'ils s'affichent
