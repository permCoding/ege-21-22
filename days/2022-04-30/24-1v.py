# AAACABBBABAAAAAABABACCCC
# __ACAB__AB_____ABABAC___
# __XX__X_____XXX___
# ['','','XX','','','X']
# max len

lst = open("./24-1.txt") \
    .readline() \
    .replace('AC', 'X') \
    .replace('AB', 'X') \
    .replace('A', ' ') \
    .replace('B', ' ') \
    .replace('C', ' ') \
    .split()

print(max(map(len, lst)))