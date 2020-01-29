import strutils, sequtils, algorithm


proc solve() =
    var N, MA, MB: int
    (N, MA, MB) = stdin.readLine.split.map(parseInt)
    var a, b, c = newSeq[int](N)
    for i in 0..<N:
        (a[i], b[i], c[i]) = stdin.readLine.split.map(parseInt)
    const INF = 50 * 100
    
    var dp: array[401, array[401, int]]
    for i in 0..400:
        dp[i].fill(INF)
    dp[0][0] = 0
    
    for i in 0..<N:
        for ca in countdown(399, 0):
            if 400 < ca + a[i]:
                continue
            for cb in countdown(399, 0):
                if 400 < cb + b[i]:
                    continue
                dp[ca + a[i]][cb + b[i]] = min(dp[ca + a[i]][cb + b[i]], dp[ca][cb] + c[i])
    
    var ans = INF
    for i in 1..400:
        if 400 < MA * i or 400 < MB * i:
            break
        ans = min(ans, dp[MA * i][MB * i])
    if ans == INF:
        echo -1
    else:
        echo ans


when is_main_module:
    solve()
