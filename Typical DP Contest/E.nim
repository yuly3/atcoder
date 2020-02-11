import strutils, math


proc solve() =
    var
        D = stdin.readLine.parseInt
        N = stdin.readLine
        len_N = len(N)
        dp: array[10010, array[101, array[2, int]]]
    const MOD = 10^9 + 7
    
    dp[0][0][0] = 1
    for i in 0..<len_N:
        for j in 0..<D:
            for sml in 0..1:
                var ni = parseInt($N[i])
                for k in 0..9:
                    var n_sml = sml
                    if sml == 0:
                        if ni < k:
                            continue
                        elif k < ni:
                            n_sml = 1
                    dp[i + 1][(j + k) mod D][n_sml] += dp[i][j][sml] mod MOD
    echo((sum(dp[len_N][0]) - 1) mod MOD)


when is_main_module:
    solve()
