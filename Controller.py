import json
from Notes import Notes


class Controller:
    def __init__(self, file_path):
        
        self.file_path = file_path
        self.notes = self.load_notes()  

    def load_notes(self):
        
        try:
            with open(self.file_path, "r") as file:
                notes_data = json.load(file)
                return [Notes.from_dict(note) for note in notes_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []  

    def save_notes(self):
        
        with open(self.file_path, "w") as file:
            notes_data = [note.to_dict() for note in self.notes]
            json.dump(notes_data, file, indent=4)

    def add_note(self, title, body):
        
        new_id = len(self.notes) + 1
        new_note = Notes(new_id, title, body)
        self.notes.append(new_note)
        self.save_notes()
        print(f"Заметка с ID {new_id} добавлена.")

    def delete_note(self, note_id):
        
        self.notes = [note for note in self.notes if note.id != note_id]
        self.save_notes()
        print(f"Заметка с ID {note_id} удалена.")

    def edit_note_body(self, note_id, new_body):
       
        for note in self.notes:
            if note.id == note_id:
                print(f"Текущий текст заметки с ID {note_id}:")
                print(note.body)
                choice = input("1. Добавить новый текст\n2. Исправить текущий текст\nВыберите действие: ")
                if choice == "1":
                    note.update_body(new_body)
                elif choice == "2":
                    note.body = new_body
                else:
                    print("Неправильный выбор. Текст заметки не изменен.")
                self.save_notes()
                print(f"Заметка с ID {note_id} отредактирована.")
                return
        print(f"Заметка с ID {note_id} не найдена.")

    def check_note_exists(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return True
        return False

    def get_all_notes(self):
        
        for note in self.notes:
            print(note)

    def get_notes_by_date(self, date):
        
        notes_on_date = [note for note in self.notes if note.created_at.startswith(date)]
        if not notes_on_date:
            print(f"Нет заметок с указанной датой: {date}")
        else:
            for note in notes_on_date:
                print(note)