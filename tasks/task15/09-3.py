''' https://inf-ege.sdamgia.ru/problem?id=34541
На числовой прямой даны два отрезка: 
    Р = [3, 38] и Q = [21, 57]. 
Какова наибольшая возможная длина интервала A, что логическое выражение
    ((х ∈ Q) → (х ∈ Р)) → ¬(х ∈ A)
тождественно истинно, те принимает значение 1 при любом значении переменной х.'''

def f(x,a,b):
    return ((21<=x<=57)<=(3<=x<=38)) <= (not(a<=x<=b))


L, R = 2, 58
m, step = 0, 2

for a in range(L*10,R*10,step):
    for b in range(a+step,R*10,step):
        lst = [f(x/10,a/10,b/10) for x in range(L*10,R*10,step)]
        if all(lst):
            m = max(m, b-a)

print(m/10)
