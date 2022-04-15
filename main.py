import pygame
import button
running = True

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("RTS GAME - v1")

button1 = button.Button(0, 0, (255, 255, 255),(255, 0, 0), screen)
button1.setLabel("test")
button1.drawButton()

pygame.display.flip()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()

            if(button1.collide(pos) == 1):
               print("collided")
    