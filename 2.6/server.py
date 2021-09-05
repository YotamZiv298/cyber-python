import socket

import protocol

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", protocol.PORT))
server_socket.listen()
print("Server is up and running")

client_socket, client_address = server_socket.accept()
print("Client connected")

while True:
    valid_msg, cmd = protocol.get_msg(client_socket)

    if valid_msg:
        print(f"Client sent: {cmd}")

        if protocol.check_cmd(cmd):
            response = protocol.create_server_rsp(cmd)
        else:
            response = "Wrong command"
    else:
        response = "Wrong protocol"
        client_socket.recv(1024)

    if cmd == "EXIT":
        break
    client_socket.send(response.encode())

print("Closing\n")
client_socket.close()
server_socket.close()
