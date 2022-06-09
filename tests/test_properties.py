from ui.map_gen import  Background
import  pygame
pygame.init()
screen = pygame.display.set_mode((800, 800))  # menu => taille 800*800
background = Background(screen, "../Sprite/Fond_ecran.tmx")  # charge la carte
background.display_map()
