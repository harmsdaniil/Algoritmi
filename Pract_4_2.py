'''1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.'''

'''1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.'''

#решение 1

# def f():
#     a = [0]*8
#     for i in range(2,100):
#         for j in range(2,10):
#             if i%j == 0:
#                 a[j-2] += 1
#     i = 0
#     while i < len(a):
#         # print(i+2, ' - ', a[i])
#         i += 1
#
# #решение 2
#
# def g():
#     count = 0
#     for i in range(2, 100):
#         if all([i % j == 0 for j in range(2,10)]):
#             print(i)
#             count += 1
#     # print(count)
#
# import timeit
#
# print(timeit.timeit("f()", setup="from __main__ import f", number=10))
# print(timeit.timeit("g()", setup="from __main__ import g", number=10))

# 0.0016749389999999933
# 0.0020693589999999998
# первое решение менее красиво, но более быстро

'''2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.'''
# Без использования решета Эратосфена
import timeit
def h():
    # N = int(input('Введите N: '))
    N = 1000

    for k in range(2, N + 1):

        prime = True

        for i in range(2, k):
            if k % i == 0:
                prime = False
                break

        # if prime:
        #     print('{} - простое число'.format(k))


# с использованием Решета Эратосфена
import math
def j():

    def primes(N):
      # """Возвращает все простые от 2 до N"""
      sieve = set(range(2, N))
      for i in range(2, int(math.sqrt(N))):
        if i in sieve:
          sieve -= set(range(2*i, N, i))
      return sieve
    return primes(1000)
    # print(primes(10))

print(timeit.timeit("h()", setup="from __main__ import h", number=10))
print(timeit.timeit("j()", setup="from __main__ import j", number=10))


