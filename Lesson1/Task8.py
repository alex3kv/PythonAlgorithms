# Вводятся три разных числа.  Найти, какое из них является средним (больше
# одного, но меньше другого).
#
print("Введите три числа: ")
x1 = int(input())
x2 = int(input())
x3 = int(input())

result = x3 

if x2 < x1 < x3 or x3 < x1 < x2:
    result = x1
elif x1 < x2 < x3 or x3 < x2 < x1:
    result = x2

print()
print(f"Среднее число = {result}")