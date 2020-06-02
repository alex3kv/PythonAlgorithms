# Сформировать из введенного числа обратное по порядку входящих в него цифр и
# вывести на экран.  Например, если введено число 3486, надо вывести 6843.
#
str_number = input("Введите число = ")

n = int(str_number)
nr = 0
while n > 0:
    nr = nr * 10
    nr += n % 10    
    n = n // 10

print(f"Введено число {str_number} обратное {nr}")
