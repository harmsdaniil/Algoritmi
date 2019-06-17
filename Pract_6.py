'''1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность
вашей ОС.'''



import sys
def f():
    n = 9000000000 #int(input("Сколько будет чисел? "))
    d = 50000 #int(input("Какую цифру считать? "))
    count = 0
    for i in range(1, n + 1):
        m = int(input("Число " + str(i) + ": "))
        while m > 0:
            if m % 10 == d:
                count += 1
            m = m // 10

    # print("Было введено %d цифр %d" % (count, d))


'''алгоритм нахождения i-го по счёту простого числа.'''

def h():
    # N = int(input('Введите N: '))
    N = 1000

    for k in range(2, N + 1):

        prime = True

        for i in range(2, k):
            if k % i == 0:
                prime = False
                break

'''алгоритм нахождения i-го по счёту простого числа с использованием Решета Эратосфена'''

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
print(sys.getrefcount(f)) #2
print(sys.getrefcount(h)) #2
print(sys.getrefcount(j)) #2