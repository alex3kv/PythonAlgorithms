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
import cProfile

N = 1000

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

def sieve(n):
	k = 1

	if  n < 100:
		k = 5
	if 100 < n and n <= 1000:
		k = 8
	if 1000 < n and n <= 2000:
		k = 9
	if 2000 < n and n <= 3000:
		k = 10

	sieve = build_sieve(k * n)	
	return sieve[n - 1]


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

print(sieve(N))
print(prime(N))

cProfile.run(f"sieve({N})")
cProfile.run(f"prime({N})")

'''
          500    1000    2000    3500             
sieve   0.003   0.006   0.012   0.022   
prime   0.013   0.027   0.064   0.110

Наиболее оптимальный алгоритм для нахождения простых чисел «Решето Эратосфена» если применить формулу распределения простых чисел в натуральном рядоу можно добиться наиболее оптимальных результатов
'''