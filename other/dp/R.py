import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def matmul(a, b, mod):
    N0 = len(a)
    N1 = len(b[0])
    N2 = len(a[0])
    res = [[0] * N1 for _ in range(N0)]
    for i in range(N0):
        for j in range(N1):
            tmp = 0
            for k in range(N2):
                tmp = (tmp + a[i][k] * b[k][j]) % mod
            res[i][j] = tmp
    return res


def matpow(a, k, mod):
    N = len(a)
    res = [[0] * N for _ in range(N)]
    for i in range(N):
        res[i][i] = 1
    while k:
        if k & 1:
            res = matmul(res, a, mod)
        a = matmul(a, a, mod)
        k >>= 1
    return res


def solve():
    N, K = map(int, rl().split())
    a = [list(map(int, rl().split())) for _ in range(N)]
    MOD = 10 ** 9 + 7
    
    a = list(map(list, zip(*a)))
    mat = matpow(a, K, MOD)
    ans = 0
    for i in range(N):
        for j in range(N):
            ans = (ans + mat[i][j]) % MOD
    print(ans)


if __name__ == '__main__':
    solve()
