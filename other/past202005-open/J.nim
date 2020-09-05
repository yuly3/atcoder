import algorithm, sequtils, strutils


var a, highest, ans: seq[int]


proc solve() =
    var N, M: int
    (N, M) = stdin.readLine.split.map(parseInt)
    a = stdin.readLine.split.map(parseInt)

    highest = newSeq[int](N)
    ans = newSeqWith(M, -1)
    var idx: int
    for i, ai in a:
        idx = highest.lower_bound(ai) - 1
        if idx != -1:
            highest[idx] = ai
            ans[i] = N - idx
    echo ans.join("\n")


when is_main_module:
    solve()
