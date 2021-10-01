# Задача №1
def division():
    result = 0
    while True:
        command = input("Введите два целых чила - первый будет числителем, второй - знаминателем, разделив их пробелом (q или й - выход): \n")
        if command.lower() in ("q", "й"):
            break
        numbers = list(command.split())
        num1 = int(numbers[0])
        num2 = int(numbers[1])
        result = num1/num2 if num2 != 0 else "Деление на 0! Будьте внимательны - ноль в знаминателе недопустим"
        print(f"Результаты деления:  {round(result,2)}")
division()

# Задача №2
users = []
def user_add(first_name, last_name, birth_year, city, email, phone_number):
    users.append({
    "Имя": first_name,
    "Фамилия": last_name,
    "Год рождения": birth_year,
    "Город": city,
    "Почта": email,
    "Телефон": phone_number
     })
    for user in users:
        message = "- "
        for key in user.keys():
            if user[key] is not None:
                message += f"{key}: {user[key]}. "
        print(message)
user_add('Sergey','Ivanov','1971','Ufa','sergch@yandex.ru','6-34-90')

# Задача №3
def max_value_sum(num_1,num_2,num_3):
    numbers = []
    numbers.append(num_1)
    numbers.append(num_2)
    numbers.append(num_3)
    a = max(numbers)
    numbers.remove(a)
    b = max(numbers)
    c = a + b
    print(f"Сумма двух максимальных значений позиционных аргументов функции max_value_sum(): {c}")
max_value_sum(9,2,3)

# Задача №4
def my_func(x, y):
    return x ** y

def my_func_2(x, y):
    counter = 1
    result = 1 / x
    while counter < abs(y):
        result = result * (1 / x)
        counter += 1
    return result

print(f'Реализация возведения степени вариантом 1: '
      f'{my_func(int(input("Основание степени Х: ")), int(input("Показатель степени Y: ")))}')

print(f'Реализация возведения степени вариантом 2: '
      f'{my_func_2(int(input("Основание степени Х: ")), int(input("Показатель степени Y: ")))}')

# Эадача №5
def calculate_sum(*nums):
    sum = 0
    flag = False
    for num in nums:
        try:
            if num:
                sum += float(num)
        except ValueError:
            flag = True
    return sum, flag

general_sum = 0

while True:
    numbers_string = input('Введите числа через пробел: ').split(' ')
    sum, stop_flag = calculate_sum(*numbers_string)
    general_sum += sum
    print(f'сумма {general_sum}')

    if stop_flag:
        break

# Эадача №6
def int_func():
    while True:
        user_input = input("Введите несколько слов через пробел (пустой ввод - выход): ")
        if user_input == "" or user_input.isspace():
            print("Ввод завершён.")
            break

        for word in user_input.split():
            print(str(word).capitalize(), end=" ")
        print()
int_func()