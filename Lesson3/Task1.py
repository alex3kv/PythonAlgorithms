'''
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов.
'''
result = {}

for divider in range(2, 10):
    result.setdefault(divider, 0)
    for dividend in range(2, 100):
        if dividend % divider == 0:
            result[divider] += 1

for key, value in result.items():
    print(f"Для чисел из диапазона [2, 99] число {key} кратно {value:>2} раз")
