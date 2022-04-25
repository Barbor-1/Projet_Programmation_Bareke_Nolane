import pygame


class Screen():
    def __init__(self, title, width=640, height=445, fill=(255, 255, 255)):
        self.title = title
        self.width = width
        self.height = height
        self.fill = fill
        self.current = False

    def makeCurrent(self):
        self.current = True
        # update screen
        pygame.display.set_caption(self.title)
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill(self.fill)
        pygame.display.flip()

    def endCurrent(self):
        self.current = False

    def getScreen(self):
        return self.screen
