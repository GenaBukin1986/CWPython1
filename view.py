import os

from allNotes import AllNotes
from note import Note
from readfile import ReadFile
from recordfile import RecordFile
from redactfile import RedactFile
from removefile import RemoveFile
from sortNotes import SortNotes


class View(object):

    def clear_console(self):
        os.system('cls')

    def show_menu(self):
        print("\t\tПриложение Заметки 1.0")
        print("\n1. Создать Заметку")
        print("2. Прочитать Заметку")
        print("3. Редактировать Заметку")
        print("4. Удалить Заметку")
        print("5. Показать все Заметки")
        print("6. Выборка Заметок по дате")
        print("7. Выход из приложения")
        answer = input("\nВведите пункт меню: ")
        return answer

    def createNote(self):
        note = Note()
        note.setHeading(input("Введите название Заметки: "))
        note.setBody_heading(input("Введите содержание заметки: "))
        # date = datetime.datetime.now()
        # print(date.year, date.month, date.day, (str(date.hour) + ":" + str(date.minute)))
        print(f"{note.getName()} создана\n")
        RecordFile(note).record()

    def removeNote(self):
        path = input("Введите Заметку, которую вы хотите удалить: ")
        RemoveFile(path).removefile()
    def redactNote(self):
        path = input("Введите Заметку, которую вы хотите редактировать: ")
        if (RedactFile(path).redactNote() != -1):
            print("Изменения внесены")
        else:
            print("Ошибка выполнения операции!")

    def readNote(self):
        path = input("Введите Заметку, которую хотите прочитать: ")
        print()
        ReadFile(path).showDic()
        print()

    def readAllNotes(self):
        print("Списко всех ваших Заметок:")
        AllNotes().allNotes()
        print()

    def sortInAscendigOrder(self):
        self.clear_console()
        print("\t\tМеню сортировки")
        print("1. Сортировка по возрастанию даты")
        print("2. Сортировка по убыванию даты")
        print("3. Выход из меню сортировки\n")
        num = input("Введит пункт меню сортировки: ")
        print()
        if num == "1":
            SortNotes().sortNotes()
        elif num == "2":
            SortNotes().sortNotesDown()
        else:
            print("Выход из меню сортировки . . .")


    def button_click(self):
        while (True):
            num = str(self.show_menu())
            if num == "1":
                self.clear_console()
                self.createNote()
            elif num == "2":
                self.clear_console()
                self.readNote()
            elif num == "3":
                self.clear_console()
                self.redactNote()

            elif num == "4":
                self.clear_console()
                self.removeNote()
                print()
            elif num == "5":
                self.clear_console()
                self.readAllNotes()
            elif num == "6":
                self.sortInAscendigOrder()
            elif num == "7":
                break
            else:
                self.clear_console()
                print("Введены некорректные данные!\nПожалуйста будьте внимательны!\n")