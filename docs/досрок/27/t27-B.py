f = open("./27-B.txt")
n = int(f.readline())
a = [int(x) for x in f]

mn_p, mn_i = 0, 0
for i in range(n):
    mn_p += a[i]*min(i, n-i)
# print(mn_p)

pr = [0] * n
pr[0] = mn_p
_i = n//2  # index напротив i
sm_pred, sm_next = sum(a[_i:]), sum(a[1:_i])
for i in range(1, n):
    sm_pred += a[i-1] - a[_i]
    sm_next += a[_i]
    pr[i] = pr[i-1] + sm_pred - sm_next
    sm_next -= a[i]
    _i = (_i+1)%n
    if pr[i] < mn_p:
        mn_p = pr[i]
        mn_i = i
print(mn_i+1)  # нумеруются от 1 до N
print(pr[:10])
