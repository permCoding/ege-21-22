''' https://inf-ege.sdamgia.ru/problem?id=36028
На числовой прямой даны два отрезка:
    P = [17, 54] и Q = [37, 83].
Какова наименьшая возможная длина интервала A, что формула
    (x ∈ P) → (((x ∈ Q) ∧ ¬(x ∈ A)) → ¬(x ∈ P))
тождественно истинна, те принимает значение 1 при любом значении переменной х.
'''
def f(x,a,b):
    return (17<=x<=54) <= (((37<=x<=83)and(not(a<=x<=b))) <= (not(17<=x<=54)))


mn = 999999
for left in range(16*10, 84*10, 2):
    for right in range(left+2, 84*10, 2):
        lst = [f(x/10,left/10,right/10) for x in range(16*10, 84*10, 2)]
        if all(lst):
            mn = min(mn, right-left)
print(mn/10)
