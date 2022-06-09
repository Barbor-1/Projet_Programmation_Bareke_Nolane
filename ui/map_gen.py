import pygame
from pytmx.util_pygame import load_pygame # 2.7 mode !

class Map: # for background not used here
    def __init__(self, screen, image_path):
        self.screen = screen
        self.path = image_path
    def display_map(self):
        self.image =  pygame.image.load(self.path)
        self.screen.blit(self.image, (0, 0))
class Background(Map): # for Tiled map

    def display_map(self):
        self.tiled_map = load_pygame(self.path) # IMPORTANT : video mode must be set + same size plz
        layer = self.tiled_map.layers[0]
        for x, y, image in layer.tiles():
            self.screen.blit(image, (x*32, y*32+60)) # 32 because tile are 32*32 and 60 because there is a toolbar of 60 of height at the top
            prop = self.tiled_map.get_tile_properties(x, y, 0) #layer 0
            #print(prop)
    def is_water(self, x, y):
            prop = self.tiled_map.get_tile_properties(x, y, 0) #layer 0
            return (prop["isWater"])
