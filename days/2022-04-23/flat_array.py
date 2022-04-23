def flat(a):
    res = []
    for elm in a:
        if type(elm) != list:
            res.append(elm)
        else:
            res.extend(flat(elm))
    return res


arr = [
    1,
    [2,3,4],
    3.5,
    '333',
    True,
    [[2,3,4],[666,99],[[[0]]]]
]
print(flat(arr))
