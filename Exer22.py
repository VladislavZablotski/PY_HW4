# # Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# # Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множе5,ств.

import random
n = int(input("Введите первое число: "))
m = int(input("Введите второе число: "))
print (n,m)
lst1 = [random.randint(0,9) for i in range(1, n + 1)]
lst2 = [random.randint(0,9) for i in range(1, m + 1)]
lst3 = []
print(lst1, lst2)
for i in lst1:
    if i in lst2 and i in lst2 and i not in lst3:
        lst3.append(i)
for i in lst3:
    if i == max(lst3):
        lst3.sort()
print(lst3)
