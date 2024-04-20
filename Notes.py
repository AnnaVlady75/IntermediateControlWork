import json
from datetime import datetime

class Notes:
    def __init__(self, id, title, body):
        
        self.id = id
        self.title = title
        self.body = body
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updated_at = self.created_at

    def update_body(self, new_body):
        
        if self.body:  
            if new_body:
                self.body += "\n" + new_body  
                self.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            else:
                print("Текст заметки не был обновлен.")
        else:
            print("Не удается обновить текст для заметки, текста не существует.")

    def to_dict(self):
        
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    @staticmethod
    def from_dict(note_dict):
        
        return Notes(
            note_dict["id"],
            note_dict["title"],
            note_dict["body"]
        )

    def __str__(self):
        
        return f"ID: {self.id}\nTitle: {self.title}\nBody: {self.body}\nCreated At: {self.created_at}\nUpdated At: {self.updated_at}"