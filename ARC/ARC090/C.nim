import strutils, sequtils


proc solve() =
    var
        N = stdin.readLine.parseInt
        A1 = stdin.readLine.split.map(parseInt)
        A2 = stdin.readLine.split.map(parseInt)
        dp: array[101, array[2, int]]
    
    dp[1][0] = A1[0]
    dp[1][1] = A1[0] + A2[0]
    for i in 1..<N:
        dp[i+1][0] = dp[i][0] + A1[i]
        dp[i+1][1] = max(dp[i+1][0] + A2[i], dp[i][1] + A2[i])
    echo dp[N][1]


when is_main_module:
    solve()
