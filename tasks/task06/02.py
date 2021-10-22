w = 1000
while True:
    s = w
    s = s // 10
    n = 1
    while s < 51:
        s = s + 5
        n = n * 2
    if n == 64:
        print(w)
        break
    w -= 1