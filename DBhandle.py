import Server


def validate_login(client_socket, username, password):
    data = \
        f"""{Server.SENDING_DATA}\n{username}\n{password}"""
    client_socket.send(data.encode('utf-8'))
    return Server.server_receive()
