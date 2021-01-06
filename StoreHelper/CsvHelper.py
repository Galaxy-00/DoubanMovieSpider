from config import Entity
import csv


class CsvHelper:
    columns = Entity.movie.keys()

    def __init__(self, name):
        self._csv_file = open(name, 'w', newline='')
        self._writer = csv.writer(self._csv_file,
                                  delimiter=',',
                                  quotechar='"',
                                  quoting=csv.QUOTE_MINIMAL)
        self._writer.writerow(CsvHelper.columns)

    def write_row(self, line):
        try:
            self._writer.writerow(line)
        except IOError as e:
            print(e)

    def close(self):
        self._csv_file.close()
