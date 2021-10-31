# Echo server program
import socket
import threading

def threaded_func(conn):
    with conn:
        while True:
            data = conn.recv(1024)
            if not data: break
            conn.sendall(data)


HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        print('Connected by', addr)
        threadObject = threading.Thread(target=threaded_func, args=[conn])
        threadObject.start()
       