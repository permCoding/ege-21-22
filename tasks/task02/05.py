''' https://inf-ege.sdamgia.ru/problem?id=14688
Логическая функция F задаётся выражением 
(x ∨ y) → (z ≡ x)
На рисунке приведён частично заполненный фрагмент таблицы истинности функции F, 
содержащий неповторяющиеся строки. 

П1	П2	П3	Функция
_	0	0	0
_   0	_	0

Определите, какому столбцу таблицы истинности функции F 
соответствует каждая из переменных x, y, z, w.
В ответе напишите буквы xyzw в том порядке, в котором идут соответствующие им столбцы.
'''
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f1 = x or y
            f2 = z == x

            res = f1 <= f2

            if res == False:
                print(x, z, y)
