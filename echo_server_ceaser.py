import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65435  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            key = "hello"
            letters = 'abcdefghijklmnogpqrstuvwxyz'
            result = ''
            for i in range(len(letters)):
                for char in key:
                    if char in letters:
                        num = letters.find(char)
                        num = num - key
                        if num < 0:
                            num = num + len(letters)
                        result = result + letters[num]
                    else:
                        result = result + char
            if not data:
                break
            conn.sendall(data)
