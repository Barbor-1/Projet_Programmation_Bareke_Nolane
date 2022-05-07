from networking import client, server
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
        self.unit_list = []

    def run(self): #main loop to call with multiprocessing : only client do server later
        running = True # TODO : SET daemon=true in order for this process to be killed when the games end
        self.comm.startClient(5) # to avoid pickle erorr
        while(running == True):
            #DEBUG

            #GET UNIT
            try:
                self.unit_list.append(self.comm.readline()) # read a line (see for multiples lines to read)
            except Exception as e:
                pass

            command = self.input_queue.get()
            if(command == "GET_UNIT"):
                self.output_queue.put(self.unit_list) # return severals unit
            self.input_queue.task_done()
            
            #first_arg = command.split(" ")
            #if(first_arg == "SET_UNIT"):
            #     pass # todo : send unit => see what to send later

    
