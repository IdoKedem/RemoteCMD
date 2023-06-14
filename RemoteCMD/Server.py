import socket, os
import DBhandle, HashMD5

SENDING_LOGIN_INFO: str = 'login info incoming!' # special string that is used when transferring login data
SENDING_CMD_COMMAND: str = 'cmd command incoming!' # special string that is used when transferring cmd commands

PORT = 4444
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def get_ipv4_address():
    """
    retrives the user's IP address
    :return: IPv4 address as a string
    """
    hostname = socket.gethostname()
    ip_address: str = socket.gethostbyname(hostname)
    return ip_address

def server_listen():
    ip: str = get_ipv4_address()
    server_socket.bind((ip, PORT))

    server_socket.listen()
    print("Server Waiting...")

def server_accept():
    global client

    client, ip = server_socket.accept()
    print("Server Connected!")

def validate_login():
    """
    this function receives login info and checks if the user
    exists in the databse
    :return: True if the user exists, False otherwise
    """
    sent_data = client.recv(1024).decode()
    login_info = sent_data.split('\n')
    if login_info[0] == SENDING_LOGIN_INFO:
        _, username, password = login_info
        return DBhandle.validate_login(username, HashMD5.encrypt(password))
    return False

def run_cmd_command():
    """
    this function runs the user's given cmd command
    :return: the cmd output
    """
    sent_data = client.recv(1024).decode()
    sent_data = sent_data.split('\n')
    if sent_data[0] == SENDING_CMD_COMMAND:
        _, command = sent_data
        return os.popen(command).read()
    return ''


