''' https://inf-ege.sdamgia.ru/problem?id=15097
Логическая функция F задаётся выражением 
(x ≡ z ) ∨ (x → (y ∧ z))
На рисунке приведён частично заполненный фрагмент таблицы истинности функции F, 
содержащий неповторяющиеся строки. 

П1	П2	П3	Функция
0	0	_	0
1   _	_	0

Определите, какому столбцу таблицы истинности функции F 
соответствует каждая из переменных x, y, z, w.
В ответе напишите буквы xyzw в том порядке, в котором идут соответствующие им столбцы.
'''
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f1 = x == z
            f2 = y and z
            f3 = x <= f2

            res = f1 or f3

            if res == False:
                print(y, z, x)
