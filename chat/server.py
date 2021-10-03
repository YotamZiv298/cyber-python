import socket
from threading import Thread

clients_dict = {}


def session_with_client(sock, num):
    while True:
        clients_dict[num] = sock

        client_data = sock.recv(1024).decode()

        if client_data == 'EXIT':
            break
        client_data = f'Client{num + 1}: {client_data}'
        print(client_data)
        sock.send(client_data.encode())

    sock.close()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 1235))
server_socket.listen(2)

while True:
    print('Server is listening...')
    client_socket, client_address = server_socket.accept()
    print(f'Connection {client_address} has been established')

    t = Thread(target=session_with_client, args=[client_socket, len(clients_dict)])
    t.start()

    if not len(clients_dict):
        break

server_socket.close()
