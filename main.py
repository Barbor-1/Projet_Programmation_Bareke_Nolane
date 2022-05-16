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
from toolbar import  Toolbar
from pytmx.util_pygame import load_pygame # 2.7 mode !
from textbox import Textbox
import pytmx

from demon_tcp import demon
from multiprocessing import process, JoinableQueue
import  network_utils
running = True
fliped = True
id = 0


#starting demon
input_queue = JoinableQueue() # Queue with task_done and join()
output_queue = JoinableQueue()
test = demon(input_queue, output_queue, port="12345") # only client for now
test.daemon = True # important pour que le process se ferme après que le le script principal s'est terminé !

if __name__ == "__main__":
    test.start() # start demon
    pygame.init()
    screen = pygame.display.set_mode((800, 800), vsync=True )
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

    textbox = Textbox(screen_object.getScreen(), 100, 100, 100, 400, (25, 25, 25))
    textbox.draw()

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

    toolbar_soldier = Toolbar(change_screen.getScreen(), button2.text_rect.w + 10, 0, os.path.join(os.getcwd(), "Soldat.png")) #relative positions ! (DONE)
    clicked_once = False
    unit_list = [unit1, unit2]

    clock = pygame.time.Clock()
    #clock = time.time()

    while running:
        events =  pygame.event.get()
        clock.tick()
        for event in events:
            if (fliped == True): # UPDATE TEXTBOX
                if(textbox.listen(event)):
                    print(textbox.getText()) # DO SOMETHING ELSE, print only for testing purposes
                screen_object.update() # UPDATE SCREEN
                pygame.display.flip()

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

                    textbox.draw()

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
                    counter = 0

                if(clicked_once == True):
                    print("put soldier at pos", int((pos[1]-60)/32))
                    temp = game.spawnUnit(change_screen.getScreen(), grid, joueur=player_one) #TODO changer joueur en fonction de la zone + changer le x
                    game.placeUnit(temp, int(((pos[1]-60)/32)), player_one, grid)
                    unit_list.append(temp)
                    data_to_send = "SET_UNIT " + str(temp) + "\n"
                    input_queue.put(data_to_send)
                    input_queue.join() # wait for command to execute
                    clicked_once = False
                if(toolbar_soldier.collide(pos)):
                    print("collide solider")
                    if(clicked_once == False):
                        last_pos = pos
                        clicked_once = True
                        print("clicked once")


                    #move image



        if(fliped == False):
            print("time" , time.time() - start_ticks, "fps ", clock.get_fps())
            if ( (time.time() - start_ticks )> 0.4): # TODO DEGAGER MULTIPROCESS => TROP LENT ?
                print("event")
                #get unit from server
                if(counter == 1): #  TO UPDATE
                    print("updating network unit")
                    input_queue.put("GET_UNIT")
                    #input_queue.join()
                    data_out = output_queue.get()
                    counter = 0
                    for data in data_out:
                        print("data treated :", data)
                        arg1 = data.split(" ")[0]
                        if(arg1 == "SET_UNIT"):
                            unit_to_create = game.spawnUnit(change_screen.getScreen(), grid, joueur=player_two)#TODO changer joueur en fonction de la zone
                            unit_to_create.setstate(data.split(" ")[1:]) # charge le
                            unit_to_create.loadImage()  # update image
                            game.placeUnit(unit_to_create, unit_to_create.getPosY(), player_two, grid) # change player

                        if(arg1 == "REMOVE_UNIT"):
                            unit_list = network_utils.remove_unit(unit_list, data.split(" ")[1])

                        if(arg1 == "UPDATE_UNIT"):
                            pass

                        if(arg1 == "UPDATE_PLAYER"):
                            pass
                counter = counter + 1

                #sending units :
                #for unit in unit_list:
                #    input_queue.put("SEND_UNIT " + str(unit) + "\n")


                #button2.drawButton() #IMPORTANT
                #toolbar_soldier.draw()
                background.display_map()

                game.showUnits(grid)
                change_screen.update()
                pygame.display.flip()
                for y in range(0, 20):
                    #prendre toute les unités d'une ligne

                        list = game.takeUnitFromAline(grid, y)

                        for i in list:
                            game.moveUnit(i, grid)
                start_ticks = time.time()
                print("new time")


