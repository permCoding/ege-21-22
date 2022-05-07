"""Для какого наименьшего натурального числа А формула
    (ДЕЛ(𝑥, 3) → ¬ДЕЛ(𝑥, 5)) ∨ (𝑥 + 𝐴 ≥ 70)
истинна при любом целом натуральном значении переменной х"""

def d(x, a):
    return x%a==0

def f(x, a):
    return (int(d(x,3)) <= int(not(d(x,5)))) or (x+a>=70)

for a in range(1, 100):
    b = True
    for x in range(1, 100):
        if f(x, a)==False:
            b = False
            break
    if b:
        print(a)
        break
