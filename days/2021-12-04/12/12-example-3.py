s = '2288282828828'

a, b = '88', '-'

pos = s.find(a)
print(s[0:pos] + b + s[pos+len(a):])
