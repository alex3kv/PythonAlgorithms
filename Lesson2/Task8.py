# Посчитать, сколько раз встречается определенная цифра в введенной
# последовательности чисел.  Количество вводимых чисел и цифра, которую
# необходимо посчитать, задаются вводом с клавиатуры.
#
def calculate(number, digit):
    result = 0
    for d in number:
        if int(d) == digit:
            result += 1
    return result

digit = int(input("Введите цифру = "))
count = int(input("Введите количество чисел = "))
print()

result = 0

for _ in range(0, count):
    n = input("Введите число = ")
    result += calculate(n, digit)

print()
print(f"Цифра {digit} встречается {result} раз в введенной последовательности чисел")
