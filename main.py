import pygame
import button
from map_gen import map
from networking import server, client
import os
from screen import Screen
running = True

pygame.init()
fliped = False
#screen = pygame.display.set_mode((800, 800)) # useless, only for testing purposes
#pygame.display.set_caption("RTS GAME - v1")

screen_object = Screen("RTS GAME - v1-MENU", 800, 800)
screen_object.makeCurrent()
screen = screen_object.getScreen()

change_screen = Screen("RTS GAME - v1")
screen2 = change_screen.getScreen()


carte = map(screen, os.path.join(os.getcwd(), "Test_carte.png")) #IMPORTANTx
carte.display_map()

button1 = button.Button(10, 10, (255, 255, 255),(255, 0, 0), screen)
button1.setLabel("test")
button1.drawButton()

button2 = button.Button(500, 10, (255, 255, 255),(150, 63, 29), screen2)
button2.setLabel("go back")

pygame.display.flip() # update display (IMPORTANT)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # put it inside class with event as argument ?| event.button == 1 : left click
            pos = pygame.mouse.get_pos()

            if(button1.collide(pos) == 1):   
               print("collided 1")
               fliped = True
               screen_object.endCurrent() #do nothing, see later
               change_screen.makeCurrent() # change screen + update screen => (maybe remove it dont know ?)
               pygame.draw.rect(screen2, (0, 255, 0), (0, 0, 200, 200))
               button2.drawButton()
               pygame.display.flip()

            if(button2.collide(pos) == 1):
                print("collided 2")
                fliped = False
                change_screen.endCurrent() #do nothing, see later
                screen_object.makeCurrent() # change screen + update screen => (maybe remove it dont know ?)
                carte.display_map()
                button1.drawButton()
                pygame.display.flip()
