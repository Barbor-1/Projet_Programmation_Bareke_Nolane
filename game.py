import pygame
from unit.unit import Unit
from grid import Grid
from player import Player

# Est-ce que le jeu est une classe ou une serie de fonction
# On va partir sur une liste de fonction
id = 0
def placeUnit(target, y, player, grid):
    #Place une unité dans la grille, dans le cas où on en creer une nouvelle
    if player.allegiance == 1:
        grid.setUnitAtGrid(0, y, target)
    if player.allegiance == -1:
        grid.setUnitAtGrid(grid.getGridSize() - 1, y, target)


def moveUnit(target, grid):
    #Ordonne l'unité d'avancer d'une case dans la grille si elle en est capable
    newPosX = target.getPosX() + target.getAllegiance()
    if newPosX <= grid.getGridSize()-1 and newPosX >=  0:
        #TODO : Verifier aussi si on est dans la base ennemie
        #TODO : dans grid, créer une fonction move
        nextTarget = grid.getUnitAtGrid(target.getPosX()+1, target.getPosY())
        if nextTarget == 0:
            #grid.setUnitAtGrid(target.getPosX()+1, target.getPosY(), target)
            #target.move(1)
            #grid.deleteUnitAtGrid(target.getPosX()-1, target.getPosY())
            grid.moveUnitAtGrid(target.getPosX() +1, target.getPosY(), target)

        else:
            if( target.attack(nextTarget)  == -1):
            #attack() vérifie déjà l'allegiance des 2 unités
                grid.deleteUnitAtGrid(nextTarget.getPosX(), nextTarget.getPosY())
                print("unit", target.getId(), "fell in combat")


# TODO : Plus de fonction, afficher les unité? avoir la grille sur l'écran. deplacé les unités sur la grille et qu'ils s'affichent
def showUnits(grid):
    size = grid.getGridSize()
    for i in range(0, size):
        for j in range(0, size):
            target = grid.getUnitAtGrid(i, j)
            if(target != 0):
                target.show()

def spawnUnit(screen, grid, joueur): # Pourquoi c'est pas en orange?
    global id
    target = Unit(screen, joueur.getAllegiance(), id)
    id = id + 1
    #Inclure un placeUnit ducoup
    return target # De cette manière l'instance serait créer dans game mais utilisable dans main? Peut bugger

