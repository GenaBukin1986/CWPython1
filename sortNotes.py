from allNotes import AllNotes
from readfile import ReadFile
import datetime


class SortNotes(object):
    def __init__(self):
        self.listNotes = AllNotes().getAllNotes()

    def sortNotes(self):

        array = []
        for i in self.listNotes:
            array.append(ReadFile(i).readFile())

        array.sort(key=lambda x:x['Дата создания/изменения заметки'])

        for i in array:
            strdata = i.get('Дата создания/изменения заметки')
            data = datetime.datetime.strptime(strdata, "%d %m %y %H %M")
            date = data.strftime("%d %m %y %H:%M")
            print(f"Заметка#{i.get('Заметка')}, Время: {date}")

    def sortNotesDown(self):
        array = []
        for i in self.listNotes:
            array.append(ReadFile(i).readFile())

        array.sort(key=lambda x: x['Дата создания/изменения заметки'],reverse=True)

        for i in array:
            strdata = i.get('Дата создания/изменения заметки')
            data = datetime.datetime.strptime(strdata, "%d %m %y %H %M")
            date = data.strftime("%d %m %y %H:%M")
            print(f"Заметка#{i.get('Заметка')}, Время: {date}")