'''Задание состоит из двух частей. 
1 часть – написать программу в соответствии со своим вариантом задания. 
Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, 
введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов 
(которое будет сокращать количество переборов) и целевую функцию для нахождения оптимального  решения.
Вариант 15. Вывести все четные натуральные числа до n, крайняя левая цифра которых не превышает 5.
Усложнение: Сумма цифр в числе должна быть чётной 
Целевая функция: Найти число с самым большим произведением цифр
'''
import numpy as np
import timeit

def is_even(num):
    return sum(int(digit) for digit in str(num)) % 2 == 0

def prod_dig(num):
    pr = 1
    for digit in str(num):
        pr *= int(digit)
    return pr

def even_a(n):
    res = []
    for i in range(2, n + 1, 2):
        first_digit = int(str(i)[0])
        if first_digit <= 5 and first_digit % 2 == 0 and is_even(i):
            res.append(i)
    return res

def even_f(n):
    ev = np.arange(2, n + 1, 2)
    res = [num for num in ev if int(str(num)[0]) <= 5 and int(str(num)[0]) % 2 == 0 and is_even(num)]
    return res

def max_prod(numbers):
    maxp = 0
    maxnum = None
    for number in numbers:
        pr = prod_dig(number)
        if pr > maxp:
            maxp = pr
            maxnum = number
    return maxnum

n = int(input("Введите n: "))

res_alg = even_a(n)
res_func = even_f(n)

time_a = timeit.timeit('even_a(n)', globals=globals(), number=1000)
time_f = timeit.timeit('even_f(n)', globals=globals(), number=1000)

print(f"Четные натуральные числа до {n}, крайняя левая цифра которых не превышает 5 и сумма цифр которых четная алгоритмически:")
print(res_alg)

print(f"Четные натуральные числа до {n}, крайняя левая цифра которых не превышает 5 и сумма цифр которых четная функциями:")
print(res_func)

print(f"Время алгоритмического варианта: {time_a:.6f} секунд")
print(f"Время варианта с функциями: {time_f:.6f} секунд")

answa = max_prod(res_alg)
answf = max_prod(res_func)

if answa is not None:
    print(f"Четное число с максимальным произведением цифр алгоритмически: {answa} \nПроизведение: {prod_dig(answa)}")
else:
    print("Нет четных чисел, удовлетворяющих условиям алгоритмически.")

if answf is not None:
    print(f"Четное число с максимальным произведением цифр функциями: {answf} \nПроизведение: {prod_dig(answf)}")
else:
    print("Нет четных чисел, удовлетворяющих условиям функциями.")