import os, csv, re
from ListSongsClass import ListSongs
import datetime

def get_err_msg():
    print('Ошибка. Повторите попытку.', end=' ')

def str_input(parameter):
    while True:
        tmp = input(f'{parameter} > ')
        if not (tmp and not tmp.isspace()):
            get_err_msg()
        else: 
            return tmp

def duration_input():
    while True:
        duration = input('Длительность (mm:ss) > ')
        if re.fullmatch(r'\d+:\d\d', duration) is None:
            get_err_msg()
        else:
            return duration

def release_year_input():
    now = datetime.datetime.now()
    while True:
        year = input('Год выхода > ')
        try:
            tmp = int(year)
            if 1500 > tmp or tmp > now.year:
                get_err_msg()
            else:
                return year
        except:
            get_err_msg()

def application():
    songs = ListSongs()
    while True:
        command = input('Введите команду (help - получить помощь) > ')
        if command == 'help':
            print(songs.get_help())
        elif command == 'add':
            print('Новая композиция:')
            author = str_input('Автор')
            title = str_input('Название')
            album = str_input('Альбом')
            release_year = release_year_input()
            duration = duration_input()
        elif command == 'del':
            pass
        elif command == 'edit':
            pass
        elif command == 'print':
            songs.print_list()
        elif command == 'find':
            pass
        elif command == 'exit':
            exit(0)
        else:
            print('Неверная команда')

if __name__ == "__main__":
    application()