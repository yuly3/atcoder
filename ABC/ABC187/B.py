import sys
from itertools import combinations

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    xy = [list(map(int, rl().split())) for _ in range(N)]
    
    ans = 0
    for i, j in combinations(range(N), 2):
        xi, yi = xy[i]
        xj, yj = xy[j]
        a = (yj - yi) / (xj - xi)
        ans += -1 <= a <= 1
    print(ans)


if __name__ == '__main__':
    solve()
