import multiprocessing
import random

from demon_tcp import demon
from multiprocessing import process, JoinableQueue
import time
input_queue = JoinableQueue() # Queue with task_done and join()
output_queue = JoinableQueue()
test = demon(input_queue, output_queue, port="12345", is_client=False)
test.daemon = True
id = 0
rand = random.Random()

if __name__ == "__main__":
    test.start() # start demon
    import pygame # IMPORTANT ! import after starting demon !
    from unit.unit import Unit
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    while True:
        unit1 = Unit(screen, -1, id)
        unit1.pos_y = random.randint(0, 19)
        id = id + 1
        input_queue.put("SET_UNIT " + str(unit1) + "\n")
        #input_queue.join()
        #data_out = output_queue.get()
        print("sending unit", unit1.getPosY(), unit1.getPosX())
        time.sleep(rand.randint(5, 10))


