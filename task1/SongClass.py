class Song(object):
    '''Класс, описывающий композицию'''
    def __init__(self, title=None, author=None, album=None, release_year=None, duration=None):
        self.__title = title
        self.__author = author
        self.__album = album
        self.__release_year = release_year
        self.__duration = duration
    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, value):
        self.__title = value
    @property
    def author(self):
        return self.__author
    @author.setter
    def author(self, value):
        self.__author = value
    @property
    def album(self):
        return self.__album
    @album.setter
    def album(self, value):
        self.__album = value
    @property
    def release_year(self):
        return self.__release_year
    @release_year.setter
    def release_year(self, value):
        self.__release_year = value
    @property
    def duration(self):
        return self.__duration
    @duration.setter
    def duration(self, value):
        self.__duration = value
    def __str__(self):
        return f'{self.__author} - {self.__title} ({self.__album}, {self.__release_year}) - {self.__duration}'

if __name__ == "__main__":
    song = Song('Make some noise', 'Noize MC', 'Amazing', '2014', '02:15')
    print(song)
    song.title = 'MAKE SOME NOISE'
    print(song)
