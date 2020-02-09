import strutils, sequtils


proc solve() =
    var
        N, M, Q: int
        li, ri: int
        counter, cumsum: array[501, array[501, int]]
    
    (N, M, Q) = stdin.readLine.split.map(parseInt)
    for _ in 1..M:
        (li, ri) = stdin.readLine.split.map(parseInt)
        inc counter[li][ri]
    for i in 1..N:
        for j in 1..N:
            cumsum[i][j] = cumsum[i][j - 1] + counter[i][j]
    
    var p, q, ans: int
    for _ in 1..Q:
        (p, q) = stdin.readLine.split.map(parseInt)
        ans = 0
        for i in p..q:
            ans += cumsum[i][q] - cumsum[i][p - 1]
        echo ans


when is_main_module:
    solve()
