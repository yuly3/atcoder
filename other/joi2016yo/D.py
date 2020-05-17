import sys
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    INF = 5 * 10 ** 18
    N, T, Q = map(int, rl().split())
    AD = [(-INF, 1)]
    for _ in range(N):
        A, D = map(int, rl().split())
        AD.append((A, D))
    AD.append((INF, 2))
    X = [int(rl()) for _ in range(Q)]
    
    t = []
    for i in range(N + 1):
        if AD[i][1] == 1 and AD[i + 1][1] == 2:
            t.append((AD[i][0] + AD[i + 1][0]) // 2)
    
    ans = []
    for xi in X:
        A, D = AD[xi]
        idx = bisect_left(t, A)
        if D == 1:
            ans.append(min(A + T, t[idx]))
        else:
            ans.append(max(A - T, t[idx - 1]))
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
