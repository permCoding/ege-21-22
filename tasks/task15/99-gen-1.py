""" 
сгенерировать все подмножества исходного множества 
    {1, 3, 4} 
"""

def get_subsets(pos):
    if pos == 0:
        subsets.append(subset[:])
    else:
        subset.append(lst[pos-1])
        get_subsets(pos-1)
        subset.pop()
        get_subsets(pos-1)


subsets = []
subset = []

lst = [1, 3, 4]
get_subsets(len(lst))
for lst in sorted(subsets, key=lambda item: len(item)):
    print(sorted(lst))
