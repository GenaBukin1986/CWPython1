import os

class RemoveFile(object):
    def __init__(self,pathfile):
        self.path = pathfile

    def removefile(self):
        if os.path.isfile(self.path + ".json"):
            os.remove(self.path + ".json")
            print(f"{self.path} удалена")
        else: print(f"{self.path} не существует!")
