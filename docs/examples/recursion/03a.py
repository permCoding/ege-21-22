def fib(n):
    if n <= 2:
        return 1
    else:
        if cash[n-1] == 0:
            cash[n-1] = fib(n-1)
        return cash[n-2]+cash[n-1]


n = 138
cash = [1,1] + [0] * (n-1)
for i in range(1, n+1):
    print(i, fib(i))
