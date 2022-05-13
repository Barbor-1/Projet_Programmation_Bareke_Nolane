import os
import pygame
import time

import game
import button
from map_gen import Map, Background
from screen import Screen
from unit.unit import Unit
from grid import Grid
from  player import Player
import  game
from toolbar import  Toolbar
from pytmx.util_pygame import load_pygame # 2.7 mode !
import pytmx
running = True

pygame.init()
fliped = True
id = 0
screen = pygame.display.set_mode((800, 800), vsync=True ) #TODO : see if vsync=True change something otherwise delete it (compatability problem ?)
#pygame.display.set_caption("RTS GAME - v1")

screen_object = Screen("RTS GAME - v1-MENU", screen, 800, 800) #TODO : change screens names
screen_object.makeCurrent()
screen = screen_object.getScreen()

change_screen = Screen("RTS GAME - v1", screen, 640, 700)
screen2 = change_screen.getScreen()
background = Background(change_screen.getScreen(), "sans_titre.tmx") #TODO : change path

# Ecran 1
carte_menu = Map(screen,
os.path.join(os.getcwd(), "Test_carte.png"))  # IMPORTANTx. B-Currently the background is placeholder
#TO CHANGE CARTE MENU
carte_menu.display_map()

button1 = button.Button(30, 70, (255, 255, 255), (255, 0, 0), screen)
button1.initButton("Next")
button1.drawButton()

font = pygame.font.SysFont('Corbel', 64)
text1 = font.render("MENU", True, (0, 0, 0))
screen.blit(text1, text1.get_rect(topleft=(10, 10)))


button2 = button.Button(1, 1, (0, 0, 0), (235, 125, 56), screen2)
button2.initButton(
    "Go back")  # Initialise values for example text_rect that could crash when we click the screen in the while
print(button2.text_rect.h, button2.text_rect.w)
screen_object.update()
pygame.display.flip()  # update display (IMPORTANT)

player_one = Player(1)
player_two = Player(-1)
grid = Grid(unit_size=32, size=640)
unit1 = game.spawnUnit(change_screen.getScreen(), grid, player_one)
game.placeUnit(unit1, 0, player_one, grid)

unit2 = game.spawnUnit(change_screen.getScreen(), grid, player_two)
game.placeUnit(unit2, 0, player_two, grid)

toolbar_soldier = Toolbar(change_screen.getScreen(), 100, 0, os.path.join(os.getcwd(), "Soldat.png"))
clicked_once = False
unit_list = []

clock = pygame.time.Clock()
#clock = time.time()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # put it inside class with event as argument ?| event.button == 1 : left click
            pos = pygame.mouse.get_pos()

            if (button2.collide(pos) == 1 and fliped == False):  # MAIN SCREEN to MENU
                mode = pygame.display.set_mode((800, 800), vsync=True ) # useless, only for testing purposes
                screen_object.screen = mode
                # B-Still able to press button 1 even if fliped, flashes white when pressed
                print("collided 1")
                fliped = True
                screen_object.makeCurrent()  # do nothing, see later
                change_screen.endCurrent()  # change screen + update screen => (maybe remove it dont know ?)
                carte_menu.display_map()
                # pygame.draw.rect(screen2, (75, 63,
                # 143), (300, 300, 200, 200))
                text1 = font.render("MENU", True, (0, 0, 0))
                screen_object.getScreen().blit(text1, text1.get_rect(topleft=(10, 10)))
                button1.drawButton()
                screen_object.update()
                pygame.display.flip()


            if (button1.collide(pos) == 1 and fliped == True):  # MENU TO MAIN SCREEN
                mode = pygame.display.set_mode((640, 700), vsync=True ) # useless, only for testing purposes
                change_screen.screen = mode
                # Menu Screen
                # B-Still able to press button 2 even if fliped
                print("collided 2")
                fliped = False
                change_screen.makeCurrent()  # do nothing, see later
                screen_object.endCurrent()  # change screen + update screen => (maybe remove it dont know ?)
                screen = change_screen.getScreen()
               # carte_menu.display_map()
                button2.drawButton()
                toolbar_soldier.draw()

                #screen.blit(text1, text1.get_rect(topleft=(10, 10)))

                background.display_map()
                change_screen.update()
                pygame.display.flip()
                start_ticks=0

            if(clicked_once == True):
                print("put soldier at pos", int((pos[1]-60)/32))
                temp = game.spawnUnit(change_screen.getScreen(), grid, joueur=player_one) #TODO changer joueur en fonction de la zone + changer le x
                game.placeUnit(temp, int(((pos[1]-60)/32)), player_one, grid)
                unit_list.append(temp)
                clicked_once = False
            if(toolbar_soldier.collide(pos)):
                print("collide solider")
                if(clicked_once == False):
                    last_pos = pos
                    clicked_once = True
                    print("clicked once")


                #move image



        if(fliped == False):
            start_ticks = start_ticks + clock.tick()
            if (start_ticks > 1000): # TODO REPLACE BY GAME MOVEMENT + limits checks + collisions ?
                print("event")
                #PUT THIS INSIDE ANOTHER FUNCTION ?
                #tick = clock.tick(1) # UPDATE FPS ?
                button2.drawButton() #IMPORTANT
                toolbar_soldier.draw()
                background.display_map()

                game.showUnits(grid)
                change_screen.update()
                pygame.display.flip()
                print(unit2.health, "x =", unit1.getPosX())
                game.moveUnit(unit1, grid)
                start_ticks = 0


