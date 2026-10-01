
import math # подключаем модуль math

x = float(input('Введите вещественное число: ')) # запрос данных у пользователя

result = math.floor(x) + math.ceil(x) # подсчёт пола и потолка числа
print(result) # вывод результата
