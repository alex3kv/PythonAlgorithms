# Написать программу, которая будет складывать, вычитать, умножать или делить
# два числа.  Числа и знак операции вводятся пользователем.  После выполнения
# вычисления программа не завершается, а запрашивает новые данные для
# вычислений.  Завершение программы должно выполняться при вводе символа '0' в
# качестве знака операции.  Если пользователь вводит неверный знак (не '0',
# '+', '-', '', '/'), программа должна сообщать об ошибке и снова запрашивать
# знак операции.  Также она должна сообщать пользователю о невозможности
# деления на ноль, если он ввел его в качестве делителя.
#
def calculate(a, b, o):
    if o == "+":
        return a + b
    elif o == "-":
        return a - b
    elif o == "*":
        return a * b
    elif o == "/":        
        return a / b    


while True:
    
    o = None

    while True:
        o = input("Введите знак операции = ")
        if o == "0" or o == "+" or o == "-" or o == "*" or o == "/":
            break
        print("Введенный знак не поддерживается, использует только поддерживаемые знаки.")
        print()

    if o == "0":
        break

    print()
    a = float(input("Введите первый аргумент = "))
    b = float(input("Введите второй аргумент = "))
    print()
           
    if o == "/" and b == 0:        
        print("На ноль делить нельзя")
        print()
        continue
        
    r = calculate(a, b, o)
        
    print(f"Для выражения \"{a} {o} {b}\" получен результат = {r}")
    print()
