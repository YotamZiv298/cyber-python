from datetime import datetime
from random import randrange

from server import SERVER_NAME, BUF_SIZE

LENGTH_FIELD_SIZE = 2
PORT = 8820

TIME_CMD = "TIME"
NAME_CMD = "NAME"
RAND_CMD = "RAND"
EXIT_CMD = "EXIT"


def check_cmd(data):
    """
    Check if the command is defined in the protocol.

    :param data: Command to check.
    :return: True if the command is defined in the protocol, else False.
    """
    return data in [TIME_CMD, NAME_CMD, RAND_CMD, EXIT_CMD]


def create_msg(data):
    """
    Create a valid protocol message, with length field.

    :param data: Data to create a valid protocol message.
    :return: Valid protocol message, with length field.
    """
    return str(len(data)).zfill(LENGTH_FIELD_SIZE) + data


def get_msg(socket):
    """
    Extracts message from protocol, without the length field.

    :param socket: Socket to get the message from.
    :return: If the length is valid returns True and the command, else returns False, "Error".
    """
    msg = socket.recv(BUF_SIZE).decode()

    length = msg[:LENGTH_FIELD_SIZE].lstrip('0')
    cmd = msg[LENGTH_FIELD_SIZE:]

    return (True, cmd) if length.isdigit() else (False, "Error")


def create_server_rsp(cmd):
    """
    Based on the command, creates a proper response.

    :param cmd: Command.
    :return: Response based on the command.
    """
    if cmd == TIME_CMD:
        return str(datetime.now().time())
    elif cmd == NAME_CMD:
        return SERVER_NAME
    elif cmd == RAND_CMD:
        return f"Random number between 0, 10: {randrange(10)}"
    elif cmd == EXIT_CMD:
        return ""
