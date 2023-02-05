# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

print("Введите число: ", end="")
num = int(input())
list1 = []

i = 1
count = 0
while count < num:
    list1.insert(count, i)
    count += 1
    i += 1
print(list1)

print("Введите число: ", end="")
X = int(input())

if X > list1[-1]:
    print(list1[-1])
    exit()

if X <= 0:
    print(list1[0])
    exit()

flag = False

for i in list1:
    if i == X:
        print(i - 1)
        exit()
