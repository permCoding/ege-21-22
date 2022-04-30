for a in range(10):
    for b in range(10):
        n = int(f'12345{a}6{b}8')
        if n%17==0:
            print(n, n//17)
