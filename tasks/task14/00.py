'''
Значение выражения 
...
записали в СС с основанием 16
Сколько значащих нулей содержится в этой записи?
'''
f = 3*4**38 + 2*4**23 + 4**20 + 3*4**5 + 2*4**4 + 1

print(hex(f)[2:].count('0'))
