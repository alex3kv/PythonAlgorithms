# Написать программу, доказывающую или проверяющую, что для множества
# натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое
# натуральное число.
#
def calculate_row(n):
    r = 0
    for i in range(1, n + 1):
        r += i
    return r

n = int(input("Ведите для формулы 1+2+...+n = n(n+1)/2 значение n = "))

right_value = n * (n + 1) / 2
left_value = calculate_row(n)

if left_value == right_value:
    print(f"Формула справедлива для {n}")
else:
    print(f"Формула неверна для {n}")
