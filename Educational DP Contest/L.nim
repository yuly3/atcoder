import strutils, sequtils, math

var dp: array[3001, array[3001, int]]


proc solve() =
    var
        N = stdin.readLine.parseInt
        a = stdin.readLine.split.map(parseInt)
    
    for l in 1..N:
        for i in 0..N - l:
            var j = i + l
            if (N - l) mod 2 == 0:
                dp[i][j] = max(dp[i+1][j] + a[i], dp[i][j-1] + a[j-1])
            else:
                dp[i][j] = min(dp[i+1][j] - a[i], dp[i][j-1] - a[j-1])
    echo dp[0][N]


when is_main_module:
    solve()
