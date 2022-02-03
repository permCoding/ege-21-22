''' https://inf-ege.sdamgia.ru/problem?id=34541
На числовой прямой даны два отрезка: 
    Р = [3, 38] и Q = [21, 57]. 
Какова наибольшая возможная длина интервала A, что логическое выражение
    ((х ∈ Q) → (х ∈ Р)) → ¬(х ∈ A)
тождественно истинно, те принимает значение 1 при любом значении переменной х.'''

def f(x,a,b):
    return ((21<=x<=57)<=(3<=x<=38)) <= (not(a<=x<=b))


m = 0
L, R = 2.0, 58.0
a = L
while a <= R:
    a += .2

    b = a + .2
    while b <= R:
        b += .2

        bx = True
        x = L
        while x <= R:
            x += .1
            if not(f(x,a,b)):
                bx = False
                break
        if bx:
            m = max(m, b-a)

print(round(m, 2))
