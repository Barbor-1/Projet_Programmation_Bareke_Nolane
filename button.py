
import pygame
class Button:
    def __init__(self, x, y, color, background_color, screen, size=16):
        self.x = x
        self.y = y
        self.screen = screen
        self.color = color
        self.size = size
        self.background_color = background_color
    def setLabel(self, label):
        self.label = label
    def drawButton(self):
        smallfont = pygame.font.SysFont('Corbel',self.size)
        self.text = smallfont.render(self.label, True , self.color)
        self.text_rect = self.text.get_rect(topleft=(self.x, self.y))
        pygame.draw.rect(self.screen, self.background_color, (self.text_rect.x, self.text_rect.y, self.text_rect.width, self.text_rect.height))

        self.screen.blit(self.text, self.text_rect)
    def collide(self, pos):
        return self.text_rect.collidepoint(pos)


