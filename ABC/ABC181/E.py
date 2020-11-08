import sys
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M = map(int, rl().split())
    H = list(map(int, rl().split()))
    W = list(map(int, rl().split()))
    
    H.sort()
    acc_l, acc_r = [0], [0]
    for i in range(1, N, 2):
        acc_l.append(acc_l[-1] + abs(H[i] - H[i - 1]))
        acc_r.append(acc_r[-1] + abs(H[i] - H[i + 1]))
    
    ans = 10 ** 12
    for wi in W:
        idx = bisect_left(H, wi)
        if idx % 2 == 0:
            ans = min(ans, acc_l[idx // 2] + abs(H[idx] - wi) + acc_r[-1] - acc_r[idx // 2])
        else:
            ans = min(ans, acc_l[idx // 2] + abs(H[idx - 1] - wi) + acc_r[-1] - acc_r[idx // 2])
    print(ans)


if __name__ == '__main__':
    solve()
