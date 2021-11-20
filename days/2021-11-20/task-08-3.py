def to_dec(s, base=2):
    dec, st = 0, 0
    for smb in s[::-1]:
        dec += int(smb) * 2**st
        st += 1
    return dec


line = '1110'
print(to_dec(line, 2))
