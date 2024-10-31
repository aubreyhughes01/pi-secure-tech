import json
import os
from cryptography.fernet import Fernet

class Keypad:
    def __init__(self):
        self.file_path = "Hardware_PWM/model_files/pin.json"
        self.key_file = "Hardware_PWM/model_files/key.json"
        self.create_key()    # Ensure key is created
        self.pin = self.read_passkey()

    def read_passkey(self):
        data = self.decrypt_data()
        return data["passkey"]

    def change_passkey(self, new_key):
        data = self.decrypt_data()

        data['passkey'] = new_key

        encrypted_data = self.encrypt_data(data)

        with open(self.file_path, 'wb') as file:
            file.write(encrypted_data)

    def create_key(self):
        if not os.path.exists(self.key_file):
            key = Fernet.generate_key()
            with open(self.key_file,'wb') as file:
                file.write(key)

    def decrypt_data(self):
        with open(self.key_file,'rb') as file:
            key = file.read()
        
        with open(self.file_path, 'rb') as file:
            encrypted_data = file.read()

        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data)

        return json.loads(decrypted_data.decode('utf-8'))  # Decode and load JSON

    def encrypt_data(self, data):
        with open(self.key_file, 'rb') as file:
            key = file.read()
        
        fernet = Fernet(key)
        json_data = json.dumps(data).encode('utf-8')  # Convert data to JSON bytes
        encrypted_data = fernet.encrypt(json_data)

        return encrypted_data
