from networking import client

client = client(ip_address='127.0.0.1')
client.startClient()
client.send("HELLO")
client.close()