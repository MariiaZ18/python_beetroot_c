import socket

c_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

mess = "HELLO CLIENT"
c_s.sendto(mess.encode("utf-8"), ('127.0.0.1', 12345))
data, addr = c_s.recvfrom(4096)
print("server says")
print(str(data))
c_s.close()
