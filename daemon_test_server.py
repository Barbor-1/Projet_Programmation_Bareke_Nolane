import multiprocessing

from demon_tcp import demon
from multiprocessing import process, JoinableQueue

input_queue = JoinableQueue() # Queue with task_done and join()
output_queue = JoinableQueue()
test = demon(input_queue, output_queue, port="12345", is_client=False)
test.daemon = True


if __name__ == "__main__":
    test.start() # start demon
    import pygame # IMPORTANT ! import after starting demon !
    from unit.unit import Unit
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    unit1 = Unit(screen,0, 1)
    unit1.pos_x = 2
    unit1.pos_y = 3
    input_queue.put("SET_UNIT " + str(unit1) + "\n")
    input_queue.join()
    print(output_queue.get())

