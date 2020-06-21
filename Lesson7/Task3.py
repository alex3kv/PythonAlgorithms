'''
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. 
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима)
'''
import random

# генерируем массив для отладки
#arr = [_ for _ in range(11)]
#random.shuffle(arr)

# генерируем массив случайных целых чисел
m = random.randint(5, 10)
arr = [random.randint(-100, 100) for _ in range(2 * m + 1)]
print(arr)

def find_median(array):

    result = array[:]

    while len(result) > 1:              
                
        idx_min = 0
        idx_max = 0

        l = len(result)

        for i in range(l):
            if result[i] < result[idx_min]:
                idx_min = i
            if result[i] > result[idx_max]:
                idx_max = i

        result[0], result[idx_min] = result[idx_min], result[0]

        # учитываем ситуацию когда максимальный элемент на 1 месте
        if idx_max == 0: idx_max = idx_min
        result[l - 1], result[idx_max] = result[idx_max], result[l - 1]

        print(result)

        result = result[1:-1]                

    return result[0]

median = find_median(arr)
print(median)
