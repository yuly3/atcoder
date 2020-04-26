import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M, V, P = map(int, rl().split())
    A = list(map(int, rl().split()))
    
    A.sort()
    
    def check(t):
        if A[t] + M < A[-P]:
            return False
        at = A[t]
        cnt = (P - 1) * M
        for idx in range(N - P + 1):
            cnt += min(M, M - A[idx] + at)
        return M * V <= cnt
    
    ok, ng = N - 1, -1
    while 1 < ok - ng:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(N - ok)


if __name__ == '__main__':
    solve()
