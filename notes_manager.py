from datetime import datetime

class NotesManager:
    def __init__(self, storage):
        self.storage = storage
        self.notes = self.storage.load_notes()

    def add_note(self, title, message):
        timestamp = datetime.now().isoformat()
        note = {
            'id': len(self.notes) + 1,
            'title': title,
            'message': message,
            'timestamp': timestamp
        }
        self.notes.append(note)
        self.storage.save_notes(self.notes)
        return note

    def get_notes(self):
        return self.notes

    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note['id'] == note_id:
                return note
        return None

    def edit_note(self, note_id, title, message):
        for note in self.notes:
            if note['id'] == note_id:
                note['title'] = title
                note['message'] = message
                note['timestamp'] = datetime.now().isoformat()
                self.storage.save_notes(self.notes)
                return True
        return False

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note['id'] != note_id]
        self.storage.save_notes(self.notes)
        return True
