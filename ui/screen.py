import pygame


class Screen(): #surface ? : https://www.pygame.org/docs/ref/surface.html + surface.blit()
    """Surface class

    :param title: title of surface (not used)
    :type title: string
    :param screen: surface to draw on (main pygame screen usually)
    :type screen: pygame.Surface
    :param width: width of surface, defaults to 640
    :type width: int, optional
    :param height: height of surface, defaults to 445
    :type height: int, optional
    :param fill: fill color, defaults to (255, 255, 255)
    :type fill: tuple (3 ints), optional
    
    """
    def __init__(self, title, screen, width=640, height=445, fill=(255, 255, 255) ):
        """init surface

        
        """
        self.title = title
        self.width = width
        self.height = height
        self.fill = fill
        self.current = False
        self.surface = pygame.Surface((self.width, self.height))
        self.screen = screen

    def makeCurrent(self):
        """make surface current
        """
        self.current = True
        # update screen
        pygame.display.set_caption(self.title)
        #self.screen = pygame.display.set_mode((self.width, self.height)) # ? to delete (see later)
        self.surface.fill(self.fill)
        #pygame.display.flip()

    def endCurrent(self): # TODO : IMPORTANT : make this function do something with makeCurrent(self)
        """do nothing : supposed to put this surface into "background mode"
        """
        self.current = False


    def getScreen(self):
        """return surface (pygame object) of this surface object

        :return: surface object
        :rtype: pygame.Surface
        """
        return self.surface

    def update(self):
        """update surface
        """
        self.screen.blit(self.surface, (0, 0))

