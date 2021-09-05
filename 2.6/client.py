import socket

import protocol

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", protocol.PORT))

while True:
    user_input = input("Enter command\n")
    valid_cmd = protocol.check_cmd(user_input)

    if valid_cmd:
        command = protocol.create_msg(user_input)
        client_socket.send(command.encode())

        if command == "EXIT":
            break

        res_data = protocol.create_server_rsp(command)

        if res_data:
            print(res_data)
        else:
            print("Response not valid\n")
    else:
        print("Not a valid command")

print("Closing\n")
client_socket.close()
