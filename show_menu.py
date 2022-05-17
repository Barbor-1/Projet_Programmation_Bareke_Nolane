from button import Button
from textbox import  Textbox
import  pygame


class ShowMenu():
    def __init__(self, menu_screen):
        self.screen = menu_screen
        self.ip = ""
        self.is_client = False
        self.port = "12345"
        self.start_client = Button(100, 150, (255, 255, 255), (255, 0, 0), self.screen)
        self.start_server = Button(800-200, 150, (255, 255, 255), (255, 0, 0), self.screen)
        self.start_client.initButton("START CLIENT")
        self.start_server.initButton("START SERVER")
        self.font = pygame.font.SysFont('Corbel', 64)
        self.server_text = self.font.render("SERVER", True,(255, 0, 0))
        self.client_text = self.font.render("CLIENT", True,(255, 0, 0))

    def draw(self):
        self.screen.blit(self.client_text, self.server_text.get_rect(topleft=(100, 50))) #TO ADJUST+ dynamic ?
        self.screen.blit(self.server_text, self.server_text.get_rect(topleft=(800-200, 50))) #TO ADJUST + dynamic ?
        self.start_client.drawButton()
        self.start_server.drawButton()
    def collide(self, pos):
        pass
    #if return value == 1 => server has been selectionned
    #if return value == 2 => client has been selectionned








