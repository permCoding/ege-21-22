''' https://inf-ege.sdamgia.ru/problem?id=7663
Автомат получает на вход трёхзначное число. 
По этому числу строится новое число по следующим правилам.
  1. Складываются первая и вторая, а также вторая и третья цифры исходного числа.
  2. Полученные два числа записываются друг за другом в порядке убывания (без разделителей).
Укажите наименьшее число, в результате обработки которого автомат выдаст число 1412.
'''
for n in range(100, 1000):
    s = str(n)
    a = int(s[0]) + int(s[1]) 
    b = int(s[1]) + int(s[2]) 
    if max(a, b) == 14 and min(a, b) == 12:
        print(n)
        break
