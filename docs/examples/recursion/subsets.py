# рекурсивный перебор всех комбинаций

def get_subsets(count):
    if count == 0:
        subsets.append(subset[:])
    else:
        subset.append(lst[count-1])
        get_subsets(count-1)
        subset.pop()
        get_subsets(count-1)


lst = [1, 4, 7]

subsets, subset = [], []
get_subsets(len(lst))
for item in sorted(subsets, key=len):
    print(item)

# стек функций ограничен 2000 - можно увеличить
# import sys
# sys.setrecursionlimit(10000)
