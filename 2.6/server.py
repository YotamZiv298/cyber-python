import socket
import protocol

BUF_SIZE = 1024
IP = "0.0.0.0"
SERVER_NAME = "Yotam's Server"


def main():
    """
    The main function.

    :return: None
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, protocol.PORT))
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
            client_socket.recv(BUF_SIZE)

        if cmd == protocol.EXIT_CMD:
            break

        response = protocol.create_msg(response)
        client_socket.send(response.encode())

    print("Closing\n")
    client_socket.close()
    server_socket.close()


if __name__ == "__main__":
    main()
