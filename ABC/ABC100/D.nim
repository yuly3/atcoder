import strutils, sequtils, math


proc solve() =
    var
        N, M: int
        x, y, z: array[1001, int]
        dp: array[1001, array[1002, int]]
    const INF = 10^14
    
    (N, M) = stdin.readLine.split.map(parseInt)
    for i in 0..<N:
        (x[i], y[i], z[i]) = stdin.readLine.split.map(parseInt)
    
    var ans = -INF
    for a in countup(-1, 1, 2):
        for b in countup(-1, 1, 2):
            for c in countup(-1, 1, 2):
                
                for i in 0..N:
                    for j in 0..M:
                        dp[i][j] = -INF
                dp[0][0] = 0
                
                for i in 0..<N:
                    let val = a*x[i] + b*y[i] + c*z[i]
                    for j in 0..M:
                        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
                        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + val)
                ans = max(ans, dp[N][M])
    echo ans


when is_main_module:
    solve()
