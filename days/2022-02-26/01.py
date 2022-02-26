def get(n):
    if n < 1:
        return 0
    else:
        print(n)
        return get(n-1)


x = 10
print(get(x))
