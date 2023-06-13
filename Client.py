import socket, tkinter as tk, Server
import DBhandle
import HashMD5


def connect_to_server():
    PORT = 4444

    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    Server.server_listen()
    client_socket.connect(('192.168.14.20', PORT))

    Server.server_accept()
    print("Client Connected!")


def send_to_server(msg: str):
    client_socket.send(msg.encode('utf-8'))

def validate_login(username_entry, password_entry):
    username = username_entry.get()
    password = HashMD5.encrypt(password_entry.get())

    if DBhandle.validate_login(client_socket, username, password):
        clear_window()
    else:
        clear_entries(username_entry, password_entry)
        tk.Label(text="Try again", font=('ariel, 15')).place(x=185, y=250)

def clear_window():
    for widget in app.winfo_children():
        widget.destroy()

def clear_entries(*entries):
    for entry in entries:
        entry.delete(0, tk.END)


def create_login_window():
    tk.Label(text="Login", font=('ariel', '30')).place(x=180, y=10)

    tk.Label(text="Username:", font=('ariel', '15')).place(x=180, y=80)
    username_entry = tk.Entry(font=('ariel', '13'))
    username_entry.place(x=140, y=110)

    tk.Label(text="Password:", font=('ariel', '15')).place(x=180, y=150)
    password_entry = tk.Entry(font=('ariel', '13'), show='*')
    password_entry.place(x=140, y=180)

    tk.Button(command=lambda: validate_login(username_entry, password_entry),
              text="Login", font=('ariel', '13')).place(x=200, y=210)

def create_cmd_window():
    pass


if __name__ == '__main__':
    connect_to_server()

    app = tk.Tk()
    app.geometry('500x400')
    app.title("RemoteCMD by Ido Kedem")

    create_login_window()


    app.mainloop()
