def solve():
    N = int(input())
    S = input()
    MOD = 10007
    
    dp = [[0] * 8 for _ in range(N + 1)]
    if S[0] == 'J':
        must = 0
    elif S[0] == 'O':
        must = 1
    else:
        must = 2
    for i in range(8):
        if i >> 0 & 1 and i >> must & 1:
            dp[1][i] = 1
    
    for i in range(1, N):
        if S[i] == 'J':
            must = 0
        elif S[i] == 'O':
            must = 1
        else:
            must = 2
        for ns in range(8):
            if not ns >> must & 1:
                continue
            for s in range(8):
                for j in range(3):
                    if ns >> j & 1 and s >> j & 1:
                        dp[i + 1][ns] += dp[i][s]
                        dp[i + 1][ns] %= MOD
                        break
    print(sum(dp[N]) % MOD)


if __name__ == '__main__':
    solve()
