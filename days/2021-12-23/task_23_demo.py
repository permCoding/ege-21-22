# из 1 => в 20 через 10
# 1) n + 1
# 2) n * 2
def F(n, k):
    if n > k:
        return 0
    if n == k:
        return 1
    return F(n+1, k) + F(n*2, k)


print(F(1, 10) * F(10, 20))