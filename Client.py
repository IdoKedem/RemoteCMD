import socket, tkinter as tk
import Server


def initialize_app():
    global app
    app = tk.Tk()
    app.geometry('500x400')
    app.title("RemoteCMD by Ido Kedem")


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
    password = password_entry.get()

    data = \
        f"""{Server.SENDING_LOGIN_INFO}\n{username}\n{password}"""
    client_socket.send(data.encode('utf-8'))

    if Server.validate_login():
        clear_window()
        create_cmd_window()
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
    tk.Label(text="REMOTE CMD", font=('ariel', '20')).place(x=150)

    global text_box
    text_box = tk.Text(width=40, height=17)
    text_box.place(x=80, y=40)
    text_box.config(state='disabled')

    cmd_entry = tk.Entry(font=('ariel', 15))
    cmd_entry.place(x=80, y=350)

    tk.Button(command=lambda: send_cmd_command(cmd_entry),
              text="Send", font=('ariel', 11)).place(x=320, y=350)

def send_cmd_command(cmd_entry):
    command = cmd_entry.get()
    clear_entries(cmd_entry)
    data = \
        f"{Server.SENDING_CMD_COMMAND}\n{command}"
    client_socket.send(data.encode('utf-8'))

    show_cmd_output()

def change_text_in_text_box(text):
    text_box.config(state='normal')
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, text)
    text_box.config(state='disabled')

def show_cmd_output():
    output = Server.run_cmd_command()
    change_text_in_text_box(output)



if __name__ == '__main__':
    connect_to_server()

    initialize_app()

    create_login_window()

    app.mainloop()
