""" 
сгенерировать все подмножества исходного множества 
    {1, 3, 4} 
"""

lst = [1, 3, 4]

subsets = []
lst = [1, 3, 4]
n = len(lst)
count = 2**n
for i in range(count):
    subset = []
    for j in range(n):
        mask = 1<<j
        if mask & i > 0:
            subset += [lst[j]]
    subsets.append(subset)

print(*subsets)
