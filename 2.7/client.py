import os
import socket

import protocol

IP = "127.0.0.1"

PHOTO_NAME = "screenshot"
PHOTO_TYPE = "jpg"
SAVED_PHOTO_LOCATION = os.getcwd() + fr"\client_files\{PHOTO_NAME}.{PHOTO_TYPE}"


def handle_server_response(client_socket, cmd):
    """
    Receive the response from the server and handle it, according to the request.

    :param client_socket: The socket of the client.
    :param cmd: Command given by the user.
    :return: None.
    """
    valid_protocol, data = protocol.get_msg(client_socket)

    if valid_protocol:
        if cmd != protocol.SEND_PHOTO_CMD:
            print(data)
        else:
            if os.path.isfile(SAVED_PHOTO_LOCATION):
                os.remove(SAVED_PHOTO_LOCATION)

            data_len = int(data)

            with open(SAVED_PHOTO_LOCATION, 'wb') as photo:
                data = client_socket.recv(protocol.BUF_SIZE)
                counter = len(data)

                if valid_protocol:
                    while counter < data_len:
                        photo.write(data)
                        data = client_socket.recv(protocol.BUF_SIZE)

                        if not valid_protocol:
                            break

                        counter += len(data)
                    photo.write(data)
    else:
        print("Error occurred")


def main():
    """
    The main function.

    :return: None.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, protocol.PORT))

    print("Welcome to remote computer application. Available commands are:\n")
    print(f""
          f"{protocol.TAKE_SCREENSHOT_CMD}\n"
          f"{protocol.SEND_PHOTO_CMD}\n"
          f"{protocol.DIR_CMD}\n"
          f"{protocol.DELETE_CMD}\n"
          f"{protocol.COPY_CMD}\n"
          f"{protocol.EXECUTE_CMD}\n"
          f"{protocol.EXIT_CMD}"
          f"")

    while True:
        cmd = input("Please enter command:\n")

        if protocol.check_cmd(cmd):
            packet = protocol.create_msg(cmd)
            client_socket.send(packet.encode())
            handle_server_response(client_socket, cmd)

            if cmd == protocol.EXIT_CMD:
                break
        else:
            print("Not a valid command, or missing parameters\n")

    client_socket.close()


if __name__ == "__main__":
    main()
