def solve():
    N, M = map(int, input().split())
    INF = 10 ** 9
    
    dp = [INF] * (2 ** N)
    dp[0] = 0
    for _ in range(M):
        a, b = map(int, input().split())
        c = list(map(lambda x: int(x) - 1, input().split()))
        open = 0
        for i in range(b):
            open += 1 << c[i]
        for i in range(2 ** N):
            if dp[i] + a <= dp[i | open]:
                dp[i | open] = dp[i] + a
    
    if dp[-1] == INF:
        print(-1)
    else:
        print(dp[-1])


if __name__ == '__main__':
    solve()
