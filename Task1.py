# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

list1 = []

print("Введите количество элементов в массиве:", end="")

quantity = int(input())

for i in range(quantity):
    print("введите число: ", end="")
    list1.insert(i, int(input()))
print(list1)

print("Введите число в массиве:", end="")
num = int(input())

count = 0


for s in list1:
    if s == num:
        count += 1

if count > 0:
    print(f"Число {num} повторяется {count} раз(а)")

