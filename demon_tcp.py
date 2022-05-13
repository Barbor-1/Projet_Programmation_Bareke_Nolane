import pickle
from queue import Empty, Queue
from networking import client, server
import multiprocessing
import sys


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
            # self.comm.startClient() # TODO : ERROR MANAGEMENT
        self.input_queue = input_queue
        self.output_queue = output_queue
        self.unit_list = []

    def run(self):  # main loop to call with multiprocessing : only client do server later
        running = True
        if(self.is_client == False):
            self.comm.accept()
            self.comm.startServer()  # IMPORTANT : to avoid pickle error
        else:
            self.comm.startClient(5)  # IMPORTANT : to avoid pickle error
        print("connected")
        sys.stdout.flush()
        # TODO : see what do if client leaves ?
        while(running == True):
            # DEBUG

            # GET UNIT FROM SERVER => TO PROCESS
            # TODO : COMMAND PROCESS
            """ self.unit_list.append(
                self.comm.readline().strip('\n')
                ) # read a line (see for multiples lines to read)
            """
            print("running")
            sys.stdout.flush()
            temp = ""
            try:
                temp = self.comm.readline()  # TODO READLINES
            except Exception as e:
                if e.args[0] != "timed out":
                    print("connexion reset, trying to reconnect")
                    if(self.is_client):
                        try:
                            self.comm.startClient()
                        except:
                            pass
                    else:
                        try:
                            self.comm.accept()
                        except:
                            pass
            sys.stdout.flush()
            
            print("receiving commands")
            sys.stdout.flush()
            command_receive = temp.split(" ")[0]

            # PAS DE GET UNIT ENTRE SERVEUR ET CLIENT :

            if(command_receive == "SET_UNIT"):  # TODO : complete with pickling
                pass
            elif(command_receive == "UPDATE_UNIT"):
                pass
            elif(command_receive == "REMOVE_UNIT"):
                pass

            try:
                command = (self.input_queue.get(False))  # nom blocking
            except Empty:
                print("queue empty")
                sys.stdout.flush()
                command = ""
            if(command == "GET_UNIT"):
                self.output_queue.put(self.unit_list)  # return severals unit
                self.input_queue.task_done()

            first_arg = command.split(" ")[0]
            print("first arg", first_arg)
            sys.stdout.flush()

            if(first_arg == "SET_UNIT"):
                unit_to_send = command.split(" ")
                print("list", unit_to_send)
                unit_to_send.pop(0)
                string2 = ""
                for i in unit_to_send:
                    string2 = string2 + i
                    string2 = string2 + " "
                string = "SET_UNIT " + string2 + "\n"
                print("sending ", string, " ", string2)
                sys.stdout.flush()
                self.comm.send(string, is_byte=False)
                self.input_queue.task_done()

            # UPDATE UNIT
            if(first_arg == "UPDATE_UNIT"):
                pass

            # REMOVE UNIT
            if(first_arg == "REMOVE_UNIT"):
                pass
