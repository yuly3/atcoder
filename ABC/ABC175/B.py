import sys
from itertools import combinations

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    _ = int(rl())
    L = list(map(int, rl().split()))
    L.sort()
    ans = 0
    for li, lj, lk in combinations(L, 3):
        ans += li < lj < lk < li + lj
    print(ans)


if __name__ == '__main__':
    solve()
