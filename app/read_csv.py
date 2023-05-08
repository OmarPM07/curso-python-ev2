
#Importar módulo de lectura de un archivo csv

import csv

#Definición de una función para la lectura del archivo csv
def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data


if __name__ == '__main__':
    data = read_csv('/Users/omarpalacios/Desktop/proyecto_python/CompreErrorPython/app/data.csv')
    print(data)