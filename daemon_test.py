import multiprocessing
from demon_tcp import demon
from multiprocessing import process, JoinableQueue
from multiprocessing import Manager
import pickle, pygame
from unit.unit import Unit
input_queue = JoinableQueue() # Queue with task_done and join()
output_queue = JoinableQueue()
test = demon(input_queue, output_queue, port="12345")
test.daemon = True

if __name__ == "__main__":
    test.start() # start demon
    #IMPORTANT : start process before callig pygame.init() !
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    unit1 = Unit(screen,0, 1)
    data = ("SET_UNIT ") + str(unit1) + "\n"
    print("command send")
    input_queue.put(data)
    input_queue.join()
    print(output_queue.get())

