from notes_manager import NotesManager
from storage import Storage

def main():
    storage = Storage('notes.json')
    manager = NotesManager(storage)

    while True:
        command = input("Введите команду (add/read/edit/delete/exit): ").strip().lower()

        if command == 'add':
            title = input("Введите заголовок заметки: ")
            message = input("Введите тело заметки: ")
            manager.add_note(title, message)
            print("Заметка успешно сохранена.")

        elif command == 'read':
            notes = manager.get_notes()
            for note in notes:
                print(f"ID: {note['id']} | Заголовок: {note['title']}")

        elif command == 'edit':
            note_id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новый заголовок заметки: ")
            message = input("Введите новое тело заметки: ")
            if manager.edit_note(note_id, title, message):
                print("Заметка успешно отредактирована.")
            else:
                print("Заметка с таким ID не найдена.")

        elif command == 'delete':
            note_id = int(input("Введите ID заметки для удаления: "))
            if manager.delete_note(note_id):
                print("Заметка успешно удалена.")
            else:
                print("Заметка с таким ID не найдена.")

        elif command == 'exit':
            print("Выход из программы.")
            break

        else:
            print("Неизвестная команда. Попробуйте снова.")

if __name__ == "__main__":
    main()
