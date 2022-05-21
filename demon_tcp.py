from ast import arg
from queue import Empty, Queue
from traceback import print_tb
from networking import client, server
import multiprocessing
import sys



class Demon(multiprocessing.Process):
    def __init__(self, input_queue, output_queue, is_client=True, address="127.0.0.1", port="1234"): # change address
        super().__init__()
        self.port = port
        self.is_client = is_client
        self.address = address
        if(self.is_client == True):
            self.comm = client(self.address, self.port)
        else:
            self.comm = server(self.port)
            # self.comm.startClient() # TODO : ERROR MANAGEMENT
        self.input_queue = input_queue
        self.output_queue = output_queue

    def run(self):  # main loop to call with multiprocessing : only client do server later
        running = True
        retry = True

        if(self.is_client == False):            
            self.comm.startServer() 
            self.comm.accept() 
            print("got a client !")
        else:
            print("not a server !", flush=True)
            while (retry == True):
                retry = False # pour réesayer de se connecter ? => compteur ? 
                try:
                    self.comm.startClient(5)  
                except Exception as e:
                    print("exception while trying to connect for the first time", e)
                    retry = True
            
            self.comm.startClient()
                    

        print("connected")
        self.output_queue.put("CONNECTED")
        sys.stdout.flush()
        # TODO : see what do if client leaves ?
        while(running == True):

            # GET UNIT FROM SERVER => TO PROCESS
            # TODO : COMMAND PROCESS
            """ self.unit_list.append(
                self.comm.readline().strip('\n')
                ) # read a line (see for multiples lines to read)
            """
            temp = ""
            #print("running")    
            sys.stdout.flush()
            try:
                temp = self.comm.readline()  # TODO READLINES ? maybe to see
            except Exception as e:
                #print("exception :", e)
                sys.stdout.flush()
                if e.args[0] != "timed out":
                    print("connexion reset, trying to reconnect", e)
                    self.output_queue.put("DISCONNECTED")
                    self.comm.close(False)
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
            #print("received commands (or not) from network")
            sys.stdout.flush()
            command_receive = temp.split(" ")[0]

            # PAS DE GET UNIT ENTRE SERVEUR ET CLIENT :
            if(command_receive == "SET_UNIT"):
                
                arguments_left = temp.split(" ")[1:]
                print("got a SET_UNIT", temp)

                #Unit_to_add = (arguments_left[0],  arguments_left[1], arguments_left[2] , arguments_left[3], arguments_left[4], arguments_left[5] ,arguments_left[6], arguments_left[7])

                self.output_queue.put(temp)
                sys.stdout.flush()
                
            elif(command_receive == "UPDATE_UNIT"): # UPDATE_UNIT id num_of_element (see setstate unit/unit.py) + data
                self.output_queue.put(temp)

            elif(command_receive == "REMOVE_UNIT"):
                self.output_queue.put(temp)

            elif(command_receive == "UPDATE_PLAYER"):
                self.output_queue.put(temp)

            elif(command_receive == "CLOSE"):
                self.comm.close()
                print("closed connexion")
        
        #COMMANDS FROM QUEUE


            try:
                command = (self.input_queue.get(False))  # nom blocking
            except (Empty, Exception) as e:
                #print("queue empty", e)
                sys.stdout.flush()
                command = ""
                #print("exception at queue reading", e)

            first_arg = command.split(" ")[0]
            sys.stdout.flush()

            if(first_arg == "SET_UNIT"):
                print("got a SET_UNIT", command)
                unit_to_send = command.split(" ")
                unit_to_send.pop(0)
                string2 = ""
                for i in unit_to_send:
                    string2 = string2 + i
                    string2 = string2 + " "
                string = "SET_UNIT " + string2 + "\n"
                print("sending ", string, " ", string2)
                sys.stdout.flush()
                self.comm.send(string, is_byte=False)

            # UPDATE UNIT
            if(first_arg == "UPDATE_UNIT"):
                print("got an update unit", command)
                self.comm.send(command)

            # REMOVE UNIT
            if(first_arg == "REMOVE_UNIT"): # REMOVE_UNIT unit_id
                print("removing unit remotely", flush=True)
                to_send = first_arg + " "
                args = command.split(" ")[1:]
                for i in args:
                    to_send += str(i) # only one arg
                    to_send += " "
                to_send += "\n"
                print("sending remove command", to_send)
                sys.stdout.flush()
                self.comm.send(to_send, is_byte=False)

            if(first_arg == "UPDATE_PLAYER"):
                self.comm.send(command, is_byte=False)

            if(first_arg == "KILL"):
                print("suicide !")
                self.comm.close(shutdown=True)
                return # quit itselt
            #print("cycle ended")
            sys.stdout.flush()

