''' https://inf-ege.sdamgia.ru/problem?id=39231
Логическая функция F задаётся выражением 
(¬z ≡ y) → ((w ∧ ¬x) ≡ (y ∧ x))
На рисунке приведён частично заполненный фрагмент таблицы истинности функции F, 
содержащий неповторяющиеся строки. 

_   -x   _   _

П1	П2	П3	П4	Функция
_	1	1	1	0
1	1	_	_	0
_   _   0	_	0

Определите, какому столбцу таблицы истинности функции F 
соответствует каждая из переменных x, y, z, w.
В ответе напишите буквы xyzw в том порядке, в котором идут соответствующие им столбцы.
'''
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f1 = not z == y
                f2 = w and not x
                f3 = y and x

                p1 = f2 == f3

                res = f1 <= p1

                if res == False:
                    print(z, w, x, y)
