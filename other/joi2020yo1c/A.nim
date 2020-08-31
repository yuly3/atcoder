import math, sequtils, strutils


proc solve() =
    var X, L, R: int
    (X, L, R) = stdin.readLine.split.map(parseInt)
    var ans, min_d: int
    min_d = 10^7
    for num in L..R:
        if abs(X - num) < min_d:
            min_d = abs(X - num)
            ans = num
    echo ans


when is_main_module:
    solve()
