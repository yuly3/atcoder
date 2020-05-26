import sequtils, strutils, algorithm

var
    AB: seq[(int, int)]
    acc0, acc1, min_acc1: array[500100, int]


proc solve() =
    let N = stdin.readLine.parseInt
    AB = newSeqWith(N, (0, 0))
    for i in 0..<N:
        (AB[i][0], AB[i][1]) = stdin.readLine.split.map(parseInt)
    
    AB.sort(cmp)
    for i in 0..<N:
        let (a, b) = AB[i]
        acc1[i + 1] = acc0[i] - a
        acc0[i + 1] = acc0[i] + b
        min_acc1[i + 1] = min(min_acc1[i], acc1[i + 1])
    
    var ans = 0
    for i in 0..<N:
        let tmp = acc0[i + 1] - AB[i][0] - min_acc1[i + 1]
        ans = max(ans, tmp)
    echo ans


when is_main_module:
    solve()
