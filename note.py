import datetime


class Note(object):
    """Класс заметки. Класс содержит поля идентификатор, заголовок,
    тело заметки и дату создания."""
    count = 1

    def __init__(self):
        self.id = Note.count
        self.heading = None
        self.body_heading = None
        self.data = datetime.datetime.now().strftime("%d %m %y %H %M")
        Note.count += 1
        self.name = "Заметка#" + str(self.id)

    def setHeading(self,heading):
        self.heading = heading

    def getId(self):
        return self.id
    def getName(self):
        return self.name

    def setBody_heading(self,body_heading):
        self.body_heading = body_heading

    def setData(self,data):
        self.data = data


    def __str__(self):
        return f"Заметка#{self.id}\n" \
               f"Заголовк заметки: {self.heading}\n" \
               f"Содержание заметки: {self.body_heading}\n" \
               f"Дата создания/изменения заметки: {self.data}"

    def getDataNote(self) -> object:
        data = {"Заметка": self.id,
                "Заголовок заметки": self.heading,
                "Содержание заметки":self.body_heading,
                "Дата создания/изменения заметки": self.data}
        return data
    