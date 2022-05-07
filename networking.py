import socket


class server():
    def __init__(self, port="2001"):  # default value to change
        self.port = port
        self.ip_address = ""

    def startServer(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = ''
        self.socket.bind((self.host, int(self.port)))
        self.socket.listen(1)

    def send(self, data):
        self.client.send(data.encode())

    def receive(self, limit):
        return (self.client.recv(limit)).decode()

    def accept(self):
        self.client, self.addr = self.socket.accept()
        self.file = self.client.makefile()

    def clientAddr(self):
        return self.addr

    def readline(self):
        return self.file.readline()

    def close(self):
        self.client.close()
    def shutdown(self):
        self.client.close()
        self.socket.shutdown(socket.SHUT_RDWR)


class client():
    def __init__(self, ip_address, port="2001"):  # default value to change
        self.port = port
        self.host = ip_address
        #print(port)
    def startClient(self, timeout=30):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.socket.settimeout(timeout)
        self.socket.connect((self.host, int(self.port)))
        self.file = self.socket.makefile(mode='rw')

    def send(self, data):
        try:
            self.socket.send(data.encode())
        except Exception as e:
            print(e) #TODO TO REMOVE LATER

    def readline(self):
        return self.file.readline()

    def close(self, shutdown=True):
        if (shutdown):
            self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()

    def receive(self, limit):
        return (self.socket.recv(limit)).decode()
# TODO : SCAN ?
