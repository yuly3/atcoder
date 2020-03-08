import strutils, math


proc solve() =
    var
        N = stdin.readLine
        dp: array[10^7 + 10, array[2, int]]
        g = [0, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
    
    dp[0][0] = g[parseInt($N[0])]
    dp[0][1] = g[parseInt($N[0]) + 1]
    for i in 1..<N.len:
        let d = parseInt($N[i])
        dp[i][0] = min(dp[i - 1][0] + g[d], dp[i - 1][1] + g[10 - d])
        dp[i][1] = min(dp[i - 1][0] + g[d + 1], dp[i - 1][1] + g[9 - d])
    echo dp[N.len - 1][0]


when is_main_module:
    solve()
