from datetime import datetime
from random import randrange

LENGTH_FIELD_SIZE = 2
PORT = 8820

COMMANDS = ["TIME", "NAME", "RAND", "EXIT"]


def check_cmd(data):
    """
    Check if the command is defined in the protocol (e.g TIME, NAME, RAND, EXIT)
    """
    return data in COMMANDS


def create_msg(data):
    """
    Create a valid protocol message, with length field
    """
    return str(len(data)).zfill(LENGTH_FIELD_SIZE) + data


def get_msg(socket):
    """
    Extract message from protocol, without the length field
       If length field does not include a number, returns False, "Error"
    """

    return True, "Hello"


def create_server_rsp(cmd):
    """
    Based on the command, create a proper response
    """
    if cmd == COMMANDS[0]:
        return datetime.now().time()
    elif cmd == COMMANDS[1]:
        return "SERVER NAME: Yotam's server"
    elif cmd == COMMANDS[2]:
        return randrange(10)
    else:
        return "Server response"
