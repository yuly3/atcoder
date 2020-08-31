import algorithm, sequtils, strutils


proc solve() =
    var N, A, B: int
    (N, A, B) = stdin.readLine.split.map(parseInt)
    var
        S = stdin.readLine
        seq_s = newSeq[char]()
    for si in S:
        seq_s.add(si)
    seq_s.reverse(A - 1, B - 1)
    echo seq_s.join("")


when is_main_module:
    solve()
