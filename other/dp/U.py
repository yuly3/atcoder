import sys
from itertools import combinations

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    a = [list(map(int, rl().split())) for _ in range(N)]
    
    score = [0] * 2 ** N
    for s in range(2 ** N):
        for i, j in combinations(range(N), 2):
            if s >> i & 1 and s >> j & 1:
                score[s] += a[i][j]
    
    dp = [0] * 2 ** N
    searched = [False] * 2 ** N
    searched[0] = True
    
    def calc(S):
        if searched[S]:
            return dp[S]
        searched[S] = True
        
        res = 0
        T = 2 ** N
        while 0 < T:
            T = (T - 1) & S
            res = max(res, score[T] + calc(S ^ T))
        dp[S] = res
        return res
    
    calc(2 ** N - 1)
    print(dp[-1])


if __name__ == '__main__':
    solve()
