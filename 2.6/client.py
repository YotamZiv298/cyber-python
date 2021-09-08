import socket
import protocol

IP = "127.0.0.1"


def main():
    """
    The main function.

    :return: None.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, protocol.PORT))

    while True:
        user_input = input("Enter command\n")
        valid_cmd = protocol.check_cmd(user_input)

        if valid_cmd:
            command = protocol.create_msg(user_input)
            client_socket.send(command.encode())

            if user_input == protocol.EXIT_CMD:
                break

            valid_res, res_data = protocol.get_msg(client_socket)

            if valid_res:
                print(res_data)
            else:
                print("Response not valid\n")
        else:
            print("Not a valid command")

    print("Closing\n")
    client_socket.close()


if __name__ == "__main__":
    main()
