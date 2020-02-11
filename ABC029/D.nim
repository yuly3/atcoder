import strutils, math


proc solve() =
    var
        N = stdin.readLine
        len_N = len(N)
        dp: array[11, array[11, array[2, int]]]
    
    dp[0][0][0] = 1
    for i in 0..<len_N:
        let ni = parseInt($N[i])
        for j in 0..<len_N:
            for sml in 0..1:
                for k in 0..9:
                    var n_sml = sml
                    if sml == 0:
                        if ni < k:
                            continue
                        if k < ni:
                            n_sml = 1
                    if k == 1:
                        dp[i + 1][j + 1][n_sml] += dp[i][j][sml]
                    else:
                        dp[i + 1][j][n_sml] += dp[i][j][sml]
    
    var ans = 0
    for i in 1..len_N:
        ans += sum(dp[len_N][i]) * i
    echo ans


when is_main_module:
    solve()
