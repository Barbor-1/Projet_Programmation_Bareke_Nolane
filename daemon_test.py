import multiprocessing
from demon_tcp import demon
from multiprocessing import process, JoinableQueue
from multiprocessing import Manager

#from unit.unit import Unit
input_queue = JoinableQueue() # Queue with task_done and join()
output_queue = JoinableQueue()
test = demon(input_queue, output_queue, port="12345")
test.daemon = True

if __name__ == "__main__":
    test.start() # start demon
    import pygame
    from unit.unit import Unit
    #IMPORTANT : start process before callig pygame.init() !
    while True:
        print("command send")
        input_queue.put("GET_UNIT")
        input_queue.join()
        unit1 = output_queue.get()
        if(len(unit1) > 0):
            unit_created = Unit()
            unit_created.setstate(unit1[0])
            print("got a unit1", unit1)
        else:
            print("got nothing")
