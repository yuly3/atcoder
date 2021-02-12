import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, K = map(int, rl().split())
    A = list(map(int, rl().split()))
    B = list(map(int, rl().split()))
    
    def check(t):
        d = 0
        x = 0
        C = B[:]
        for i in range(N - 1, -1, -1):
            C[i], d = max(0, C[i] - d), max(0, d - C[i])
            if C[i] == 0:
                continue
            y = -(-C[i] // (t - A[i]))
            d += y * (t - A[i]) - C[i]
            x += y
        return x <= K
    
    ok, ng = A[-1] + sum(B), A[-1]
    while ok - ng != 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)


if __name__ == '__main__':
    solve()
