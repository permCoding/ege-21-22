# https://inf-ege.sdamgia.ru/problem?id=36879
"""В строках, содержащих менее 25 букв G, найти макс
расст между одинаковыми буквами в одной строке. """

m = 0
with open("./inf_26_04_21_24.txt") as f:
    for s in f:
        if s.count("G") < 25:
            r = 0
            for i in range(len(s)):
                last = s.rfind(s[i])
                r = max(r, last-i)        
            m = max(m, r)
print(m)
