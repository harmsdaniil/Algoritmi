'''1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.


a = [0]*8
for i in range(2,100):
    for j in range(2,10):
        if i%j == 0:
            a[j-2] += 1
i = 0
while i < len(a):
    print(i+2, ' - ', a[i])
    i += 1

2.Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с
нуля), т.к. именно в этих позициях первого массива стоят четные числа.


from random import random
N = 12
arr = [0]*N
even = []
for i in range(N):
    arr[i] = int(random() * 10) + 10
    if arr[i] % 2 == 0:
        even.append(i)
print(arr)
print('Индексы четных элементов: ', even)


3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import random
N = 15
arr = [0]*N
for i in range(N):
    arr[i] = int(random()*100)
    print(arr[i],end=' ')
print()

mn = min(arr)
mx = max(arr)
imn = arr.index(mn)
imx = arr.index(mx)
print('arr[%d]=%d arr[%d]=%d' % (imn + 1, mn, imx + 1, mx))
arr[imn], arr[imx] = arr[imx], arr[imn]

for i in range(15):
    print(arr[i], end=' ')
print()

4. Определить, какое число в массиве встречается чаще всего.

import collections

import random
m = [random.randint(1,5) for i in range(20)]
print(m)
d = collections.Counter(m)

# print(d)
print(d.most_common(1))


5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве.

from random import random

N = 15
arr = []
for i in range(N):
    arr.append(int(random() * 100) - 50)
print(arr)

i = 0
index = -1
while i < N:
    if arr[i] < 0 and index == -1:
        index = i
    elif arr[i] < 0 and arr[i] > arr[index]:
        index = i
    i += 1

print(index + 1, ':', arr[index])


6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный
 и максимальный элементы в сумму не включать.

from random import random

N = 10
a = [0]*N
for i in range(N):
    a[i] = int(random()*50)
    print('%3d' % a[i], end='')
print()

min_id = 0
max_id = 0
for i in range(1,N):
    if a[i] < a[min_id]:
        min_id = i
    elif a[i] > a[max_id]:
        max_id = i
print(a[min_id], a[max_id])

if min_id > max_id:
    min_id, max_id = max_id, min_id

summa = 0
for i in range(min_id+1, max_id):
    summa += a[i]
print(summa)

7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба 
являться минимальными), так и различаться.

from random import random

N = 10
a = []
for i in range(N):
    a.append(int(random() * 100))
    print("%3d" % a[i], end='')
print()

if a[0] > a[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0

for i in range(2, N):
    if a[i] < a[min1]:
        b = min1
        min1 = i
        if a[b] < a[min2]:
            min2 = b
    elif a[i] < a[min2]:
        min2 = i

print("№%3d:%3d" % (min1 + 1, a[min1]))
print("№%3d:%3d" % (min2 + 1, a[min2]))

8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму 
введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

M = 5
N = 4
a = []
for i in range(N):
    b = []
    s = 0
    print("%d-я строка:" % i)
    for j in range(M - 1):
        n = int(input())
        s += n
        b.append(n)
    b.append(s)
    a.append(b)

for i in a:
    print(i)

9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import random
M = 10
N = 5
a = []
for i in range(N):
    b = []
    for j in range(M):
        n = int(random()*200)
        b.append(n)
        print('%4d' % n,end='')
    a.append(b)
    print()

mx = -1
for j in range(M):
    mn = 200
    for i in range(N):
        if a[i][j] < mn:
            mn = a[i][j]
    if mn > mx:
        mx = mn
print("Максимальный среди минимальных: ", mx)





Доп.
Написать функцию, которая генерит матрицы нужного размера и заполняет её по спирали
N=2
1 2
4 3

N=3
1 2 3
8 9 4
7 6 5

N = 5
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9

'''

n = int(input('Введите число размерности матрицы: '))
mat = [[0]*n for i in range(n)]
st, m = 1, 0

mat[n//2][n//2]=n*n
for v in range(n//2):

    for i in range(n-m):
        mat[v][i+v] = st
        st+=1

    for i in range(v+1, n-v):
        mat[i][-v-1] = st
        st+=1

    for i in range(v+1, n-v):
        mat[-v-1][-i-1] =st
        st+=1

    for i in range(v+1, n-(v+1)):
        mat[-i-1][v]=st
        st+=1

    m+=2

for i in mat:
    print(*i)