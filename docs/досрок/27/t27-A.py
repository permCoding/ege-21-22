f = open("./27-A.txt")
n = int(f.readline())
a = [int(x) for x in f]

mn_p, mn_i = 10**10, 0
for i in range(n):
    pr_i = 0
    for j in range(n):
        dist = abs(i-j)
        pr_i += a[j]*min(dist, n-dist)
    if pr_i < mn_p:
        mn_p = pr_i
        mn_i = i

print(mn_i+1)  # нумеруются от 1 до N
