import multiprocessing
from demon_tcp import demon
from multiprocessing import process, JoinableQueue
from multiprocessing import Manager
import pygame"
from unit.unit import Unit
#from unit.unit import Unit
input_queue = JoinableQueue() # Queue with task_done and join()
output_queue = JoinableQueue()
test = demon(input_queue, output_queue, port="12345")
test.daemon = True # important pour que le process se ferme après que le le script principal s'est terminé !
if __name__ == "__main__":
    test.start() # start demon

    #IMPORTANT : start process before callig pygame.init() !
    #while True:
    input_queue.put("GET_UNIT")
    print("command send\n",flush=True)
    input_queue.join()
    unit1 = output_queue.get()
    if(len(unit1) > 0):
        unit_created = Unit()
        unit_created.setstate(unit1[0])
        print("got a unit1", unit1)
    else:
        print("got nothing")
        
