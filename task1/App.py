import os, csv, re
from ListSongsClass import ListSongs
import datetime

class Application(object):
    '''Основное приложение'''
    # конструктор класса: инициализируем список композиция для манипуляций над ними
    def __init__(self):
        self.songs = ListSongs()
    # старт приложения
    def start(self):
        while True:
            command = input('Введите команду (help - получить помощь) > ')
            if command == 'help':
                print(self.songs.get_help())
            elif command == 'add':
                result = self.__add()
                if result:
                    print('Запись успешно добавлена!')
                else:
                    print('При добавление произошла ошибка')
            elif command == 'del':
                pass
            elif command == 'edit':
                pass
            elif command == 'print':
                self.__print()
            elif command == 'find':
                pass
            elif command == 'exit':
                self.songs.save_songs()
                exit(0)
            else:
                print('Неверная команда')
    # добавление новой композиции
    def __add(self):
        print('Новая композиция:')
        d = {
            'author' : self.str_input('Автор'),
            'title' : self.str_input('Название'),
            'album' : self.str_input('Альбом'),
            'release_year' : self.release_year_input(),
            'duration' : self.duration_input()
        }
        return True if self.songs.add_song(d) else False
    def __del(self):
        pass
    def __find(self):
        pass
    def __print(self):
        self.songs.print_list()
    @classmethod
    def get_err_msg(cls):
        print('Ошибка. Повторите попытку.', end=' ')
    @classmethod
    def str_input(cls, parameter):
        while True:
            tmp = input(f'{parameter} > ')
            if not (tmp and not tmp.isspace()):
                cls.get_err_msg()
            else: 
                return tmp
    @classmethod
    def duration_input(cls):
        while True:
            duration = input('Длительность (mm:ss) > ')
            if re.fullmatch(r'\d+:\d\d', duration) is None:
                cls.get_err_msg()
            else:
                return duration
    @classmethod
    def release_year_input(cls):
        now = datetime.datetime.now()
        while True:
            year = input('Год выхода > ')
            try:
                tmp = int(year)
                if 1500 > tmp or tmp > now.year:
                    cls.get_err_msg()
                else:
                    return year
            except:
                cls.get_err_msg()

if __name__ == "__main__":
    app = Application()
    app.start()