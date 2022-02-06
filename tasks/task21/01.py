# https://inf-ege.sdamgia.ru/problem?id=27750

from functools import lru_cache
@lru_cache(None)

def f(x, y):
    if x+y >= 82:
        return 0
    moves = [f(x+1,y),f(x,y+1),f(x*4,y),f(x,y*4)]
    lose = list(filter(lambda x: x<=0, moves))
    # lose = [move for move in moves if move <= 0]
    return (-max(lose)+1) if lose else -max(moves)

for s in range(1, 83):
    print(s, f(4,s))
