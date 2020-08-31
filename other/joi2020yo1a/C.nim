import algorithm, sequtils, strutils


proc solve() =
    var N, M: int
    (N, M) = stdin.readLine.split.map(parseInt)
    var
        A = stdin.readLine.split.map(parseInt)
        B = stdin.readLine.split.map(parseInt)
        C = concat(A, B)
    C.sort()
    echo C.join("\n")


when is_main_module:
    solve()
