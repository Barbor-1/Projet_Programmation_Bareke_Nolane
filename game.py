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
        target.move()
