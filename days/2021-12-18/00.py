'''
https://replit.com/@pCoding/parser-txt#main.py
если работаете локально у себя на компе, то
сначала нужно установить библиотеку requests
для этого в консоли наберите и запустите:
pip install requests
'''
import requests  

link = 'https://pcoding.ru/csv/18.txt'
'''
вывести направления обучения в порядке убывания 
минимального балла ЕГЭ для поступления
'''
s = requests.get(link).content.decode('utf-8')
# print(s)
with open('data.txt', 'w') as f:
    f.write(s)

lines = s.split('\n')[1:]
# print(lines)

lst = [line.split(';') for line in lines]

lst.sort(key=lambda x: int(x[2]), reverse=True)

for item in lst:
    print(' - '.join(reversed(item[1:3])))
