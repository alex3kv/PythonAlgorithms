# Пользователь вводит номер буквы в алфавите.  Определить, какая это буква.
START_INDEX = ord("a") - 1

i1 = int(input("Введите номер строчной латинской буквы в алфавите = "))
l1 = chr(START_INDEX + i1)

print(f"Под номером {i1} соотвествует следующая строчкая буква в латинском алфавите - {l1}")
