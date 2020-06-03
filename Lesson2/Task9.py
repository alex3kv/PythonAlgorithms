# Среди натуральных чисел, которые были введены, найти наибольшее по сумме
# цифр.  Вывести на экран это число и сумму его цифр.
#
def calculate(number):
    result = 0
    for d in number:        
            result += int(d)
    return result

count = int(input("Введите количество чисел = "))
print()

max_sum = 0
max_sum_number = None

for _ in range(0, count):
    n = input("Введите число = ")
    cur_sum = calculate(n)
    if cur_sum > max_sum:
        max_sum = cur_sum
        max_sum_number = n

print()
print(f"Наибольшая сумма чисел равна {max_sum} у числа {max_sum_number}")
