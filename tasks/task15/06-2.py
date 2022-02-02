''' https://inf-ege.sdamgia.ru/problem?id=37150
Для какого наибольшего целого неотрицательного числа A выражение
    (2x + y ≠ 70) ∨ (x < y) ∨ (A < x)
тождественно истинно, т.е. принимает значение 1 при любых целых неотрицательных x и y?
Источник: ЕГЭ по информатике 24.06.2021. Основная волна (вариант Евгения Джобса)'''

def f(x, y, a):
    return (2*x+y!=70) or (x<y) or (a<x)


for a in range(200, 0, -1):
    for x in range(1, 200):
        for y in range(1, 200):
            if f(x, y, a) == False:
                break
        else:
            continue
        break
    else:
        print(a)
        break
