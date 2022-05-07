# ¬(𝑥 → 𝑤)∨(𝑦 ≡ 𝑧)∨𝑦

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = not(x<=w) or (y==z) or y
                if f == 0:
                    print(y,x,w,z)