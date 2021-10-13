# Домашнее задание №1
import os

DIR = 'files'
file_path = os.path.join(DIR, 'first_dz.txt')
file = open(file_path, 'a',  encoding='utf-8')

while True:
    string = input('Введите что-либо: ')

    if not string:
        file.close()
        print('Выход')
        break
    file.write(f'{string}\n')

# Домашнее задание №2
import os

DIR = 'files'
file_path = os.path.join(DIR, 'second_dz.txt')
file = open(file_path, 'r', encoding='utf-8')
lines = file.readlines()

print(f'В файле {len(lines)} строк(и)')

i = 1
for string in lines:
    print(f'В строке {i} {len(string.split())} слов')
    i+=1
file.close()

# Домашнее задание №3
import os

DIR = 'files'
file_path = os.path.join(DIR, 'third_dz.txt')
file = open(file_path, 'r', encoding='utf-8')
lines = file.readlines()
sum = 0
for row in lines:
    line = row.split()
    if (float(line[1]) < 20000):
        print(f'{line[0]} Имеет оклад менее 20000руб 00коп')

    sum += float(line[1])
print(f'Средний заработок по больнице: {sum/len(lines)} руб')

file.close()

# Домашнее задание №4
import os

DIR = 'files'
file_to_read_path = os.path.join(DIR, 'fourth_dz.txt')
file_to_write_path = os.path.join(DIR, 'fourth_dz-cyr.txt')

dictionary = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open(file_to_read_path, 'r', encoding='utf-8') as file_read:
    lines = file_read.readlines()

with open(file_to_write_path, 'a', encoding='utf-8') as file_write:
    for line in lines:
        row = line.split()
        row[0] = dictionary[row[0]]
        print(' '.join(row), file=file_write)

# Домашнее задание №5
import os

DIR = 'files'
file_to_read_path = os.path.join(DIR, 'fifth_dz.txt')
file_to_write_path = os.path.join(DIR, 'fifth_dz.txt')
nums_list_to_write = []

while True:
    try:
        num = float(input('Введите число: '))
        nums_list_to_write.append(str(num))
    except ValueError:
        print('Ввод чисел прерван.')
        break

# Домашнее задание №6
import os, re

DIR = 'files'
file_to_read_path = os.path.join(DIR, 'sixth_dz.txt')
def calculate_hours(calc_line: str):
    line_of_hours = re.sub(r'\D', ' ', calc_line)
    ttl_hours = 0
    for hour in line_of_hours.split():
        ttl_hours += float(hour)
    return ttl_hours

overall_subject_info = {}
with open(file_to_read_path, 'r', encoding='utf-8') as file_read:
    for line in file_read.readlines():
        listed_line = line.split(': ')
        overall_subject_info[listed_line[0]] = calculate_hours(listed_line[1])

print(f'Итого имеем:\n {overall_subject_info}')

# Домашнее задание №7
import os, json

DIR = 'files'
file_to_read_path = os.path.join(DIR, 'seventh_dz.txt')
file_to_write_path = os.path.join(DIR, 'seventh_dz.json')

result = []
profit = {}
average = []

with open(file_to_read_path, 'r', encoding='utf-8') as file_read:
    counter = 1
    while True:
        line = file_read.readline().split()

        if not line:
            break

        profit[line[0]] = float(line[-2]) - float(line[-1])

        if profit[line[0]] > 0:
            average.append(profit[line[0]])

        counter += 1


result = [profit, {'average_profit': sum(average) / len(average)}]

with open(file_to_write_path, 'w', encoding='utf-8') as file_write:
    json.dump(result, file_write)