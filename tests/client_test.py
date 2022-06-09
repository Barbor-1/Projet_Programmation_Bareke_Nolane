from pydoc import cli
from numpy import byte
import pygame
from networking.networking import client
import pickle
import time
from unit.unit import Unit
client = client(ip_address='127.0.0.1', port="12345")
client.startClient()
print("connected")
pygame.init()
screen = pygame.display.set_mode((800, 800))

unit1 = Unit(screen, 1, 0)
client.send("hello\nbonjour\n")
client.close()
