import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 1235))

while True:
    client_socket.send(input('Enter a message:').encode())
    data = client_socket.recv(1024).decode()
    print(data)
