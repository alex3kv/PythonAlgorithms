"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Примечание: 
Если воспользоваться функциями hex() и/или int() для преобразования систем счисления, задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит. 
Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.
"""
from collections import deque

class HexNumber:
    
    HEX_NUM = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, 
                0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

    def __init__(self, value):
       self.__value = list(value)

    @staticmethod
    def add(num1, num2):

        result = deque()

        transfer = 0

        if len(num2) > len(num1):
            num1, num2 = deque(num2), deque(num1)
        else:
            num1, num2 = deque(num1), deque(num2)

        while num1:

            if num2:
                res = HexNumber.HEX_NUM[num1.pop()] + HexNumber.HEX_NUM[num2.pop()] + transfer
            else:
                res = HexNumber.HEX_NUM[num1.pop()] + transfer

            transfer = 0

            if res < 16:
                result.appendleft(HexNumber.HEX_NUM[res])
            else:
                result.appendleft(HexNumber.HEX_NUM[res - 16])
                transfer = 1

        if transfer:
            result.appendleft("1")

        return list(result)

    def __add__(self, other):
        result = HexNumber.add(self.__value, other.value)
        return HexNumber(result)

    @staticmethod
    def mul(num1, num2):

        result = deque()

        spam = deque([deque() for _ in range(len(num2))])

        num1, num2 = num1.copy(), deque(num2)

        for i in range(len(num2)):
            m = HexNumber.HEX_NUM[num2.pop()]

            for j in range(len(num1) - 1, -1, -1):
                spam[i].appendleft(m * HexNumber.HEX_NUM[num1[j]])

            for _ in range(i):
                spam[i].append(0)

        transfer = 0

        for _ in range(len(spam[-1])):
            res = transfer

            for i in range(len(spam)):
                if spam[i]:
                    res += spam[i].pop()

            if res < 16:
                result.appendleft(HexNumber.HEX_NUM[res])

            else:
                result.appendleft(HexNumber.HEX_NUM[res % 16])
                transfer = res // 16

        if transfer:
                result.appendleft(HexNumber.HEX_NUM[transfer])

        return list(result)

    def __mul__(self, other):       
        result = HexNumber.mul(self.__value, other.value)
        return HexNumber(result)

    def __str__(self):        
        return "".join(self.__value)

    @property
    def value(self):
        return self.__value

#a = input("Введите число 1: ").upper()
#b = input("Введите число 2: ").upper()
a = "A2"
b = "C4F"

a1 = HexNumber(a)
b1 = HexNumber(b)

print(f"{a} + {b} = {a1 + b1}")
print(f"{a} * {b} = {a1 * b1}")
