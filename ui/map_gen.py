import pygame
from pytmx.util_pygame import load_pygame # 2.7 mode !

class Map: # for background not used here
    """used to load an image and draw it (in the background)

    :param screen: surface to draw on
    :type screen: pygame.Surface
    :param image_path: path to image
    :type image_path: string

    """
    def __init__(self, screen, image_path):
        """init function
       
        """

        self.screen = screen
        self.path = image_path
    def display_map(self):
        """draw image
        """
        self.image =  pygame.image.load(self.path)
        self.screen.blit(self.image, (0, 0))
class Background(Map): # for Tiled map
    """class for tiled map

    :param Map: inherit from Map class
    """
    def display_map(self):
        """draw map
        """
        self.tiled_map = load_pygame(self.path) # IMPORTANT : video mode must be set + same size plz
        layer = self.tiled_map.layers[0]
        for x, y, image in layer.tiles():
            self.screen.blit(image, (x*32, y*32+60)) # 32 because tile are 32*32 and 60 because there is a toolbar of 60 of height at the top
            prop = self.tiled_map.get_tile_properties(x, y, 0) #layer 0
            #print(prop)
    def is_water(self, x, y):
        """test if point (x, y), is on water

        :param x: position x of the point
        :type x: int
        :param y: position y of the point
        :type y:  int
        :return: True if on water, otherwise return False
        :rtype: bool

        """
        prop = self.tiled_map.get_tile_properties(x, y, 0) #layer 0
        return (prop["isWater"])
