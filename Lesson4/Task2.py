'''
Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».

Примечание. Вспомните классический способ проверки числа на простоту.

Пример работы программ:
sieve(2)
3
prime(4)
7
sieve(5)
11
prime(1)
2
'''
import math

def build_sieve(n):
	arr = [i for i in range(n)]
	arr[1] = 0

	for i in range(2, n):

		if arr[i] != 0:			
			j = i * 2

			while j < n:
				arr[j] = 0
				j += i

	return [i for i in arr if i != 0]

print(build_sieve(100))

def sieve(n):
	sieve = build_sieve(100)	
	return sieve[n-1]

print(sieve(5))

# проверка числа на простоту
def is_prime(n):

	if n == 2:
		return True

	max = math.ceil(math.sqrt(n))
	for i in range(2, max + 1):
		if n % i == 0:
			return False
	return True

# находит n-ое простое число
def prime(max_index):
	i = 0
	number = 1
	while True:		
		number += 1

		if is_prime(number):
			i += 1
		
		if i == max_index:
			break
	return number

print(prime(5))
