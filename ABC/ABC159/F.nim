import strutils, sequtils


proc `%=`*(n: var int, m: int) = (n = n mod m)


const MOD = 998244353
var dp: array[3010, array[3010, array[3, int]]]


proc solve() =
    var N, S: int
    (N, S) = stdin.readLine.split.map(parseInt)
    let A = stdin.readLine.split.map(parseInt)

    dp[0][0][0] = 1
    var nj: int
    for i in 0..<N:
        for j in 0..S:
            dp[i + 1][j][0] += dp[i][j][0]
            dp[i + 1][j][0] %= MOD
            dp[i + 1][j][1] += dp[i][j][0] + dp[i][j][1]
            dp[i + 1][j][1] %= MOD
            dp[i + 1][j][2] += dp[i][j][0] + dp[i][j][1] + dp[i][j][2]
            dp[i + 1][j][2] %= MOD
            nj = A[i] + j
            if nj <= S:
                dp[i + 1][nj][1] += dp[i][j][0] + dp[i][j][1]
                dp[i + 1][nj][1] %= MOD
                dp[i + 1][nj][2] += dp[i][j][0] + dp[i][j][1]
                dp[i + 1][nj][2] %= MOD
    echo dp[N][S][2]


when is_main_module:
    solve()
