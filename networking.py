from socket import socket


class server():
    def __init__(self):
        self.port = 2001
        self.ip_address = ""

    def startServer(self):
        self.socket = socket.socket()
        self.host = socket.gethostname()
        self.socket.bind((self.host, self.port))

    def send(self, data):
        self.client.send(data)

    def accept(self):
        self.client, self.addr = self.socket.accept()

    def clientAddr(self):
        return self.addr

    def close(self):
        self.socket.close()


class client():
    def __init__(self, ip_address):
        self.port = 2001
        self.host = ip_address

    def startClient(self):
        self.socket = socket.socket()
        self.socket.bind((self.host, self.port))

    def send(self, data):
        self.socket.send(data)

    def close(self):
        self.socket.close()
