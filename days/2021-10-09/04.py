def bin_to_dec(s):
    st = len(s) - 1
    res = 0
    for smb in s:  # цикл по коллекции
        res += int(smb)*2**st
        st -= 1
    return res


x = input('Введите двоичное число - ')
print(bin_to_dec(x))


