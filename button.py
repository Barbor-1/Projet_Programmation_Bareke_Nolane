
import pygame
class Button:
    def __init__(self, x, y, color, background_color, screen, size=32):
        self.x = x
        self.y = y
        self.screen = screen
        self.color = color
        self.size = size
        self.background_color = background_color
    def initButton(self, label, center=False): # Initialisation
        self.label = label
        smallfont = pygame.font.SysFont("Sprite/CORBEL.TTF",self.size) # can change it ?
        self.text = smallfont.render(self.label, True , self.color) # render font
        if(center == False): # for button centering
            self.text_rect = self.text.get_rect(topleft=(self.x, self.y)) # get rectangle
        else:
            self.text_rect = self.text.get_rect(center=(self.x, self.y)) # get rectangle

    def drawButton(self): # Affiche le bouton
        pygame.draw.rect(self.screen, self.background_color, (self.text_rect.x, self.text_rect.y, self.text_rect.width, self.text_rect.height))
        self.screen.blit(self.text, self.text_rect) # blit it
    def collide(self, pos): # Appeler quand on clique sur le bouton
        return self.text_rect.collidepoint(pos)


