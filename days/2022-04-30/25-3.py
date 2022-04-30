for a in range(10):
    for b in range(11):
        e = '' if b==0 else b-1
        n = int(f'12345{a}7{e}8')
        if n%23==0:
            print(n, n//23)
