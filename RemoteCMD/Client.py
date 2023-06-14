import socket, tkinter as tk
import Server


def initialize_app():
    global app
    app = tk.Tk()
    app.geometry('500x400')
    app.title("RemoteCMD by Ido Kedem")


def get_ipv4_address():
    """
    retrives the user's IP address
    :return: IPv4 address as a string
    """
    hostname = socket.gethostname()
    ip_address: str = socket.gethostbyname(hostname)
    return ip_address

def connect_to_server():
    """
    this function connets to the server without the user needing to
    run the Server.py scripts
    :return:
    """
    PORT = 4444

    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    Server.server_listen()

    ip: str = get_ipv4_address()
    client_socket.connect((ip, PORT))

    Server.server_accept()
    print("Client Connected!")


def send_to_server(msg: str):
    client_socket.send(msg.encode('utf-8'))

def validate_login(username_entry: tk.Entry, password_entry: tk.Entry):
    """
    this function validates the login info the user provided and
    act accordingly
    :param username_entry: the usernames entry
    :param password_entry: the password
    :return:
    """

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
    """
    clears the window from widgets
    :return:
    """
    for widget in app.winfo_children():
        widget.destroy()

def clear_entries(*entries):
    """
    clears text in all given entries
    :param entries: a tuple of all desired entries
    :return:
    """
    for entry in entries:
        entry.delete(0, tk.END)


def create_login_window():
    """
    this function creates the first window the user sees
    :return:
    """
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
    """
    this function creates the second window the user sees
    :return:
    """
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
    """
    this function sends the user's command to the server and shows
    its output
    :param cmd_entry:
    :return:
    """
    command = cmd_entry.get()
    clear_entries(cmd_entry)
    data = \
        f"{Server.SENDING_CMD_COMMAND}\n{command}"
    client_socket.send(data.encode('utf-8'))

    show_cmd_output()

def change_text_in_text_box(text):
    """
    this function changes the text in the cmd output text widget
    :param text: the text that will be inserted
    :return:
    """
    text_box.config(state='normal')
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, text)
    text_box.config(state='disabled')

def show_cmd_output():
    """
    shows the cmd output to the user
    :return:
    """
    output = Server.run_cmd_command()
    change_text_in_text_box(output)



if __name__ == '__main__':
    get_ipv4_address()
    connect_to_server()

    initialize_app()

    create_login_window()

    app.mainloop()
