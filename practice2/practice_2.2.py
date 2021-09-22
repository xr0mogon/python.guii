#  2. Для списка реализовать обмен значений соседних элементов,
#  т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
#  При нечетном количестве элементов последний сохранить на своем месте.
#  Для заполнения списка элементов необходимо использовать функцию input().

index1 = 0
index2 = 1
new_list = []
n = int(input('Введите КОЛИЧЕСТВО элементов будущего списка: '))

for i in range(n):
    new_list.append(input('Введите новый элемент списка: '))
print(new_list, type(new_list))

while n > 1:
    new_list[index1], new_list[index2] = new_list[index2], new_list[index1]
    index1 += 2
    index2 += 2
    n -= 2
print(new_list)
