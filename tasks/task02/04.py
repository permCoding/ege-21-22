''' https://inf-ege.sdamgia.ru/problem?id=38936
Логическая функция F задаётся выражением 
(x ≡ ¬y) → ((x ∧ w) ≡ (z ∧ ¬w))
На рисунке приведён частично заполненный фрагмент таблицы истинности функции F, 
содержащий неповторяющиеся строки. 

П1	П2	П3	П4	Функция
1	1	_	1	0
_   1	1	_	0
0	_	_	_	0

Определите, какому столбцу таблицы истинности функции F 
соответствует каждая из переменных x, y, z, w.
В ответе напишите буквы xyzw в том порядке, в котором идут соответствующие им столбцы.
'''
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f1 = x == (not y)
                f2 = w and x
                f3 = z and not w

                p1 = f2 == f3

                res = f1 <= p1

                if res == False:
                    print(w, z, y, x)
