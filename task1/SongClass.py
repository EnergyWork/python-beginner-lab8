
class Song(object):
    '''Класс, описывающий композицию'''
    def __init__(self):
        self._title = None
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        self._title = value
