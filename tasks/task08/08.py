d = {
    'E': '0',
    'T': '1'
}

line = 'TTET'
new_line = ''
for smb in line:
    new_line += d[smb]
print(new_line)
