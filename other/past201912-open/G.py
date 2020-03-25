import sys
from itertools import combinations

rl = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

ans = -(10 ** 12)


def solve():
    N = int(rl())
    a = [[0] * N for _ in range(N - 1)]
    for i in range(N - 1):
        ai = list(map(int, rl().split()))
        cnt = 0
        for j in range(i + 1, N):
            a[i][j] = ai[cnt]
            cnt += 1
    
    def calc(m, _g1, _g2, _g3):
        g1, g2, g3 = _g1, _g2, _g3
        
        if m != N:
            calc(m + 1, g1 + [m], g2, g3)
            calc(m + 1, g1, g2 + [m], g3)
            calc(m + 1, g1, g2, g3 + [m])
        else:
            happiness = 0
            if 1 < len(g1):
                for x, y in combinations(g1, 2):
                    happiness += a[x][y]
            if 1 < len(g2):
                for x, y in combinations(g2, 2):
                    happiness += a[x][y]
            if 1 < len(g3):
                for x, y in combinations(g3, 2):
                    happiness += a[x][y]
            global ans
            ans = max(ans, happiness)
    
    calc(0, [], [], [])
    global ans
    print(ans)


if __name__ == '__main__':
    solve()
