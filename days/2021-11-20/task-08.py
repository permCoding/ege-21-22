def to_dec(s, base=2):
    result = 0
    st = len(s) - 1
    for i in range(len(s)):
        result += int(s[i]) * base ** st
        st -= 1
    return result


line = '1234'
print(to_dec(line, 5))
