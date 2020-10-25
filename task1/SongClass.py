
class Song(object):
    '''Класс, описывающий композицию'''
    def __init__(self):
        self._title = None
        self._author = None
        self._album = None
        self._year_out = None
        self._duration = None
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        self._title = value
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, value):
        self._author = value
