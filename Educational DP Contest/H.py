def solve():
    MOD = 10 ** 9 + 7
    H, W = map(int, input().split())
    maze = ['' for _ in range(H)]
    for i in range(H):
        maze[i] = input()

    dp = [[0] * W for _ in range(H)]
    for i in range(H):
        if maze[i][0] == '.':
            dp[i][0] = 1
        else:
            break
    for i in range(W):
        if maze[0][i] == '.':
            dp[0][i] = 1
        else:
            break

    for i in range(1, H):
        for j in range(1, W):
            if maze[i][j] != '#':
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                dp[i][j] %= MOD
    print(dp[H - 1][W - 1])


if __name__ == '__main__':
    solve()
