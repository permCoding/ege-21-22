lst = list(map(int, open("17-1.txt").readlines()))

# минимальный элемент в последовательности, кратный 23

# mn = max(lst)
# for elm in lst:
#     if elm%23==0:
#         mn = min(mn, elm)
# print(mn)

# mn = min(filter(lambda elm: elm%23==0, lst))
# print(mn)

mn = min([elm for elm in lst if elm%23==0])
# print(mn)

cnt, sm = 0, 0
for i in range(len(lst)-1):
    if lst[i]%mn==0 or lst[i+1]%mn==0: 
        cnt += 1
        sm = max(sm, lst[i]+lst[i+1])
print(cnt, sm)
