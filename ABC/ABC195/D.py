import sys
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M, Q = map(int, rl().split())
    WV = [list(map(int, rl().split())) for _ in range(N)]
    X = list(map(int, rl().split()))
    LR = [list(map(int, rl().split())) for _ in range(Q)]
    
    WV.sort(key=lambda it: (-it[1], it[0]))
    ans = []
    for left, right in LR:
        su = 0
        box = X[:left - 1] + X[right:]
        box.sort()
        for i, (wi, vi) in enumerate(WV):
            idx = bisect_left(box, wi)
            if idx != len(box):
                su += vi
                del box[idx]
        ans.append(su)
    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    solve()
