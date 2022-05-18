import pygame

pygame.init()
fliped = False
screen = pygame.display.set_mode((1920, 1080)) # useless, only for testing purposes
#pygame.display.set_caption("RTS GAME - v1")


image = pygame.image.load("Sprite/Placeholder.png")
rect = image.get_rect()
screen.blit(image, rect)
while True:
    screen.fill((0, 0, 0))
    rect.move_ip(1, 1)
    screen.blit(image, rect)
    pygame.display.flip()
