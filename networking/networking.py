import socket


class server():
    """
    server class
    """
    def __init__(self, port="2001"):  # default value to change
        """

        :param port: port number, defaults to "2001"
        :type port: string, optional
        """
        self.port = port
        self.ip_address = ""

    def startServer(self):
        """
        start server
        :return:
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = ''
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # idk why ?
        self.socket.bind((self.host, int(self.port)))
        self.socket.listen(1)  # one for onyl one client

    def send(self, data, is_byte=False):  # byte = True : no encoding
        """send data

        :param data: data to send
        :type data: string if is_byte = False, otherwise byte
        :param is_byte: if byte = True : no encoding , defaults to False
        :type is_byte: bool, optional
        """
        if (is_byte == True):
            self.client.send(data)
        else:
            self.client.send(data.encode())

    def receive(self, limit, is_byte=False):  # byte = True : no encoding
        """receive data

        :param limit: receive limit
        :type limit: int
        :param is_byte: if byte = True : no encoding , defaults to False
        :type is_byte: bool, optional
        :return: data in string if is_byte = False, otherwise in byte form
        :rtype:  string or byte
        """
        if (is_byte == True):
            return self.client.recv(limit)
        else:
            return (self.client.recv(limit)).decode()

    def accept(self, timeout=0.1):  # timeout important
        """accept client (only one)

        :param timeout: timeout, defaults to 0.1s
        :type timeout: float, optional
        """
        self.client, self.addr = self.socket.accept()
        self.client.settimeout(timeout)
        # self.file = self.client.makefile()

    def clientAddr(self):
        """return client address

        :return: address
        :rtype: string
        """
        return self.addr

    def readline(self):  # read a line from buffer
        """read a line from buffer

        :raises Exception: if buffer is empty => client disconnected
        :return: data read without \n
        :rtype: string 
        """
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
        """close connexion

        :param shutdown: if True, also shutdown socket, defaults to True
        :type shutdown: bool, optional
        """
        try:
            self.client.close()
        except:
            pass
        if (shutdown == True):
            try:
                self.socket.shutdown(socket.SHUT_RDWR)
            except:
                pass

    def shutdown(self):
        """
        shutdown socket

        """
        self.client.close()
        self.socket.shutdown(socket.SHUT_RDWR)


class client():
    """client class

    """
    def __init__(self, ip_address, port="2001"):  # default value to change
        """init

        :param ip_address: ip address to connect into
        :type ip_address: _type_
        :param port: _description_, defaults to "2001"
        :type port: str, optional
        """
        self.port = port
        self.host = ip_address
        # print(port)

    def startClient(self, timeout=0.1):
        """start client

        :param timeout: timeout in seconds, defaults to 0.1s
        :type timeout: float, optional
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # ? dont no
        self.socket.connect((self.host, int(self.port)))
        self.socket.settimeout(timeout)  # TODO : CHANGE # see where to put it ? before of after connect ?

        # self.socket.setblocking(False)
        # self.file = self.socket.makefile(mode='rw')

    def send(self, data, is_byte=False):
        """
         send data

        :param data: data to send
        :type data: string if is_byte = False, otherwise byte
        :param is_byte: if byte = True : no encoding , defaults to False
        :type is_byte: bool, optional
        """
        if (is_byte == True):
            self.socket.send(data)
        else:
            self.socket.send(data.encode())

    def readline(self):  # read line from buffer
        """read a line from buffer

        :raises Exception: if buffer is empty => client disconnected
        :return: data read without \n
        :rtype: string 
        """
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
        """close socket

        :param shutdown: if true, also shutdown socketx, defaults to True
        :type shutdown: bool, optional
        """
        try:
            if (shutdown):
                self.socket.shutdown(socket.SHUT_RDWR)
            self.socket.close()
        except:
            pass

    def receive(self, limit, is_byte=False):  # byte = True : no encoding
        """receive data

        :param limit: receive limit
        :type limit: int
        :param is_byte: if byte = True : no encoding , defaults to False
        :type is_byte: bool, optional
        :return: data in string if is_byte = False, otherwise in byte form
        :rtype:  string or byte
        """
        if (is_byte == True):
            return (self.socket.recv(limit))
        else:
            return (self.socket.recv(limit)).decode()

# TODO : SCAN ?
