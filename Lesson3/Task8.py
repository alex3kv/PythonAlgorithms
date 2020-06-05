'''
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. 
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. 
В конце следует вывести полученную матрицу.
'''
matrix = []

print("Введите элементы матрицы:")
for i in range(1, 5):
    print()
    print(f"Ввод строки {i}")

    row = []
    row_sum = 0

    for j in range(1, 5):
        el = int(input(f"Введите элемент ({i},{j}) = "))
        row.append(el)
        row_sum += el

    row.append(row_sum)
    matrix.append(row)

print()
print("Полученная матрица:")
for row in matrix:
    for item in row:
        print(f"{item:>4}", end="")
    print()
