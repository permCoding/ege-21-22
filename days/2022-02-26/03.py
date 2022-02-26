def get(n, b):
    # if n == z:
    #     return 0
    if n > b:
        return 0
    if n == b:
        return 1
    if n < b:
        return get(n+1, b) + get(n*2, b)


p1 = get(1, 10)
p2 = get(10, 20)
print(p1 * p2)
