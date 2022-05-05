from demon_tcp import demon
from multiprocessing import Process, JoinableQueue

input_queue = JoinableQueue() # Queue with task_done and join()
output_queue = JoinableQueue()
test = demon(input_queue, output_queue, port=12345)
input_queue.put("HELLO")
test.daemon = True
if __name__ == "__main__":
    test.start() # start demon
    while True:
        input_queue.put("GET_UNIT")

