''' https://inf-ege.sdamgia.ru/problem?id=34548
На числовой прямой даны два отрезка: 
    P = [2, 10] и Q = [6, 14].
Какова наибольшая возможная длина интервала A, что формула
    ((x ∈ А) → (x ∈ P)) ∨ (x ∈ Q)
тождественно истинна, те принимает значение 1 при любом значении переменной х.'''

def f(x, a, b):
    return ((a<=x<=b)<=(2<=x<=10)) or (6<=x<=14)


L, R, s, m = 1.0, 15.0, .1, 0

a = L
while a <= R:
    a += s

    b = a + s
    while b <= R:
        b += s

        x = L
        while x <= R:
            x += s
            if not(f(x,a,b)):
                break
        else:
            m = max(m, b-a)

print(round(m, 2))
