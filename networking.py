import socket


class server():
    def __init__(self, port="2001"):  # default value to change
        self.port = port
        self.ip_address = ""

    def startServer(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = ''
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # test
        self.socket.bind((self.host, int(self.port)))
        self.socket.listen(1)


    def send(self, data, is_byte=False):
        if (is_byte == True):
            self.client.send(data)
        else:
            self.client.send(data.encode())

    def receive(self, limit, is_byte=False): # byte = True : no encoding
        if(is_byte == True):
            return (self.client.recv(limit))
        else:
            return (self.client.recv(limit)).decode()

    def accept(self, timeout=5):
        self.client, self.addr = self.socket.accept()
        self.client.settimeout(timeout)
        #self.file = self.client.makefile()

    def clientAddr(self):
        return self.addr

    def readline(self):
        str = ""
        chr = self.receive(1)
        while(chr != '\n'):
            str = str + chr
            chr = self.receive(1)
            if(chr == ''):
                print("empty")
                raise Exception("no data left, connexion dead ? ")
        return str

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
    def startClient(self, timeout=5):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.socket.connect((self.host, int(self.port)))
        self.socket.settimeout(timeout) #TODO : CHANGE
        #self.socket.setblocking(False)
        #self.file = self.socket.makefile(mode='rw')

    def send(self, data, is_byte=False):
        if (is_byte == True):
            self.socket.send(data)
        else:
            self.socket.send(data.encode())

    def readline(self):
        str = ""
        chr = self.receive(1)
        while(chr != '\n'):
            str = str + chr
            chr = self.receive(1)
            if(chr == ''):
                print("empty")
                raise Exception("no data left, connexion dead ? ")
        return str
        

    def close(self, shutdown=True):
        if (shutdown):
            self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()

    def receive(self, limit, is_byte=False): # byte = True : no encoding
        if(is_byte == True):
            return (self.socket.recv(limit))
        else:
            return (self.socket.recv(limit)).decode()

# TODO : SCAN ?
