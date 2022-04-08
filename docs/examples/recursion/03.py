def fib(n):
    if n <= 2:
        return 1
    else:
        if cash[n-2] == 0:
            cash[n-2] = fib(n-2)
        if cash[n-1] == 0:
            cash[n-1] = fib(n-1)
        return cash[n-2]+cash[n-1]


n = 138
cash = [0] * (n+1)
for i in range(1, n+1):
    print(i, fib(i))
