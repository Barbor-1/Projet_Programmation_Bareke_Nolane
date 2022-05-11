import os
import pygame
import time

import game
import button
from map_gen import map
from screen import Screen
from unit.unit import Unit

running = True

pygame.init()
fliped = True
# screen = pygame.display.set_mode((800, 800)) # useless, only for testing purposes
# pygame.display.set_caption("RTS GAME - v1")

screen_object = Screen("RTS GAME - v1-MENU", 800, 800)
screen_object.makeCurrent()
screen = screen_object.getScreen()

change_screen = Screen("RTS GAME - v1", 800, 800)
screen2 = change_screen.getScreen()

# Ecran 1
carte_menu = map(screen,
            os.path.join(os.getcwd(), "Test_carte.png"))  # IMPORTANTx. B-Currently the background is placeholder
carte_menu.display_map()

button1 = button.Button(30, 70, (255, 255, 255), (255, 0, 0), screen2)
button1.initButton("Next")
button1.drawButton()

font = pygame.font.SysFont('Corbel', 64)
text1 = font.render("MENU", True, (0, 0, 0))
screen.blit(text1, text1.get_rect(topleft=(10, 10)))
# Ecran 2
carte2 = map(screen2,
             os.path.join(os.getcwd(), "Placeholder.png"))  # B- Next time i will make a picture that fits the game

button2 = button.Button(10, 10, (0, 0, 0), (235, 125, 56), screen2)
button2.initButton(
    "Go back")  # Initialise values for example text_rect that could crash when we click the screen in the while

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
                pygame.display.flip()


            if (button1.collide(pos) == 1 and fliped == True):  # MENU TO MAIN SCREEN
                # Menu Screen
                # B-Still able to press button 2 even if fliped
                print("collided 2")
                fliped = False
                change_screen.makeCurrent()  # do nothing, see later
                screen_object.endCurrent()  # change screen + update screen => (maybe remove it dont know ?)
                screen = change_screen.getScreen()
                carte_menu.display_map()
                button1.drawButton()
                screen.blit(text1, text1.get_rect(topleft=(10, 10)))
                pygame.display.flip()

        if (fliped == False): # TODO REPLACE BY GAME MOVEMENT + limits checks + collisions ?
            #PUT THIS INSIDE ANOTHER FUNCTION ?
            tick = clock.tick(3600) # UPDATE FPS ?
            carte2.display_map()
            button2.drawButton()
            unit_1.move(1) #TODO : see on windows for smooth movement
            print(unit_1.getPosX(), unit_1.getPosY())
            unit_1.show()
            pygame.display.flip()
