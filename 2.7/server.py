import glob
import os
import shutil
import socket
import subprocess

import pyautogui

import protocol

BUF_SIZE = 1024

IP = "0.0.0.0"

PHOTO_NAME = "screenshot"
PHOTO_TYPE = "jpg"
PHOTO_PATH = os.getcwd() + fr"\server_files\{PHOTO_NAME}.{PHOTO_TYPE}"


def check_client_request(cmd):
    """
    Breaks cmd to command and parameters and checks if the command and params are good.

    :param cmd: Full command.
    :return:
        valid - True/False.
        command - The requested cmd.
        params - List of the cmd params.
    """
    data = cmd.split()

    valid = True if protocol.check_cmd(cmd) else False
    command = data[0]
    params = data[1:]

    return valid, command, params


def handle_client_request(command, params):
    """
    Creates the response to the client, given the command and params are legal.

    :param command: Command.
    :param params: Parameters for the command.
    :return: The requested data.
    """
    if command == protocol.DIR_CMD:
        files_list = glob.glob(fr"{params[0]}\**\*", recursive=True)

        return '\n'.join(files_list)
    elif command == protocol.DELETE_CMD:
        try:
            os.remove(params[0])

            return "Removed"
        except OSError:
            return "Failed to remove"
    elif command == protocol.COPY_CMD:
        try:
            shutil.copy(params[0], params[1])

            return "Copied"
        except OSError:
            return "Failed to copy"
    elif command == protocol.EXECUTE_CMD:
        try:
            subprocess.call(params[0])

            return "Executed"
        except OSError:
            return "Failed to execute"
    elif command == protocol.TAKE_SCREENSHOT_CMD:
        if os.path.isfile(PHOTO_PATH):
            os.remove(PHOTO_PATH)

        image = pyautogui.screenshot()
        image.save(PHOTO_PATH)

        return "Screenshot taken"
    elif command == protocol.SEND_PHOTO_CMD:
        try:
            return str(os.stat(PHOTO_PATH).st_size)
        except FileNotFoundError:
            return "File does not exist"
    elif command == protocol.EXIT_CMD:
        return "Connection closed"


def main():
    """
    The main function.

    :return: None.
    """
    server_socket = socket.socket()
    server_socket.bind((IP, protocol.PORT))
    server_socket.listen()

    (client_socket, client_address) = server_socket.accept()

    while True:
        valid_protocol, cmd = protocol.get_msg(client_socket)

        if valid_protocol:
            valid_cmd, command, params = check_client_request(cmd)

            if valid_cmd:
                response = handle_client_request(command, params)
                response = protocol.create_msg(response)
                client_socket.send(response.encode())

                if command == protocol.SEND_PHOTO_CMD:
                    with open(PHOTO_PATH, 'rb') as photo:
                        photo_data = photo.read(BUF_SIZE)
                        client_socket.send(photo_data)

                        while photo_data != bytes(''.encode()):
                            photo_data = photo.read(BUF_SIZE)
                            client_socket.send(photo_data)

                if command == protocol.EXIT_CMD:
                    break
            else:
                response = "Bad command or parameters"
                client_socket.send(response.encode())
        else:
            response = "Packet not according to protocol"
            client_socket.send(response.encode())
            client_socket.recv(BUF_SIZE)

    print("Closing connection")
    client_socket.close()
    server_socket.close()


if __name__ == "__main__":
    main()
