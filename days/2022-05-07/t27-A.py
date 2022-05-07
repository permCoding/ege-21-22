f = open("t27-A.txt")
n = int(f.readline())
a = [int(e) for e in f]

mn_i, mn_p = 0, 10**10
for i in range(n):  # позиция завода
    tm_p = 0
    for j in range(n):  # поз контейнера
        d = abs(i-j)
        tm_p += min(d, n-d) *a[j]
    if tm_p < mn_p:
        mn_p = tm_p
        mn_i = i

print(mn_i+1, mn_p)

'''расстояние от контейнера 
до перерабатывающего завода, 
умноженное на количество мусора 
в этом контейнере
Контейнеры от 1 до N.'''