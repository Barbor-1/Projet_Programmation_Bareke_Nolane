import pygame
import button
from map_gen import map
from networking import server
import os
from screen import Screen
running = True

pygame.init()

#screen = pygame.display.set_mode((800, 800))
#pygame.display.set_caption("RTS GAME - v1")

screen_object = Screen("RTS GAME - v1", 800, 800)
screen_object.makeCurrent()
screen = screen_object.getScreen()

change_screen = Screen("RTS GAME - v1")
screen2 = change_screen.getScreen()


carte = map(screen, os.path.join(os.getcwd(), "carte.bmp"))
carte.display_map()

button1 = button.Button(10, 10, (255, 255, 255),(255, 0, 0), screen)
button1.setLabel("test")
button1.drawButton()


pygame.display.flip() # update display (IMPORTANT)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # put it inside class
            pos = pygame.mouse.get_pos()

            if(button1.collide(pos) == 1):
               print("collided")
               screen_object.endCurrent() #do nothing, see later
               change_screen.makeCurrent() # change screen
               pygame.draw.rect(screen2, (0, 255, 0), (0, 0, 200, 200))
               pygame.display.flip()


        
    