# Язык программирования - Python 3

R_0 = R_1 = R_2_1 = R_2_2 = -2000
# Переменные, в которых мы будем хранить числа

N = int(input())
# Не будем проверять входные данные на корректность
# В ЕГЭ (но не в реальной жизни!) это не нужно

for i in range(N):
    num = int(input())
    if num % 3 == 0:
        R_0 = max(R_0, num)
        # Перезаписываем число на большее, если возможно
    elif num % 3 == 1:
        R_1 = max(R_1, num)
    elif num % 3 == 2:
        # Можно и else, но так более понятно
        if num > R_2_1:
            R_2_1, R_2_2 = num, R_2_1
            # Нужно хранить 2 наибольших числа, причём R_2_1 >= R_2_2
        elif num > R_2_2:
            R_2_2 = num

R = max(R_0 + R_1, R_2_1 + R_2_2)
# Это - вычисленное контрольное значение
if R < 0:
    # Если такого числа нет, R будет отрицательно
    # Так как все числа не превышают 1000
    R = 1
print("Вычисленное контрольное значение: {}".format(R))

# Осталось проверить пришедшее число
result = int(input())
if R == result:
    print("Контроль пройден")
else:
    print("Контроль не пройден")
