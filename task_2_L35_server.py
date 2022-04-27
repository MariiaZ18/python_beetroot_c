import socket
from threading import Thread


class Client(Thread):
    def __init__(self, host, port):
        Thread.__init__(self)
        self.host = host
        self.port = port

    def run(self):
        while True:
            data = conn.recv(2048)
            if not data:
                break
            conn.sendall(data)
        conn.close()


host = '127.0.0.1'
port = 65432
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
threads = []

while True:
    s.listen(4)
    print("Waiting for connections from  clients...")
    (conn, (ip, port)) = s.accept()
    new_thread = Client(host, port)
    new_thread.start()
    threads.append(new_thread)
    for thread in threads:
        thread.join()