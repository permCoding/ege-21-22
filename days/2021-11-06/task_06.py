from os import system


def ver_01():
    # x + 12 = 30
    # x = int(input())
    for x in range(1, 1000):
        result = x + 12
        if result == 30:
            print(f"x = {x}")
            break


def ver_4101():
    s = int(input())
    n = 740
    while s + n < 1200:
        s = s + 6
        n = n - 4
    print(n)  # 68


def ver_4101_2():
    for s0 in range(500, 0, -1):
        # s = int(input())
        s = s0
        n = 740
        while s + n < 1200:
            s = s + 6
            n = n - 4
        if n == 68:
            print(s0)


if __name__ == '__main__':
    system("cls")
    # ver_01()
    ver_4101_2()
