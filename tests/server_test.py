from socket import socket
from networking.networking import server
import pickle
from unit.unit import Unit
server = server(port="12345")
server.startServer()
server.accept()
while(True):
    try:
        unit1 = server.readline()
        print(unit1)

    except Exception as e:
        if e.args[0] == "timed out":
            print("timed out")
        else: # ConnectionResetError or something else => test for reset connexion
            print(e)
            print("connexion reset, trying to reconnect")
            server.accept()
   # unit1 = pickle.loads(unit1)
    print("got unit1")
    #server.close()
    #break


