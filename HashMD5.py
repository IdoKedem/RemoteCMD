import hashlib

def encrypt(text):
    encrypted = hashlib.md5(text.encode('utf-8'))
    return encrypted.hexdigest()

