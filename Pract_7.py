'''1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами
на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована
в виде функции. По возможности доработайте алгоритм (сделайте его умнее).'''

# from random import randint
#
# def bubble(array):
#     for i in range(N - 1):
#         for j in range(N - i - 1):
#             if array[j] < array[j + 1]:
#                 buff = array[j]
#                 array[j] = array[j + 1]
#                 array[j + 1] = buff
#
# N = 10
# a = []
# for i in range(N):
#     a.append(randint(-100, 100))
#
# print(a)
# bubble(a)
# print(a)



'''2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами 
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.'''

# from random import randint
# def merge(left_list, right_list):
#     sorted_list = []
#     left_list_index = right_list_index = 0
#     # Мы будет часто используем длины списков, поэтому удобно сразу создавать переменные для этого
#     left_list_length, right_list_length = len(left_list), len(right_list)
#     for _ in range(left_list_length + right_list_length):
#         if left_list_index < left_list_length and right_list_index < right_list_length:
#             # Мы проверяем, какое значение с начала каждого списка меньше
#             # Если элемент в начале левого списка меньше, добавляем его в отсортированный список
#             if left_list[left_list_index] <= right_list[right_list_index]:
#                 sorted_list.append(left_list[left_list_index])
#                 left_list_index += 1
#             # Если элемент в начале правого списка меньше, добавляем его в отсортированный список
#             else:
#                 sorted_list.append(right_list[right_list_index])
#                 right_list_index += 1
#         # Если мы достигли конца левого списка, добавляем элементы из правого списка
#         elif left_list_index == left_list_length:
#             sorted_list.append(right_list[right_list_index])
#             right_list_index += 1
#         # Если мы достигли конца правого списка, добавляем элементы из левого списка
#         elif right_list_index == right_list_length:
#             sorted_list.append(left_list[left_list_index])
#             left_list_index += 1
#     return sorted_list
# def merge_sort(nums):
#     # Если список представляет собой один элемент, возвращаем его
#     if len(nums) <= 1:
#         return nums
#     # Используем деление с округленим по наименьшему целому для получения средней точки, индексы должны быть целыми числами
#     mid = len(nums) // 2
#     # Сортируем и объединяем каждую половину
#     left_list = merge_sort(nums[:mid])
#     right_list = merge_sort(nums[mid:])
#     # Объединить отсортированные списки в новый
#     return merge(left_list, right_list)
# # Проверяем, что все работает
# random_list_of_nums = [120, 45, 68, 250, 176]
#
# N = 10
# a = []
# for i in range(N):
#     a.append(randint(0, 50))
# print(a)
# a = merge_sort(a)
# print(a)

'''3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. 
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше 
медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком 
сложно, то используйте метод сортировки, который не рассматривался на уроках'''

from random import randint

m = 4
size = 2 * m + 1
a = []
for i in range(size):
    a.append(randint(1,50))
lst3 = a


print(f'Исходный НЕотсортированный список:\n {lst3}\n')


def median(lst):
    # нахождение медианы для четного кол-ва элементов
    if len(lst) % 2 == 0:
        center = []

        for i in lst:
            b = 0

            for j in lst:

                if i < j:
                    b += 1

            if len(lst) == b * 2 + 2 or len(lst) == b * 2:
                center.append(i)
        return sum(center) / 2

    # нахождение медианы для НЕ четного кол-ва элементов
    else:
        for i in lst:
            num = i
            b = 0

            for j in lst:

                if i < j:
                    b += 1

            if len(lst) == 2 * b + 1:
                return num


print(f'Медиана НЕотсортированного списка: {median(lst3)}\n')

print(f'Отсортированный список: \n{sorted(lst3)}')
