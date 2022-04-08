



def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-2)+fib(n-1)


for i in range(30, 38):
    print(i, fib(i))
