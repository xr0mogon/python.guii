# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.


my_str = input("Введите несколько слов: ").split(' ')
word = ''
n = 1
print(my_str)

for word in my_str:
    if len(word) >= 10:  # Если слово длинное, выводить только первые 10 букв в слове.
        print(f'{n}.{word[0:10]}')
        n += 1
    else:
        print(f'{n}.{word}')
        n += 1

#
# for i in my_str:
# #   print(i)
#     if i.isalpha():
#         word += i
#     elif len(word) >= 10:  # Если слово длинное, выводить только первые 10 букв в слове.
#         print(word[0:10])
#     else:
#         if word:
#             print(f'{n+1}.(word)')
#             word = ''

#
# while my_str[i] != split():

# if (my_str[]) != ' ':




# print('.\n'.join(my_string.split[0:10]))


# n =
# while n > 0:
#     print(my_string[n])