import pygame
from unit.unit import Unit
from grid import Grid
from player import Player

# Liste de fonctions pour main
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
        #TODO : Verifier aussi si on est dans la base enntarget.getAllegiance()emie
        nextTarget = grid.getUnitAtGrid(target.getPosX()+target.getAllegiance(), target.getPosY())
        if nextTarget == 0:
            grid.moveUnitAtGrid(target.getPosX() +target.getAllegiance(), target.getPosY(), target)

        else:
            if( target.attack(nextTarget)  == -1): # if target.attack return -1 => nextTarget is dead and should be removed
            #attack() vérifie déjà l'allegiance des 2 unités
                grid.deleteUnitAtGrid(nextTarget.getPosX(), nextTarget.getPosY())
                print("unit", target.getId(), "fell in combat")


def showUnits(grid):
    size = grid.getGridSize()
    for i in range(0, size):
        for j in range(0, size):
            target = grid.getUnitAtGrid(i, j)
            if(target != 0):
                target.show(60)

def spawnUnit(screen, grid, joueur):
    global id
    target = Unit(screen, joueur.getAllegiance(), id)
    id = id + 1
    #Inclure un placeUnit ducoup?
    return target  # De cette manière l'instance serait créer dans game mais utilisable dans main


def takeUnitFromAline(grid, y):
    ret = []
    for x in range(0, grid.getGridSize()):
        target = grid.getUnitAtGrid(x, y)
        if(target != 0):
            ret.append(target)
    return  ret

