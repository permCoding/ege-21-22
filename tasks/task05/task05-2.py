'''
На вход алгоритма подаётся натуральное число N. 
Алгоритм строит по нему новое число R следующим образом.

1. Строится двоичная запись числа N.
2. К этой записи дописываются справа ещё два разряда по следующему
правилу:
    а) складываются все цифры двоичной записи числа N, 
    и остаток от деления суммы на 2 дописывается в конец числа (справа).
        Например, запись 11100 преобразуется в запись 111001;
    б) над этой записью производятся те же действия – 
    справа дописывается остаток от деления суммы её цифр на 2.

Полученная таким образом запись 
    (в ней на два разряда больше, чем в записи исходного числа N) 
является двоичной записью результирующего числа R.

Укажите такое наименьшее число N, для которого результат работы
данного алгоритма больше числа 77. 
В ответе это число запишите в десятичной системе счисления.
'''
def get(n):
    n = bin(n)
    n += str(n.count('1') % 2)
    n += str(n.count('1') % 2)
    return int(n, 2)


for n in range(1, 100):
    res = get(n)
    if res > 77:
        print(n, res)
        break
