'''
Значение выражения 
345^5 + 7^3 - 1 - X
записали в СС с основанием 7
в записи оказалось 12 цифр 6
При каком минимальном целом положительном X это возможно?
'''

def to_ss(num, base):
    '''перевод в СС с основанием base <= 9'''
    result = ''
    while num > 0:
        ost = num % base
        num //= base
        result = str(ost) + result
    return result


x = 0
while True:  # цикл с постусловием
    x += 1
    f = 343**5 + 7**3 - 1 - x
    r = to_ss(f, 7)
    if r.count('6') == 12:
        break

print(x)