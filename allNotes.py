import os


class AllNotes(object):
    def allNotes(self):
        for i in os.listdir(path='.'):
            if 'Заметка' in i:
                print(i[:-5])

    def getAllNotes(self):
        list = []
        for i in os.listdir(path='.'):
            if 'Заметка' in i:
                list.append(i[:-5])
        return list