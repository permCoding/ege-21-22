x = input('Введите двоичное число - ')
k = len(x)
y = 0
for i in range(k):
    y += int(x[i]) * 2**(k-1-i)
print(y)


# 110(2) = 1*2**2 + 1*2**1 + 0*2**0 = 6(10)

# for - по индексам
# for - по элементам коллекции
