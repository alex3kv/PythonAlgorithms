'''
Определить, какое число в массиве встречается чаще всего.
'''
import random

# генерируем массив случайных целых чисел
arr = [random.randint(1, 10) for _ in range(random.randint(10, 30))]
print(arr)

res = {}
max_number_count = 0
max_number = None

for el in arr:
    res.setdefault(el, 0)
    res[el] += 1
    if(res[el] > max_number_count):
        max_number_count = res[el]
        max_number = el

print(res)
print(f"Число {max_number} встречается {max_number_count} раз")
