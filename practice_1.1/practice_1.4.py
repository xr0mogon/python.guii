# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
# число вводится, как число, а не текст

num1 = int(input('Введите целое положительное число: '))
print(num1)
n = num1 // 10
print(n, 'отделяем последнее число')
r = num1 % 10
print(r, 'возвращаем остаток от деления на 10')

while n != 0:
    d = n % 10
    print(d, ' счетчик внутри цикла')
    print('n=', n)
    n //= 10
    print('n//=10 n=', n)
    if d > r:
        r = d
print(f'наибольшей цифрой в числе {num1} будет {r}')

# второй способ
# ls = []
# while num1 > 10:
#     ls.append(num1 % 10)
#     print(ls)
#     num1 //= 10
#     print(num1)
# print(max(ls))
