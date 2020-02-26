def solve():
    N = int(input())
    S = [input() for _ in range(5)]
    
    dp = [[5000] * 3 for _ in range(N + 1)]
    dp[0][0], dp[0][1], dp[0][2] = 0, 0, 0
    
    for i in range(1, N + 1):
        r, b, w = 0, 0, 0
        for j in range(5):
            if S[j][i - 1] == 'R':
                r += 1
            elif S[j][i - 1] == 'B':
                b += 1
            elif S[j][i - 1] == 'W':
                w += 1
        rbw = [r, b, w]
        for j in range(3):
            for k in range(3):
                if j == k:
                    continue
                dp[i][k] = min(dp[i][k], dp[i - 1][j] + 5 - rbw[k])
    print(min(dp[N]))


if __name__ == '__main__':
    solve()
