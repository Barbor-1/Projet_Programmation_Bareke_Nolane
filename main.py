import os
import pygame
import pytmx
import time
from multiprocessing import process, JoinableQueue
#from pytmx.util_pygame import load_pygame  # 2.7 mode !

import button
import game
import network_utils
from demon_tcp import demon
from grid import Grid
from map_gen import Map, Background
from player import Player
from screen import Screen
from show_menu import ShowMenu
from textbox import Textbox
from toolbar import Toolbar
from unit.unit import Unit

running = True
fliped = True  # TRUE => menu
switch_back = False
id = 0
cancel = 0 # Pour afficher une image quand on a pas assez d'argent
is_client = False
# starting demon
input_queue = JoinableQueue()  # Queue with task_done and join()
output_queue = JoinableQueue()


if __name__ == "__main__":
    player_name = ""
    IP = ""
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    # pygame.display.set_caption("RTS GAME - v1")

    menu_screen = Screen("RTS GAME - v1-MENU", screen, 800, 800)  # TODO : change screens names
    menu_screen.makeCurrent()
    screen = menu_screen.getScreen()

    main_screen = Screen("RTS GAME - v1", screen, 640, 700)
    background = Background(main_screen.getScreen(), "Sprite/sans_titre.tmx")  # TODO : change path

    # Ecran 1
    # carte_menu = Map(screen, os.path.join(os.getcwd(), "Test_carte.png"))  # IMPORTANTx. B-Currently the background is placeholder
    # TODO CHANGE CARTE MENU

    menu_screen.getScreen().fill((80, 80, 80))

    show_menu = ShowMenu(menu_screen.getScreen())
    show_menu.draw()

    font = pygame.font.SysFont('Sprite/CORBEL.TTF', 64)
    text1 = font.render("MENU", True, (0, 0, 0))
    screen.blit(text1, text1.get_rect(topleft=(10, 10)))

    # textbox = Textbox(menu_screen.getScreen(), 100, 100, 100, 400, (25, 25, 25))
    # textbox.draw()

    button2 = button.Button(1, 1, (0, 0, 0), (235, 125, 56), main_screen.getScreen())
    button2.initButton(
        "Go back")  # Initialise values for example text_rect that could crash when we click the screen in the while
    print(button2.text_rect.h, button2.text_rect.w)
    menu_screen.update()
    pygame.display.flip()  # update display (IMPORTANT)

    player_one = game.setPlayer(1)  # notre joueur
    player_two = game.setPlayer(-1)  # joueur ennemi

    grid = Grid(unit_size=32, size=640)
    unit1 = game.spawnUnit(main_screen.getScreen(), grid, player_one)
    game.placeUnit(unit1, 0, player_one, grid)

    unit2 = game.spawnUnit(main_screen.getScreen(), grid, player_two)
    game.placeUnit(unit2, 0, player_two, grid)

    toolbar_soldier = Toolbar(main_screen.getScreen(), button2.text_rect.w + 10, 0,
                              os.path.join(os.getcwd(), "Sprite/Soldat.png"))  # relative positions ! (DONE)
    clicked_once = False
    unit_list = [unit1, unit2]

    clock = pygame.time.Clock()
    # clock = time.time()

    while running:
        events = pygame.event.get()
        clock.tick()
        for event in events:
            # if (fliped == True): # UPDATE TEXTBOX
            #    if(textbox.listen(event)):
            #        print(textbox.getText()) # DO SOMETHING ELSE, print only for testing purposes
            #    menu_screen.update() # UPDATE SCREEN
            #    pygame.display.flip()

            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # put it inside class with event as argument ?| event.button == 1 : left click
                pos = pygame.mouse.get_pos()

                if (button2.collide(pos) == 1 and fliped == False) or( fliped == False and switch_back == True):  # MAIN SCREEN to MENU
                    test.terminate()
                    mode = pygame.display.set_mode((800, 800), vsync=True)  # useless, only for testing purposes
                    menu_screen.screen = mode
                    switch_back = False


                    # B-Still able to press button 1 even if fliped, flashes white when pressed
                    print("collided 1")
                    fliped = True

                    menu_screen.makeCurrent()  # do nothing, see later
                    main_screen.endCurrent()  # change screen + update screen => (maybe remove it dont know ?)

                    # textbox.draw()
                    menu_screen.getScreen().fill((80, 80, 80))

                    text1 = font.render("MENU", True, (0, 0, 0))
                    menu_screen.getScreen().blit(text1, text1.get_rect(topleft=(10, 10)))

                    show_menu.draw()

                    menu_screen.update()
                    pygame.display.flip()

                if (clicked_once == True):
                    pos_to_place = int((pos[1] - 60) / 32)
                    if (pos_to_place < 0):
                        clicked_once = False
                    else:
                        print("put soldier at pos", pos_to_place)
                        temp = game.spawnUnit(main_screen.getScreen(), grid,
                                              joueur=player_one)  # TODO changer joueur en fonction de la zone + changer le x
                        game.placeUnit(temp, pos_to_place, player_one, grid)
                        unit_list.append(temp)
                        data_to_send = "SET_UNIT " + str(temp) + "\n"
                        input_queue.put(data_to_send)
                        # input_queue.join() # not waiting for command
                        clicked_once = False
                        player_one.cost(30)  # TODO avoir le coût lié a une valeur de toolbar par exemple
                        print("money :", player_one.getMoney())

                if (toolbar_soldier.collide(pos) and fliped == False):
                    print("collide solider")
                    if (clicked_once == False):
                        last_pos = pos  # utiliser nulle part?
                        if (player_one.getMoney() >= 30):
                            clicked_once = True
                            print("clicked once")
                        else :
                            cancel = 1
            if (fliped == True):
                res = show_menu.collide(event)
                menu_screen.update()  # for textbox
                pygame.display.flip()

                if(res == 4):
                    IP = show_menu.getIpText()
                    print("IP", IP)

                if (res == 1):
                    print("server has bene selected")
                    test = demon(input_queue, output_queue, port="9999", is_client=False)  # only client for now
                    test.daemon = True  # important pour que le process se ferme après que le le script principal s'est terminé !
                    test.start()

                    wait_for_connect = output_queue.get()
                    while(wait_for_connect !=  "CONNECTED"):
                        print("waiting", wait_for_connect)
                        wait_for_connect = output_queue.get()
                    print("connected from client")

                    mode = pygame.display.set_mode((640, 700), vsync=True)  # useless, only for testing purposes
                    main_screen.screen = mode
                    # Menu Screen
                    # B-Still able to press button 2 even if fliped

                    print("switched to main screen")
                    fliped = False
                    main_screen.makeCurrent()  # do nothing, see later
                    menu_screen.endCurrent()  # change screen + update screen => (maybe remove it dont know ?)
                    screen = main_screen.getScreen()
                    # carte_menu.display_map()
                    button2.drawButton()
                    toolbar_soldier.draw()

                    background.display_map()
                    main_screen.update()
                    pygame.display.flip()
                    start_ticks = 0
                    counter = 0






                if (res == 2):
                    print("client has been selected")
                    test = demon(input_queue, output_queue, port="9999", is_client=True, address=IP)  # only client for now
                    test.daemon = True  # important pour que le process se ferme après que le le script principal s'est terminé !
                    test.start()

                    wait_for_connect = output_queue.get()
                    while(wait_for_connect !=  "CONNECTED"):
                        print("waiting", wait_for_connect)
                        wait_for_connect = output_queue.get()
                    print("connected from client")

                    mode = pygame.display.set_mode((640, 700), vsync=True)  # useless, only for testing purposes
                    main_screen.screen = mode
                    # Menu Screen
                    # B-Still able to press button 2 even if fliped

                    print("switched to ma""in screen")
                    fliped = False

                    main_screen.makeCurrent()  # do nothing, see later
                    menu_screen.endCurrent()  # change screen + update screen => (maybe remove it dont know ?)

                    screen = main_screen.getScreen()

                    # carte_menu.display_map()
                    button2.drawButton()
                    toolbar_soldier.draw()
                    background.display_map()

                    main_screen.update()
                    pygame.display.flip()

                    start_ticks = 0
                    counter = 0


        if (fliped == False):
            exception = False
            # print("time" , time.time() - start_ticks, "fps ", clock.get_fps())
            if ((time.time() - start_ticks) > 0.5):  # TODO DEGAGER MULTIPROCESS => TROP LENT ?
                # print("event")
                # get unit from server
                if (counter == 1):  # TO UPDATE
                    try:
                        data_out = output_queue.get(False)  # not blocking
                    except Exception as e:
                        exception = True
                        # print("Exception while getting output from server ", e, flush=True)
                    counter = 0
                    if (exception == False):  # no exception
                        print("got update from server")

                        print("data treated :", data_out)
                        arg1 = data_out.split(" ")[0]
                        if (arg1 == "SET_UNIT"):
                            print("got a new unit !")
                            unit_to_create = game.spawnUnit(main_screen.getScreen(), grid,
                                                            joueur=player_two)  # TODO changer joueur en fonction de la zone
                            unit_to_create.setstate(data_out.split(" ")[1:])  # charge l'état du joueur
                            unit_to_create.loadImage()  # update image
                            game.placeUnit(unit_to_create, unit_to_create.getPosY(), player_two, grid)  # change player

                        if (arg1 == "REMOVE_UNIT"):
                            print("got a new unit to remove")
                            unit_list = network_utils.remove_unit(unit_list, data_out.split(" ")[1])

                        if (arg1 == "UPDATE_UNIT"):  # TODO
                            print("got a new unit to update")
                            pass

                        if (arg1 == "UPDATE_PLAYER"):  # TODO
                            print("got a player to update")
                            pass
                        if(arg1 == "DISCONNECTED"):
                            output_queue.put("CLOSE")
                            switch_back = False

                counter = counter + 1

                # #sending units : TODO : les mettre a jour au lieu de les créer et les créer juste dans le cas où le joueur les crée
                # for unit in unit_list:
                #    input_queue.put("SEND_UNIT " + str(unit) + "\n")
                main_screen.getScreen().fill((255, 255, 255))
                button2.drawButton()  # IMPORTANT
                toolbar_soldier.draw()
                if cancel == 1:
                    #Pas fait de la meilleur manière, devrait peut etre mis dans une fonction
                    toolbar_soldier.cancel()
                    cancel = 0
                background.display_map()
                game.showHealth(main_screen.getScreen())
                game.showWealth(main_screen.getScreen())


                game.showUnits(grid)
                main_screen.update()
                pygame.display.flip()
                for y in range(0, 20):
                    # prendre toute les unités d'une ligne

                    unitList = game.takeUnitFromAline(grid, y)

                    for i in unitList:
                        game.moveUnit(i, grid, output_queue)  # TODO UPDATE UNIT HEALTH IN CASE OF DAMAGE AND REMOVE IT IF NECESSARY

                player_one.gain(2) # Fait gagner de l'argent


                start_ticks = time.time()
