'''
В одномерном массиве целых чисел определить два наименьших элемента. 
Они могут быть как равны между собой (оба минимальны), так и различаться.
'''
import random

# генерируем массив случайных целых чисел от 0 до 99 со случайным размером от 10 до 30
arr = [random.randint(0, 99) for _ in range(random.randint(10, 30))]
print(arr)

min_first = 0
min_second = 0

for i, el in enumerate(arr):
    if arr[min_first] >= el:        
        min_first = i    

for i, el in enumerate(arr):    
    if arr[min_second] >= el and min_first != i:        
        min_second = i
        
print(f"Первый и второй минимальные элементы {arr[min_first]} и {arr[min_second]}")
