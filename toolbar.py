# TO DO
import pygame


class Toolbar():
    def __init__(self, screen, x, y, path):
        self.screen = screen
        self.image_path = path
        self.image = pygame.image.load(self.image_path)

        self.x = x
        self.y = y

        self.rect = self.image.get_rect()
        self.rect.move(self.x, self.y)


    def draw(self):
        self.rect = self.image.get_rect() # update rect
        self.rect.x= self.x
        self.rect.y = self.y
        self.screen.blit(self.image, (self.x, self.y))
        #pygame.draw.rect(self.screen, (255, 0, 0), self.rect)


    def collide(self, pos):
        return self.rect.collidepoint(pos)

    def cancel(self):
        self.image = pygame.image.load("Sprite/Cancel-1.png")
        self.screen.blit(self.image, (self.x, self.y))
        self.image = pygame.image.load(self.image_path)
    #todo move function
