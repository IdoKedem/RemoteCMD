import socket, tkinter as tk, Server


def send_to_server(msg: str):
    client_socket.send(msg.encode('utf-8'))


if __name__ == '__main__':
    PORT = 4444

    global client_socket

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    Server.server_listen()

    client_socket.connect(('192.168.14.20', PORT))

    Server.server_accept()

    print("Client Connected!")

    Server.server_recive()


    app = tk.Tk()
    app.geometry('600x600')
    app.title("RemoteCMD by Ido Kedem")




    app.mainloop()
