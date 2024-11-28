from cryptography.fernet import Fernet

#Generates a encrpytion key
def generate_key():
    return Fernet.generate_key()

#encrypt a message
def encrypt_message(key, message):
    #stores an existing key
    fernet = Fernet(key)
    return fernet.encrypt(message.encode())

#decrypt a message
def decrypt_message(key, encrypted_message):
    #stores an existing key
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_message).decode()

#encrpyts a file
def encrypt_file(key, input_filepath):
    #opens and reads a file to be encrpyted
    with open(input_filepath, 'rb') as file:
        data = file.read()
    #stores an existing key
    fernet = Fernet(key)
    return fernet.encrypt(data)

#decrpyts a file
def decrypt_file(key, input_filepath):
    #opens and reads an encrpyted file to decrypt it
    with open(input_filepath, 'rb') as file:
        encrypted_data = file.read()
    #stores an existing key
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data)
