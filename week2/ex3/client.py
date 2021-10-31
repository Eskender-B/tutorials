# Echo client program
import socket

HOST = '127.0.0.1'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        message = input('Enter message: ')
        s.sendall(message.encode())
        data = s.recv(1024)
        print('Received', data.decode())