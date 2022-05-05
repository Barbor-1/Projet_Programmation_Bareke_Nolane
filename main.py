import pygame
import pygame_widgets
import button
from map_gen import map
from networking import server, client
import os
from screen import Screen
import pygame_widgets # for textbox
running = True

pygame.init()
fliped = False
#screen = pygame.display.set_mode((800, 800)) # useless, only for testing purposes
#pygame.display.set_caption("RTS GAME - v1")

screen_object = Screen("RTS GAME - v1-MENU", 800, 800)
screen_object.makeCurrent()
screen = screen_object.getScreen()

change_screen = Screen("RTS GAME - v1", 800, 800)
screen2 = change_screen.getScreen()

# Ecran 1
carte = map(screen, os.path.join(os.getcwd(), "Test_carte.png")) #IMPORTANTx. B-Currently the background is placeholder
carte.display_map()

button1 = button.Button(30, 70, (255, 255, 255),(255, 0, 0), screen)
button1.initButton("Next")
button1.drawButton()

font = pygame.font.SysFont('Corbel',64)
text1 = font.render("MENU", True, (0, 0, 0))
screen.blit(text1, text1.get_rect(topleft=(10, 10)))
# Ecran 2
carte2 = map(screen2, os.path.join(os.getcwd(), "Placeholder.png"))#B- Next time i will make a picture that fits the game

button2 = button.Button(10, 10, (0, 0, 0),(235, 125, 56), screen2)
button2.initButton("Go back")#Initialise values for example text_rect that could crash when we click the screen in the while

pygame.display.flip() # update display (IMPORTANT)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # put it inside class with event as argument ?| event.button == 1 : left click
            pos = pygame.mouse.get_pos()

            if(button1.collide(pos) == 1 and fliped == False):
                #B-Still able to press button 1 even if fliped, flashes white when pressed
               print("collided 1")
               fliped = True
               screen_object.endCurrent() #do nothing, see later
               change_screen.makeCurrent() # change screen + update screen => (maybe remove it dont know ?)
               carte2.display_map()
               pygame.draw.rect(screen2, (75, 63, 143), (300, 300, 200, 200))
               button2.drawButton()
               pygame.display.flip()

            if(button2.collide(pos) == 1 and fliped == True):
                #Menu Screen
                #B-Still able to press button 2 even if fliped
                print("collided 2")
                fliped = False
                change_screen.endCurrent() #do nothing, see later
                screen_object.makeCurrent() # change screen + update screen => (maybe remove it dont know ?)
                carte.display_map()
                button1.drawButton()
                screen.blit(text1, text1.get_rect(topleft=(10, 10)))
                pygame.display.flip()
