# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером
# 32 и заканчивая 127-м включительно.  Вывод выполнить в табличной форме: по
# десять пар «код-символ» в каждой строке.
#
index = 0
for code in range(32, 128):
    index += 1
    print(f"{code:4} \"{chr(code)}\" ", end = "")
    if(index >= 10):
        index = 0
        print()
print()
