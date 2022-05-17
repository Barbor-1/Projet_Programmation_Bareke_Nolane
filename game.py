import pygame
from unit.unit import Unit
from grid import Grid
from player import Player

# Liste de fonctions pour main
id = 0
playerList = []


def setPlayer(allegiance):
    joueur = Player(allegiance)
    playerList.append(joueur)
    return joueur


def getPlayer(allegiance):
    for joueur in playerList:
        if joueur.getAllegiance() == allegiance:
            return joueur


def placeUnit(target, y, player, grid):
    # Place une unité dans la grille, dans le cas où on en creer une nouvelle
    if player.allegiance == 1:
        grid.setUnitAtGrid(0, y, target)
    if player.allegiance == -1:
        grid.setUnitAtGrid(grid.getGridSize() - 1, y, target)


def moveUnit(target, grid):
    # Ordonne l'unité d'avancer d'une case dans la grille si elle en est capable
    newPosX = target.getPosX() + target.getAllegiance()
    if newPosX <= grid.getGridSize() - 1 and newPosX >= 0:
        nextTarget = grid.getUnitAtGrid(target.getPosX() + target.getAllegiance(), target.getPosY())
        if nextTarget == 0:
            grid.moveUnitAtGrid(target.getPosX() + target.getAllegiance(), target.getPosY(), target)
            print("new pos X", newPosX)

        else:
            if (target.attack(
                    nextTarget) == -1):  # if target.attack return -1 => nextTarget is dead and should be removed
                # attack() vérifie déjà l'allegiance des 2 unités
                grid.deleteUnitAtGrid(nextTarget.getPosX(), nextTarget.getPosY())
                print("unit", nextTarget.getId(), "fell in combat")
        if target.getAllegiance() == 1:
            if (target.getPosX() == grid.getGridSize() - 1):
                ennemi = getPlayer(-1)
                target.hurtPlayer(ennemi)
                grid.deleteUnitAtGrid(target.getPosX(), target.getPosY())
                print("unit", target.getId(), "attacked enemy base")
        if target.getAllegiance() == -1:
            if (target.getPosX() == 0):
                ennemi = getPlayer(1)
                target.hurtPlayer(ennemi)
                grid.deleteUnitAtGrid(target.getPosX(), target.getPosY())
                print("unit", target.getId(), "attacked enemy base")
                # Bug l'unité attaque avant la fin


def showUnits(grid):
    size = grid.getGridSize()
    for i in range(0, size):
        for j in range(0, size):
            target = grid.getUnitAtGrid(i, j)
            if (target != 0):
                target.show(60)


def spawnUnit(screen, grid, joueur):
    global id
    target = Unit(screen, joueur.getAllegiance(), id)
    id = id + 1
    # Inclure un placeUnit ducoup?
    return target  # De cette manière l'instance serait créer dans game mais utilisable dans main


def takeUnitFromAline(grid, y):
    ret = []
    for x in range(0, grid.getGridSize()):
        target = grid.getUnitAtGrid(x, y)
        if (target != 0):
            ret.append(target)
    return ret


def showHealth(screen):
    font = pygame.font.SysFont('Corbel', 64)
    player1 = getPlayer(1)
    player2 = getPlayer(-1)
    health = str(player1.getHealth()) + " " + str(player2.getHealth())
    print(health)
    text1 = font.render(health, True, (0, 0, 0))
    screen.blit(text1, text1.get_rect(center=(0, -300)))
