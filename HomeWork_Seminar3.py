# # Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# # Пример:

# # - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# some_list = [2, 4, 5, 9, 3]
# sum = 0
# for i in range(1, len(some_list), 2):
#     sum = sum + some_list[i]
# print(sum)

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# from random import randint
# some_list = [randint(1, 10) for _ in range(6)]
# new_list = []
# print(some_list)
# if len(some_list) % 2 == 0:
#     for i in range(0, len(some_list) // 2):
#         new_list.append(some_list[i] * some_list[len(some_list) - 1 - i])
# else:
#     for i in range(0, len(some_list) // 2 + 1):
#             new_list.append(some_list[i] * some_list[len(some_list) - 1 - i])
# print(new_list)

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


# some_list = [1.1, 1.2, 3.1, 5.3, 10.01]
# max = 0
# min = 1
# for i in range(0, len(some_list)):
#     some_list[i] = some_list[i] % 1
#     if some_list[i] >= max:
#         max = some_list[i]
#     if some_list[i] <= min:
#         min = some_list[i]
# print(max - min)


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


# number = int(input('Введите десятичное число: '))
# # some_list = []
# d = ''
# while number > 0:
#     d = str(number % 2) + d
#     number = number // 2
# print(d)


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


number = int(input('Введите число: '))
fib = [0] * (((number + 1) * 2) - 1)
fib[number + 1] = 1
for i in range((number + 2), ((number * 2) + 1)):
    fib[i] = fib[i - 2] + fib[i - 1]


for i in range(0, number + 1, 2):
    fib[i] = fib[len(fib) - 1 - i] * (-1)


for i in range(1, number + 1, 2):
    fib[i] = fib[len(fib) - 1 - i]

print(fib)


