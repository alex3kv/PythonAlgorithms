'''
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
'''
import random

# генерируем массив случайных целых чисел
arr = [random.randint(-10, 10) for _ in range(random.randint(10, 30))]
print(arr)

max_negative_number = None

for el in arr:
    if el < 0:
        if max_negative_number == None:
            max_negative_number = el
        if  el > max_negative_number:
            max_negative_number = el

print(f"Максимальныое отрицательное число {max_negative_number}")
