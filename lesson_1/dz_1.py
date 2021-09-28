# задание 1
word = input('введите слово')
print("слово типа string:   ",word)
number = input('введите в число')
print('ваше число типа  int:  ', number)

# задание 2
a = input("введите число: ")
number = int(a)
twice_number = int(a + a)
triple_number = int(a + a + a)
print(number + twice_number + triple_number)

# задание 3
msec = input('Введите миллисекунды:  ')
hour = round(int(msec)/3600000)
minutes = round((int(msec) - hour*3600000)/60000)
sec = round((int(msec) - hour*3600000 - minutes*60000)/1000)
print('часы:', hour)
print('минуты:',minutes)
print('секунды:',sec)

# задание 4
numb = input("Введите число: ")
real = int(numb)
list = []
while real > 0:
    item = real%10
    list.append(item)
    real = int(real/10)
print("Максимальное значение в этом числе: ", max(list))
print("Минимальное значение в этом числе: ", min(list))

# задание 5
a = int(input("Введите выручку: "))
b = int(input("Введите издержки: "))
profit = int(a-b)
if a>b:
    print("Выручка составляет: ", profit)
    print("Рентабельность составила: ", int(profit/a*100), " %" )
    count = input("Введите количнство сотрудников: ")
    print("Прибыль на каждого сотрудника составила: ", profit/int(count))
else :
    print("Убыток составил: ", b - a)

# задание 6
a = float(input("Введите начальную длину пробега: "))
b = int(input("Введите конечный результат пробега: "))
distination = []
while a < b:
    print(f"Первый день: {a}")
    a = round(a + a * 0.1, 2)
    distination.append(a)
print("Достижение вашего результата осуществиться через ",len(distination), " дней")

# this only for my first pull request
def first(a,b):
    c = a + b
    return c
