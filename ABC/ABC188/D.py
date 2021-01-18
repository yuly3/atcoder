import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, C = map(int, rl().split())
    abc = [list(map(int, rl().split())) for _ in range(N)]
    for i in range(N):
        abc[i][0] -= 1
    
    ab = set()
    for a, b, _ in abc:
        ab.add(a)
        ab.add(b)
    idx_to_day = list(sorted(ab))
    day_to_idx = {v: i for i, v in enumerate(idx_to_day)}
    M = len(day_to_idx)
    
    imos = [0] * (M + 1)
    for a, b, c in abc:
        imos[day_to_idx[a]] += c
        imos[day_to_idx[b]] -= c
    imos = list(accumulate(imos))
    
    ans = 0
    for i in range(M - 1):
        ans += (idx_to_day[i + 1] - idx_to_day[i]) * min(C, imos[i])
    print(ans)


if __name__ == '__main__':
    solve()
