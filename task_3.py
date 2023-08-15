import csv
import json
import os
import pickle
from os.path import getsize, abspath, join


class Writer_path_info:

    def __init__(self, file_name='data', path=os.getcwd()):
        self.path = path
        self.file_name = file_name
        self.__data = self.__get_directory_items(path)

    def __get_directory_size(self, directory):
        directory = abspath(directory)
        total = 0
        try:
            for entry in os.scandir(directory):
                if entry.is_file():
                    total += entry.stat().st_size
                elif entry.is_dir():
                    total += self.__get_directory_size(entry.path)
        except NotADirectoryError:
            return getsize(directory)
        except PermissionError:
            return 0
        return total

    def __get_directory_items(self, path):
        res_list = []
        for dir_path, dir_name, file_name in os.walk(path):
            dict = {
                f'Родительская директория': dir_path,
                f'Вложенные директории': {dir: self.__get_directory_size(join(dir_path, dir)) for dir in dir_name},
                f'Вложенные файлы': {file: getsize(join(dir_path, file)) for file in file_name}
            }
            res_list.append(dict)
        return res_list

    def write_JSON(self):
        with open(f'{self.file_name}.json', 'w', encoding='UTF-8') as f:
            json.dump(self.__data, f, indent=2, ensure_ascii=False)

    def write_CSV(self):
        with open(f'{self.file_name}.csv', 'w', newline='', encoding='utf-8') as f:
            csv_write = csv.DictWriter(f, fieldnames=['Родительская директория', 'Вложенные директории',
                                                      'Вложенные файлы'],
                                       dialect='excel-tab', quoting=csv.QUOTE_ALL)
            csv_write.writeheader()
            csv_write.writerows(self.__data)

    def write_PICKLE(self):
        with open(f'{self.file_name}.pickle', 'wb') as f:
            pickle.dump(self.__data, f)


wr = Writer_path_info('newfile_1')
wr.write_CSV()
wr.write_JSON()
wr.write_PICKLE()

wr2 = Writer_path_info('newfile_2', 'venv')
wr2.write_JSON()