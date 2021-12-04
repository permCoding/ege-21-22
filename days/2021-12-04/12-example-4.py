def repl(s, a, b):
    pos = s.find(a)
    return s[0:pos] + b + s[pos+len(a):]


s = '8' * 70
while s.find('2222') >= 0 or s.find('8888') >= 0:
    if s.find('2222') >= 0:
        s = repl(s, '2222', '88')
    else:
        s = repl(s, '8888', '22')
print(s)

'''
ПОКА нашлось (2222) ИЛИ нашлось (8888)
    ЕСЛИ нашлось (2222)
        ТО заменить (2222, 88)
    ИНАЧЕ заменить (8888, 22)
'''