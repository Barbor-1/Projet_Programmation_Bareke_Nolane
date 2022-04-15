import socket


class server():
    def __init__(self):
        self.port = 2001
        self.ip_address = ""

    def startServer(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = ''
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
    def send(self, data):
        self.client.send(data.encode())
    def receive(self, limit):
        return (self.client.recv(limit)).decode()
    def accept(self):
        self.client, self.addr = self.socket.accept()

    def clientAddr(self):
        return self.addr

    def close(self):
        self.client.shutdown(socket.SHUT_RDWR)
        self.client.close()

class client():
    def __init__(self, ip_address):
        self.port = 2001
        self.host = ip_address

    def startClient(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def send(self, data):
        self.socket.send(data.encode())

    def close(self):
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()
    
    def receive(self, limit):
        return (self.socket.recv(limit)).decode()