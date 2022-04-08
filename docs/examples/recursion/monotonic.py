import time


def fib(n):
    return 1 if n <= 2 else fib(n-2)+fib(n-1)


start = time.monotonic()

for i in range(30, 40):
    print(i, fib(i))

stop = time.monotonic()

print(round(stop-start, 3))
