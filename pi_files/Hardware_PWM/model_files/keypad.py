import json
import os
from cryptography.fernet import Fernet

class Keypad:
    def __init__(self):
        self.file_path = "Hardware_PWM/persistence_files/pin.json"
        self.key_file = "Hardware_PWM/persistence_files/key.key"
        self.create_key()    # Ensure key is created
        self.pin = self.read_passkey()

    def read_passkey(self):
        data = self.decrypt_data()      # decrypt the json file
        json_data = json.loads(data.decode("utf-8"))    # convert the data into a python dictionary
        return json_data["passkey"]

    def change_passkey(self, new_key):
        data = self.decrypt_data()
        json_data = json.loads(data.decode("utf-8"))

        json_data['passkey'] = new_key
        data = json.dumps(json_data).encode("utf-8")
        
        encrypted_data = self.encrypt_data(data)

        with open(self.file_path, 'wb') as file:
            file.write(encrypted_data)

    def create_key(self):
        if not os.path.exists(self.key_file):
            key = Fernet.generate_key()
            with open(self.key_file,'wb') as file:  # save key
                file.write(key)

            with open(self.file_path, "rb") as file:  # read in the json file
                data = file.read()

            fernet = Fernet(key)
            encrypted_data = fernet.encrypt(data)   # encrypt the json file

            with open(self.file_path, "wb") as file:   # save the encrypted json file
                file.write(encrypted_data)


    def decrypt_data(self):
        with open(self.key_file, "rb") as file:
            key = file.read()
        
        with open(self.file_path, 'rb') as file:
            encrypted_data = file.read()

        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data)

        return decrypted_data

    def encrypt_data(self, data):
        with open(self.key_file, 'rb') as file:
            key = file.read()
        
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data)

        return encrypted_data

