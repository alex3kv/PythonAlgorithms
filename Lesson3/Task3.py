'''
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''
import random

# генерируем массив случайных целых чисел от 0 до 99 со случайным размером от 10 до 30
arr = [random.randint(0, 99) for _ in range(random.randint(10, 30))]
print(arr)

min_idx = 0
max_idx = 0

for i, el in enumerate(arr):
    if arr[min_idx] > el:
        min_idx = i
    if arr[max_idx] < el:
        max_idx = i

arr[min_idx], arr[max_idx] = arr[max_idx], arr[min_idx]
print(arr)
