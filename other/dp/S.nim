import strutils, math


proc solve() =
    var
        K = stdin.readLine
        D = stdin.readLine.parseInt
        len_K = len(K)
        dp: array[10010, array[100, array[2, int]]]
    const MOD = 10^9 + 7

    dp[0][0][0] = 1
    for i in 0..<len_K:
        let ki = parseInt($K[i])
        for j in 0..<D:
            for sml in 0..1:
                for k in 0..9:
                    var n_sml = sml
                    if sml == 0:
                        if ki < k:
                            continue
                        if k < ki:
                            n_sml = 1
                    dp[i + 1][(j + k) mod D][n_sml] += dp[i][j][sml] mod MOD
    echo((sum(dp[len_K][0]) - 1) mod MOD)


when is_main_module:
    solve()
