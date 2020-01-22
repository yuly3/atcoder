import strutils, sequtils, math

var dp: array[10 ^ 5 + 1, bool]

proc solve() =
    var N, K: int
    (N, K) = stdin.readLine.split.map(parseInt)
    var a = stdin.readLine.split.map(parseInt)

    for i in 1..K:
        for j in 0..<N:
            if 0 <= i - a[j]:
                dp[i] = dp[i] or not dp[i - a[j]]
    
    if dp[K]:
        echo "First"
    else:
        echo "Second"

when is_main_module:
    solve()
