import socket

host = '127.0.0.1'
port = 65432
BUFFER_SIZE = 2000
message = input("Enter message: ").encode()

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((host, port))
c.send(message)
data = c.recv(BUFFER_SIZE)
print(data)
message = input("Enter message: ").encode()

c.close()
