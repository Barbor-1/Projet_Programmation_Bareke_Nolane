# TO DO
import pygame


class Toolbar(): #barre en haut avec le soldat
    """
    Toolbar class :
    :param screen : surface
    :param : path to the image
    :param : x : position of the toolbar
    :param : y : position of the toolbar


    """
    def __init__(self, screen, x, y, path):
        self.screen = screen
        self.image_path = path
        self.image = pygame.image.load(self.image_path)

        self.x = x
        self.y = y

        self.rect = self.image.get_rect()
        self.rect.move(self.x, self.y)

        self.font = pygame.font.SysFont("Sprite/CORBEL.TTF",12)
        self.text = self.font.render("30", True , (0, 0, 0)) # render font

    def draw(self):  #affiche la barre : ne pas oublier de refresh la surface et l'écran
        """
        draw the toolbar

        :return:
        """
        self.rect = self.image.get_rect() # update rect
        self.rect.x= self.x
        self.rect.y = self.y
        self.screen.blit(self.image, (self.x, self.y))
        self.screen.blit(self.text, (self.x, self.y+self.image.get_rect().height + 2))
        #pygame.draw.rect(self.screen, (255, 0, 0), self.rect)


    def collide(self, pos):
        """



        :param pos: position of the mouse
        :return:
        """
        return self.rect.collidepoint(pos)

    def cancel(self):
        """
        cancel animation


        :return:
        """
        #Affiche un symbole stop quand on n'a pas assez de ressource et que l'on clique, le symbole disparait au prochain cycle d'affichage
        self.image = pygame.image.load("Sprite/Cancel-1.png")
        self.screen.blit(self.image, (self.x, self.y))
        self.image = pygame.image.load(self.image_path)
    #todo move function
