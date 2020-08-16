import sequtils, strutils

var
    items: array[3010, array[3010, int]]
    dp: array[3010, array[3010, array[4, int]]]


proc solve() =
    var R, C, K: int
    (R, C, K) = stdin.readLine.split.map(parseInt)
    var r, c, v: int
    for _ in 0..<K:
        (r, c, v) = stdin.readLine.split.map(parseInt)
        dec r; dec c
        items[r][c] = v
    
    dp[0][0][1] = items[0][0]
    for r in 1..<R:
        dp[r][0][0] = dp[r - 1][0][1]
        dp[r][0][1] = dp[r][0][0] + items[r][0]
    for c in 1..<C:
        dp[0][c][1] = max(dp[0][c - 1][1], items[0][c])
        dp[0][c][2] = max(dp[0][c - 1][2], dp[0][c - 1][1] + items[0][c])
        dp[0][c][3] = max(dp[0][c - 1][3], dp[0][c - 1][2] + items[0][c])
    
    for r in 1..<R:
        for c in 1..<C:
            dp[r][c][0] = max(max(dp[r - 1][c]), dp[r][c - 1][0])
            dp[r][c][1] = max([max(dp[r - 1][c]) + items[r][c], dp[r][c - 1][0] + items[r][c], dp[r][c - 1][1]])
            dp[r][c][2] = max(dp[r][c - 1][2], dp[r][c - 1][1] + items[r][c])
            dp[r][c][3] = max(dp[r][c - 1][3], dp[r][c - 1][2] + items[r][c])
    echo max(dp[R - 1][C - 1])


when is_main_module:
    solve()
