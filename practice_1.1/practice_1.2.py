# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и
#  выведите в формате чч:мм:сс. Используйте форматирование строк.

# 60 sec = 1 min
# 3600 sec = 60 * 60 = 1 hour
# hour = s / 3600
# min = (s - hour * 3600) / 60
# sec = s - hour * 3600 - min * 60

time = int(input('Введите секунды: '))
hour = 3600
minutes = 60

hh = time // hour
mm = (time - (hh * hour)) // minutes
ss = time - (hh * hour) - (mm * minutes)
print('{}:{}:{}'.format(hh, mm, ss))
