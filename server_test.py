from networking import server

server = server(port=12345)
server.startServer()
server.accept()
while(True):
    server.send("HELLO\n")
    data = server.readline()
    if data != "":
        print(data)
    else:
        server.close()
        server.accept()

