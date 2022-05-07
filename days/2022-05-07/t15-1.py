# (Дел(х,3) → ¬ Дел(х,5)) ∨ (х+А⩾ 90)

def f(x, a):
    return ((x%3==0)<=(not(x%5==0))) or (x+a>=90)


for a in range(1, 200):
    b = True
    for x in range(1, 200):
        if f(x, a)==False:
            b = False
            break
    if b:
        print(a)
        break