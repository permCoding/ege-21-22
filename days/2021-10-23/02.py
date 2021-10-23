inp = 2000
while inp > 0:
    s = inp
    s = s // 10
    n = 1
    while s < 51:
        s = s + 5
        n = n * 2
    if n == 64:
        print(inp, n)
        # break
    inp -= 1
