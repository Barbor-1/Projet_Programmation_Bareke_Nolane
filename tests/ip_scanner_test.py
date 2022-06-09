from multiprocessing.connection import Client
from pydoc import cli
import re
from socket import timeout
import netifaces
from networking.networking import client
from networking.ip_utils import IP
import time

def netmask_ip(netmask, ip_address): #TODO reformat with IP class 
    ip_address_bit = []
    netmask_bit = []
    result = []
    temp = ip_address.split(".")
    string = ""
    for i in temp:
        ip_address_bit.append(int(i))
    print(temp)
    temp = netmask.split(".")
    for i in temp:
        netmask_bit.append(int(i))
    for i in range(0, len(netmask_bit)):
        result.append(ip_address_bit[i] & netmask_bit[i])
    for i in range(0, len(result)):
        string += str(result[i])
        if(i != (len(result) - 1)):
            string += "."
    #print("str", string)
    return string
def test_connection(client, ip):
    client.host = ip
    start = time.time()
    try:

        client.startClient(2)
    except Exception as e:
        print("cannot connect", e)
        print(time.time() - start)

        #client.close() pas de connexion établie : on ne ferme pas le socket donc
        return False
    #connection ok 
    client.close()
    return True


# TODO : string to array => class


ifaces_list = []
ct = 0
for i in netifaces.interfaces():
    addr = netifaces.ifaddresses(i)
    try:
        ifaces_list.append(addr[netifaces.AF_INET][0])
        print(ct, addr[netifaces.AF_INET][0])
        ct += 1
    except:
        print("no ip address ")

choice = int(input("your interface choice "))
client = client(ip_address=ifaces_list[choice]["addr"])

try:
    client.startClient()

except Exception as a:
    print("cant connect", a)
client.close()
# we have scanned the ip

begin_ip = netmask_ip(ifaces_list[choice]["netmask"], ifaces_list[choice]["addr"])
IP = IP(begin_ip)
netmask_bit = IP.netmask_to_bit(ifaces_list[choice]["netmask"])
end_ip = []
for i in range(0, len(netmask_bit)):
    #print(255-netmask_bit[i])
    end_ip.append( IP.to_bit()[i] | (255-netmask_bit[i]))
print("end ip ", end_ip)


temp = IP.to_bit()
while ( not IP.test_ip(temp, end_ip)): # not going until broadcast
    #do something
    temp_str = IP.from_bit(temp)
    res = test_connection(client, temp_str)
    
    print("ip ", temp, "res ", res)
    #add 1 to ip
    for i in range(len(netmask_bit)-1, 0, -1):
        if(i == 3):
            if(temp[i] == 255-netmask_bit[i]):
                temp[i-1] += 1
            else:
                temp[i] += 1
        else:
            if(temp[i-1] == 255-netmask_bit[i-1]):
                temp[i-1] = 0
                temp[i] += 1
    #print("ip ", temp)
    
    
        
