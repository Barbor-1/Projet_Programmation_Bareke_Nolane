from ipaddress import ip_address
from networking import client, server
from mailbox_tcpDemon import MailboxTcp
import multiprocessing

class demon(multiprocessing.Process):
    def __init__(self, input_queue, output_queue, is_client=True, address="127.0.0.1", port="1234"):
        super().__init__()
        self.port = port
        self.is_client = is_client
        self.address = address
        if(self.is_client == True):
            self.comm = client(self.address, self.port)
        else:
            self.comm = server()
            #self.comm.startClient() # TODO : ERROR MANAGEMENT 
        self.input_queue = input_queue
        self.output_queue = output_queue

    def run(self): #main loop to call with multiprocessing
        running = True # TODO : SET daemon=true in order for this process to be killed when the games end
        while(running == True):
            #DEBUG
            self.output_queue.put(self.input_queue.get())
            self.input_queue.task_done()

    
