import pygame

from ui.button import Button
from ui.textbox import Textbox
import socket
#socket.gethostbyname(socket.gethostname()))


class ShowMenu():
    """handling menu

    :param menu_screen: menu surface
    :type menu_screen: pygame.Surface

    """
    def __init__(self, menu_screen):
        """init the elements of the menu

        """
        self.screen = menu_screen
        self.height = self.screen.get_size()[1]
        self.width = self.screen.get_size()[0]

        self.ip = ""
        self.is_client = False
        self.port = "12345"

        self.start_client = Button(self.width / 3, 150, (255, 255, 255), (255, 0, 0), self.screen)
        self.start_server = Button(self.width - self.width / 3, 150, (255, 255, 255), (255, 0, 0), self.screen)

        self.start_client.initButton("START CLIENT", True)
        self.start_server.initButton("START SERVER", True)

        self.font = pygame.font.SysFont('Sprite/CORBEL.TTF', 64)

        self.server_text = self.font.render("SERVER", True, (255, 0, 0))
        self.client_text = self.font.render("CLIENT", True, (255, 0, 0))

        self.textbox_IP = Textbox(self.screen, self.width / 3, 200, 40, self.server_text.get_rect().width, (0, 0, 0),
                                  (255, 0, 0))
        self.ip_text = self.font.render("IP :", True, (255, 0, 0))
        self.server_ip = self.font.render(socket.gethostbyname(socket.gethostname()), True, (255, 0, 0))

    def draw(self):
        """draw this menu
        """
        self.screen.blit(self.client_text,
                         self.server_text.get_rect(center=(self.width / 3, 50))) 

        self.screen.blit(self.server_text,

                         self.server_text.get_rect(center=(self.width - self.width / 3, 50))) 

        self.screen.blit(self.server_ip,
                         self.server_ip.get_rect(center=(self.width - self.width / 3, 250)))
        self.screen.blit(self.ip_text, 
                        self.ip_text.get_rect(center=(self.width - self.width / 3, 200)))

        self.start_client.drawButton()
        self.start_server.drawButton()
        self.textbox_IP.draw()

    def collide(self, event):
        """check for collision

        :param event: event to check (only one)
        :type event: pygame.Event
        :return:  if return value == 1 => server has been selectionned
                  if return value == 2 => client has been selectionned
                  if return value == 4 => IP has been entered
        :rtype: int
        """

        if(self.textbox_IP.listen(event) == True):
            return 4

        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
            pos = pygame.mouse.get_pos()

            if (self.start_client.collide(pos) == 1):
                return 2

            if (self.start_server.collide(pos) == 1):
                return 1

            return -1  # nothing

    # if return value == 1 => server has been selectionned
    # if return value == 2 => client has been selectionned
    #if return value == 4 => IP has been entered


    def getIpText(self):
        """return the text with has been entered into the textbox of the ip address

        :return: text
        :rtype: string
        """
        return  self.textbox_IP.getText()
