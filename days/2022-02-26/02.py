def get(n):
    if n > b:
        return 0
    if n == b:
        return 1
    if n < b:
        way1 = get(n+1)
        way2 = get(n*2)
        return way1 + way2


a, b = 1, 10
print(get(a))
