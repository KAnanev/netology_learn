# Задача № 1

# Придумайте по одному примеру использования каждого типа данных: list, tuple, set, dictionary. Например,
# при помощи словаря мы можем не только делать быстрый поиск кварти (как в лекции), но и хранить "записную книжку":

# list
# Списки используются для хранения элементов, объединенных каким либо признаком.
# Например список продуктов:
list_product = ['Яблоки', 'Макароны', 'Картошка', 'Мясо']

# tuple
# Кортеж используется если изменение элементов и/или расширение списка не предполагается:
# Например времена года
tuple_seasons = tuple(['Лето', 'Осень', 'Зима', 'Весна'])

# set
# Множества проверяют принадлежит ли значение набору уникальных элементов, без индексации.
# Например множество чисел, которые мы как нить получили, но нам необходимо удалить дубликаты
set_num = set([1, 2, 1, 3, 2, 4])

# dictionary
# Словарь необходим, для того чтобы была возможность доступа по ключу
# Например по имени человека можно узнать его фамилию
first_name = ['Иван', 'Герман', 'Йохан']
last_name = ['Петров', 'Греф', 'Вайс']
full_name = {first: last for (first, last) in zip(first_name, last_name)}
print(full_name.get('Иван'))


# Задача № 2

import csv

flats_list = list()

with open('output.csv', newline='') as csvfile:
    flats_csv = csv.reader(csvfile, delimiter=';')
    flats_list = list(flats_csv)

# можете посмотреть содержимое файла с квартирами через print, можете - на вкладке output.csv
# print (flats_list)


# TODO 1:
# 1) Напишите цикл, который проходит по всем квартирам, и показывает только новостройки
# и их порядковые номера в файле. Подсказка - вам нужно изменить этот код:
# count = 0
# for index, flat in enumerate(flats_list):
#     if 'новостройка' in flat:
#         count += 1
#         print(f'Номер в списке - {index}, {flat}')
# # 2) добавьте в код подсчет количества новостроек
# print(f'Количество новостроек - {count}\n')

# TODO 2:
# 1) Сделайте описание квартиры в виде словаря, а не списка.
# Используйте следующие поля из файла output.csv: ID, Количество комнат;Новостройка/вторичка, Цена (руб).
# У вас должно получиться примерно так:
# flat_info = {"id":flat[0], "rooms":flat[1], "type":flat[2], "price":flat[11]}

# 2) Измените код, который создавал словарь для поиска квартир по метро так, чтобы значением словаря был не список ID
# квартир, а список описаний квартир в виде словаря, который вы сделали в п.1
subway_dict = {}
flats_list.pop(0)
for flat in flats_list:
    flat_info = {"id": flat[0], "rooms": flat[1], "type": flat[2], "price": flat[11]}
    if len(flat[3]) != 0:
        subway = flat[3].replace("м.", "")
    if subway not in subway_dict.keys():
        subway_dict[subway] = list()
    subway_dict[subway].append(flat_info)

# 3) Самостоятельно напишите код, который подсчитывает и выводит, сколько квартир нашлось у каждого метро.
for metro in subway_dict:
    print(f'Квартир у метро {metro} - {len(subway_dict[metro])}')
