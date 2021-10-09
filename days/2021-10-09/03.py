def bin_to_dec(x):
    k = len(x)
    y = 0
    for i in range(k):
        y += int(x[i]) * 2**(k-1-i)
    return y


x = input('Введите двоичное число - ')
print(bin_to_dec(x))


