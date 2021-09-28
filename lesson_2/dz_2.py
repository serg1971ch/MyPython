# Задание№1
instances = ['Sergei', 32, 23.1, bool('789'),{1,2,5}, [5,3,9],(1,4,7),{'Moscow': 1, 'Samara':5}]
for el in instances:
    print(type(el))

# Задание№2
my_input = [1,2]
while len(my_input) < 10:
    item   = int(input("Please enter a number to be added 10 elements, if you want to finish type ==> 100:\n"))
    print(item)
    my_input.append(item)
    if item == 00:
        break
print("Исходный массив: ",my_input)
if len(my_input) % 2 == 0:
    i = 0
    while i < len(my_input):
        el = my_input[i]
        my_input[i] = my_input[i+1]
        my_input[i+1] = el
        i += 2
else:
    i = 0
    while i < len(my_input) - 1:
        el = my_input[i]
        my_input[i] = my_input[i + 1]
        my_input[i + 1] = el
        i += 2
print("Заданный массив", my_input)

# Задание№3
number = int(input("Enter month number: "))
if number <= 12 and number >= 1:
    month_dict = {1: 'January',
                  2: 'February',
                  3: 'March',
                  4: 'April',
                  5: 'May',
                  6: 'June',
                  7: 'Jule',
                  8: 'August',
                  9: 'September',
                  10: 'October',
                  11: 'November',
                  12: 'December'}
    month_list = list(month_dict.values())
    for i, el in enumerate(month_list):
        if i == number-1:
            print(f"Month from list is {month_list[i]}")
            break
    print(f"Month from dict is {month_dict[number]}")
else:
    print("You made a mistake")

# Задание№4
my_str = input("Enter string: ")
a = my_str.split(' ')
for i, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}. - {el}")


# Задание№5
number = int(input("Enter number: "))
my_list = [7, 4, 3, 2]
c = my_list.count(number)
for element in my_list:
    if c > 0:
        i = my_list.index(number)
        my_list.insert(i+c, number)
        break
    else:
        if number > element:
            j = my_list.index(element)
            my_list.insert(j, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)

