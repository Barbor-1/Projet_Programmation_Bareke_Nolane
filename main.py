import os
import pygame
import time

import game
import button
from map_gen import map
from screen import Screen
from unit.unit import Unit

from pytmx.util_pygame import load_pygame # 2.7 mode !
import pytmx
running = True

pygame.init()
fliped = True
screen = pygame.display.set_mode((800, 800)) # useless, only for testing purposes
#pygame.display.set_caption("RTS GAME - v1")

screen_object = Screen("RTS GAME - v1-MENU", screen, 800, 800)
screen_object.makeCurrent()
screen = screen_object.getScreen()

tiled_map = load_pygame("/home/local/AD/nd393594/Bureau/sans_titre.tmx") # IMPORTANT : video mode must be set + same size plz

change_screen = Screen("RTS GAME - v1", screen, 640, 700)
screen2 = change_screen.getScreen()

# Ecran 1
carte_menu = map(screen,
os.path.join(os.getcwd(), "Test_carte.png"))  # IMPORTANTx. B-Currently the background is placeholder
#TO CHANGE CARTE MENU
carte_menu.display_map()

button1 = button.Button(30, 70, (255, 255, 255), (255, 0, 0), screen)
button1.initButton("Next")
button1.drawButton()

font = pygame.font.SysFont('Corbel', 64)
text1 = font.render("MENU", True, (0, 0, 0))
screen.blit(text1, text1.get_rect(topleft=(10, 10)))


button2 = button.Button(10, 10, (0, 0, 0), (235, 125, 56), screen2)
button2.initButton(
    "Go back")  # Initialise values for example text_rect that could crash when we click the screen in the while

screen_object.update()
pygame.display.flip()  # update display (IMPORTANT)
unit_1 = Unit(screen2)


clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # put it inside class with event as argument ?| event.button == 1 : left click
            pos = pygame.mouse.get_pos()

            if (button2.collide(pos) == 1 and fliped == False):  # MAIN SCREEN to MENU
                mode = pygame.display.set_mode((800, 800)) # useless, only for testing purposes
                screen_object.screen = mode
                # B-Still able to press button 1 even if fliped, flashes white when pressed
                print("collided 1")
                fliped = True
                screen_object.makeCurrent()  # do nothing, see later
                change_screen.endCurrent()  # change screen + update screen => (maybe remove it dont know ?)
                carte_menu.display_map()
                # pygame.draw.rect(screen2, (75, 63, 143), (300, 300, 200, 200))
                text1 = font.render("MENU", True, (0, 0, 0))
                screen2.blit(text1, text1.get_rect(topleft=(10, 10)))
                button1.drawButton()
                screen_object.update()
                pygame.display.flip()


            if (button1.collide(pos) == 1 and fliped == True):  # MENU TO MAIN SCREEN
                mode = pygame.display.set_mode((640, 700)) # useless, only for testing purposes
                change_screen.screen = mode
                # Menu Screen
                # B-Still able to press button 2 even if fliped
                print("collided 2")
                fliped = False
                change_screen.makeCurrent()  # do nothing, see later
                screen_object.endCurrent()  # change screen + update screen => (maybe remove it dont know ?)
                screen = change_screen.getScreen()
               # carte_menu.display_map()
                button1.drawButton()
                screen.blit(text1, text1.get_rect(topleft=(10, 10)))
                layer = tiled_map.layers[0]
                for x, y, image in layer.tiles():
                    screen.blit(image, (x*32, y*32+60))
                change_screen.update()
                pygame.display.flip()

                unit_1.screen = screen



        if (fliped == False): # TODO REPLACE BY GAME MOVEMENT + limits checks + collisions ?
            #PUT THIS INSIDE ANOTHER FUNCTION ?
            tick = clock.tick(3600) # UPDATE FPS ?
            button2.drawButton() #IMPORTANT
            unit_1.move(1) #TODO : see on windows for smooth movement
            unit_1.pos_y = 60
            print(unit_1.getPosX(), unit_1.getPosY())
            unit_1.show()
            change_screen.update()
            pygame.display.flip()
