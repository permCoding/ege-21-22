def f(a,b):
    if a==b: return 1
    if a>=b: return 0
    return f(a+2,b) + f(a*2,b)

print(f(1,20)*f(20,52))