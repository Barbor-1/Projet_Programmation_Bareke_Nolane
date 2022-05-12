import pygame

class Map:
    def __init__(self, screen, image_path):
        self.screen = screen
        self.path = image_path
    def display_map(self):
        self.image =  pygame.image.load(self.path)
        self.screen.blit(self.image, (0, 0))
