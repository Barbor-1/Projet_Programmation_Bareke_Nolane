from networking import client

client = client(ip_address='127.0.0.1', port="12345")
client.startClient()
client.send("HELLO")
print(client.readline())
client.close()
