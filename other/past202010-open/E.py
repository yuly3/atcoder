import sys
from itertools import permutations

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    S = rl().rstrip()
    
    for t in permutations(S, N):
        T = ''.join(t)
        if T != S and T[::-1] != S:
            print(T)
            return
    print('None')


if __name__ == '__main__':
    solve()
