import sequtils, strutils

proc solve() =
    var W = parseInt(readLine(stdin))
    var N, K: int
    (N, K) = stdin.readLine.strip.split.map(parseInt)
    var AB = mapIt(0..<N, stdin.readLine.strip.split.map(parseInt))
    
    var dp : array[51, array[51, array[10001, int]]]
    for i in 0..<N:
        for j in 0..<K:
            for k in 0..W:
                if 0 <= k - AB[i][0]:
                    dp[i+1][j+1][k] = max(dp[i][j+1][k], dp[i][j][k-AB[i][0]] + AB[i][1])
                else:
                    dp[i+1][j+1][k] = dp[i][j+1][k]
    echo dp[N][K][W]

solve()
