import pygame


class Screen(): #surface ? : https://www.pygame.org/docs/ref/surface.html + surface.blit()
    def __init__(self, title, width=640, height=445, fill=(255, 255, 255)):
        self.title = title
        self.width = width
        self.height = height
        self.fill = fill
        self.current = False
        self.screen = pygame.display.set_mode((self.width, self.height))

    def makeCurrent(self):
        self.current = True
        # update screen
        pygame.display.set_caption(self.title)
        self.screen = pygame.display.set_mode((self.width, self.height)) # ? to delete (see later)
        self.screen.fill(self.fill)
        pygame.display.flip()

    def endCurrent(self): # TODO : IMPORTANT : make this function do something with makeCurrent(self)
        self.current = False

    def getScreen(self):
        return self.screen
