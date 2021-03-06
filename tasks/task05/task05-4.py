'''
https://inf-ege.sdamgia.ru/problem?id=27005
На вход алгоритма подаётся натуральное число N. 
Алгоритм строит по нему новое число следующим образом.

1. Из цифр, образующих десятичную запись N, 
   строятся наибольшее и наименьшее возможные двузначные числа 
   (числа не могут начинаться с нуля).

2. На экран выводится разность полученных двузначных чисел.

Чему равно наименьшее возможное трёхзначное число N, 
в результате обработки которого на экране автомата появится число 70?
'''

for n in range(100, 1000):
    mn = int(''.join(sorted(list(str(n)))[:2]))
    mx = int(''.join(sorted(list(str(n)))[-2:][::-1]))
    if mn < 10 or mx < 10:
        continue
    if mx-mn == 70:
        print(n)
        break
