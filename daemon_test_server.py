from copyreg import pickle
from http import server
import multiprocessing

import py
import pygame
from demon_tcp import demon
from multiprocessing import process, JoinableQueue
from multiprocessing import Manager
from unit.unit import Unit
input_queue = JoinableQueue() # Queue with task_done and join()
output_queue = JoinableQueue()
test = demon(input_queue, output_queue, port="12345", is_client=False)
test.daemon = True
pygame.init()
screen = pygame.screen.set_mode((800, 800))
unit1 = Unit(screen,0, 1)
if __name__ == "__main__":
    test.start() # start demon
    input_queue.put("SEND_UNIT " + pickle.loads(unit1))
    input_queue.join()
    print(output_queue.get())

