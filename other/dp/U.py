import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    a = [list(map(int, rl().split())) for _ in range(N)]
    INF = 10 ** 18
    
    dp = [0] * 2 ** N
    searched = [False] * 2 ** N
    searched[0] = True
    c = [0] * 2 ** N
    
    for s in range(2 ** N):
        tmp = 0
        for i in range(N):
            if not s >> i & 1:
                continue
            for j in range(i + 1, N):
                if s >> j & 1:
                    tmp += a[i][j]
        c[s] = tmp
    
    def calc(S):
        if searched[S]:
            return dp[S]
        searched[S] = True
        
        res = -INF
        T = 2 ** N
        while 0 < T:
            T = (T - 1) & S
            res = max(res, c[T] + calc(S ^ T))
        dp[S] = res
        return res
    
    calc(2 ** N - 1)
    print(dp[-1])


if __name__ == '__main__':
    solve()
