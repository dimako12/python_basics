"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
n = int(input('введите число'))
##total = (n+int(str(n) + str(n)) + int(str(n) + (str(n) + (str(n)))
total = (n + int(str(n) + str(n)) + int(str(n) + str(n)+ str(n)))
print("Сумма чисел n + nn + nnn - %d" % total)