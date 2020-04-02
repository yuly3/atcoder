import strutils, sequtils, math

var dp: array[101, array[10^5 + 1, int]]
var cumsum: array[10^5 + 1, int]


proc solve() =
    var N, K: int
    (N, K) = stdin.readLine.split.map(parseInt)
    var a = stdin.readLine.split.map(parseInt)
    const MOD = 10^9 + 7

    dp[0][0] = 1
    for i in 0..<N:
        cumsum[0] = 0
        for j in 0..K + 1:
            cumsum[j+1] = cumsum[j] + dp[i][j]
        for j in 0..K:
            dp[i+1][j] = (cumsum[j+1] - cumsum[max(0, j - a[i])]) mod MOD
    echo dp[N][K]


when is_main_module:
    solve()
