import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    at = [list(map(int, rl().split())) for _ in range(N)]
    
    INF = 10 ** 18
    ma = INF
    mi = -INF
    acc = 0
    for ai, ti in at:
        if ti == 1:
            mi += ai
            ma += ai
            acc += ai
        elif ti == 2:
            if mi < ai:
                mi = ai
            if ma < ai:
                ma = ai
        else:
            if ai < mi:
                mi = ai
            if ai < ma:
                ma = ai
    
    Q = int(rl())
    x = list(map(int, rl().split()))
    ans = [0] * Q
    for i, xi in enumerate(x):
        ans[i] = min(ma, max(mi, xi + acc))
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
