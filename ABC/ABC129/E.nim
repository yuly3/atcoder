import math


proc solve() =
    var
        L = stdin.readLine
        len_L = len(L)
        dp: array[100010, array[2, int]]
    const MOD = 10^9 + 7
    
    dp[0][0] = 1
    for i in 0..<len_L:
        dp[i + 1][1] += dp[i][1] * 3 mod MOD
        if L[i] == '1':
            dp[i + 1][0] += dp[i][0] * 2 mod MOD
            dp[i + 1][1] += dp[i][0] mod MOD
        else:
            dp[i + 1][0] += dp[i][0] mod MOD
    echo(sum(dp[len_L]) mod MOD)


when is_main_module:
    solve()
