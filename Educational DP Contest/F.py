def solve():
    s = input()
    t = input()

    len_s, len_t = len(s), len(t)
    dp = [[0] * 3001 for _ in range(3001)]
    for i in range(len_s):
        for j in range(len_t):
            if s[i] == t[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

    ans = ''
    i, j = len_s, len_t
    while 0 < i and 0 < j:
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j-1]:
            j -= 1
        else:
            ans += s[i-1]
            i -= 1
            j -= 1
    print(ans[::-1])


if __name__ == '__main__':
    solve()
