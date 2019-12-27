def solve():
    N, *p = map(int, open(0).read().split())
    perfect = sum(p)
    dp = [0 for _ in range(perfect+1)]
    dp[0] = 1
    for i in range(N):
        for j in range(perfect, -1, -1):
            if dp[j] == 1:
                dp[j+p[i]] = 1
    print(sum(dp))


if __name__ == '__main__':
    solve()
