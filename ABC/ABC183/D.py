import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, W = map(int, rl().split())
    STP = [list(map(int, rl().split())) for _ in range(N)]
    
    imos = [0] * 200010
    for s, t, p in STP:
        imos[s] += p
        imos[t] -= p
    
    imos = list(accumulate(imos))
    print('Yes' if max(imos) <= W else 'No')


if __name__ == '__main__':
    solve()
