from demon_tcp import demon
from multiprocessing import Process, JoinableQueue

input_queue = JoinableQueue() # Queue with task_done and join()
output_queue = JoinableQueue()
test = demon(input_queue, output_queue)
input_queue.put("HELLO")
test.daemon = True
if __name__ == "__main__":
    test.start()
    for i in range(0, 10):
        input_queue.put(i)
    input_queue.join() # wait for demon to respond 
    while not output_queue.empty():
        print(output_queue.get())
        