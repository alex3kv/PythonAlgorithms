'''
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. 
Сами минимальный и максимальный элементы в сумму не включать.
'''
import random

# генерируем массив случайных целых чисел
arr = [random.randint(0, 100) for _ in range(random.randint(10, 30))]
print(arr)

min_idx = 0
max_idx = 0

for i, el in enumerate(arr):
    if arr[min_idx] > el:
        min_idx = i
    if arr[max_idx] < el:
        max_idx = i

step = 1 if min_idx < max_idx else -1

result = 0
for i in range(min_idx + step, max_idx, step):
    result += arr[i]

print(f"Сумма чисел, находящихся между минимальным {arr[min_idx]} и максимальным {arr[max_idx]} элементами, равна {result}")
