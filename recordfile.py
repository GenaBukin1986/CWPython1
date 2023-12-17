import json

from note import Note


class RecordFile(object):
    """Класс, который принимает словарь с данными
    и записывает в json файл"""

    def __init__(self,Note):
        self.data = Note
    def record(self):
        with open(self.data.getName() + ".json", "w",encoding='utf8') as json_file:
            json.dump(self.data.getDataNote(),json_file,ensure_ascii=False)

