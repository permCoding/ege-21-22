f = open("t27-B.txt")
n = int(f.readline())
a = [int(e) for e in f]

mn_i, mn_p = 0, 0  # вычислить для 0-ой точки
for j in range(n):  # поз контейнера
    mn_p += min(j, n-j) * a[j]
# print(mn_i+1, mn_p)

# перебрать стоимость для всех остальных
tm_p = mn_p
_i = n//2
p_pred = sum(a[_i:])  # a[_i]*1 + a[_i+1]*1
p_next = sum(a[1:_i])  # a[1]*1 + a[2]*1

for i in range(1, n):
    p_pred += -a[_i] + a[i-1]  # тут была ошибка p_pred = ...
    p_next += +a[_i] - a[i]  # тут была ошибка p_next = ...
    tm_p += p_pred - p_next - a[i]
    _i += 1
    if _i == n: _i = 0
    if tm_p < mn_p:
        mn_p = tm_p
        mn_i = i

print(mn_i+1, mn_p)
