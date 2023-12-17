import json
import datetime

from readfile import ReadFile


class RedactFile(object):
    def __init__(self,namenote):
        self.nameNote = namenote
        self.namefile = namenote + ".json"

    def redactNote(self):
        readNote = ReadFile(self.nameNote)
        if (readNote.showRedact() == -1):
            return -1
        dic = readNote.readFile()
        answer = input("\nКакой пункт Заметки вы хотите отредактировать: ")
        if answer == "1":
            heading = input("Введите Новый заголовок Заметки: ")
            dic['Заголовок заметки'] = heading
            dic['Дата создания/изменения заметки'] = datetime.datetime.now().strftime("%d %m %y %H %M")
            with open(self.namefile, "w", encoding='utf8') as json_file:
                json.dump(dic, json_file, ensure_ascii=False)
        elif answer == "2":
            heading_body = input("Введите новое содержание Заметки: ")
            dic['Содержание заметки'] = heading_body
            dic['Дата создания/изменения заметки'] = datetime.datetime.now().strftime("%d %m %y %H %M")

            with open(self.namefile, "w", encoding='utf8') as json_file:
                json.dump(dic, json_file, ensure_ascii=False)
        elif answer == "3":
            heading = input("Введите Новый заголовок Заметки: ")
            heading_body = input("Введите новое содержание Заметки: ")
            dic['Заголовок заметки'] = heading
            dic['Содержание заметки'] = heading_body
            dic['Дата создания/изменения заметки'] = datetime.datetime.now().strftime("%d %m %y %H %M")

            with open(self.namefile, "w", encoding='utf8') as json_file:
                json.dump(dic, json_file, ensure_ascii=False)
        elif answer == "4":
            print("Выход из режима редактировния")
        else:
            print("Введены некорректные данные!")
            return -1



