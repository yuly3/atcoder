import sequtils, strutils, tables


proc solve() =
    var N, M: int
    (N, M) = stdin.readLine.split.map(parseInt)
    var
        A = stdin.readLine.split.map(parseInt)
        counter = A.toCountTable()
    echo counter.largest().val


when is_main_module:
    solve()
