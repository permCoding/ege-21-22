""" 
сгенерировать все подмножества исходного множества 
    {1, 3, 4} 
"""

lst = [1, 3, 4]

n = len(lst)
subsets = []
for i in range(2 ** n):
    subset = []
    bin_num = bin(i)[2:].rjust(3, '0')
    # print(bin_num)
    for j in range(n):
        if bin_num[j] == '1':
            subset += [lst[j]]
    subsets.append(subset)

print(*subsets)
