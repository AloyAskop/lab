'''
Требуется для своего варианта второй части л.р. №6 (усложненной программы) разработать реализацию с использованием графического интерфейса. 
Допускается использовать любую графическую библиотеку питона. 
Рекомендуется использовать внутреннюю библиотеку питона  tkinter.
В программе должны быть реализованы минимум одно окно ввода, одно окно вывода (со скролингом), одно текстовое поле, одна кнопка.
'''

import tkinter as tk
from tkinter import scrolledtext

def is_even(num):
    return sum(int(digit) for digit in str(num)) % 2 == 0

def prod_dig(num):
    pr = 1
    for digit in str(num):
        pr *= int(digit)
    return pr

def even_f(n):
    ev = range(2, n + 1, 2)
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

def calculate_even_numbers():
    try:
        n = int(entry.get())
        if n < 2:
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, "Введите число больше или равное 2.")
            return
        results = even_f(n)
        if results:
            optimal_number = max_prod(results)
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, f"Четные числа: {results}\nОптимальное число: {optimal_number}")
        else:
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, "Нет четных чисел, соответствующих условиям.")
    except ValueError:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Пожалуйста, введите корректное целое число.")

root = tk.Tk()
root.title("Четные числа")

label = tk.Label(root, text="Введите число:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Вычислить", command=calculate_even_numbers)
button.pack()

output_text = scrolledtext.ScrolledText(root, width=40, height=10)
output_text.pack()

root.mainloop()