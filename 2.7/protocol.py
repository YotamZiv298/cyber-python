import os

from server import BUF_SIZE

LENGTH_FIELD_SIZE = 4
PORT = 8820

DIR_CMD = "DIR"
DELETE_CMD = "DELETE"
COPY_CMD = "COPY"
EXECUTE_CMD = "EXECUTE"
TAKE_SCREENSHOT_CMD = "TAKE_SCREENSHOT"
SEND_PHOTO_CMD = "SEND_PHOTO"
EXIT_CMD = "EXIT"


def check_cmd(data):
    """
    Check if the command is defined in the protocol, including all parameters.

    :param data: Command with params.
    :return: True if the command is defined in the protocol, else False.
    """
    data = data.split()

    if data[0] == TAKE_SCREENSHOT_CMD or data[0] == SEND_PHOTO_CMD or data[0] == EXIT_CMD:
        if len(data) == 1:
            return True
    elif data[0] == DIR_CMD:
        if len(data) == 2 and os.path.isdir(data[1]):
            return True
    elif data[0] == DELETE_CMD or data[0] == EXECUTE_CMD:
        if len(data) == 2 and os.path.isfile(data[1]):
            return True
    elif data[0] == COPY_CMD:
        if len(data) == 3 and os.path.isfile(data[1]) and os.path.isdir(data[2].rsplit('\\', 1)[0]):
            return True

    return False


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
