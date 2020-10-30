from ListSongsClass import ListSongs
import datetime, re

class Application:
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
                result = self.__del()
                if result:
                    print('Запись успешно удалена')
                else:
                    print('При удалении произошла ошибка, попробуйте снова')
            elif command == 'edit':
                result = self.__edit()
                if result:
                    print('Запись успешно изменена')
                else:
                    print('При изменении данных произошла ошибка, попробуйте снова')
            elif command.__contains__('print'):
                cmd = command.split()
                if len(cmd) == 1:
                    self.__print_list()
                elif len(cmd) == 2:
                    self.__print_album_songs(cmd[1])
                else:
                    print('Неверный формат команды print')
            elif command == 'find':
                self.__find()
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
    # удаление композиции
    def __del(self):
        author = input('Удаление записи\nВведите автора:')
        list_os_songs = self.songs.get_songs_of_author(author)
        if list_os_songs is None:
            print('Такого автора нет в списке Ваших записей')
            return False
        else:
            print('Выберите какую запись удалить:')     
            for i, song in enumerate(list_os_songs):
                print(f'{i}. {song} ')
            selected = input('Введите номер или название > ')
            try:
                selected = int(selected)
                ret_result = self.songs.del_song(author, list_os_songs[selected].title)
            except Exception:
                ret_result = self.songs.del_song(author, selected)
        return ret_result
    # поиск записи по названию
    def __find(self):
        search = input('Поиск: ')
        songs_search_list = self.songs.find_song(search)
        for i, song in enumerate(songs_search_list):
            print(f'{i}. {song}')
    # выбор изменяемого параматре одного
    def __edit(self):
        author = input('Изменение записи\nВведите автора > ')
        list_os_songs = self.songs.get_songs_of_author(author)
        if list_os_songs is None:
            print('Такого автора нет в списке Ваших записей')
            return False
        else:
            print('Выберите какую запись изменить:')     
            for i, song in enumerate(list_os_songs):
                print(f'{i}. {song} ')
            selected = input('Введите номер или название > ')
            try:
                selected = int(selected)
                ret_result = self.__edit_song_data(author, list_os_songs[selected].title)
            except Exception:
                ret_result = self.__edit_song_data(author, selected)
        return ret_result
    # изменение параметра
    def __edit_song_data(self, author, title):
        fieldnames = self.songs.get_fieldnames()
        print('Изменяемые параметры:')
        for i, s in enumerate(fieldnames):
            print(f'{i} - {s}')
        stt = input('Выберите параметр который надо изменить > ')
        try:
            stt = int(stt)
            if len(fieldnames) < stt < 0:
                return False
            print(f'Новое значения для {fieldnames[stt]}')
            new_value = self.str_input(fieldnames[stt])
            stt = fieldnames[stt]
        except:
            if stt not in fieldnames:
                return False
            new_value = input(f'Новое значения для {stt}')

        if not (new_value and not new_value.isspace()):
            print('Была введена пустая строка')
            return False
        else:
            ret_value = self.songs.edit_song(author, title, stt, new_value)
        return ret_value
    # вывод списка всех запией
    def __print_list(self):
        '''Вывод всех записей'''
        songs_list = self.songs.get_list()
        if type(songs_list) is list:
            print('Список всех записей:')
            for song in songs_list:
                print(song)
        else:
            print(songs_list)
    # вывод записей из альбома одного автора
    def __print_album_songs(self, author):
        '''Получание всех альбомов определенного автора'''
        if self.songs.is_author(author):
            albums = list(set(self.songs.get_albums(author))) # -> list(str)
            print('Выберите нужный Вам альбом:')
            for i, alb in enumerate(albums):
                print(f' {i} - {alb}')
            selected = input('Введите номер или название > ')
            try:
                selected = int(selected)
                try:
                    songs_for_album = self.songs.get_songs_for_album(albums[selected])
                    for song in songs_for_album:
                        print(song)
                except IndexError:
                    print('Нет такого номера в списке')
            except Exception:
                songs_for_album = self.songs.get_songs_for_album(selected)
                for song in songs_for_album:
                    print(song)
        else:
            print('Такого авторе нет в списке ваших записей')
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