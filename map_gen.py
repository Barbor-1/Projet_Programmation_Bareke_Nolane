import pygame

from pytmx.util_pygame import load_pygame # 2.7 mode !

class Map:
    def __init__(self, screen, image_path):
        self.screen = screen
        self.path = image_path
    def display_map(self):
        self.image =  pygame.image.load(self.path)
        self.screen.blit(self.image, (0, 0))
class Background(Map):

    def display_map(self):
        tiled_map = load_pygame(self.path) # IMPORTANT : video mode must be set + same size plz
        layer = tiled_map.layers[0]
        for x, y, image in layer.tiles():
            self.screen.blit(image, (x*32, y*32+60))

