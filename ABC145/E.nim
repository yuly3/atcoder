import strutils, sequtils, algorithm


proc solve() =
    var N, T: int
    (N, T) = stdin.readLine.split.map(parseInt)
    var AB = newSeqWith(N, newSeq[int](2))
    for i in 0..<N:
        (AB[i][0], AB[i][1]) = stdin.readLine.split.map(parseInt)
    AB = AB.sortedByIt(it[0])
    
    var
        dp: array[3001, int]
        ans = 0
    
    for ab in AB:
        let (a, b) = (ab[0], ab[1])
        ans = max(ans, dp[T-1] + b)
        for i in countdown(T-1, a):
            dp[i] = max(dp[i], dp[i - a] + b)
    echo ans


when is_main_module:
    solve()
