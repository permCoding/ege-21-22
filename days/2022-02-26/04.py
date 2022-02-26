def get(a, b):
    count = 0
    lst = [a]
    while len(lst) > 0:
        last = lst.pop()
        if last == b:
            count += 1
        if last < b:
            lst = [last + 1, last * 2] + lst
    return count


p1 = get(1, 10)
p2 = get(10, 20)
print(p1 * p2)
