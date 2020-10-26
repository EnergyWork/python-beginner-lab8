import os, csv
#import pandas as pd
from SongClass import Song

class ListSongs(object):
    def __init__(self):
        self.__path_to_csv_file = os.getcwd() + '.\\task1\\songs.csv'
        self.__list_songs = self.__read_data_csv()
    def __read_data_csv(self):
        with open(self.__path_to_csv_file, encoding='utf-8') as csv_file:
            data = csv.DictReader(csv_file, delimiter=',')
            data_tmp = []
            for row in data:
                song = Song(
                    row['title'],
                    row['author'],
                    row['album'],
                    row['release_year'],
                    row['duration']
                )
                data_tmp.append(song)
        return data_tmp
    def add_song(self):
        pass
    def del_song(self):
        pass
    def edit_song(self):
        pass
    def print_list(self):
        print('Список композиций:')
        for song in self.__list_songs:
            print(song)
    def find_song(self):
        pass
    def get_help(self):
        """
        Метод возвращает список команд для работы с приложением
        """
        ret_help = '''
        Доступные команды:
            add - добавить запись
            del - удалить запись
            edit - изменение данных о записи
            print - вывод всего списка композиций
            find - поиск записи по названию и длительности
            help - получить список всех команд
            exit - выход
        '''
        return ret_help
    def __str__(self):
        return 'Ошибка вывода'


if __name__ == "__main__":
    lst = ListSongs()
    lst.print_list()
