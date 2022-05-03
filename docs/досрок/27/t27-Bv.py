f = open("./27-B.txt")
n = int(f.readline())
a = [int(x) for x in f]

mn_p, mn_i = 0, 0  # min стоимость и индекс
for i in range(n):  # sm для i==0
    mn_p += a[i] * min(i, n-i)

_i = n//2  # index напротив i, пока i==0
sm_next = sum(a[1:_i])  # sum цепочки после i
sm_pred = sum(a[_i:])  # sum цепочки до i
tmp = mn_p  # текущая суммарная стоимость
for i in range(1, n):
    sm_next += +a[_i] - a[i]
    sm_pred += -a[_i] + a[i-1]
    tmp += sm_pred - sm_next - a[i]
    _i += 1  # меняем index напротив i
    if _i==n: _i = 0  # при переходе через n
    if tmp < mn_p:
        mn_p = tmp
        mn_i = i

print(mn_i+1, mn_p)  # нумерация от 1 до N
