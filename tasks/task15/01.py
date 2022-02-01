def check(g1, g2, elm):
    return g1 <= elm <= g2


d = []
g1 = 16
while g1 <= 81:
    g1 += .1
    g2 = g1 + .1
    while g2 <= 81:
        g2 += .1
        b = True
        x = 16
        while x <= 81:
            x += .1
        
            f1 = check(17, 58, x)
            f2 = not(check(29, 80, x))
            f3 = not(check(g1, g2, x))
            f4 = not(check(17, 58, x))
            p = (f2 and f3) <= f4
            r = f1 <= p
            if r == False:
                b = False
                break
        if b:
            # print(g1, g2)
            d += [g2 - g1]

print(round(min(d), 1))
