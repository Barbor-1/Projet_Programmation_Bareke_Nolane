import pygame


class Screen(): #surface ? : https://www.pygame.org/docs/ref/surface.html + surface.blit()
    def __init__(self, title, screen, width=640, height=445, fill=(255, 255, 255) ):
        self.title = title
        self.width = width
        self.height = height
        self.fill = fill
        self.current = False
        self.surface = pygame.Surface((self.width, self.height))
        self.screen = screen

    def makeCurrent(self):
        self.current = True
        # update screen
        pygame.display.set_caption(self.title)
        #self.screen = pygame.display.set_mode((self.width, self.height)) # ? to delete (see later)
        self.surface.fill(self.fill)
        #pygame.display.flip()

    def endCurrent(self): # TODO : IMPORTANT : make this function do something with makeCurrent(self)
        self.current = False


    def getScreen(self):
        return self.surface

    def update(self):
        self.screen.blit(self.surface, (0, 0))

