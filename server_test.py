from networking import server

server = server()
server.startServer()
server.accept()
while(True):
    data = server.receive(2000)
    if data != "":
        print(data)
    else:
        server.close()
        server.accept()

