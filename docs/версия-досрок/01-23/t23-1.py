def F(n, k):
    if n > k: return 0
    if n == k: return 1
    return F(n+2, k) + F(n*2, k)

print(F(1, 20) * F(20, 52))