import csv

from config import Entity


class CsvHelper:
    columns = Entity.movie.keys()  # csv文件的表头

    def __init__(self, filename: str) -> None:
        '''
        初始化csv writer
        :param filename: 存储csv的文件名
        '''
        self._csv_file = open(filename, 'w', newline='')
        self._writer = csv.writer(self._csv_file,
                                  delimiter=',',
                                  quotechar='"',
                                  quoting=csv.QUOTE_MINIMAL)
        self._writer.writerow(CsvHelper.columns)

    def write_row(self, line: str) -> None:
        '''
        向csv文件中写入一行数据
        :param line: 向csv文件的写入的一行数据
        '''
        try:
            self._writer.writerow(line)
        except IOError as e:
            print(e)

    def close(self) -> None:
        '''
        关闭csv writer
        '''
        self._csv_file.close()
