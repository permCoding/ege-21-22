def fib(n):
    if n <= 2:
        return 1
    else:
        if cash.get(n-2) == None:
            cash[n-2] = fib(n-2)
        if cash.get(n-1) == None:
            cash[n-1] = fib(n-1)
        return cash.get(n-2)+cash.get(n-1)


n = 138
cash = {}
for i in range(1, n+1):
    print(i, fib(i))
