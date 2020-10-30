import os, csv
from SongClass import Song

class ListSongs:
    def __init__(self, file_name='songs.csv'):
        self.__path_to_csv_file = os.getcwd() + f'.\\task1\\{file_name}'
        self.__list_songs = self.__read_data_csv()
        self.__field_names = 'author,title,album,release_year,duration'.split(',')
    def __read_data_csv(self):
        '''Чтение файла с данными в список'''
        try:
            # попытка открыть файл для чтения, иначе исключение
            with open(self.__path_to_csv_file, encoding='utf-8') as csv_file:
                data = csv.DictReader(csv_file, delimiter=',')
                data_tmp = []
                for row in data:
                    song = Song(data=row, is_dict=True)
                    data_tmp.append(song)
            return data_tmp
        except FileNotFoundError:
            # не нашли указанный файл
            file_name = os.path.split(self.__path_to_csv_file)[1]
            print(f'Файл {file_name} отсутствует:')
            # то создаем новый и работаем с ним
            with open(self.__path_to_csv_file, 'w') as f:
                wr = csv.writer(f)
                wr.writerow('author,title,album,release_year,duration'.split(','))
            print(f'Был создан новый файл хранения {file_name}')
    def add_song(self, song_data):
        '''Добавление новой композиции в рабочий список'''
        try:
            self.__list_songs.append(Song(data=song_data, is_dict=True))
            return True
        except Exception:
            return False
    def del_song(self, author, title):
        '''Удаление композиции из списка'''
        for i, song in enumerate(self.__list_songs):
            if song.author == author and song.title == title:
                self.__list_songs.pop(i)
                return True
        else:
            return False
        return False
    def edit_song(self, author, title, param, new_param_value):
        '''Изменить информацию о композиции'''
        for song in self.__list_songs:
            if author == song.author and title == song.title:
                try:   
                    setattr(song, param, new_param_value)
                    return True
                except:
                    return False
        else:
            return False
    def get_list(self):
        '''Вывести весь список'''
        if not self.__list_songs:
            return 'Список композиций пуст'
        else:
            return self.__list_songs
    def print_album(self, author):
        print('Список композиций ')
    def find_song(self, search_str):
        '''Найти композицию по названю/автору/длительности'''
        tmp = []
        for song in self.__list_songs:
            if search_str in song.title or\
                search_str in song.album or\
                    search_str in song.author or\
                        search_str in song.release_year or\
                            search_str in song.duration:
                            tmp.append(song)
        return tmp if len(tmp) > 0 else None
    def get_albums(self, author):
        albums = []
        for song in list(filter(lambda x: x.author == author, self.__list_songs)):
           albums.append(song.album)
        return albums
    def get_songs_for_album(self, album):
        tmp = []
        for song in self.__list_songs:
            if song.album == album:
                tmp.append(song)
        return tmp if len(tmp) > 0 else ['У этого автора нет такого альбома']
    def get_songs_of_author(self, author):
        tmp = []
        for song in self.__list_songs:
            if song.author == author:
                tmp.append(song)
        return tmp if len(tmp) > 0 else None
    def is_author(self, author):
        for song in self.__list_songs:
            if song.author == author:
                return True
        else:
            return False
    def save_songs(self):
        '''Сохранить рабочий список, перезаписав файл'''
        with open(self.__path_to_csv_file, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.__field_names, delimiter=',')
            writer.writeheader()
            writer.writerows([song.get_like_dict() for song in self.__list_songs])
    def get_help(self):
        '''Метод возвращает список команд для работы с приложением'''
        ret_help = '''
        Доступные команды:
            add - добавить запись
            del - удалить запись
            edit - изменение данных о записи
            print [author] - вывод всего списка записей или записей из альбома исполнителя
            find - поиск записи по названию и длительности
            help - получить список всех команд
            exit - выход
        '''
        return ret_help
    def get_fieldnames(self):
        return self.__field_names
    def __str__(self):
        return 'Ошибка вывода > используйте print_list() для вывода списка композиций'

if __name__ == "__main__":
    lst = ListSongs()
