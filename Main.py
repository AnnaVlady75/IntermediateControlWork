from Controller import Controller

def main():
    file_path = "notes.json" 
    note_manager = Controller(file_path) 

    while True:
        print("\nМеню:")
        print("1. Добавить заметку")
        print("2. Удалить заметку")
        print("3. Редактировать заметку")
        print("4. Показать все заметки")
        print("5. Показать заметки по дате (YYYY-MM-DD):")
        print("6. Выход")

        choice = input("Введите цифру меню: ")  

        if choice == "1":
            title = input("Введите заголовок заметки: ")  
            body = input("Введите тело заметки: ")  
            note_manager.add_note(title, body)  
        elif choice == "2":
            note_id = int(input("Введите ID заметки для удаления: "))  
            note_manager.delete_note(note_id)  
        elif choice == "3":
            note_id = int(input("Введите ID заметки для редактирования: "))  
            if note_manager.check_note_exists(note_id):  
                new_body = input("Введите новое тело заметки: ")  
                note_manager.edit_note_body(note_id, new_body)  
            else:
                print("Ошибка: Заметка с ID {} не существует.".format(note_id))
        elif choice == "4":
            note_manager.get_all_notes()  
        elif choice == "5":
            date = input("Введите дату в формате (YYYY-MM-DD) для вывода заметки: ")  
            note_manager.get_notes_by_date(date)  
        elif choice == "6":
            print("Excelent!")  
            break  
        else:
            print("Неправильный выбор меню. Попытайтесь снова.")  

if __name__ == "__main__":
    main()  