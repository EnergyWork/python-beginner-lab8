class Song:
    '''Класс, описывающий композицию'''
    def __init__(self, \
        title=None, author=None, album=None, release_year=None, duration=None,\
            data=None, is_dict=False):
        if is_dict:
            if type(data) is dict:
                self.__title = data['title']
                self.__author = data['author']
                self.__album = data['album']
                self.__release_year = data['release_year']
                self.__duration = data['duration']
            else:
                print('Неверный формат добавляемых данных')
        else:
            if type(data) is not dict:
                self.__title = title
                self.__author = author
                self.__album = album
                self.__release_year = release_year
                self.__duration = duration
            else:
                print('Неверный формат добавляемых данных')
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
    def get_like_dict(self):
        '''Возвращает объект Song в виде словаря'''
        return {
            'author' : self.author,
            'title' : self.title,
            'album' : self.album,
            'release_year' : self.release_year,
            'duration' : self.duration
        }
    def get_str(self):
        return f'{self.__author} - {self.__title} ({self.__album}, {self.__release_year}) - {self.__duration}'
    def __str__(self):
        return f'{self.__author} - {self.__title} ({self.__album}, {self.__release_year}) - {self.__duration}'

if __name__ == "__main__":
    song = Song('Make some noise', 'Noize MC', 'Amazing', '2014', '02:15')
    print(song)
    song.title = 'MAKE SOME NOISE'
    print(song)
