import sys
from itertools import combinations

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    ABCD= list(map(int, rl().split()))
    
    sm = sum(ABCD)
    for i in range(1, 4):
        for ids in combinations(range(4), i):
            n = 0
            for id in ids:
                n += ABCD[id]
            if n == sm - n:
                print('Yes')
                return
    print('No')


if __name__ == '__main__':
    solve()
