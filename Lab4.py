'''
Вариант 15.
Последовательности натуральных чисел, расположенных в порядке возрастания. Для каждой такой последовательности минимальное число вывести прописью.
'''
import re

def number_to_words(num):
    digit_to_word = {
        '0': 'ноль',
        '1': 'один',
        '2': 'два',
        '3': 'три',
        '4': 'четыре',
        '5': 'пять',
        '6': 'шесть',
        '7': 'семь',
        '8': 'восемь',
        '9': 'девять'
    }
    return ' '.join(digit_to_word[digit] for digit in str(num))

try:
    with open('input.txt', 'r', encoding='utf-8') as file:
        cont = file.read().strip()

    cont = re.sub(r'[^0-9\s-]', '', cont)

    nums = [int(num) for num in re.findall(r'-?\b[1-9]\d*\b', cont)]
    cur = []
    results = []

    for num in nums:
        if not cur or num > cur[-1]:
            cur.append(num)
        else:
            if len(cur) > 1:
                min_num = min(cur)
                min_num_w = number_to_words(min_num)
                sr = [str(num) for num in cur if num != min_num]
                results.append(f"{min_num_w} {' '.join(sr)}")
            cur = [num]

    if len(cur) > 1:
        min_num = min(cur)
        min_num_w = number_to_words(min_num)
        sr = [str(num) for num in cur if num != min_num]
        results.append(f"{min_num_w} {' '.join(sr)}")

    for result in results:
        print(result)

except Exception as e:
    print(e)