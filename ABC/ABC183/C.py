import sys
from itertools import permutations

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, K = map(int, rl().split())
    T = [list(map(int, rl().split())) for _ in range(N)]
    
    ans = 0
    for directions in permutations(range(1, N), N - 1):
        cur = 0
        cost = 0
        for nex in directions:
            cost += T[cur][nex]
            cur = nex
        cost += T[cur][0]
        ans += cost == K
    print(ans)


if __name__ == '__main__':
    solve()
