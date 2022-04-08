# массив массивов в плоский массив рекурсивно

def flat(lst):
    res = []
    for item in lst:
        if type(item) != list:
            res.append(item)
        else:
            tmp = flat(item)
            for elm in tmp:
                res.append(elm)
    return res


arr = [
    12,
    [1,2,3],
    [[90],[80],70],
    [[[55]]]
]
print(sorted(flat(arr)))
