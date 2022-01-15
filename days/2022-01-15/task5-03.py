''' https://inf-ege.sdamgia.ru/problem?id=15622
На вход алгоритма подаётся натуральное число N. 
Алгоритм строит по нему новое число R следующим образом.
  1. Строится двоичная запись числа N.
  2. К этой записи дописываются справа ещё два разряда по следующему 
     правилу: складываются все цифры двоичной записи, если
     а) сумма нечетная к числу дописывается 11,
     б) сумма четная, дописывается 00.

Полученная таким образом запись является двоичной записью искомого числа R. 
Укажите такое наименьшее число R, которое превышает 114 и может являться результатом работы алгоритма. 
В ответе это число запишите в десятичной системе счисления.
'''

n = 28
b = bin(n)[2:]
b += '11' if b.count('1') % 2 != 0 else '00'
r = int(b, 2)
print(r)
