import sys

rl = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def solve():
    N, M = map(int, rl().split())
    S, C = ['' for _ in range(M)], [0] * M
    for i in range(M):
        S[i], ci = rl().split()
        C[i] = int(ci)
    
    INF = 10 ** 18
    dp = [INF] * (1 << N)
    dp[0] = 0
    
    for i in range(M):
        si = S[i]
        cs = 0
        for j in range(N):
            if si[j] == 'Y':
                cs += 1 << (N - j - 1)
        
        for ps in range(1 << N):
            dp[ps | cs] = min(dp[ps | cs], dp[ps] + C[i])
    
    if dp[-1] == INF:
        print(-1)
    else:
        print(dp[-1])


if __name__ == '__main__':
    solve()
