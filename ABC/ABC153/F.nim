import strutils, sequtils, algorithm, math


proc solve() =
    var N, D, A: int
    (N, D, A) = stdin.readLine.split.map(parseInt)
    var
        XH = newSeqWith(N, stdin.readLine.split.map(parseInt))
        cumsum: array[2 * 10 ^ 5 + 3, int]
        i, j, ans = 0
    const INF = 10 ^ 10
    
    XH.add(@[-1, 0])
    XH.add(@[INF, 0])
    XH = XH.sortedByIt(it[0])

    while i <= N:
        while i <= N and XH[i][1] <= cumsum[i] * A:
            cumsum[i + 1] += cumsum[i]
            inc i
        while j <= N and XH[j][0] <= XH[i][0] + 2 * D:
            inc j
        var m = (XH[i][1] - cumsum[i] * A + A - 1) div A
        cumsum[i] += m
        cumsum[j] -= m
        ans += m
    echo ans


when is_main_module:
    solve()
