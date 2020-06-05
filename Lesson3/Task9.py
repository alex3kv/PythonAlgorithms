'''
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
'''
import random

matrix = [[random.randint(0, 99) for _ in range(1,5)] for _ in range(1, 5)]
print(matrix)

max_row_min = None

for row in matrix:

    row_min = None

    for item in row:
        if row_min == None or row_min > item:           
            row_min = item

    if max_row_min == None or max_row_min < row_min:
        max_row_min = row_min    

print(f"Максимальный элемент среди минимальных элементов столбцов матрицы = {max_row_min}")
