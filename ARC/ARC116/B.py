import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A = list(map(int, rl().split()))
    MOD = 998244353
    
    A.sort()
    t = A[-1]
    ans = 0
    for i in range(N - 2, -1, -1):
        ans += A[i] * t
        ans %= MOD
        t *= 2
        t += A[i]
        t %= MOD
    
    for ai in A:
        ans += ai ** 2
        ans %= MOD
    print(ans)


if __name__ == '__main__':
    solve()
