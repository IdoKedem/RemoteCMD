import socket

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

def server_recive():
    msg = client.recv(1024)
    print(msg.decode())

if __name__ == '__main__':
    # PORT = 4444
    # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #
    # server_socket.bind(('192.168.14.20', PORT))
    #
    # server_socket.listen()
    # print("Server Waiting...")
    #
    # client, ip = server_socket.accept()
    # print("Server Connected!")
    #
    # a = client.recv(1024).decode()
    # print(a)

    pass