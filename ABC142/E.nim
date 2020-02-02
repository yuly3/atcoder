import strutils, sequtils, math, algorithm


proc solve() =
    var
        N, M: int
        a, b: int
    (N, M) = stdin.readLine.split.map(parseInt)
    const INF = 10^9
    
    var dp: array[2^12, int]
    dp.fill(INF)
    dp[0] = 0

    for _ in 0..<M:
        (a, b) = stdin.readLine.split.map(parseInt)
        var
            c = stdin.readLine.split.map(parseInt)
            can_open = 0
        for ci in c:
            can_open += 1 shl (ci - 1)
        for i in 0..<2^N:
            dp[i or can_open] = min(dp[i or can_open], dp[i] + a)
    
    if dp[2^N - 1] == INF:
        echo -1
    else:
        echo dp[2^N - 1]


when is_main_module:
    solve()
