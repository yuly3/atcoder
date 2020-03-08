def solve():
    N, M = map(int, input().split())
    graph = [0] * N
    for _ in range(M):
        x, y = map(lambda x: int(x) - 1, input().split())
        graph[x] |= 1 << y
    
    dp = [0] * (1 << N)
    dp[0] = 1
    for s in range(1, 1 << N):
        for i in range(N):
            if (s >> i) & 1 and not graph[i] & s:
                dp[s] += dp[s ^ (1 << i)]
    print(dp[-1])


if __name__ == '__main__':
    solve()
