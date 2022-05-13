from networking import server
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
        print(e)
   # unit1 = pickle.loads(unit1)
    print("got unit1")


