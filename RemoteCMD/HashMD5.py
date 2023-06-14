import hashlib

def encrypt(text):
    """
    this function encrypts text to HashMD5
    :param text: utf8 string which will be encrypted
    :return: the hashed string
    """
    encrypted = hashlib.md5(text.encode('utf-8'))
    return encrypted.hexdigest()

