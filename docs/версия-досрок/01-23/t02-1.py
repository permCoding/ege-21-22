
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = not(x<=w) or (y==z) or y
                if f == False:
                    print(y,x,w,z)
