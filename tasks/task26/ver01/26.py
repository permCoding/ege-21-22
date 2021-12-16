'''
https://inf-ege.sdamgia.ru/problem?id=39255
1. Нужно купить как можно больше изделий, независимо от их типа и модификации.
2. Если можно разными способами купить максимальное количество изделий, 
    нужно выбрать тот способ, при котором будет куплено как можно больше изделий B.
3. Если можно разными способами купить максимальное количество изделий с одинаковым количеством изделий B, 
    нужно выбрать тот способ, при котором вся покупка будет дешевле.
Определите, сколько всего будет куплено изделий B и какая сумма останется неиспользованной.
'''
lines = open('26.txt').readlines()

n, mx = map(int, lines[0].split())
print(n, mx)
lst = map(lambda line: [int(line.split()[0]), line.split()[1]], lines[1:n+1])

lst = sorted(lst, key=lambda x: x[0])

from functools import reduce
def get(w):
    return reduce(lambda a,b: a+b[0], w, 0)

res = []
for item in lst:
    res += [item]
    if get(res) > mx:
        res.pop()
        break
print(len(res))

for item in res:
    print(item)
