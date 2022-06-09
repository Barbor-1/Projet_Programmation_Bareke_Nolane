import os
import pygame

from grid import Grid
from player import Player
from unit.unit import Unit
from map_gen import  Background
# Liste de fonctions pour main
id = 0
playerList = []


def setPlayer(allegiance): # Ajoute le joueur a la liste de joueur
    joueur = Player(allegiance)
    playerList.append(joueur)
    return joueur


def getPlayer(allegiance):  # get player with allegiance
    for joueur in playerList:
        if joueur.getAllegiance() == allegiance:
            return joueur


def placeUnit(target, y, player, grid):  # put unit on grid
    # Place une unité dans la grille, dans le cas où on en creer une nouvelle
    if player.allegiance == 1:
        grid.setUnitAtGrid(0, y, target)
    if player.allegiance == -1:
        grid.setUnitAtGrid(grid.getGridSize() - 1, y, target)


def moveUnit(target, grid, inputQueue, background):  # SEULEMENT POUR LE SERVEUR : moving units
    # Ordonne l'unité d'avancer d'une case dans la grille si elle en est capable
    newPosX = target.getPosX() + target.getAllegiance()
    to_move = 1
    if newPosX <= grid.getGridSize() - 1 and newPosX >= 0:
        nextTarget = grid.getUnitAtGrid(target.getPosX() + target.getAllegiance(), target.getPosY())
        if nextTarget == 0:
            if(background.is_water(target.getPosX(), target.getPosY()) == True):
                print("on water")
                target.changeSprite(3*target.getAllegiance())  # Change le sprite en position de base
                #inputQueue.put("UPDATE_UNIT " + str(target.id) + " 0 " + "0.5" + "\n") # 0.5 => sprite = sprite-water
                to_move += 0.5
                if(target.half_walk == True):
                    grid.moveUnitAtGrid(target.getPosX() + target.getAllegiance(), target.getPosY(), target)
                    target.half_walk = False
                target.half_walk = True



            else:
                target.changeSprite(target.getAllegiance())  # Change le sprite en position de base
                grid.moveUnitAtGrid(target.getPosX() + target.getAllegiance(), target.getPosY(), target)
            inputQueue.put("UPDATE_UNIT " + str(target.id) + " 0 " + str(to_move) + "\n")
            # print("new pos X", newPosX)

        else:  # Si la prochaine case contient une unité
            inputQueue.put("ATTACKED " + str(target.getId()) + "\n")  # trigger annimation
            if (target.attack(nextTarget) == -1):  # if target.attack return -1 => nextTarget is dead and should be removed
                # attack() vérifie déjà l'allegiance des 2 unités
                grid.deleteUnitAtGrid(nextTarget.getPosX(), nextTarget.getPosY())
                print("unit", nextTarget.getId(), "fell in combat")
                inputQueue.put("REMOVE_UNIT " + str(nextTarget.getId()) + "\n")
        if target.getAllegiance() == 1:  # moi attaque l'ennemi
            if (target.getPosX() == grid.getGridSize() - 1):  # unité a la dernière position de l'ecran
                ennemi = getPlayer(-1)
                target.hurtPlayer(ennemi)
                inputQueue.put("UPDATE_PLAYER" + " 1 " + str(target.getAttack()) + "\n")  # see from server perspective
                grid.deleteUnitAtGrid(target.getPosX(), target.getPosY())
                inputQueue.put("REMOVE_UNIT " + str(target.id) + "\n")  # see for sync of units
                print("unit", target.getId(), "attacked enemy base")
                if (ennemi.getHealth() <= 0):
                    print("ennemy has died")
                    inputQueue.put(
                        "LOST " + str(-1 * ennemi.getAllegiance()) + "\n")  # *-1 car ennemi => ami pour le client
                    return -2  # ennemy has died => launch end screen
        if target.getAllegiance() == -1:  # l'ennemi m'attaque
            if (target.getPosX() == 0):  # unité ennemi : dans la première position de l'écran
                ennemi = getPlayer(1)  # get my player
                target.hurtPlayer(ennemi)  # damage it
                grid.deleteUnitAtGrid(target.getPosX(), target.getPosY())  # #delete unit
                print("unit", target.getId(), "attacked enemy base")
                inputQueue.put("REMOVE_UNIT " + str(target.id) + "\n")  # send to remote player
                inputQueue.put("UPDATE_PLAYER" + " -1 " + str(target.getAttack()) + "\n")  # send to remote player
                print("health ", ennemi.getHealth())
                if (ennemi.getHealth() <= 0):
                    inputQueue.put(
                        "LOST " + str(-1 * ennemi.getAllegiance()) + "\n")  # *-1 car ennemi => ami pour le client
                    return -3  # i died

                # TODO test if player has lost


def showUnits(grid):  # show unit => put unit on screen
    size = grid.getGridSize()
    for i in range(0, size):
        for j in range(0, size):
            target = grid.getUnitAtGrid(i, j)
            if (target != 0):
                target.show(60)  # put this unit on screen : 60 a cause de la  barre


def spawnUnit(screen, grid, joueur):  # create unit
    global id
    target = Unit(screen, joueur.getAllegiance(), id)
    id = id + 1
    # Inclure un placeUnit ducoup?
    return target  # De cette manière l'instance serait créer dans game mais utilisable dans main


def takeUnitFromAline(grid, y):  # take all units from a line otherwise some units might go too fast
    ret = []
    for x in range(0, grid.getGridSize()):
        target = grid.getUnitAtGrid(x, y)
        if (target != 0):
            ret.append(target)
    return ret


def showHealth(screen):  # Affiche la santé des joueurs
    font = pygame.font.SysFont('Sprite/Sprite/Sprite/Sprite/Sprite/Sprite/Sprite/Sprite/Sprite/Sprite/CORBEL.TTF', 64)
    player1 = getPlayer(1)
    player2 = getPlayer(-1)
    health = str(player1.getHealth()) + " " + str(player2.getHealth())
    # print(health)
    text1 = font.render(health, True, (0, 0, 0))
    # print("size, ", screen.get_size()[0]/2)
    screen.blit(text1, text1.get_rect(center=(screen.get_size()[0] / 2, 60 / 2)))
    # TODO Faire que le texte ne s'écrase pas l'un par dessus l'autre (ajouté un fond d'écran sur la toolbar?)
    # TODO Affichage, faire une fonction qui affiche tout et gère la distance des textes


# Pas impossible de fusionner showHealth et showWealth
def showWealth(screen): # Affiche les ressources du joueur
    font = pygame.font.SysFont('Corbel', 16)
    player1 = getPlayer(1)
    health = str(player1.getMoney())
    # print(health)

    text1 = font.render(health, True, (0, 0, 0))
    width = screen.get_size()[0]
    moneyImage = pygame.image.load(os.path.join(os.getcwd(), "Sprite/Money-1.png"))
    screen.blit(text1, text1.get_rect(center=(width - width / 4 + 15 + text1.get_rect().width, 50)))
    screen.blit(moneyImage, moneyImage.get_rect(center=(width - width / 4 + 10, 30)))


def resetPlayer():  # reseting players
    for player in playerList:
        player.money = 0
        player.health = 200
