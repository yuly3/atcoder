import strutils, sequtils, math, algorithm


proc solve() =
    var H, N: int
    (H, N) = stdin.readLine.split.map(parseInt)
    var AB = newSeqWith(N, stdin.readLine.split.map(parseInt))

    var dp: array[10^4 + 1, int]
    dp.fill(10^9)
    dp[0] = 0

    for h in 1..H:
        for i in 0..<N:
            var (pw, mp) = (AB[i][0], AB[i][1])
            mp += dp[max(0, h - pw)]
            dp[h] = min(dp[h], mp)
    echo dp[H]


when is_main_module:
    solve()
