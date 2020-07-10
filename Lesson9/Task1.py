'''
1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.

Примечания:
* в сумму не включаем пустую строку и строку целиком;
* без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача считается не решённой.
'''

def calculate_substrings(s:str) -> int:
    
	length = len(s)

	hash_set = set()

	for i in range(length):
		for j in range(i, length):
			hash_set.add(hash(s[i:j + 1].encode('utf-8')))

	return len(list(hash_set))


s = input('Введите строку: ')
result = calculate_substrings(s)

print(f'Количество неповторяющихся подстрок - {result}')
