import socket


class server():
    def __init__(self, port="2001"):  # default value to change
        self.port = port
        self.ip_address = ""

    def startServer(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = ''
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # idk why ?
        self.socket.bind((self.host, int(self.port)))
        self.socket.listen(1)  # one for onyl one client

    def send(self, data, is_byte=False):  # byte = True : no encoding
        if (is_byte == True):
            self.client.send(data)
        else:
            self.client.send(data.encode())

    def receive(self, limit, is_byte=False):  # byte = True : no encoding
        if (is_byte == True):
            return self.client.recv(limit)
        else:
            return (self.client.recv(limit)).decode()

    def accept(self, timeout=0.1):  # timeout important
        self.client, self.addr = self.socket.accept()
        self.client.settimeout(timeout)
        # self.file = self.client.makefile()

    def clientAddr(self):
        return self.addr

    def readline(self):  # read a line from buffer
        str = ""
        chr = self.receive(1)
        while (chr != '\n'):
            str = str + chr
            chr = self.receive(1)
            if (chr == ''):
                print("empty")  # to remove ?
                raise Exception("empty")
        return str

    def close(self, shutdown=True):
        self.client.close()
        if (shutdown == True):
            self.socket.shutdown(socket.SHUT_RDWR)

    def shutdown(self):
        self.client.close()
        self.socket.shutdown(socket.SHUT_RDWR)


class client():
    def __init__(self, ip_address, port="2001"):  # default value to change
        self.port = port
        self.host = ip_address
        # print(port)

    def startClient(self, timeout=0.1):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # ? dont no
        self.socket.connect((self.host, int(self.port)))
        self.socket.settimeout(timeout)  # TODO : CHANGE # see where to put it ? before of after connect ?

        # self.socket.setblocking(False)
        # self.file = self.socket.makefile(mode='rw')

    def send(self, data, is_byte=False):
        if (is_byte == True):
            self.socket.send(data)
        else:
            self.socket.send(data.encode())

    def readline(self):  # read line from buffer
        str = ""
        try:
            chr = self.receive(1)
        except Exception as e:
            raise e
        while (chr != '\n'):
            str = str + chr
            try:
                chr = self.receive(1)
            except Exception as e:
                raise e
            if (chr == ''):
                print("empty")
                raise Exception("empty")
        return str

    def close(self, shutdown=True):  # close
        if (shutdown):
            self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()

    def receive(self, limit, is_byte=False):  # byte = True : no encoding
        if (is_byte == True):
            return (self.socket.recv(limit))
        else:
            return (self.socket.recv(limit)).decode()

# TODO : SCAN ?
