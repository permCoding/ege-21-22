def bin_to_dec(s):
    st, res = 0, 0  # множественное присваивание
    for smb in s[::-1]:  # цикл по коллекции
        res += int(smb)*2**st
        st += 1
    return res


# 11001
x = input('Введите двоичное число - ')
print(bin_to_dec(x))


