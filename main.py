"""main game loop
"""

import multiprocessing
import os
import pygame
import pytmx
import signal
import time
from multiprocessing import process, JoinableQueue

import unit.unit
from ui import button
import game
from networking import network_utils
from demon_tcp import Demon
from ui.grid import Grid
from ui.map_gen import Map, Background
from unit.player import Player
from ui.screen import Screen
from ui.show_menu import ShowMenu
from ui.textbox import Textbox
from ui.toolbar import Toolbar
from unit.unit import Unit


# from pytmx.util_pygame import load_pygame  # 2.7 mode !

running = True
fliped = True  # TRUE => menu, FALSE => game
id = 0
cancel = 0  # Pour afficher une image quand on a pas assez d'argent
is_client = False
# starting demon
input_queue = JoinableQueue()  # Queue main => démon
output_queue = JoinableQueue()  # Queue démon => main
demon = ""  # pour utiliser la variable demon partout
defaut_port = "9699"

back_menu_event = Event1 = pygame.event.Event(pygame.USEREVENT, attr1='Event1') #event for back button
if __name__ == "__main__":
    IP = ""  # addresse IP pour le client
    pygame.init()
    screen = pygame.display.set_mode((800, 800))  # menu => taille 800*800
    pygame.mouse.set_cursor(
        pygame.cursors.arrow)  # for constitency issue with textbox : in order always have the same cursor
    # pygame.display.set_caption("RTS GAME - v1")

    menu_screen = Screen("RTS GAME - v1-MENU", screen,
                         800, 800)  # crée la surface du menu
    menu_screen.makeCurrent()  # change la surface courante par celle du menu
    screen = menu_screen.getScreen()  # screen contient la surface qui sert a dessiner

    main_screen = Screen("RTS GAME - v1", screen, 640,
                         700)  # surface du jeu en lui même
    background = Background(main_screen.getScreen(),
                            "Sprite/Fond_ecran.tmx")  # charge la carte

    menu_screen.getScreen().fill((80, 80, 80))  # menu gris (fond)

    show_menu = ShowMenu(menu_screen.getScreen())  # crée le menu
    show_menu.draw()  # affiche le menu

    font = pygame.font.SysFont('Sprite/CORBEL.TTF', 64)  # police
    text1 = font.render("MENU", True, (0, 0, 0))  # TEXTE MENU
    screen.blit(text1, text1.get_rect(topleft=(10, 10)))  # affiche le  texte

    button2 = button.Button(1, 1, (0, 0, 0), (235, 125, 56),
                            main_screen.getScreen())  # bouton
    button2.initButton(  # initialise le bouton
        "Go back")
    # print(button2.text_rect.h, button2.text_rect.w) #DEBUG
    menu_screen.update()  # met a jour la surface du menu
    pygame.display.flip()  # update display (IMPORTANT)

    player_one = game.setPlayer(1)  # notre joueur
    player_two = game.setPlayer(-1)  # joueur ennemi

    grid = Grid(unit_size=32, size=640)  # grille des unités

    toolbar_soldier = Toolbar(main_screen.getScreen(), button2.text_rect.w + 10, 0,
                              os.path.join(os.getcwd(), "Sprite/Soldat.png"))  # relative positions ! (DONE)
    clicked_once = False

    clock = pygame.time.Clock()  # pour nombre FPS
    # clock = time.time()

    while (running == True):
        events = pygame.event.get()  # get event list
        clock.tick()  # met a jour le nombre de fps

        for event in events:

            if event.type == pygame.QUIT:  # on quitte
                input_queue.put("CLOSE")  # ferme la connexion
                # tue le process demon_tcp par lui même
                input_queue.put("KILL")
                print("closing")  # DEBUG
                print("active children", multiprocessing.active_children())
                # tue tous les process enfants dans le cas où demon_tcp ne répond pas
                for prc in multiprocessing.active_children():
                    prc.join(5)
                    if (prc.exitcode == None):  # process was not killed
                        print("killing process", prc.pid)
                        try:
                            os.kill(prc.pid, signal.SIGKILL)
                        except:
                            print("cant kill")
                print("after killling", multiprocessing.active_children())
                pygame.quit()  # quitting pygame
                quit()  # quitte

            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or (
                    event == back_menu_event):  # click gauche
                pos = pygame.mouse.get_pos()  # position de la souris

                # MAIN SCREEN to MENU
                if (button2.collide(pos) == 1 and fliped == False) or (event == back_menu_event):

                    input_queue.put("CLOSE")  # ferme la connexion
                    # tue le process demon_tcp par lui même
                    input_queue.put("KILL")
                    print("closing")  # DEBUG
                    print("active children",
                          multiprocessing.active_children())  # DEBUG
                    # tue tous les process enfants dans le cas où demon_tcp ne répond pas
                    for prc in multiprocessing.active_children():
                        prc.join(5)
                        if (prc.exitcode == None):  # process was not killed
                            print("killing process", prc.pid)
                            try:
                                os.kill(prc.pid, signal.SIGKILL)
                            except:
                                print("cant kill")
                    print("after killling", multiprocessing.active_children())

                    # met a jout la taille de l'écran
                    mode = pygame.display.set_mode((800, 800))
                    menu_screen.screen = mode  # met a jour la surface

                    # B-Still able to press button 1 even if fliped, flashes white when pressed
                    print("collided 1")
                    fliped = True  # resetting flags for menu / main screen switching
                    switch_back = False  # reset flag for force going back to menu

                    menu_screen.makeCurrent()  # do nothing, see later
                    # change screen + update screen => (maybe remove it dont know ?)
                    main_screen.endCurrent()

                    # textbox.draw()
                    menu_screen.getScreen().fill((80, 80, 80))  # écran tout gris

                    text1 = font.render(
                        "MENU", True, (0, 0, 0))  # texte du menu
                    menu_screen.getScreen().blit(text1, text1.get_rect(topleft=(10, 10)))

                    show_menu.draw()  # affiche le menu

                    menu_screen.update()  # met a jour l'écran
                    pygame.display.flip()

                if (clicked_once == True):

                    pos_to_place = int((pos[
                        1] - 60) / 32)  # position de la future unité => 1 case fait 32*32 + le terrain de jeu commence qu'a 60 pixels
                    if (pos_to_place < 0):  # si au dessus du terrain de jeu
                        clicked_once = False  # reset flag
                    else:
                        print("put soldier at pos", pos_to_place)
                        temp = game.spawnUnit(main_screen.getScreen(), grid,
                                              joueur=player_one)  # spawn l'unité
                        if (grid.getUnitAtGrid(0, pos_to_place) == 0):
                            game.placeUnit(temp, pos_to_place, player_one,
                                           grid)  # place une unité seulement si dans la case de l'unité il n'y a rien

                        data_to_send = "SET_UNIT " + str(temp) + "\n"
                        input_queue.put(data_to_send)  # update network unit

                        clicked_once = False  # reset flag

                        player_one.cost(30)
                        # enlève 30 d'argent au joueur
                        print("money :", player_one.getMoney())  # debug

                if (toolbar_soldier.collide(pos) and fliped == False):  # mode jeu + boutton cliqué
                    print("collide solider")
                    if (clicked_once == False):  # premier clik
                        if (player_one.getMoney() >= 30):  # si assez d'argent
                            clicked_once = True
                            print("clicked once")
                        else:
                            cancel = 1  # on cancel l'action (animation)
            if (fliped == True):  # si on est en mode menu
                res = show_menu.collide(event)  # test des colision
                menu_screen.update()  # for textbox update
                pygame.display.flip()

                if (res == 4):  # on a entré l'addresse IP
                    IP = show_menu.getIpText()
                    print("IP", IP)

                if (res == 1):  # le serveur a été sélectionné
                    is_client = False  # flag for unit update
                    print("server has bene selected")
                    demon = Demon(input_queue, output_queue,
                                  port=defaut_port, is_client=False)  # init demon
                    # important pour que le process se ferme après que le le script principal s'est terminé !
                    demon.daemon = True
                    demon.start()

                    wait_for_connect = output_queue.get()  # attend que le démon se connecte
                    while (wait_for_connect != "CONNECTED"):
                        print("waiting", wait_for_connect)
                        wait_for_connect = output_queue.get()
                        pygame.display.flip()  # update display in order to avoid freeze
                    print("connected from client")
                    game.resetPlayer()

                    print("health", player_one.getHealth(),
                          player_two.getHealth())
                    mode = pygame.display.set_mode((640, 700),
                                                   vsync=True)  # switch screen into menu mode (put inside function ? idk)
                    main_screen.screen = mode
                    # Menu Screen to main screen

                    print("switched to main screen")
                    fliped = False
                    main_screen.makeCurrent()  # do nothing, see later
                    # change screen + update screen => (maybe remove it dont know ?)
                    menu_screen.endCurrent()
                    screen = main_screen.getScreen()  #
                    # carte_menu.display_map()
                    button2.drawButton()  # back button
                    toolbar_soldier.draw()  # toolbar on top

                    background.display_map()  # display map
                    main_screen.update()  # update screen
                    pygame.display.flip()
                    start_ticks = 0  # reset tick counter
                    counter = 0  # for network update delaying

                if (res == 2):  # client sélectionné
                    game.resetPlayer()
                    is_client = True  # flag for unit update
                    print("client has been selected")
                    IP = show_menu.getIpText()  # si pas entrée => update addresse IP
                    demon = Demon(input_queue, output_queue, port=defaut_port, is_client=True,
                                  address=IP)  # même chose que le serveur sauf qui'il faut précisé l'addresse IP
                    # important pour que le process se ferme après que le le script principal s'est terminé !
                    demon.daemon = True
                    demon.start()

                    wait_for_connect = output_queue.get()  # attends que le client se connecte
                    while (wait_for_connect != "CONNECTED"):
                        wait_for_connect = output_queue.get()
                        print("waiting", wait_for_connect)
                        pygame.display.flip()  # pour évite de freeze le jeu

                    print("connected from client")

                    # met a jour la taille de l'écran
                    mode = pygame.display.set_mode((640, 700), vsync=True)
                    main_screen.screen = mode  # met a jour la surface
                    # Menu Screen
                    # B-Still able to press button 2 even if fliped

                    # change pour l'écran de jeu
                    print("switched to main screen")
                    fliped = False

                    main_screen.makeCurrent()  # do nothing, see later
                    # change screen + update screen => (maybe remove it dont know ?)
                    menu_screen.endCurrent()

                    screen = main_screen.getScreen()

                    # carte_menu.display_map()
                    button2.drawButton()  # back button
                    toolbar_soldier.draw()
                    background.display_map()

                    main_screen.update()  # UPDATE SCREEN
                    pygame.display.flip()

                    start_ticks = 0
                    counter = 0

        if (fliped == False):  # mode jeu
            exception = False  # flag exception
            # print("time" , time.time() - start_ticks, "fps ", clock.get_fps())
            if ((time.time() - start_ticks) > 0.5) or (
                    is_client == True):  # les ticks de mise a jour se font tout les 0.5 secondes MIN ou si on est un client => pas de ticks car pas de mise a jour de la "physique"
                # print("event")
                # get unit from server
                if (
                        counter == 1):  # pour faire que la mise a jour réseau se fasse tout les x ticks de physique (ici 1 mise a jour réseau / tick)
                    try:
                        # not blocking => reçoit les mises a jour du serveur
                        data_out = output_queue.get(False)
                    except Exception as e:
                        exception = True
                        # print("Exception while getting output from server ", e, flush=True)
                    counter = 0
                    if (exception == False):  # no exception
                        print("got update from server")

                        print("data treated :", data_out)
                        # premier argument de la commande
                        arg1 = data_out.split(" ")[0]
                        if (arg1 == "SET_UNIT"):
                            print("got a new unit !")  # spawn unit
                            unit_to_create = game.spawnUnit(main_screen.getScreen(), grid,
                                                            joueur=player_two)  # crée l'unité
                            unit_to_create.setstate(data_out.split(" ")[
                                                    1:])  # charge l'état de l'unité sauf l'ALLEGIANCE CAR CELLE CI EST TOUJOURS -1 => ennemie
                            unit_to_create.loadImage()  # update image
                            game.placeUnit(unit_to_create, unit_to_create.getPosY(
                            ), player_two, grid)  # place l'unité

                        elif (arg1 == "REMOVE_UNIT"):  # REMOVE UNIT
                            print("got a new unit to remove")
                            unit_list = network_utils.remove_unit(
                                grid, data_out.split(" ")[1])

                        elif (arg1 == "UPDATE_UNIT"):  # update unit
                            print("got a new unit to update")
                            unit_id = data_out.split(" ")[1]
                            movement = data_out.split(" ")[3]
                            # we are only able to update the x position
                            if (data_out.split(" ")[2] == "0"):
                                network_utils.move_unit(
                                    grid, int(unit_id), float(movement))  # move unit

                        elif (arg1 == "DISCONNECTED"):
                            pass  # see later for return button

                        elif (arg1 == "UPDATE_PLAYER"):  # met a jour le joueur => vie du joueur
                            value = int(data_out.split(" ")[2])
                            player_id = int(data_out.split(" ")[1])
                            player_ret = game.getPlayer(player_id)
                            player_ret.hurt(value)

                        elif (arg1 == "ATTACKED" and is_client == True):  # attack unit
                            # trigged animation
                            unit_id = data_out.split(" ")[1]
                            network_utils.animate_unit(grid, unit_id)
                        elif (arg1 == "LOST"):  # i lost => trigger return to menu
                            player_id = int(data_out.split(" ")[1])
                            print("player ", player_id, " has died")

                            if (player_id == player_two.getAllegiance()):  # DEBUG
                                print("ennemi died")
                            elif (player_id == player_one.getAllegiance()):
                                print("i died")
                            # send back to menu
                            pygame.event.post(back_menu_event)

                counter = counter + 1  # for slowing down network pull rate

                # Partie affichage Interface
                main_screen.getScreen().fill((255, 255, 255))  # vide l'écran
                button2.drawButton()  # IMPORTANT # affiche le bouton retour
                # affiche le boutton pour placer une unité (ou plusieurs see later)
                toolbar_soldier.draw()
                # pas asser d'argent => petite annimation (marche pas ?)
                if cancel == 1:
                    # Pas fait de la meilleur manière, devrait peut etre mis dans une fonction
                    toolbar_soldier.cancel()
                    cancel = 0

                background.display_map()  # met a jout la carte
                # met a jour la vie des joueurs
                game.showHealth(main_screen.getScreen())
                # met a jout l'argent du joueur
                game.showWealth(main_screen.getScreen())

                game.showUnits(grid)  # affiche les unités
                main_screen.update()  # IMPORTANT : UPDATE SCREEN
                pygame.display.flip()
                if (is_client == False):  # seul le serveur met a jour les unités (et tout le reste)
                    # print("moving unit from server")
                    for y in range(0, 20):
                        # prendre toute les unités d'une ligne

                        unitList = game.takeUnitFromAline(grid,
                                                          y)  # déplace les unités d'une ligne pour éviter de déplacer plusieur fois une unité

                        # pour chaque unité de la ligne, la déplacer
                        for i in range(0, len(unitList)):
                            ret = game.moveUnit(
                                unitList[i], grid, input_queue, background)
                            print(unitList[i].getPosX())

                            if (ret == -2):
                                print("ennemy died")
                                # send end screen to ennemy
                                # launch end screen
                                # send back to menu
                                pygame.event.post(back_menu_event)

                            elif (ret == -3):
                                print("i died")
                                # send end screen to ennemy                               switch_back = True
                                # launch end screen
                                # send back to menu
                                pygame.event.post(back_menu_event)

                    player_one.gain(2)  # Fait gagner de l'argent
                    # met a jour le temps de dernière éxécution de ce code dans le server
                    start_ticks = time.time()

                if (is_client == True):
                    if ((
                            time.time() - start_ticks) > 0.5):  # we need to take ticks for money update for the client in order for him not to gain infinite sum of money
                        player_one.gain(2)  # Fait gagner de l'argent
                        # print("money event")
                        start_ticks = time.time()  # update "fake ticks" for client
