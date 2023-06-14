import socket
import DBhandle, HashMD5

SENDING_LOGIN_INFO: str = '$$$' # special string that is used when transferring login data

PORT = 4444
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def server_listen():
    server_socket.bind(('192.168.14.20', PORT))

    server_socket.listen()
    print("Server Waiting...")

def server_accept():
    global client

    client, ip = server_socket.accept()
    print("Server Connected!")

def server_receive():
    msg = client.recv(1024).decode()
    return msg

def validate_login():
    msg = server_receive()
    data = msg.split('\n')
    if data[0] == SENDING_LOGIN_INFO:
        _, username, password = data
        password = HashMD5.encrypt(password)
        return DBhandle.validate_login(username, password)
    return False



