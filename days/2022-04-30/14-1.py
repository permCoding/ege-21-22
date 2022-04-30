def fa():
    n = 7 * 512**1912 + \
        6 * 64**1994 - \
        5 * 8**1991 - \
        4 * 8**1960 - 2022
    return oct(n).count('7')

def fb(base=8):
    n = 7 * 512**1912 + \
        6 * 64**1994 - \
        5 * 8**1991 - \
        4 * 8**1960 - 2022
    cnt = 0
    while n > 0:
        if n%base==7: cnt += 1
        n //= base
    return cnt

print(fa())
print(fb())