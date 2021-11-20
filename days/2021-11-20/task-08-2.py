dct = {
    'Е': '0',
    'Л': '1',
    'М': '2',
    'Р': '3',
    'У': '4'
}


def to_dec(s, base=2):
    result = 0
    st = len(s) - 1
    for i in range(len(s)):
        result += int(s[i]) * base ** st
        st -= 1
    return result


def to_dig(s):
    result = ''
    for smb in s:
        result += dct[smb]
    return result


line = 'ЛЕЕЕУРМРМРМУУЕЕЕЕ'
new_line = to_dig(line)
print(to_dec(new_line, 5))
