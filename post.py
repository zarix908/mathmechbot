class Post:
    def __init__(self, id, text):
        self.__id = id
        self.__text = text

    @property
    def id(self):
        return self.__id

    @property
    def text(self):
        return self.__text
