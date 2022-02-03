''' https://inf-ege.sdamgia.ru/problem?id=34548
На числовой прямой даны два отрезка:
P = [17, 54] и Q = [37, 83].
Какова наименьшая возможная длина интервала A, что формула
    (x ∈ P) → (((x ∈ Q) ∧ ¬(x ∈ A)) → ¬(x ∈ P))
тождественно истинна, те принимает значение 1 при любом значении переменной х.
'''
def f(x,a,b):
    return (17<=x<=54) <= (((37<=x<=83)and(not(a<=x<=b))) <= (not(17<=x<=54)))

m = 83-17
for a in range(17, 84):
    for b in range(17,84):
        bx = True
        for x in range(17,84):
            if f(x,a,b) == False:
                bx = False
                break
        if bx:
            m = min(m,b-a)
print(m)        
