import re


class IP():
    """is not used !
    """
    def __init__(self, ip=""):
        self.ip_str = ip

    def to_bit(self):
        temp = self.ip_str.split(".")
        ret = []
        for i in temp:
            ret.append(int(i))
        return ret

    def from_bit(self, bit_ip):
        self.ip_str = ""
        for i in range(0, len(bit_ip)):
            self.ip_str += str(bit_ip[i])
            if(i != len(bit_ip) - 1):
                self.ip_str += "."
        return self.ip_str

    def netmask_and(self, netmask_bit):
        ret = []
        bit_ip = self.from_bit()
        for i in range(0, len(bit_ip)):
            ret.append(bit_ip[i] & netmask_bit[i])
        return ret

    def netmask_to_str(self, netmask_bit):
        string = ""
        for i in range(0, len(netmask_bit)):
            string += str(netmask_bit[i])
            if(i != len(netmask_bit) - 1):
                string += "."
        return string
    def netmask_to_bit(self, netmask_str):
        temp = netmask_str.split(".")
        ret = []
        for i in temp:
            ret.append(int(i))
        return ret
    def test_ip(self, bit_ip1, bit_ip2):
        for i in range(0, len(bit_ip1)):
            if(bit_ip1[i] != bit_ip2[i]):
                return False
        return True
