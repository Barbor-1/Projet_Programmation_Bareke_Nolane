import pygame

from button import Button
from textbox import Textbox


class ShowMenu():
    def __init__(self, menu_screen):
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
        self.font = pygame.font.SysFont('CORBEL.TTF', 64)
        self.server_text = self.font.render("SERVER", True, (255, 0, 0))
        self.client_text = self.font.render("CLIENT", True, (255, 0, 0))
        self.textbox_player = Textbox(self.screen, self.width / 2, self.height - 20, 40, 400, (0, 0, 0),
                                      (255, 0, 0))

    def draw(self):
        self.screen.blit(self.client_text,
                         self.server_text.get_rect(center=(self.width / 3, 50)))  # TO ADJUST+ dynamic ?
        self.screen.blit(self.server_text,
                         self.server_text.get_rect(center=(self.width - self.width / 3, 50)))  # TO ADJUST + dynamic ?
        self.start_client.drawButton()
        self.start_server.drawButton()
        self.textbox_player.draw()

    def collide(self, pos, event):
        if( self.textbox_player.listen(event) == True):
            return 3
        if(self.start_client.collide(pos) == True):
            return  2
        if(self.start_server.collide(pos) == True):
            return 1
        return -1 # nothing


    # if return value == 1 => server has been selectionned
    # if return value == 2 => client has been selectionned
    #if return value == 3 => player nmae is available

    def getPlayerText(self):
        pass
