s = '8' * 70
while '2222' in s or '8888' in s:
    s = s.replace('2222', '88') if '2222' in s else s.replace('8888', '22')
print(s)

'''
ПОКА нашлось (2222) ИЛИ нашлось (8888)
    ЕСЛИ нашлось (2222)
        ТО заменить (2222, 88)
    ИНАЧЕ заменить (8888, 22)
'''