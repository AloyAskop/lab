'''Требуется написать ООП с графическим интерфейсом в соответствии со своим вариантом. 
Должны быть реализованы минимум один класс, три атрибута, четыре метода (функции). 
Ввод данных из файла с контролем правильности ввода. 
Базы данных не использовать. При необходимости сохранять информацию в файлах, разделяя значения запятыми (CSV файлы) или пробелами.
Для GUI и визуализации использовать библиотеку tkinter.
Объекты – пятиугольники
Функции:	сегментация
визуализация
раскраска
перемещение на плоскости
'''

import tkinter as tk
from tkinter import messagebox
from math import cos, sin

class Pentagon:
    def __init__(self, x, y, color="blue"):
        self.x = x
        self.y = y
        self.color = color
        self.segments = []

    def segment(self):
        self.segments = [(self.x + i * 10, self.y) for i in range(5)]
        return self.segments

    def visualize(self, canvas):
        points = self.calculate_points()
        canvas.create_polygon(points, fill=self.color)

    def colorize(self, color):
        self.color = color

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def calculate_points(self):
        points = []
        for i in range(5):
            angle = 2 * 3.14159 * i / 5
            x = self.x + 50 * cos(angle)
            y = self.y + 50 * sin(angle)
            points.append((x, y))
        return points

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Pentagon App")
        self.root.geometry("600x600")
        self.root.resizable(False,False)
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        self.pentagons = []
        self.current_pentagon_index = None

        self.input_frame = tk.Frame(root)
        self.input_frame.pack(side=tk.LEFT, padx=10)

        self.x_label = tk.Label(self.input_frame, text="Введите X:")
        self.x_label.grid(row=0, column=0)
        self.x_entry = tk.Entry(self.input_frame)
        self.x_entry.grid(row=0, column=1)

        self.y_label = tk.Label(self.input_frame, text="Введите Y:")
        self.y_label.grid(row=1, column=0)
        self.y_entry = tk.Entry(self.input_frame)
        self.y_entry.grid(row=1, column=1)

        self.color_label = tk.Label(self.input_frame, text="Введите цвет:")
        self.color_label.grid(row=2, column=0)
        self.color_entry = tk.Entry(self.input_frame)
        self.color_entry.grid(row=2, column=1)

        self.select_index_label = tk.Label(self.input_frame, text="Введите номер для выбора:")
        self.select_index_label.grid(row=3, column=0)
        self.select_index_entry = tk.Entry(self.input_frame)
        self.select_index_entry.grid(row=3, column=1)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(side=tk.LEFT)

        self.create_button = tk.Button(self.button_frame, text="Создать пятиугольник", command=self.create_pentagon)
        self.create_button.pack(pady=5)

        self.select_button = tk.Button(self.button_frame, text="Выбрать пятиугольник", command=self.select_pentagon)
        self.select_button.pack(pady=5)

        self.segment_button = tk.Button(self.button_frame, text="Сегментация", command=self.segment_pentagon)
        self.segment_button.pack(pady=5)

        self.color_button = tk.Button(self.button_frame, text="Раскрасить", command=self.color_pentagon)
        self.color_button.pack(pady=5)

        self.move_button = tk.Button(self.button_frame, text="Переместить", command=self.move_pentagon)
        self.move_button.pack(pady=5)

        self.segment_output = tk.Text(root, height=40, width=20)
        self.segment_output.pack(pady=10)

        self.dx_label = tk.Label(self.input_frame, text="Введите dx:")
        self.dx_label.grid(row=4, column=0)
        self.dx_entry = tk.Entry(self.input_frame)
        self.dx_entry.grid(row=4, column=1)

        self.dy_label = tk.Label(self.input_frame, text="Введите dy:")
        self.dy_label.grid(row=5, column=0)
        self.dy_entry = tk.Entry(self.input_frame)
        self.dy_entry.grid(row=5, column=1)
    def create_pentagon(self):
        try:
            x = int(self.x_entry.get())
            y = int(self.y_entry.get())
            color = self.color_entry.get() or "blue"
            pentagon = Pentagon(x, y, color)
            self.pentagons.append(pentagon)
            self.current_pentagon_index = len(self.pentagons) - 1
            pentagon.visualize(self.canvas)
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректные координаты.")

    def select_pentagon(self):
        try:
            index = int(self.select_index_entry.get()) - 1
            if 0 <= index < len(self.pentagons):
                self.current_pentagon_index = index
            else:
                messagebox.showerror("Ошибка", "Выберите корректный номер пятиугольника.")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректный номер.")

    def segment_pentagon(self):
        if self.current_pentagon_index is not None:
            segments = self.pentagons[self.current_pentagon_index].segment()
            self.segment_output.delete(1.0, tk.END)
            self.segment_output.insert(tk.END, f"Сегменты: {segments}\n")
        else:
            messagebox.showwarning("Предупреждение", "Сначала выберите пятиугольник.")

    def color_pentagon(self):
        if self.current_pentagon_index is not None:
            color = self.color_entry.get()
            self.pentagons[self.current_pentagon_index].colorize(color)
            self.canvas.delete("all")
            for pentagon in self.pentagons:
                pentagon.visualize(self.canvas)
        else:
            messagebox.showwarning("Предупреждение", "Сначала выберите пятиугольник.")

    def move_pentagon(self):
        if self.current_pentagon_index is not None:
            try:
                dx = int(self.dx_entry.get())
                dy = int(self.dy_entry.get())
                self.pentagons[self.current_pentagon_index].move(dx, dy)
                self.canvas.delete("all")
                for pentagon in self.pentagons:
                    pentagon.visualize(self.canvas)
            except ValueError:
                messagebox.showerror("Ошибка", "Введите корректные значения для dx и dy.")
        else:
            messagebox.showwarning("Предупреждение", "Сначала выберите пятиугольник.")


root = tk.Tk()
app = App(root)
root.mainloop() 
