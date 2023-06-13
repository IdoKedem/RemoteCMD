import socket, sqlite3
import HashMD5

PORT = 4444
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

SENDING_DATA: str = '$$$' # special string that is used when transferring login data

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
    data = msg.split('\n')
    if data[0] == SENDING_DATA:
        _, username, password = data
        return validate_login(username, password)

    print("unknown data")

connection = sqlite3.connect('Usersdb.db')
cursor = connection.cursor()


def validate_login(username, password):
    cursor.execute(f"""SELECT * FROM users WHERE 
                username = '{username}' AND password = '{password}'""")
    data = cursor.fetchone()
    return bool(data)

class User:
    def __init__(self, username, password: str):
        self.username = username
        self.password = HashMD5.encrypt(password)

    def __str__(self):
        return \
            f"Username: {self.username} \nPassword: {self.password}"

def run(command):
    cursor.execute(command)
    connection.commit()

def initialize_db():

    run("""CREATE TABLE IF NOT EXISTS users(
            ID INTEGER PRIMARY KEY, username TEXT, password TEXT)""")
    users = \
        [User('David', 'Lenovo'), User('Moshe', 'Asus')]

    for user in users:
        run(f"""INSERT INTO users (username, password) VALUES('{user.username}',
                '{user.password}')""")
        print(user)

initialize_db()

