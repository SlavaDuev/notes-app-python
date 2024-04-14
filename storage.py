import json

class Storage:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_notes(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_notes(self, notes):
        with open(self.file_path, 'w') as file:
            json.dump(notes, file)
