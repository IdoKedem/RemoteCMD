import sqlite3
import HashMD5


connection = sqlite3.connect('Usersdb.db')
cursor = connection.cursor()

def validate_login(username, password):
    """
    checks whether a user exists in the database using their
    username and password
    :param username: the username
    :param password: hashed password
    :return: True if the user exists, False otherwise
    """
    cursor.execute(f"""SELECT * FROM users WHERE
                username = '{username}' AND password = '{password}'""")
    user_row = cursor.fetchone()
    return bool(user_row)

class User:
    def __init__(self, username, password: str):
        self.username = username
        self.password = HashMD5.encrypt(password)

    def __str__(self):
        return \
            f"Username: {self.username} \nPassword: {self.password}"

def run(command):
    """
    this function runs a sqlite3 command in the database
    :param command: the command
    :return:
    """
    cursor.execute(command)
    connection.commit()

def initialize_db():
    """
    this function initialize the database at the start of the script
    with the permitted users
    :return:
    """
    run("""CREATE TABLE IF NOT EXISTS users(
            ID INTEGER PRIMARY KEY, username TEXT, password TEXT)""")
    users = \
        [User('David', 'Lenovo'), User('Moshe', 'Asus')]

    for user in users:
        run(f"""INSERT INTO users (username, password) VALUES('{user.username}',
                '{user.password}')""")
        print(user)

initialize_db()
