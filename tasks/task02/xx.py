for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            f = z <= int(not x or y)
            print(x,y,z,f)
