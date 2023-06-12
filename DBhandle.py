import sqlite3
import HashMD5

connection = sqlite3.connect('Usersdb.db')
cursor = connection.cursor()

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
    users = []

    users.append(User('David', 'Lenovo'))
    users.append(User('Moshe', 'Asus'))

    for user in users:

        run(f""" INSERT INTO users (username, password) VALUES('{user.username}',
                '{user.password}')""")
        print(user)

initialize_db()