'''Ctrl+C - остановать программу принудительно'''

def get_number(a, b):
    '''введите число от a до b'''
    while True:
        num = int(input(f"Введите число от {a} до {b} - "))
        if a <= num <= b:
            break
    return num


x = get_number(50, 75)
y = get_number(0, 10)
print(x, '\n', y)
