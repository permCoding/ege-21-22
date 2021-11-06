k=[]
for s0 in range (100, 800):
    s=s0
    n=10
    while s-n<1000:
        s=s+n
        n=n+5
    if n==80:
        k+=[s0]

print('k =', k)
print(len(k))
print(max(k))
print(min(k))
print(sum(k))
