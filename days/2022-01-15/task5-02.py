''' https://inf-ege.sdamgia.ru/problem?id=35463
Алгоритм получает на вход натуральное число N > 1 и строит по нему новое число R следующим образом:
    1. Строится двоичная запись числа N.
    2. Подсчитывается количество нулей и единиц в полученной записи. 
    Если их количество одинаково, в конец записи добавляется её последняя цифра. 
    В противном случае в конец записи добавляется та цифра, 
    которая встречается реже.
    3. Шаг 2 повторяется ещё два раза
    4. Результат переводится в десятичную систему.
При каком наименьшем числе N > 99 в результате работы алгоритма получится число, кратное 4?
'''

n = 99
while True:
    n += 1
    b = bin(n)[2:]

    d1, d0 = b.count('1'), b.count('0')
    b += b[-1] if d0==d1 else ('0' if d0<d1 else '1')
    d1, d0 = b.count('1'), b.count('0')
    b += b[-1] if d0==d1 else ('0' if d0<d1 else '1')
    d1, d0 = b.count('1'), b.count('0')
    b += b[-1] if d0==d1 else ('0' if d0<d1 else '1')

    r = int(b, 2)
    if r % 4 == 0:
        print(n)
        break