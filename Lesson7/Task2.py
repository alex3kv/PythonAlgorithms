'''
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). 
Выведите на экран исходный и отсортированный массивы.
'''
import random

# генерируем массив для отладки
#arr = [float(_) for _ in range(10)]
#random.shuffle(arr)

# генерируем массив случайных целых чисел
arr = [random.uniform(0, 50) for _ in range(random.randint(5, 10))]
print(arr)

'''
1. Сортируемый массив разбивается на две части примерно одинакового размера;
2. Каждая из получившихся частей сортируется отдельно, например — тем же самым алгоритмом;
3. Два упорядоченных массива половинного размера соединяются в один.

1.1. — 2.1. Рекурсивное разбиение задачи на меньшие происходит до тех пор, пока размер массива не достигнет единицы (любой массив длины 1 можно считать упорядоченным).
3.1. Соединение двух упорядоченных массивов в один.
Основную идею слияния двух отсортированных массивов можно объяснить на следующем примере. Пусть мы имеем два уже отсортированных по возрастанию подмассива. Тогда:
3.2. Слияние двух подмассивов в третий результирующий массив.
На каждом шаге мы берём меньший из двух первых элементов подмассивов и записываем его в результирующий массив. Счётчики номеров элементов результирующего массива и подмассива, из которого был взят элемент, увеличиваем на 1.
3.4. «Прицепление» остатка.
Когда один из подмассивов закончился, мы добавляем все оставшиеся элементы второго подмассива в результирующий массив.
'''

def merge_sort(array):

    def _merge(left, right):

        result = []

        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])                
                left = left[1:]
            else:
                result.append(right[0])                
                right = right[1:]
        
        while len(left) > 0:
            result.append(left[0])                
            left = left[1:]

        while len(right) > 0:
            result.append(right[0])                
            right = right[1:]

        return result

    def _sort(arr):
        
        l = len(arr)

        if l <= 1:            
            return arr

        i = l // 2

        left = arr[:i]
        right = arr[i:]

        #print(left, right)
        return _merge(_sort(left), _sort(right))
    
    return _sort(array)


arr = merge_sort(arr)
print(arr)
