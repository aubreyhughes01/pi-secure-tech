import json

class Keypad:
    def __init__(self):
        self.file_path = "./key.json"
        self.pin = self.read_passkey()

    def read_passkey(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            return data["passkey"]

    def change_passkey(self, new_key):
        with open(self.file_path, 'r') as file:
            data = json.load(file)

        data['passkey'] = new_key

        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

