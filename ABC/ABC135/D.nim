import math

var dp: array[10^5+1, array[13, int64]]


proc solve(): void =
    const MOD : int64 = 10^9+7
    let
        S = stdin.readLine
        N = S.len

    dp[0][0] = 1

    for i, ch in S:
        if ch == '?':
            for j in 0..9:
                for k in 0..12:
                    var m = (k * 10 + j) mod 13
                    dp[i+1][m] += dp[i][k]
                    dp[i+1][m] = dp[i+1][m] mod MOD
        else:
            for k in 0..12:
                var m = (k * 10 + ord(ch) - ord('0')) mod 13
                dp[i+1][m] += dp[i][k]
                dp[i+1][m] = dp[i+1][m] mod MOD
    echo dp[N][5] mod MOD
    return

when is_main_module:
    solve()
