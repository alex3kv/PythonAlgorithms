# Посчитать четные и нечетные цифры введенного натурального числа.  Например,
# если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и
# 5).
#
n = input("Введите число = ")

even = 0
odd = 0

for d in n:
    digit = int(d)

    if digit % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"В введенном числе {n} посчитано: {even} - четных цифр и {odd} - нечетных цифр")
