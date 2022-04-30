def f(n,k):
    if n==k: return 1
    if n>k: return 0
    return f(n+2,k) + f(n*2,k)

print(f(1,20) * f(20,52))