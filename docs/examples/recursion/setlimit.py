import sys


def sum(n):
    if n==0:
        return 0
    else:
        return n + sum(n-1)


d = sys.getrecursionlimit()
print(d)  # 1000
sys.setrecursionlimit(2000)

num = 1900
print(sum(num))

