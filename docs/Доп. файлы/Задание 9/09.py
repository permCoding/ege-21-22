def check(line):
    a, b, c = map(int, line.split(';'))
    return (a<b+c) * (b<a+c) * (c<a+b)


print(sum([check(line) for line in open("9.csv").readlines()]))
