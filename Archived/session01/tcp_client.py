import socket
target_host = "10.0.1.68" # home-lab 
target_port = 80

# create a socket object 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# create the client
client.connect((target_host, target_port))

# send some data 
client.send(b'GET / HTTP/1.1\r\nHost: 10.0.1.68\r\n\r\n')

# receive some data 
response = client.recv(4096)

print(response)