import yaml
import csv
from itertools import chain
import time

class YAMLParser():

    def __init__(self):
        self.csv_file = open('ymlste.csv', 'w', newline='')

    def parse_one_yml(self, i: int):
        t1 = time.clock()
        file = open('ste{}.yml'.format(i))
        #csv_file = open('ymlste.csv', 'w', newline='')
        inserted_list = list()
        writer = csv.writer(self.csv_file, delimiter=',')
        one_object = list()
        a = yaml.load(file)
        date = list(a.keys())[0]
        one_object.append(date)
        a1 = a[date] # date
        for key, value in a1.items():
            strange = value
            first_level = list()
            first_level.append(date)
            first_level.append(key) # AF, SU, ..., UX, VN с 4 цифрами без пробелов
            first_level.append(strange['FROM'])
            first_level.append(strange['STATUS'])
            first_level.append(strange['TO'])
            for key2, value2 in strange['FF'].items():
                second_level = list()
                buffer_list = list()
                buffer_list.append(key2) # DT FB KE SU с пробелом и много цифр
                buffer_list.append(value2['CLASS'])
                buffer_list.append(value2['FARE'])
                second_level.append(buffer_list)
                for second in second_level:
                    inserted_list = list(chain(first_level, second))
                    writer.writerow(inserted_list)
        t2 = time.clock()
        file.close()
        #csv_file.close()
        print('Парсинг 1 файла занимает {} c'.format(t2-t1))

    def parse_all(self):
        for j in range(1,367):
            self.parse_one_yml(j)
        self.csv_file.close()

if __name__ == "__main__":
    yaml1 = YAMLParser()
    yaml1.parse_all()
    
