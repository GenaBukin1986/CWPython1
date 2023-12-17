import json
import os
import datetime


class ReadFile(object):
    """Класс чтения заметки из json файла"""
    def __init__(self,namefile):
        self.name = namefile
        self.namefile = namefile + ".json"

    def readFile(self):
        if (os.path.exists(self.namefile)):
            with open(self.namefile, "r",encoding='utf8') as json_file:
                parsed = json.load(json_file)
                dic = json.dumps(parsed,indent=4,sort_keys=True,ensure_ascii=False)
                dic = dic.replace("{","").replace("}","").replace("\n","").replace("\"","")
                dic = dic.strip()
                # id = dic[:dic.find(":")].replace("\"","")
                dic = dic.split(",")
                dic = [i.strip().split(":") for i in dic]
                dictionary = dict()
                for i in dic:
                    dictionary[i[0]] = i[1].strip()
                return dictionary
        else:
           print(f"{self.name} не существует!")
           return -1

    def showDic(self):
        if self.readFile() != -1:
            dic = self.readFile()
            strdata = dic.get('Дата создания/изменения заметки')
            data = datetime.datetime.strptime(strdata, "%d %m %y %H %M")
            date = data.strftime("%d %m %y %H:%M")
            print(f"Заметка#{dic.get('Заметка')}\n"
                  f"Заголовок заметки: {dic.get('Заголовок заметки')}\n"
                  f"Содержание заметки: {dic.get('Содержание заметки')}\n"
                  f"Датасоздания/изменения заметки: {date}")
        else:
            return -1

    def showRedact(self):
        if self.readFile() != -1:
            dic = self.readFile()
            print(f"Заметка#{dic.get('Заметка')}\n"
                  f"1. Заголовок заметки\n"
                  f"2. Содержание заметки\n"
                  f"3. Редактировать оба пункта\n"
                  f"4. Выход из режима редактирования")
        else:
            return -1



